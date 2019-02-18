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
    -A                  Automatically writes 'merge COMPARE into BASE branch' as the PR message

    -i                  Run in interactive mode. This will prompt the user to select
                        base and compare branches from a repo the user was currently
                        in when running repobot, unless --repo was specified

    --message <text>    Sets the message as a one-liner of <text>. No markdown is supported here.

    --title <text>      Set the title of the pull request

    --repo              Specify a repo for the pull request.

Description:
    TODO
"""
import sys
import re
import json
from colorama import init, Fore, Style
from repobot.commands.base import Base
from repobot.commands.utils import set_token
from repobot.commands.utils import absdirname, allowescape, editorprompt
import subprocess
import requests
import keyring

class New(Base):

    @set_token
    def run(self, basicauth):
        if self.options['-i']:
            return _interactivemode()

        base_branch = self._parsebranchformat(self.options['<base_branch>'], self._getdefaultbranch())
        compare_branch = self._parsebranchformat(self.options['<compare_branch>'], self._getcurrentbranch())
        message = self.options.get('<commitMessage>') or self._promptmessage()
        self.__postpr(base_branch, compare_branch, message)


    def _parsebranchformat(self, branch, fallback_branch=None):
        """Returns a list as [owner, repo, branch] list. Fills in missing values with defaults"""
        sections = branch.split('/') if branch is not None else []

        print(sections)
        if len(sections) > 3:
            print("Syntax error: branch string contains too many slashes (%s)" % branch)
            sys.exit(1)
        if len(sections) == 0:
            sections.insert(0, fallback_branch)
        if len(sections) == 1:
            sections.insert(0, self._getcurrentrepo())
        if len(sections) == 2:
            sections.insert(0, keyring.get_password('repobot', 'username'))
        return sections


    def _interactivemode(self):
        pass

    def _getcurrentrepo(self) -> str:
        res = subprocess.check_output(absdirname(__file__) + '/getcurrentrepo.sh')
        return str(res, 'utf-8').strip('\n')

    def _getdefaultbranch(self):
        """Gets the default branch from github (usually master)"""
        #res = None
        try:
            res = subprocess.check_output(". %s/%s" % ( absdirname(__file__), "getdefaultbranch.sh" ), shell=True)
        except subprocess.CalledProcessError as ex:
            if ex.returncode == 10:
                print('ERROR: multiple remotes detected. Repobot only supports repositories with one remote')
                sys.exit(10)
            else:
                print(ex.__dict__)
                print('ERROR: an unknown error occured :(')
                sys.exit(ex.returncode)
        return str(res, 'utf-8').strip('\n')


    def _getcurrentbranch(self):
        """Gets the branch currently on"""
        res = subprocess.check_output(". %s/%s" % (absdirname(__file__), "getcurrentbranch.sh"), shell=True)
        return str(res, 'utf-8').strip('\n')


    @allowescape
    def _promptmessage(self):
        initial_message="""

%-------%
Write your commit message above the percent divider; Everything below it will be ignored
To abort, quit with a blank message (or quit without saving)
You can set your editor explicitly in your shell with `export EDITOR=vim`, for example.
        """
        res = editorprompt(text=initial_message.encode('utf-8'))
        message = ''
        for i in res.split('\n'):
            if i == '%-------%':
                break
            message += i + '\n'
        message = message.strip()

        if bool(message) is False:
            print('PR comment blank or unchanged. Aborting')
            sys.exit(2)

        return message

    @set_token
    def __postpr(self, base_branch, compare_branch, message, basicauth):
        POST_URL = 'https://api.github.com/repos/%s/%s/pulls' % (base_branch[0],
                                                                 base_branch[1],)
        data = {'title': self.options.get('<commitTitle>', 'Merge %s:%s into %s:%s' % \
                         (compare_branch[0], compare_branch[2], base_branch[0], base_branch[2])),
                'head': compare_branch[2] if compare_branch[0] == base_branch[0] else '%s:%s'%(compare_branch[0],compare_branch[2]),
                'base': base_branch[2],
                'body': message}

        res = requests.post(POST_URL, auth=basicauth, json=data)
        # success is 201
        if res.status_code != 201:
            print(Fore.RED + 'Pull request not created.' + Style.RESET_ALL)
            print(json.dumps(res.json(), indent=2))
        else:
            print(Fore.GREEN + 'Pull request created.' + Style.RESET_ALL)
            print('View it at %s' % res.json()['html_url'])
