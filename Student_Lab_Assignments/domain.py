class Student:

    def __init__(self,a,b,c):
        self.__ID=a
        self.__name=b
        self.__group=c

    def setStudentID(self,a):
        self.__ID=a

    def setName (self,b):
        self.__name=b

    def setGroup(self,c):
        self.__group=c

    def getID(self):
        return self.__ID

    def getName(self):
        return self.__name

    def getGroup(self):
        return self.__group


    def __str__(self):
        r="Student ID: "
        r+=str(self.__ID)
        r+=" Name : "
        r+=self.__name
        r+= " Group : "
        r+= str(self.__group)
        return r


class Assignment:

    def __init__(self,a,b,c):
        self.__ID=a
        self.__description=b
        self.__deadline=c

    def getID(self):
        return self.__ID

    def getDeadline(self):
        return self.__deadline

    def getDesc(self):
        return self.__description

    def __str__(self):
        r="Assignment ID: "
        r+=str(self.__ID)
        r+="  Description :  "
        r+=str(self.__description)
        r+="  Deadline :  "
        r+= str(self.__deadline)
        return r

    def setDescription(self,d):
        self.__description=d

    def setDeadline(self,d):
        self.__deadline=d

class Grade:

    def __init__(self,a,b,c):
        self.__studentID=a
        self.__assignmentID=b
        self.__grade=c

    def getID(self):
        return self.__studentID

    def getS(self):
        return self.__assignmentID

    def get(self):
        return self.__grade

    def set(self,g):
        self.__grade=g

    def strH(self):
        r = "Student ID: "
        r += str(self.__studentID)
        r += " Assignment ID: "
        r += str(self.__assignmentID)
        return r

    def __str__(self):

        r = "Student ID: "
        r += str(self.__studentID)
        r += " Assignment ID: "
        r += str(self.__assignmentID)
        r+= " Grade : "
        r+=str(self.__grade)

        return r