


import sys
import logging

from .topCommand import Command
from .topCommand import UnknownCommand
from .topCommand import InvalidCommandModule



def main():
    try:
        command = Command(sys.stdout)
        command.dispatch(sys.argv[1:])
    except UnknownCommand as exception:
        sys.stderr.write(exception.message)
        exit(2)
    except InvalidCommandModule as exception:
        sys.stderr.write(exception.message)
        exit(3)
