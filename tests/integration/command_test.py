


import pytest
import sys

from jam.command import UnknownCommand
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
