# repobot/commands/login.py
'''set login token'''

from .base import Base

class Login(Base):
    '''login class'''

    def run(self):
        if self.options['<token>'] is None:
            self.options['<token>'] = input("Provide a personal access token:\n> ")


