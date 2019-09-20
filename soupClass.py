#!/usr/bin/env python3
from Portal import Portal

class SOUP():
    portal = None

    def __init__(self):
        self.portal = Portal("http://ufm.edu/Portal")

    def programOne(self):
        self.portal.run()

    def programTwo(self):
        print(f"Running {self.programTwo}")

    def programThree(self):
        print(f"Running {self.programTwo}")

    def exec(self, Program):
        Program(self)

    programNumber = {
        1 : programOne,
        2 : programTwo,
        3 : programThree,
    }

    def getProgramNumber(self, args):
        for eachInt in args.integers:
            program = self.programNumber.get(int(eachInt))
            self.exec(program)

    def start(self, args):
        self.getProgramNumber(args)