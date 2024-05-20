from enum import Enum

class Tools(Enum):
    NGINX = {'default': 'geerlingguy.nginx', 'versions': ['latest', '3.1.4', '3.1.3']}
    APACHE = {'default': 'geerlingguy.apache', 'versions': ['latest', '3.3.0', '3.3.1']}
