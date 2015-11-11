


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

    def __init__(self, out):
        self.out = out

    def dispatch(self, arguments):
        options  = get_options(getdoc(self), arguments)

        command = options['COMMAND']

        if command is None:
            raise SystemExit(getdoc(self))

        if not hasattr(self, command):
            raise UnknownCommand(command, self)

        handler = getattr(self, command)
        docstring = getdoc(handler)

        if docstring is None:
            raise UnknownCommand(command, self)

        handler(options)

    def init(self, options):
        """Init command
        """
        self.log('Command init')

    def log(self, message):
        self.out.write(message)



class UnknownCommand(Exception):
    def __init__(self, command, supercommand):
        self.message = "Unknown command: %s" % command
        super(UnknownCommand, self).__init__(self.message)

        self.command = command
        self.supercommand = supercommand
