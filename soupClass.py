#!/usr/bin/env python3
from Portal import Portal
from Estudios import Estudios
from CS import CS
from Directorio import Directorio
import os, shutil

class SOUP():
    portal = None
    estudios = None
    cs = None
    directorio = None

    def __init__(self):
        self.portal = Portal("http://ufm.edu/Portal")
        self.estudios = Estudios("http://ufm.edu/Estudios")
        self.cs = CS("https://fce.ufm.edu/carrera/cs/")
        self.directorio = Directorio("https://www.ufm.edu/Directorio")

    def programOne(self):
        self.portal.run()

    def programTwo(self):
        self.estudios.run()

    def programThree(self):
        self.cs.run()

    def programFour(self):
        self.directorio.run()

    def exec(self, Program):
        Program(self)

    programNumber = {
        1 : programOne,
        2 : programTwo,
        3 : programThree,
        4 : programFour
    }

    def getProgramNumber(self, args):
        for eachInt in args.integers:
            program = self.programNumber.get(int(eachInt))
            self.exec(program)

    def printDev(self):
        print(os.environ["DEV_PROGRA"])

    def start(self, args):
        if args.integers is None:
            args.integers = [1,2,3,4]
        self.printDev()
        self.getProgramNumber(args)
        