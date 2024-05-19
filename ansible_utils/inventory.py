import os

def get_host_nicknames():
    host_nicknames = []
    with open(os.path.expanduser("~/.ssh/config")) as f:
        for line in f:
            if line.strip() and not line.strip().startswith('#'):
                words = line.split()
                if words[0] == 'Host':
                    host_nicknames.append(words[1])
    return host_nicknames
