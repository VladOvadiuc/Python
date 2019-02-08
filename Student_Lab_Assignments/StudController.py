from domain import Student
class StudController:

    def __init__(self, studRepo):
        self._repository = studRepo

    def findStudID(self,ID):
        '''
                Search a if an ID is in studRepo
                :param ID: the id to be found
                :return: true or false if the id is found
                '''

        for i in range(len(self._repository.getAll())):
            s = self._repository.getAll()[i]
            if s.getID() == ID:
                return s
        return -1

    def findGroup(self,g):
        '''
        Search a if a group is in studRepo
        :param g: the group to be found
        :return: true or false if the group is found
        '''

        for i in range(len(self._repository.getAll())):
             s = self._repository.getAll()[i]
             if s.getGroup() == g:
                 return True
        return False


    def add(self, StudID,name,group):
        '''
        Add a student to the repository
        :param stud: the student to be added
        :return: the updated repository for students
        '''
        stude = Student(StudID, name, group)
        self._repository.add(stude)
        return stude

    def remove(self,ID):
        '''
        Removes a student BY ID
        :param id: the id of the student to be removed
        :return: the updated repository for students
        '''
        exist = True
        while exist == True:
            exist = False
            for s in self._repository.getAll():
                if s.getID() == ID:
                    self._repository.remove(s)
                    exist = True
                    return s

    def removeAllStud(self):
        '''
        removes all the students from repository
        '''
        self._repository.removeAll()

    def getAllStudent(self):
        '''

        :return: the repository for students
        '''
        return self._repository.getAll()

    def update(self,id,name,group):
        '''
        updates the name and the group of a student BY ID
        :param id: the id of student to update
        :param name: the the new name
        :return:
        '''
        for s in self._repository.getAll():
            if s.getID() == id:
                old=s
                s.setName(name)
                s.setGroup(group)
                new=s
                print(self._repository.update(old,new))
                return self._repository.update(old,new)


