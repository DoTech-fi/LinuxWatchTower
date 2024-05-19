import os

def set_target():
    nickname = input("Enter your nickname (Host): ")
    server = input("Enter your server address (HostName): ")
    user = input("Enter your user (User): ")
    identity_file = input(f"Enter your identity file path (IdentityFile) (default is {os.path.expanduser('~/.ssh/id_rsa')}): ") or os.path.expanduser('~/.ssh/id_rsa')
    port = input(f"Enter your port number (Port) (default is 22): ") or '22'

    default_path = os.path.expanduser("~/.ssh/config")
    config_path = input(f"Enter the path to your config file (default is {default_path}): ") or default_path

    with open(config_path, 'a') as configfile:
        configfile.write(f"\nHost {nickname}\n")
        configfile.write(f"   HostName {server}\n")
        configfile.write(f"   User {user}\n")
        configfile.write(f"   IdentityFile {identity_file}\n")
        configfile.write(f"   Port {port}\n")
