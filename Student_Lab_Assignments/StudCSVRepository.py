from repository import Repository
from domain import Student

class StudCSVRepository(Repository):
    def __init__(self, fileName):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def add(self, stud):
        Repository.add(self, stud)
        self.__storeToFile()

    def delete(self, studId):
        Repository.remove(self, studId)
        self.__storeToFile()

    def update(self,old,new):
        Repository.update(self,old,new)
        self.__storeToFile()

    def __loadFromFile(self):

            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                stud = Student(int(attrs[0]), attrs[1], attrs[2])
                Repository.add(self, stud)
                line = f.readline().strip()

            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        studs = Repository.getAll(self)
        for s in studs:
            strf = str(s.getID()) + "," + s.getName() + "," + str(s.getGroup())+ "\n"
            f.write(strf)
        f.close()
