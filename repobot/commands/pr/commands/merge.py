"""
rbot pr new - CREATE PULL REQUESTS

Usage:
    rbot pr merge
    rbot pr merge <ownerRepo>
    rbot pr merge <ownerRepo> <pullReqId> [--force|-f]

Description:
    Merge a pull request. In the first format, will promt the user to chose from a
    list of open requests, as determined by the git repository the user is in.

    In the second format, will prompt the user to chose from a list of open requests
    as specified in the <repo> repositoy.

    In the third request, will promp
"""
import sys
import re
import json
from colorama import init, Fore, Style, Back
from repobot.commands.base import Base
from repobot.commands.utils import set_token, absdirname, allowescape, editorprompt, yn_input
import subprocess
import requests
import keyring
from .new import New

class Merge(New):

    @allowescape
    @set_token
    def run(self, basicauth):
        pass


    def _parsebranchformat(self, branch, fallback_branch=None):
        """Returns a list as [owner, repo, branch] list. Fills in missing values with defaults"""
        sections = branch.split('/') if branch is not None else []

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

    @set_token
    def _getprs(self, repo=None) -> list:
        if repo is None:
            repo = _getcurrentrepo()


        res = requests.post(POST_URL, auth=basicauth, json=data)

        # Accept header: application/vnd.github.symmetra-preview+json for emojis
    def _parseownerrepoformat(self, ownerRepo) -> dict:
        if '/' not in ownerRepo:
            owner = keyring.get_password('repobot', username)
            user = ownerRepo
        else:
            [owner, user] = ownerRepo.split('/')




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
    def __postmerge(self, base_branch, compare_branch, message, basicauth):
        pass
