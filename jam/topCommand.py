


import sys

from docopt import docopt
from docopt import DocoptExit
from inspect import getdoc

from .command import *


def get_options(docstring, arguments):
    try:
        return docopt(docstring, arguments)
    except DocoptExit:
        raise SystemExit(docstring)



def get_handler(self, commandKey):

    g = globals()

    if not commandKey in g.keys():
        return False

    module = g[commandKey]

    if not hasattr(module, commandKey.title()):
        raise InvalidCommandModule(commandKey)

    commandClass = getattr(g[commandKey], commandKey.title())
    command = commandClass(self.out)

    return command.run



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

        handler = get_handler(self, command)

        if handler == False:
            raise UnknownCommand(command, self)

        docstring = getdoc(handler)

        if docstring is None:
            raise UnknownCommand(command, self)

        handler(options)



class UnknownCommand(Exception):
    def __init__(self, command, supercommand):
        self.message = "Unknown command: %s" % command
        super(UnknownCommand, self).__init__(self.message)

        self.command = command
        self.supercommand = supercommand



class InvalidCommandModule(Exception):
    def __init__(self, module):
        self.message = "Module %s must declare %s class" % (module, module.title())

        super(InvalidCommandModule, self).__init__(self.message)
