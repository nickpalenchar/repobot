# new.py
'''create a new repo'''
import json
import sys
import requests

from .base import Base
from .utils import set_token, cinput, yn_input, allowescape

class New(Base):

    @set_token
    def run(self, basicauth):
        name = self.getname()
        description = self.getdescription()
        isprivate = self.getprivateoption()
        hasreadme = self.getreadmeoption()

        data = {'name': name,
                'description': description,
                'private': isprivate,
                'auto_init': hasreadme,}
        res = requests.post('https://api.github.com/user/repos', auth=basicauth, json=data)
        if res.status_code == 201:
            resdata = res.json()
            print('Successfully created at ' + resdata['clone_url'])
            #@TODO: Finish self.cloneprompt for git cloning automatically
        else:
            print('Couldn\'t create repo')
            print(json.dumps(res.json(), indent=2))

    @allowescape
    def getname(self):
        if self.options['<repo_name>'] is not None:
            return self.options['<repo_name>']
        return cinput('Repo name: ',
                      expression=r'^[a-z|A-Z|0-9|\-\_]*$',
                      error_message='Invalid name - use [a-z|A-Z|0-9|-_] characters only.')

    @allowescape
    def getdescription(self):
        if self.options['-D'] is not False:
            return ''
        return input('Description (optional): ')

    @allowescape
    def getprivateoption(self) -> bool:
        if self.options['-D']:
            return 'false'
        if self.options['--private']:
            return 'true'
        return yn_input('Private Repository? ', default=False)

    @allowescape
    def getreadmeoption(self) -> bool:
        if self.options['-D'] is not False:
            return 'false'
        return yn_input('Initialize with a README? ', default=False)

    @allowescape
    def cloneprompt(self, cloneurl):
        if self.options['-C'] or yn_input('Clone into current working directory now? ', default=False):
            args = ['git', 'clone', cloneurl]
            return subprocess.run(args, shell=True, check=True)
