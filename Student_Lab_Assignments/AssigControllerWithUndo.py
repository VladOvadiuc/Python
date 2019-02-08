from undoController import *
from AssigController import AssigController


class AssigControllerWithUndo(AssigController):
    def __init__(self, undoController, GradeController, repository):
        AssigController.__init__(self, repository)
        self._GradeController = GradeController
        self._undoController = undoController

    def add(self, assigID, desc, deadline):
        '''
        Adds an assignment
        :param assigID: the id of the assignment
        :param desc: the description
        :param deadline: deadline
        :return: the added assignment
        '''
        assig = AssigController.add(self, assigID, desc, deadline)
        redo = FunctionCall(self.add, assigID, desc, deadline)
        undo = FunctionCall(self.remove, assigID)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        return assig

    def remove(self, assigID):
        '''
        Removes an assignment by it's id
        :param assigID: the id
        :return: the removed assignment
        '''
        assig = AssigController.remove(self, assigID)
        redo = FunctionCall(self.remove, assigID)
        undo = FunctionCall(self.add, assig.getID(), assig.getDesc(), assig.getDeadline())
        operation = Operation(redo, undo)
        for s in self._GradeController.getAllGrade():
            if s.getS() == assigID:
                self._GradeController.removeS(s.getS())
        self._undoController.recordOperation(operation)

        return assig

    def update(self, id, Desc, Deadline):
        '''
        updates an assignemnt
        :param id: the id of the assignment to be updated
        :param Desc: the new description
        :param Deadline: the new deadline
        :return: the updated assignment
        '''
        old = AssigController.findID(self, id)
        undo = FunctionCall(self.update, old.getID(), old.getDesc(), old.getDeadline())
        assig = AssigController.update(self, id, Desc, Deadline)
        redo = FunctionCall(self.update, assig.getID(), assig.getDesc(), assig.getDeadline())

        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        return assig
