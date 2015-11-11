


import sys

from jam.command import Command

from unittest.mock import MagicMock
from unittest import TestCase as BaseTestCase



class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        self.command = Command(sys.stdout)
        sys.stdout.write = MagicMock()
