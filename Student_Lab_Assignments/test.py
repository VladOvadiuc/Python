import unittest
from repository import Repository
from domain import Student
from repository import RepositoryException
from StudControllerWithUndo import *
from AssigControllerWithUndo import *
from GradeController import *
from controller import Controller
repo=Repository()
studRepo=Repository()
assigRepo=Repository()
gradeRepo=Repository()

class Test(unittest.TestCase):

    def testRepository(self):
        self.assertEqual(len(repo),0)
        s=Student(12,"Anamaria",900)
        repo.add(s)
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo.getAll(),[s])
        #self.assertRaises(RepositoryException,repo.add,s)
        s2=Student(12,"Ana",901)
        s3=Student(1,"Ben",908)
        self.assertRaises(RepositoryException,repo.remove,s3)
        x=repo.update(s,s2)
        self.assertEqual(x,s2)
        repo.remove(s)
        self.assertEqual(len(repo),0)

    def testStudController(self):
        self.studRepo=Repository()
        self._StudController=StudController(self.studRepo)
        self.assertEqual(len(self.studRepo),0)
        self._StudController.add(13,"mara",8)
        self.assertEqual(len(self.studRepo),1)
        self.assertEqual(self._StudController.findGroup(8),True)
        self.assertEqual(self._StudController.findGroup(915),False)
        self.assertEqual(self._StudController.findStudID(1),-1)
        self._StudController.add(14,"George",9)
        self.assertEqual(len(self.studRepo),2)
        self._StudController.remove(13)
        self.assertEqual(len(self.studRepo), 1)
        self._StudController.removeAllStud()
        self.assertEqual(len(self.studRepo), 0)

