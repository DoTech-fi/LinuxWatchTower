from ansible_utils.ansible_executor import install_tool
from ansible_utils.inventory import get_host_nicknames
from ansible_utils.roles import Tools
from db.database import log_installation, check_installation

def interactive_install():
    host_nicknames = get_host_nicknames()
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
        installed = check_installation(nickname, tool.name)
        status = "(present)" if installed else "(absent)"
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

    result = install_tool(nickname, tool.value['default'], version)
    if result == 0:
        log_installation(nickname, tool_name, version)
