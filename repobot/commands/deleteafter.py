import .utils

@checkshellcommand('git')
def hello():
    print('this sohuld work')

@checkshellcommand('helloooaa')
def nope():
    print('this sohuld not')

hello()
nope()
