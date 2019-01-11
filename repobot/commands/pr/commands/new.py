"""
rbot pr new - CREATE PULL REQUESTS

Usage:
    rbot pr new
    rbot pr new -i [--repo=<repo>]
    rbot pr new <base_branch> [<compare_branch>]
    rbot pr new <repo>/<base_branch> [<compare_branch>]
    rbet pr new <repo>/<base_branch> [<repo>/<compare_branch>]

Options:
    -i      Run in interactive mode. This will prompt the user to select
            base and compare branches from a repo the user was currently
            in when running repobot, unless --repo was specified

    --repo  Specify a repo for the pull request.

Description:
    TODO
"""

from repobot.commands.base import Base
from repobot.commands.utils import set_token
import requests

class New(Base):

    @set_token
    def run(self, basicauth):
        if self.options['-i']:
            return _interactivemode()

        base_branch = self._addrepotobranch(self.options['<base_branch>'] or self._getdefaultbranch())
        compare_branch = self._addrepotobranch(self.options['<compare_branch>'] or self._getcurrentbranch())

        message = self._promptmessage()

    def _interactivemode(pass):
        pass

    def _getdefaultbranch(pass):
        """Gets the default branch from github (usually master)"""

    def _parsecurrentbranch(pass):
        """Gets the branch currently on"""

    def _promptmessage(self):
        pass


        print('opiton')
        print(self.options)
        print('running the pr')
