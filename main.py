import argparse
import os
from db.database import init_db
from ssh.config import set_target
from tools import interactive_install, check_state

def display_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            print(file.read())
    else:
        print("README.md file not found.")

def main():
    init_db()
    parser = argparse.ArgumentParser(description='Linux Watch Tower', epilog='Use -h or --help for more info')

    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('set-target', help='Set a new target')
    subparsers.add_parser('install', help='Install a tool on a target')
    subparsers.add_parser('check-state', help='Check the state of tools on a target')

    args = parser.parse_args()

    if args.command is None:
        display_readme()
        return

    if args.command == 'set-target':
        set_target()
    elif args.command == 'install':
        interactive_install()
    elif args.command == 'check-state':
        check_state()

if __name__ == "__main__":
    main()