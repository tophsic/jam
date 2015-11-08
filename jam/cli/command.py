


import sys

from docopt import docopt
from docopt import DocoptExit
from inspect import getdoc



def get_options(docstring, arguments):
    try:
        return docopt(docstring, arguments)
    except DocoptExit:
        raise SystemExit(docstring)



class Command(object):
    """Run daily common task in Docker+Compose environment

    Usage:
        jam [COMMAND] [ARGS...]
        jam -h|--help

    Commands:
        init        Initialize dev environment
        run         Run command in Compose environment
        stop        Stop environment
        up          Start environment
    """

    def dispatch(self, arguments):
        options  = get_options(getdoc(self), arguments)

        command = options['COMMAND']

        if command is None:
            raise SystemExit(getdoc(self))

        if not hasattr(self, command):
            raise UnknownCommand(command, self)



class UnknownCommand(Exception):
    def __init__(self, command, supercommand):
        super(UnknownCommand, self).__init__("Unknown command: %s" % command)

        self.command = command
        self.supercommand = supercommand
