


import sys
import logging

from .command import Command
from .command import UnknownCommand



def main():
    try:
        command = Command(sys.stdout)
        command.dispatch(sys.argv[1:])
    except UnknownCommand as exception:
        sys.stderr.write(exception.message)
        exit(2)
