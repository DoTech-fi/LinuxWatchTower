import os

def get_input(prompt, default=None):
    while True:
        value = input(f"{prompt} " + (f"(default is {default}): " if default else ": "))
        if value or default:
            return value or default
        else:
            print("This field is required. Please enter a value.")

def set_target():
    nickname = get_input("Enter your nickname (Host)")
    server = get_input("Enter your server address (HostName)")
    user = get_input("Enter your user (User)")
    identity_file = get_input("Enter your identity file path (IdentityFile)", os.path.expanduser('~/.ssh/id_rsa'))
    port = get_input("Enter your port number (Port)", '22')

    default_path = os.path.expanduser("~/.ssh/config")
    config_path = get_input("Enter the path to your config file", default_path)

    with open(config_path, 'a') as configfile:
        configfile.write(f"\nHost {nickname}\n")
        configfile.write(f"   HostName {server}\n")
        configfile.write(f"   User {user}\n")
        configfile.write(f"   IdentityFile {identity_file}\n")
        configfile.write(f"   Port {port}\n")