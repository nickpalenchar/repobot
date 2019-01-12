"""
rbot pr new - CREATE PULL REQUESTS

Usage:
    rbot pr new
    rbot pr new -i [--repo=<repo>]
    rbot pr new <base_branch> [<compare_branch>]
    rbot pr new <repo>/<base_branch> [<compare_branch>]
    rbot pr new <repo>/<base_branch> [<repo>/<compare_branch>]
    rbot pr new <owner>/<repo>/<base_branch> [<repo>/<compare_branch>]

Options:
    -i      Run in interactive mode. This will prompt the user to select
            base and compare branches from a repo the user was currently
            in when running repobot, unless --repo was specified

    --repo  Specify a repo for the pull request.

Description:
    TODO
"""

import sys
from repobot.commands.base import Base
from repobot.commands.utils import set_token
from repobot.commands.utils import absdirname
import subprocess
import requests
import keyring

class New(Base):

    @set_token
    def run(self, basicauth):
        if self.options['-i']:
            return _interactivemode()

        base_branch = self._parsebranchformat(self.options['<base_branch>'] or self._getdefaultbranch())
        compare_branch = self._parsebranchformat(self.options['<compare_branch>'] or self._getcurrentbranch())

        message = self._promptmessage()

    def _parsebranchformat(self, branch):
        """Returns a list as [owner, repo, branch] list. Fills in missing values with defaults"""
        sections = branch.split('/')
        if len(sections) > 3:
            print("Syntax error: branch string contains too many slashes (%s)" % branch)
            sys.exit(1)
        if len(sections) == 1:
            sections.insert(0, self._parsecurrentbranch())
        if len(sections) == 2:
            sections.insert(0, keyring.get_password('repobot', 'username'))
        return sections


    def _interactivemode(self):
        pass

    def _getdefaultbranch(self):
        """Gets the default branch from github (usually master)"""
        print('current >>>>' + absdirname(__file__))
        res = None 
        try:
            res = subprocess.check_output(". %s/%s" %(absdirname(__file__), "getdefaultbranch.sh"), shell=True)
        except subprocess.CalledProcessError as ex:
            print('oh an error')
            print(ex.__dict__)
        print('HIOOOOUEOHUSEOHUNEOHUTNEOHUTNSOH')
        print(res.strip(b'\n'))
        sys.exit()

    def _parsecurrentbranch(self):
        """Gets the branch currently on"""
        return subprocess.check_output("sh %s/%s" % (absdirname(__file__), "parsecurrentbranch.sh"))

    def _promptmessage(self):
        pass


        print('opiton')
        print(self.options)
        print('running the pr')
