import argparse
import asyncio
from bot.main import main

class ManageProj:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Manage your project")
        self.subparsers = self.parser.add_subparsers(dest="command")

        # Define commands
        self.add_command('runserver', self.runserver)

    def add_command(self, name, func):
        parser = self.subparsers.add_parser(name)
        parser.set_defaults(func=func)

    def runserver(self, args):
        print("Starting the server...")
        asyncio.run(main())


    def execute(self):
        args = self.parser.parse_args()
        if hasattr(args, 'func'):
            args.func(args)
        else:
            self.parser.print_help()

if __name__ == "__main__":
    manager = ManageProj()
    manager.execute()
