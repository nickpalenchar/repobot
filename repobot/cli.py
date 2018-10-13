"""
repobot

Usage:
    rbot add [<repo_name>]
    rbot info <repo_name>
    rbot pr [<repo_name] [<branch]
    rbot hello
"""

from inspect import getmembers, isclass

from docopt import docopt

#from . import __version__ as VERSION
VERSION='1.0.0'

def main():
    """Main CLI entrypoint."""
    import repobot.commands
    options = docopt(__doc__, version=VERSION)
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        print('try ', k)
        print(hasattr(repobot.commands, k))
        if hasattr(repobot.commands, k) and v:
            print('GOT ONE')
            module = getattr(repobot.commands, k)
            repobot.commands = getmembers(module, isclass)
            command = [command[1] for command in repobot.commands if command[0] != 'Base'][0]
            
            command = command(options)
            print('the command', command)
            print('the func,', command.run)
            command.run()

if __name__ == '__main__':
    main()
