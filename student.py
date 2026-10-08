class student:
    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.gradez = []
        s.isPassed = "NO"
        s.honor = "?"

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / len(self.gradez)
        return avg

    def checkHonor(self):
        if self.calcaverage() > 90:
            self.honor = True
        else:
            self.honor = False

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + str(self.id))
        print("Name is: " + str(self.name))
        print("Grades Count: " + str(len(self.gradez)))
        print("Honor Student: " + str(self.honor))
        print("Final Grade = " + str(self.letter))


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades(50)  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(0)  # IndexError
    a.report()


startrun()
