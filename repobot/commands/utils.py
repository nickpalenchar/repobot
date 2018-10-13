# repobot/commands/utils.py
'''utility functions and wrappers'''

from functools import wraps
import requests
from requests.auth import HTTPBasicAuth
import keyring

class GitHubAuthenticationError(Exception):
    pass

class CredentialsNotFound(Exception):
    pass

def set_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = keyring.get_password('repobot', 'username')
        password = keyring.get_password('repobot', 'password')

        #r = requests.get('https://api.github.com/user', auth='')
        if password is None:
            return CredentialsNotFound('Set credentials first with `repobot login`')

        res = func(*args, basicauth=requests.auth.HTTPBasicAuth(username, password), **kwargs)
        
        print('YO')
        if res.status_code == 401:
            print('error AUTH')
            return GitHubAuthenticationError(
                'Unauthorized. Use `repobot` login to update credentials')
        
    return wrapper
