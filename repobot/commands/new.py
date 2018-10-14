# new.py
'''create a new repo'''

from .base import Base
import requests

from .utils import set_token, cinput

class New(Base):

    @set_token
    def run(self, basicauth):
        
        if self.options['<repo_name>'] is not None:
            print('named repo flow')
        else:
            name = cinput('Repo name: ', expression=r'^[a-z|A-Z|0-9|\-\_]*$', error_message='use an e')
            description = input('Description (optional): ')
