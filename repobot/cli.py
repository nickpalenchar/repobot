"""
repobot

Usage:
    rbot login
    rbot new [<repo_name>] [-DC] [--private]
    rbot info <repo_name>
    rbot pr [<repo_name] [<branch]
    rbot hello [<world>] [--name=<yours>]
"""

from inspect import getmembers, isclass

from docopt import docopt

#from . import __version__ as VERSION
VERSION='1.0.0'

def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            rcommands = getmembers(module, isclass)
            command = [command[1] for command in rcommands if command[0] != 'Base'][0]
            command = command(options)
            command.run()

if __name__ == '__main__':
    main()
