


from jam.cli.command import Command
from jam.cli.command import UnknownCommand
from unittest import TestCase
import pytest



class InitTestCase(TestCase):

    @classmethod
    def setUpClass(self):
        self.command = Command()

    def test_no_command(self):
        with pytest.raises(SystemExit):
            self.command.dispatch([])

    def test_unknown_command(self):
        with pytest.raises(UnknownCommand):
            self.command.dispatch(['unknown'])
