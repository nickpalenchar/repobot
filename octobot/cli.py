"""
octobot

Usage:
    oct createrepo <repo_name>
    oct authenticate <username> <token>

"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import octobot.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(octobot.commands, k) and v:
            module = getattr(octobot.commands, k)
            octobot.commands = getmembers(module, isclass)
            command = [command[1] for command in octobot.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()

if __name__ == '__main__':
    main()
