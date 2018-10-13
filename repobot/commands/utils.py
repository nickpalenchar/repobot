# repobot/commands/utils.py
'''utility functions and wrappers'''

import sys
from functools import wraps
from requests.auth import HTTPBasicAuth
import keyring
import requests

class GitHubAuthenticationError(Exception):
    pass

class CredentialsNotFound(Exception):
    pass

def set_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = keyring.get_password('repobot', 'username')
        password = keyring.get_password('repobot', 'password')

        if password is None:
            print('Set credentials first with `repobot login`')
            sys.exit(0)

        r = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username, password))
        if r.status_code == 401:
            print('Invalid Auth credentials. Please log in again')
            sys.exit(0)
        
        func(*args, basicauth=HTTPBasicAuth(username, password), **kwargs)
        
        
    return wrapper
