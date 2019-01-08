# repobot/commands/hello.py
'''
rbot pr - MANAGE PULL REQUESTS

Usage:
    rbot pr new
    rbot pr new <compare_branch>
    rbot pr new <base_branch> <compare_branch>
    rbot pr merge
    '''

from ..base import SubcommandBase
from json import dumps
from docopt import docopt
from ..utils import set_token
import requests

class Pr(SubcommandBase):

    def run(self):

        print(self.argv)
        self.options = docopt(__doc__, argv=self.argv[1:], help=True)

        if self.options['new']:
            return self.new()
        if self.options['merge']:
            return self.merge()


        #r = requests.get('https://api.github.com/user', auth=basicauth)
        print(self.argv)
        print(self.options)
        print('the re was')
        print('Hello, from pr!')
        print('You suplied the following optons:', dumps(self.options, indent=2, sort_keys=True))

    @set_token
    def new(self, basicauth):
        if self.options['<base_branch>'] and self.options['<compare_branch>']:
            print('base and compare')

    @set_token
    def merge(self, basicauth):
        print('merge')
