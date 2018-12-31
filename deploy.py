import keyring
import shutil
import sys
import os

print(sys.argv[0])
DIRNAME = os.path.dirname(os.path.realpath(__file__)) 

if 'authenticate' in sys.argv: 
    keyring.set_password('rbotdeploy', 'username', input('username: '))
    keyring.set_password('rbotdeploy', 'pw', input('password: '))

username = keyring.get_password('rbotdeploy', 'username')
password = keyring.get_password('rbotdeploy', 'pw')


shutil.rmtree(os.path.join(DIRNAME, 'dist'))
shutil.rmtree(os.path.join(DIRNAME, 'build'))

os.system('python %s sdist bdist_wheel' % os.path.join(DIRNAME, 'setup.py'))

os.system('twine upload -u %s -p %s %s' % (keyring.get_password('rbotdeploy', 'username'),
                                           keyring.get_password('rbotdeploy', 'pw'),
                                           DIRNAME + '/dist/*',))

