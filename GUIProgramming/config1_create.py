# config_file_create.py
from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'debug': 'true',
    'secret_key': 'abc123',
    'log_path': '/my_app/log',
    'python_version': '3',
    'package_path': '/usr/local'
}

config['db'] = {
    'db_name': 'myapp_dev',
    'db_host': 'localhost',
    'db_port': '8889'
}

config['files'] = {
    'use_cdn': 'false',
    'images_path': 'GUIProgramming\icon2.pngGUIProgramming\icon2.png',
    'python_path': '${settings:package_path}/bin/python${settings:python_version}'
}

with open('./dev1139.ini', 'w') as f:
    config.write(f)