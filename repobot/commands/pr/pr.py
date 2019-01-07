# repobot/commands/hello.py
'''pr - MANAGE PULL REQUESTS

Usage:
    rbot pr create
    rbot pr create <compare_branch>
    rbot pr create <base_branch> <compare_branch>
    rbot pr merge
    '''

from ..base import Base
from json import dumps

from ..utils import set_token
import requests

class Pr(Base):

    @set_token
    def run(self, basicauth):       
        r = requests.get('https://api.github.com/user', auth=basicauth)
        print('the re was', r)
        print('Hello, world!')
        print('You suplied the following optons:', dumps(self.options, indent=2, sort_keys=True))
