from datetime import *
from domain import Grade
class UI:
    def __init__(self  ,controller , StudControllerWithUndo,AssigControllerWithUndo,GradeController,undoController):
        self._StudControllerWithUndo = StudControllerWithUndo
        self._AssigControllerWithUndo = AssigControllerWithUndo
        self._GradeController = GradeController
        self._controller = controller
        self._undoController= undoController

    def readCommand(self):
        cmd=input("command: ")
        if cmd.find(" ")==-1:
            command=cmd
            params=""
        else:
            command = cmd[0:cmd.find(" ")]
            params = cmd[cmd.find(" "):]
            params = params.split(",")
            for i in range(0, len(params)):
                params[i] = params[i].strip()
        return (command,params)

    def helpCommand(self):
        print("1.Add")
        print("\t Student or Assignment ")
        print("2.Remove ")
        print("\t Student or Assignment")
        print("3.Update ")
        print("\t Student name/group or Assignment description/deadline")
        print ("4. List")
        print("\t Students or Assignments or Homework or Grades")
        print("5. Give assignment")
        print("\t Student or Group")
        print ("6.Grade student")
        print ("Statistics")
        print (" \t 7.All students who received a given assignment ")
        print(" \t 8. All students who are late in handing in at least one assignment")
        print(" \t 9.Best students")
        print(" \t 10.All assignments for which there is at least one grade")
        print(".Help")
        print(".Exit")


    def start(self):

        UI.helpCommand(self)
        while True:
            command = input("command: ")
            if command=="add" or command=="1":
                UI.readStudOrAssig(self)
            elif command=="remove" or command=="2":
                UI.removeCommand(self)
            elif command=="list" or command=="4":
                UI.listCommand(self)
            elif command=="remove all":
                UI.removeAll(self)
            elif command=="give" or command=="5":
                UI.giveCommand(self)
            elif command=="update" or command=="3":
                UI.updateCommand(self)
            elif command=="grade"or command=="6":
                UI.gradeCommand(self)
            elif command== "exit":
                return []
            elif command=="help":
                UI.helpCommand(self)
            elif command=="recieve" or command=="7":
                UI.recieveCommand(self)
            elif command=="late" or command=="8":
                UI.lateCommand(self)
            elif command=="best" or command=="9":
                UI.bestCommand(self)
            elif command=="10":
                UI.command10(self)
            elif command=="undo":
                try:
                    self._undoController.undo()
                except :print("No operation to undo")
            elif command=="redo":
                try:
                    self._undoController.redo()
                except :print("No operation to redo")


            else:
                print("========INVALID COMMAND========")


    def readStudOrAssig(self):
        '''
        Reads aa student or an assignment
        :return:
        '''
        c = input("Stud or Assig ? ")
        if c == "Stud" or c == "stud":
            try:
                i = int(input("Student ID: "))
                n = input("Name: ")
                g = int(input("Group: "))
                if self._StudControllerWithUndo.findStudID(i) == -1:
                    self._undoController.newOperation()
                    self._StudControllerWithUndo.add(i,n,g)
                else:
                    print("===== Invalid Student =====")
            except: print ("")
        elif c == "Assig" or c == "assig":
            try:
                i = int(input("Assignment ID: "))
                d = input("Description: ")
                print("Deadline: ")
                y = int(input("give year "))
                m = int(input("give month "))
                z = int(input("give day "))
                x = date(y, m, z)
                if self._AssigControllerWithUndo.findID(i) == -1:
                    self._undoController.newOperation()
                    self._AssigControllerWithUndo.add(i,d,x)
                else:
                    print("===== Invalid Assignment =====")
            except:
                print("")

    def removeCommand(self):
        '''
        Removes an assignment or a student
        :return:
        '''
        c = input("Stud or Assig ? ")
        if c=="Stud" or c=="stud":

            try:
                pos = int(input("Give ID : "))
                self._undoController.newOperation()
                self._StudControllerWithUndo.remove(pos)
            except:
                print("===== Invalid Position ===== ")
        elif c=="Assig" or c=="assig":
            try:
                pos = int(input("Give ID : "))

                self._undoController.newOperation()
                self._AssigControllerWithUndo.remove(pos)
            except:
                print("===== Invalid Position ===== ")

    def removeAll(self):
        '''
        Clears the repository
        :return:
        '''
        c=input("Stud or Assig or grade : ")
        if c=="stud":
            self._StudControllerWithUndo.removeAllStud()
        elif c=="assig":
            self._AssigControllerWithUndo.removeAllAssig()
        elif c=="grade":
            self._GradeController.removeAllGrade()
        else: print ("Invalid")

    def updateCommand(self):
        '''
        updates the name/group of a student or the description/deadline of an assignment
        :return:
        '''
        x=input("stud or assig? : ")
        if x=="stud":
            try:
                y=int(input("what id? : "))
                q=self._StudControllerWithUndo.findStudID(y)
                if q != -1:
                    z=input("what to update? name or group? ")
                    if z=="name":
                        n=input("give name : ")
                        self._undoController.newOperation()
                        self._StudControllerWithUndo.update(y,n,q.getGroup())
                    elif z=="group":
                        n=int(input("give group : "))
                        self._undoController.newOperation()
                        self._StudControllerWithUndo.update(y, q.getName(),n)
                    else: print("===== Invalid Input ===== ")
                else:
                    print("===== Invalid ID ===== ")
            except:
                print("")
        elif x=="assig":
            try:
                y = int(input("what id? "))
                q = self._AssigControllerWithUndo.findID(y)
                if q!=-1:
                    z = input("what to update? description or deadline? : ")
                    if z == "description":
                        n = input("give description : ")
                        self._undoController.newOperation()
                        self._AssigControllerWithUndo.update(y, n,q.getDeadline())
                    elif z == "deadline":
                        try:
                            d = int(input("give year "))
                            m = int(input("give month "))
                            z = int(input("give day "))
                            x = date(d, m, z)
                            self._undoController.newOperation()
                            self._AssigControllerWithUndo.update(y,q.getDesc(), x)
                        except:
                            print ("Invalid date")
                    else:
                        print("===== Invalid Input ===== ")
                else:
                    print("===== Invalid ID ===== ")
            except:
                print("")
        else: print("===== Invalid Input ===== ")

    def giveCommand(self):
        '''gives assignments to a student or to a group'''
        g=input(" To a student or a group? ")
        if g=="student" or g=="Student":
            try:
                s = int(input(" Student ID : "))
                a = int(input(" Assignment ID : "))
                if self._StudControllerWithUndo.findStudID(s) !=-1 and self._AssigControllerWithUndo.findID(a) !=-1:
                    if not self._GradeController.findHW(s,a):
                        x = Grade(s, a, 0)
                        self._GradeController.addHW(x)
                    else:
                        print("===== Invalid Input ===== ")
                else:
                    print("===== Invalid Input ===== ")
            except:
                print("====== Invalid Input ======")
        elif g=="Group" or g== "group":
            try:
                s = int(input(" Group Number : "))
                a = int(input(" Assignment ID : "))
                if self._StudControllerWithUndo.findGroup(s) and self._AssigControllerWithUndo.findID(a):
                    for d in self._StudControllerWithUndo.getAllStudent():
                        if d.getGroup()==s:
                            g=d.getID()
                            x = Grade(g, a, 0)
                            if not self._GradeController.findHW(g, a):
                                self._GradeController.addHW(x)
                else:
                    print("===== Invalid Input ===== ")
            except:
                print("====== Invalid Input ======")


    def listCommand(self):
        '''
        List the students, the assignemnts ,homework or grades
        :return:
        '''
        c=input("Stud or Assig or Homework or Grade ? ")
        if c=="stud":
            for n in self._StudControllerWithUndo.getAllStudent():
                print(str(n))
        elif c=="assig":
            for n in self._AssigControllerWithUndo.getAllAssig():
                print(str(n))
        elif c=="homework":
            for n in self._GradeController.getAllGrade():
                if n.get()==0:
                    print(n.strH())
        elif c=="grade":
            for n in self._GradeController.getAllGrade():
                if n.get() != 0:
                    print(str(n))
        else: print ("====== Invalid Input ======")

    def gradeCommand(self):
        '''
        grades an assignment ungraded for each student
        :return:
        '''
        q=0
        for n in self._GradeController.getAllGrade():
            if n.get() == 0:
                q+=1
                print(n.strH())
        if q!=0:
            try:
                s = int(input("Select Student : "))
                a = int(input("Select Assignment : "))
                g = float(input("Grade (float) : "))
                if self._GradeController.findHW(s, a):
                    self._GradeController.grade(s,a,g)
                else:
                    print ("Already graded")
            except :
                print("INVALID")
        else:
            print("No students to be graded")

    def recieveCommand(self):
        '''
        All students who received a given assignment, ordered alphabetically or by average
            grade for that assignment.
        :return:
        '''
        t=[]
        x=0
        try:
            c=int(input("Give assignment : "))
            for r in self._GradeController.getAllGrade():
                if r.getS()==c:
                    x=1
            if x == 0:
                print("Nobody recieved this assignment")
                return
            if self._AssigControllerWithUndo.findID(c) !=-1:
                d=int(input("Which order? \n \t 1. Alphabetically \n \t 2. By average grade \n"))
                t=self._controller.recieve(c,d)

            else:
                print("===Invalid Assignment===")
        except:
            print("====== Invalid Input ======")

        for i in t:
            print (i)

    def lateCommand(self):
        '''
        All students who are late in handing in at least one assignment. These are all the
            students who have an ungraded assignment for which the deadline has passed.
        :return:
        '''
        t=[]
        data=datetime.now()
        dt=data.date()
        t = self._controller.late(dt)
        if len(t)>0:
            for i in t:
                print(i)
        else:
            print ("Nobody is late ")

    def bestCommand(self):
        '''
        Students with the best school situation, sorted in descending order of the average grade
                    received for all assignments.
        :return:
        '''
        t=[]
        t=self._controller.best()
        #if len(t)!=0:
        for i in t:
                print (i)
        #else:
            #print("No graded students")

    def command10(self):
        '''
        All assignments for which there is at least one grade, sorted in descending order of the
                average grade received by all students who received that assignment.
        :return:
        '''
        t=[]
        t = self._controller.average()
        if len(t)!=0:
            for i in t:
                print (i)
        else:
            print("No assignment graded")

