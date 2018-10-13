# repobot/commands/login.py
'''set login token'''

from .base import Base

import keyring
import sys
import re

class Login(Base):
    '''login class'''

    def run(self):
        token = self.options['<token>'] 
        
        if token is None:
            token = input("Provide a personal access token:\n> ")

        if keyring.get_password('repobot', 'auth') is not None:
            # @TODO get the -f flag
            print('Auth token already exists! (*****%s)' % keyring.get_password('repobot', 'auth')[-6:])
            confirm = input('Replace ******%s with new key? [y/N] ' % token[-6:])
            if re.match('ye?s?', confirm, flags=2) is None:
                sys.exit(0)
            #@TODO: do a keyring test

        keyring.set_password('repobot', 'auth', token)
        print('Successfully authenticated')        
