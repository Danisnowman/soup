class Address:
    name = ""
    faculty = ""
    number = ""

    def __init__(self, faculty, name, number):
        self.faculty = faculty
        self.name = name
        self.number = number


    def getFaculty(self):
        return self.faculty

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number
        