"""
repobot

Usage:
    rbot login
    rbot new [<repo_name>] [-DC] [--private --clone --org=<org_name>]
    rbot ls [--params=<param_str>] [--limit <number>|--all]
    rbot pr (new|merge)
    rbot hello [<world>] [--name=<yours>]


Options:
    -D                Use all defaluts.
    --clone           Automatically clone the created repo.
    --org=<org_name>  Create in the <org_name> that you're a member of.
    --limit <number>  For getting lists, shows only the number of entries specified. Overrules --all
    --all             For getting lists, inclued all entries. Is ignored when --limit is set
    --help            Show additional descriptions for any sub commands.

Examples:
    Create a new repository named foo
        rbot new foo

    Create a new private repository named foo and automatically clone it
        rbot new --private -C foo

    Create a new repository named foo in orgization xyzorg, using system defaults
        rbot new --org=xyzorg -D foo
"""

from inspect import getmembers, isclass
from docopt import docopt
import repobot.commands as commands
from repobot import __version__ as VERSION
import sys

def main():
    """Main CLI entrypoint."""

    # First, check if a subcommand was given and automatically reroute if it is.
    delegateIfSubcommand(subcommands=['pr'])

    # intercept help in case sepecific command is also specified
    if '--help' in sys.argv:
        sys.argv.remove('--help')
        options = docopt(__doc__, help=False, version=VERSION)
        options['--help'] = True
    else:
        options = docopt(__doc__, help=False, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            rcommands = getmembers(module, isclass)
            command = [command[1] for command in rcommands if command[0] != 'Base'][0]
            command = command(options)
            command.run()

def delegateIfSubcommand(subcommands=[]):
    if len(sys.argv) is 1:
        return
    if sys.argv[1] in subcommands:
        module = getattr(commands, sys.argv[1])
        rcommands = getmembers(module, isclass)
        subcommand = [command[1] for command in rcommands if command[0] != 'SubcommandBase'][0]
        subcommand = subcommand(sys.argv)
        subcommand.run()
        sys.exit(0)



if __name__ == '__main__':
    main()
