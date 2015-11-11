


class Init:

    def __init__(self, out):
        self.out = out

    def run(self, options):
        """Init command
        """

        self.log('Command init')

    def log(self, message):
        self.out.write(message)
