import os
from ansible_utils.ansible_executor import install_tool
from ansible_utils.check_tool import check_tool_remote
from ansible_utils.inventory import get_host_nicknames
from ansible_utils.roles import Tools
from db.database import log_installation, check_installation, update_installation

def install_ansible_role(role_name, version='latest'):
    import subprocess
    if version == 'latest':
        cmd = f"ansible-galaxy role install {role_name}"
    else:
        cmd = f"ansible-galaxy role install {role_name},{version}"
    result = subprocess.run(cmd, shell=True, check=True)
    return result.returncode == 0

def interactive_install():
    default_config_path = os.path.expanduser("~/.ssh/config")
    config_path = input(f"Enter the path to your config file (default is {default_config_path}): ") or default_config_path

    host_nicknames = get_host_nicknames(config_path=config_path)
    if not host_nicknames:
        print("No hosts found in the SSH config file.")
        return

    print("Available hosts:")
    for index, nickname in enumerate(host_nicknames, start=1):
        print(f"{index}. {nickname}")

    host_index = int(input("Select the host by number: ")) - 1
    if host_index < 0 or host_index >= len(host_nicknames):
        print("Invalid selection.")
        return

    nickname = host_nicknames[host_index]
    print(f"Selected host: {nickname}")

    print("Available tools:")
    tool_list = list(Tools)
    for index, tool in enumerate(tool_list, start=1):
        installed_in_db = check_installation(nickname, tool.name)
        status = "(present)" if installed_in_db else "(absent)"
        print(f"{index}. {tool.name} {status}")

    tool_index = int(input("Select the tool by number: ")) - 1
    if tool_index < 0 or tool_index >= len(tool_list):
        print("Invalid selection.")
        return

    tool = tool_list[tool_index]
    tool_name = tool.name
    print(f"Selected tool: {tool_name}")

    print(f"Available versions for {tool_name}: {', '.join(tool.value['versions'])}")
    version = input("Enter the version to install (default is 'latest'): ") or 'latest'
    
    if version not in tool.value['versions']:
        print("Invalid version.")
        return

    if not check_tool_remote(nickname, tool_name):
        print(f"Installing {tool_name} version {version}...")
        if install_ansible_role(tool.value['default'], version):
            log_installation(nickname, tool_name, version)
            print(f"Successfully installed {tool_name} version {version}.")
        else:
            print(f"Failed to install {tool_name} version {version}.")
    else:
        print(f"{tool_name} is already installed on the remote host but not in the DB. Updating the DB.")
        log_installation(nickname, tool_name, 'unknown')

    result = install_tool(nickname, tool.value['default'], version)
    if result == 0:
        log_installation(nickname, tool_name, version)

def check_state():
    default_config_path = os.path.expanduser("~/.ssh/config")
    config_path = input(f"Enter the path to your config file (default is {default_config_path}): ") or default_config_path

    host_nicknames = get_host_nicknames(config_path=config_path)
    if not host_nicknames:
        print("No hosts found in the SSH config file.")
        return

    print("Available hosts:")
    for index, nickname in enumerate(host_nicknames, start=1):
        print(f"{index}. {nickname}")

    host_index = int(input("Select the host by number (or 0 to check all hosts): ")) - 1

    if host_index == -1:
        selected_hosts = host_nicknames
    elif 0 <= host_index < len(host_nicknames):
        selected_hosts = [host_nicknames[host_index]]
    else:
        print("Invalid selection.")
        return

    for nickname in selected_hosts:
        print(f"\nChecking state for host: {nickname}")
        for tool in Tools:
            tool_name = tool.name
            installed_in_db = check_installation(nickname, tool_name)
            installed_on_remote = check_tool_remote(nickname, tool_name)

            if installed_in_db and installed_on_remote:
                state = "present in both DB and remote host"
            elif installed_in_db:
                state = "present in DB only"
            elif installed_on_remote:
                state = "present on remote host only"
            else:
                state = "absent"

            print(f"{tool_name}: {state}")

        update_db = input(f"Do you want to update the local DB to match the remote state for host {nickname}? (yes/no): ").strip().lower()
        if update_db == 'yes':
            for tool in Tools:
                tool_name = tool.name
                installed_on_remote = check_tool_remote(nickname, tool_name)
                if installed_on_remote:
                    log_installation(nickname, tool_name, 'unknown')
                    print(f"Updated DB: {tool_name} is now marked as installed for host {nickname} in the DB.")
                else:
                    update_installation(nickname, tool_name, remove=True)
                    print(f"DB not updated for {tool_name} as it is not installed on the remote host {nickname}.")