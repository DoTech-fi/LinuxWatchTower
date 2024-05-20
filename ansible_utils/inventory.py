import os

def get_host_nicknames(config_path):
    host_nicknames = []
    with open(config_path) as f:
        for line in f:
            if line.strip() and not line.strip().startswith('#'):
                words = line.split()
                if words[0] == 'Host':
                    host_nicknames.append(words[1])
    return host_nicknames
