


import pytest
import sys

from jam.topCommand import UnknownCommand
from jam.topCommand import InvalidCommandModule
from jam.tests.main import TestCase


class CommandTestCase(TestCase):

    def test_no_command(self):
        with pytest.raises(SystemExit):
            self.command.dispatch([])

    def test_unknown_command(self):
        with pytest.raises(UnknownCommand):
            self.command.dispatch(['unknown'])

    def test_no_docstring(self):
        with pytest.raises(UnknownCommand):
            self.command.dispatch(['log'])

    def test_invalid_module(self):
        with pytest.raises(InvalidCommandModule):
            self.command.dispatch(['getdoc'])
