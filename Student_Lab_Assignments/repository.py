class RepositoryException(Exception):
    def __init__(self,message):
        self.__message = message

    def __str__(self):
        return self.__message

from ClassList import *
class Repository:

    def __init__(self):
        self._data =List()

    def add(self,object):
        '''
        add an object to the repository
        :param object: the object
        :return:
        '''
        if self.find(object.getID()) != None:
            pass
            #raise RepositoryException("Element having id=" + str(object.getID()) + " already stored!")
        self._data.append(object)

    def find(self, objectId):
        '''
        Searches fo an id in repository
        :param objectId: the id to search
        :return: the object with the id/ None if is not found
        '''
        for e in self._data:
            if objectId == e.getID():
                return e
        return None

    def remove(self,obj):
        '''
        Removes an object from the repository
        :param obj: the object to be removed
        :return:
        '''
        if self.find(obj.getID()) == None:
            raise RepositoryException("Element having id=" + str(obj.getID()) + " is not stored!")
        self._data.remove(obj)

    def getAll(self):
        '''
        returns the whole repository
        :return:
        '''
        return self._data

    def removeAll(self):
        '''
        clear the repository
        :return:
        '''
        while len(self._data):
            for s in self._data:
                self._data.remove(s)

    def update(self,old,new):
        '''
        Update an object from repo
        :param old: the old value
        :param new: the new value
        :return: the updated object
        '''
        el = self.find(old.getID())
        if el == None:
            raise RepositoryException("Element not found!")
        for s in self._data:
            if s==old:
                s=new
                return s

    def __len__(self):
        return len(self._data)
