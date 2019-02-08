from Repository import Repository


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

                Repository.add(self, )
                line = f.readline().strip()

            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        words = Repository.getAll(self)
        for s in words:
            strf = str(s.getWord)+ "\n"
            f.write(strf)
        f.close()
