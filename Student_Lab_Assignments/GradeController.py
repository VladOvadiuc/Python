class GradeController:

    def __init__(self,gradeRepo):
        self.__gradeRepo = gradeRepo

    def addHW(self,assig):
        '''
        add an assignment to the repository
        :param assig: the assignment to be added
        :return:
        '''
        self.__gradeRepo.add(assig)

    def getAllGrade(self):
        '''
        :return: the repository for grades
        '''
        return self.__gradeRepo.getAll()

    def removeStud(self,stud):
        self.__gradeRepo.remove(stud)

    def remove(self,ID):
        '''
        removes a grade by the id of student
        :param ID: the id of student
        :return:
        '''
        while self.findGradeID(ID):
            self.removeID(ID)

    def findGradeID(self,ID):
        '''
        Searches for the id of an assignemt
        :param ID: the id
        :return: true/false if is found or not
        '''
        for i in range(len(self.__gradeRepo.getAll())):
            s = self.__gradeRepo.getAll()[i]
            if s.getID() == ID:
                return True
        return False

    def findGrade(self,x):
        '''
        searches for a grade by the id of an assignment
        :param x: the id of the assignment
        :return: the position of the grade/-1 if not found
        '''
        for i in range(len(self.__gradeRepo)):
            s=self.__gradeRepo.getAll()[i]
            if s.getS()==x:
                return i
        return -1

    def removeID(self,ID):
        exist=True
        while exist==True:
            exist=False
            for s in self.__gradeRepo.getAll():
                if s.getID()==ID:
                    self.__gradeRepo.remove(s)
                    exist=True

    def removeS(self,ID):
        exist=True
        while exist==True:
            exist=False
            for s in self.__gradeRepo.getAll():
                if s.getS()==ID:
                    self.__gradeRepo.remove(s)
                    exist=True

    def removeGradeS(self,ID):
        '''
        removes a grade by the id of assignment
        :param ID: the id of the assignment
        '''
        while self.findGrade(ID) !=-1:
            self.removeS(ID)

    def removeAllGrade(self):
        '''
        removes all the grades
        '''
        self.__gradeRepo.removeAll()

    def findHW(self,s,a):
        '''
        searches if a given student has a given assignment
        :param s: the id of student
        :param a: the id of assignment
        :return: true/false if that student has already recieve the assignment
        '''
        for i in range(len(self.__gradeRepo.getAll())):
             x = self.__gradeRepo.getAll()[i]
             if x.getID() == s and x.getS() == a:
                return True
        return False

    def grade(self,s,a,g):
        '''
        sets the grade of a student
        :param s: the id of the student to be graded
        :param a: the id of the assignment
        :param g: the grade
        :return: true/false if the student recieved the assignemt and the grade was 0
        '''
        for c in self.__gradeRepo.getAll():
            if c.getID() == s and c.getS()==a and c.get()==0:
                old=c
                c.set(g)
                new=c
                self.__gradeRepo.update(old, new)
                return True
        return False
