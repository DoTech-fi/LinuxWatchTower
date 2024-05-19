# Linux Watch Tower

Linux Watch Tower is a command-line tool designed to facilitate the installation and management of specific software tools (such as Apache, Nginx and ...) on remote servers via SSH using Ansible. It provides an interactive interface for setting up SSH targets and installing these tools while logging the installation states in an SQLite database.

## Features

- **Set SSH Target**: Configure SSH target hosts by adding entries to your `~/.ssh/config` file.
- **Check Installation Status**: Verify if a specific tool has already been installed on a given host.
- **Log Installations**: Log installation details (host, tool, version, and date) into an SQLite database.
- **List SSH Hosts**: Read the user's SSH config file to list available SSH host nicknames.
- **Interactive Installation**: Provide an interactive interface for users to select a host and tool to install.
- **Ansible Playbook Execution**: Use Ansible to manage installations dynamically based on user input.

## Setting Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Follow these steps to set up a virtual environment and install the required packages:

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

3. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DoTech-fi/LinuxWatchTower
   cd LinuxWatchTower
   ```

2. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Set an SSH Target
Set up a new SSH target host:
```bash
python main.py set-target
```
This command will prompt you to enter the server address, user, identity file, and a nickname for the host, and then add this information to your SSH config file.

### Interactive Installation
Provide an interactive interface to select a host and tool for installation:
```bash
python main.py install
```
This command will list available SSH hosts and tools, check their installation status, and allow you to initiate the installation process.

## Example Workflow

1. **Set up an SSH target:**
   ```bash
   python main.py set-target
   ```

2. **Interactive installation of a tool (e.g., Nginx):**
   ```bash
   python main.py install
   ```

## License

Linux Watch Tower is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Acknowledgements

- [Jeff Geerling](https://github.com/geerlingguy) for his Ansible roles
- All contributors and users for their support and feedback
