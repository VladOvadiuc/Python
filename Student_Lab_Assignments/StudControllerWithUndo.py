from undoController import *
from StudController import StudController


class StudControllerWithUndo(StudController):
    def __init__(self,undoController,GradeController,repository):
        StudController.__init__(self,repository)
        self._GradeController = GradeController
        self._undoController = undoController

    def add(self,StudID,name,group):
        '''
        Adds an student
        :param StudID: the id
        :param name: the name of stud
        :param group: the group
        :return: the added student
        '''
        student=StudController.add(self,StudID,name,group)
        redo=FunctionCall(self.add,StudID,name,group)
        undo=FunctionCall(self.remove,StudID)
        operation = Operation(redo,undo)
        self._undoController.recordOperation(operation)
        return student

    def remove(self,StudID):
        '''
        Removes a student by it's id
        :param StudID: the id of the student
        :return: the removed student
        '''
        student=StudController.remove(self,StudID)
        redo = FunctionCall(self.remove,StudID)
        undo = FunctionCall(self.add,student.getID(),student.getName(),student.getGroup())
        operation = Operation(redo, undo)
        for s in self._GradeController.getAllGrade():
            if s.getID() == StudID:
                self._GradeController.remove(s.getID())
        self._undoController.recordOperation(operation)

        return student

    def update(self,id,name,group):
        '''
        Updates a student
        :param id: the id of the student
        :param name: the new name
        :param group: the new group
        :return: the updated student
        '''
        old=StudController.findStudID(self,id)
        undo = FunctionCall(self.update, old.getID(), old.getName(), old.getGroup())
        student = StudController.update(self, id,name,group)
        redo = FunctionCall(self.update, student.getID(),student.getName(),student.getGroup())

        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        return student


