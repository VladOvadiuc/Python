from domain import Assignment
class AssigController:

    def __init__(self,assigRepo):
        self.__assigRepo = assigRepo

    def findID(self, ID):
        '''
        Search an assignment by it's id
        :param ID: the id to be found
        :return: true / false if the id is found or not
        '''
        for i in range(len(self.__assigRepo.getAll())):
            s = self.__assigRepo.getAll()[i]
            if s.getID() == ID:
                return s
        return -1

    def add(self,assigID,desc,deadline):
        '''
        Add a assignment in repository
        :param assig: the assignment to be added
        '''
        assig=Assignment(assigID,desc,deadline)
        self.__assigRepo.add(assig)
        return assig

    def remove(self,ID):
        '''
        Remove an assignment by id
        :param pos: the id of assignment to remove
        '''

        exist = True
        while exist == True:
            exist = False
            for s in self.__assigRepo.getAll():
                if s.getID() == ID:
                    self.__assigRepo.remove(s)
                    exist = True
                    return s

    def removeAllAssig(self):
        '''
        removes all asignments from repository
        '''
        self.__assigRepo.removeAll()



    def getAllAssig(self):
        '''
        :return: the repository for assignments
        '''
        return self.__assigRepo.getAll()



    def update(self,id,descr,deadline):
        '''
        update the description and the deadline of an assignment BY ID
        :param id: the id of the assignment to update
        :param descr: the new description
        :param deadline: the new deadline
        '''
        for s in self.__assigRepo.getAll():
            if s.getID()==id:
                old=s
                s.setDescription(descr)
                s.setDeadline(deadline)
                new=s
                return self.__assigRepo.update(old, new)

