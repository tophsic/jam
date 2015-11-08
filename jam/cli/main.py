


import sys
import logging

from .command import Command



def main():
    command = Command()
    command.dispatch(sys.argv[1:])
