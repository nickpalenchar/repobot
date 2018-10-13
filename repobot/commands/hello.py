# repobot/commands/hello.py
'''Test hello command'''

from .base import Base
from json import dumps

class Hello(Base):
    '''say hello world'''

    def run(self):
        print('Hello, world!')
        print('You suplied the following optons:', dumps(self.options, indent=2, sort_keys=True))
