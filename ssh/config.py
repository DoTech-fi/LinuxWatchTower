import os

def set_target():
    server = input("Enter your server address: ")
    user = input("Enter your user: ")
    identity_file = input(f"Enter your identity file path (default is {os.path.expanduser('~/.ssh/id_rsa')}): ") or os.path.expanduser('~/.ssh/id_rsa')
    nickname = input("Enter your nickname: ")

    default_path = os.path.expanduser("~/.ssh/config")
    config_path = input(f"Enter the path to your config file (default is {default_path}): ") or default_path

    with open(config_path, 'a') as configfile:
        configfile.write(f"\nHost {nickname}\n")
        configfile.write(f"   HostName {server}\n")
        configfile.write(f"   User {user}\n")
        configfile.write(f"   IdentityFile {identity_file}\n")
