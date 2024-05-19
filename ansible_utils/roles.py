from enum import Enum

class Tools(Enum):
    NGINX = {'default': 'geerlingguy.nginx', 'versions': ['latest']}
    APACHE = {'default': 'geerlingguy.apache', 'versions': ['latest']}
