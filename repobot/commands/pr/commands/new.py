"""
rbot pr new - CREATE PULL REQUESTS

Usage:
    rbot pr new
    rbot pr new <base_branch> [<compare_branch>]

Options:
"""

from repobot.commands.base import Base
from repobot.commands.utils import set_token
import requests

class New(Base):

    @set_token
    def run(self, basicauth):
        print('opiton')
        print(self.options)
        print('running the pr')
