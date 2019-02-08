from datetime import *
from ClassList import*
class Controller:

    def __init__(self,studRepo,assigRepo,gradeRepo):
        self.__gradeRepo = gradeRepo
        self.__assigRepo = assigRepo
        self.__studRepo = studRepo

    def recieve(self,a,o):
        '''
        All students who received a given assignment, ordered alphabetically or by average
            grade for that assignment.
        :param a: the assignment
        :param o: the order. if o ==1 the list will be sorted alphabetically
                the list is firstly order by grade
        :return: the list of students who received the assignment
        '''

        t=[]
        d=self.__gradeRepo.getAll()
        #d=sorted(d,key=lambda x:x.get())
        d=gnomeSort(d,lambda x:x.get())
        for s in d:
            if s.getS()==a:
                for x in self.__studRepo.getAll():
                    if x.getID() ==s.getID():
                        id=x.getID()
                        n=x.getName()
                        g=x.getGroup()
                        qw=" Has grade : "
                        qe=s.get()
                        r=(id,n,g,qw,qe)
                        t.append(r)
        if o==1:
            #t=sorted (t, key=lambda x:x[1])
            t=gnomeSort(t,lambda x:x[1])
        return t

    def late(self,d):
        '''
        All students who are late in handing in at least one assignment. These are all the
            students who have an ungraded assignment for which the deadline has passed.
        :param d: the current day
        :return: the list of students
        '''
        t=[]
        for s in self.__gradeRepo.getAll():
            if s.get()==0:
                f=s.getID()
                x= s.getS()
                for y in self.__assigRepo.getAll():
                    if y.getID()==x and y.getDeadline() < d:
                        for x in self.__studRepo.getAll():
                            if x.getID() ==f:
                                r= "Student ( "
                                r += str(x.getID())
                                r+= " "
                                r += str(x.getName())
                                r += " "
                                r += str(x.getGroup())
                                r+= ") is late in handing assigment : "
                                r+= str(y.getID())

                                t.append(r)

        return t

    def best(self):
        '''

        :return: Students with the best school situation, sorted in descending order of the average grade
                    received for all assignments.

        '''
        t=[]
        for s in self.__studRepo.getAll():
            n=0
            summ=0
            for a in self.__gradeRepo.getAll():
                if s.getID() == a.getID():
                    n += 1
                    summ += float(a.get())
            if n!=0:
                m=float(summ/n)
                t.append([s.getID(),s.getName(),s.getGroup(),"Has average grade : ",float(m)])
        #t=sorted(t,key=lambda x:x[4],reverse=True)
        t=gnomeSort(t,lambda x:x[4],reverse=True)
        return t

    def average(self):
        '''

        :return:All assignments for which there is at least one grade, sorted in descending order of the
                average grade received by all students who received that assignment.

        '''
        t=[]
        for s in self.__assigRepo.getAll():
            n = 0
            summ = 0
            for a in self.__gradeRepo.getAll():
                if s.getID() == a.getS() and a.get() != 0:
                    n += 1
                    summ += float(a.get())
            if n != 0:
                m = float(summ / n)
                t.append(["Assignment ID : " ,s.getID(), " Average grade : ",float(m)])
            t = sorted(t, key=lambda x: x[3], reverse=True)
            #t=gnomeSort(t,lambda x: x[3], True)

        return t