


import pytest
import sys

from jam.tests.main import TestCase


class InitTestCase(TestCase):

    def test_init(self):
        self.command.dispatch(['init'])

        sys.stdout.write.assert_called_with('Command init')
