#!/usr/bin/env python3
from Portal import Portal
import os

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

    def printDev(self):
        print(os.environ["DEV_PROGRA"])
        print("==========================")

    def start(self, args):
        self.printDev()
        self.getProgramNumber(args)