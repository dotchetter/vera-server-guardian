from pyttman import Feature
from pyttman.core.communication.command import Command


class FooCommand(Command):
    pass


class GuardianFeature(Feature):
    commands = (FooCommand,)
