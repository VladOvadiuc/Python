class Square:
    def __init__(self,x,y):
        self._x=x
        self._y=y
    def getx(self):
        return self._x
    def gety(self):
        return self._y

class Board:
    def __init__(self):
        self.__b=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    def isNotHit(self,l,c):
        '''
        Checks if a square is hit
        :param l: the line
        :param c: the column
        :return: 0/1 if the square is not hit
        '''
        if self.__b[l][c]==0 :
            return 0
        if self.__b[l][c]==1 :
            return 1

    def isFree(self,l,c):
        '''
        checks if a square is free
        :param l: the line
        :param c: the column
        :return: true/false if free
        '''
        if self.__b[l][c]==0 or self.__b[l][c]==1:
            return True
        return False

    def getAll(self):
        '''
        gets all the squares
        :return:
        '''
        return self.__b

    def getSquare(self,l,c):
        '''
        Gets 1 square
        :param l: the line
        :param c: the column
        :return:
        '''
        return self.__b[l][c]

    def getFree(self):
        '''
        gets free squares
        :return:
        '''
        rez=[]
        for i in range(0,8):
            for j in range(0,8):
                if self.isFree(i,j):
                    rez.append(Square(i,j))
        return rez

    def __str__(self):
        r=""
        r+= "   A B C D E F G H \n \n"
        for i in range(0,8):
            r+=str(i)+ "  "
            for j in range(0,8):
                r+=str(self.getSquare(i,j))
                r+=" "
            r+="\n"

        return r

    def play(self,l,c):
        '''

        :param l: line
        :param c: column
        :return: the square or error
        '''
        if l<0 or c<0 or l>7 or c>7 :
            raise Exception("Bad coordonates")
        if self.isNotHit(l,c)==0:
            self.__b[l][c]="-"
        elif self.isNotHit(l,c)==1:
            self.__b[l][c] = "x"
        return self.__b[l][c]

    def set(self,l,c,x):
        self.__b[l][c]=x


from random import randint
class Game:
    def __init__(self):
        self.__board=Board()

    def player(self,l,c):
        '''
        the player's turn
        :param l: line
        :param c: column
        :return: x if hit
        '''
        s=self.__board.play(l,c)
        if s=="x":
            return "x"

    def setX(self,l,c):
        '''
        sets the square "x"-hit
        :param l:line
        :param c: column
        :return:
        '''
        self.__board.set(l,c,"x")

    def setC(self,l,c):
        '''
                sets the square "-" :miss
                :param l:line
                :param c: column
                :return:
                '''
        self.__board.set(l,c,"-")

    def computer(self):
        '''
        computer's turn
        :return:
        '''
        empty=self.__board.getFree()
        if len(empty)!=0:
            p=randint(0,len(empty)-1)
            self.__board.play(empty[p].getx(),empty[p].gety())
            return Square(empty[p].getx(),empty[p].gety())

    def isWon(self):
        '''
        checks if won
        :return: true/false
        '''
        b=self.__board
        for i in range(0,8):
            for j in range(0,8):
                if b.getSquare(i,j)==1:
                    return False
        return True

    def __str__(self):
        return str(self.__board)

    def placeB(self,l,c,d,x):
        '''
        places the battle ship
        :param l: the line
        :param c: the column
        :param d: the direction
        :param x: the dimension
        :return:
        '''
        b=self.__board

        if d=="d" or d==0:
            if l+x>7:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l+1,c) and b.isFree(l+2,c) and b.isFree(l+3,c):
                b.set(l,c,1)
                b.set(l+1,c,1)
                b.set(l+2,c,1)
                b.set(l+3,c,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")

        if d=="u" or d==1:
            if l-x<0:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l-1,c) and b.isFree(l-2,c) and b.isFree(l-3,c):
                b.set(l,c,1)
                b.set(l-1,c,1)
                b.set(l-2,c,1)
                b.set(l-3,c,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="r"or d==2:
            if c+x>7:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l,c+1) and b.isFree(l,c+2) and b.isFree(l,c+3):
                b.set(l,c,1)
                b.set(l,c+1,1)
                b.set(l,c+2,1)
                b.set(l,c+3,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="l" or d==3:
            if c-x<0:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l,c-1) and b.isFree(l,c-2) and b.isFree(l,c-3):
                b.set(l,c,1)
                b.set(l,c-1,1)
                b.set(l,c-2,1)
                b.set(l,c-3,1)
            else:
                raise Exception("ship reach out of the playing area or overlap")

    def placeC(self,l,c,d,x):
        '''
                places the cruiser ship
                :param l: the line
                :param c: the column
                :param d: the direction
                :param x: the dimension
                :return:
                '''
        b=self.__board
        if d=="d" or d==0:
            if l+x>7:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l+1,c) and b.isFree(l+2,c):
                b.set(l,c,1)
                b.set(l+1,c,1)
                b.set(l+2,c,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="u"or d==1:
            if l-x<0:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l-1,c) and b.isFree(l-2,c):
                b.set(l,c,1)
                b.set(l-1,c,1)
                b.set(l-2,c,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="r"or d==2:
            if c+x>7:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l,c+1) and b.isFree(l,c+2) :
                b.set(l,c,1)
                b.set(l,c+1,1)
                b.set(l,c+2,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="l" or d==3:
            if c-x<0:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l,c-1) and b.isFree(l,c-2) :
                b.set(l,c,1)
                b.set(l,c-1,1)
                b.set(l,c-2,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")

    def placeD(self,l,c,d,x):
        '''
                places the destroier ship
                :param l: the line
                :param c: the column
                :param d: the direction
                :param x: the dimension
                :return:
                '''
        b=self.__board
        if d=="d" or d==0:
            if l+x>7:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l+1,c):
                b.set(l,c,1)
                b.set(l+1,c,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="u" or d==1:
            if l-x<0:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l-1,c) :
                b.set(l,c,1)
                b.set(l-1,c,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="r" or d==2:
            if c+x>7:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l,c+1) :
                b.set(l,c,1)
                b.set(l,c+1,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")
        if d=="l" or d==3:
            if c-x<0:
                raise Exception ("Invalid")
            if b.isFree(l,c) and b.isFree(l,c-1) :
                b.set(l,c,1)
                b.set(l,c-1,1)
            else :
                raise Exception("ship reach out of the playing area or overlap")


    def autoPlace(self):
        '''
        autoplaces the ships
        :return:
        '''
        exist=True
        while True:
            try:
                l=randint(0,7)
                c=randint(0,7)
                d=randint(0,3)
                #print (l,c,d, " B ")
                self.placeB(l,c,d,4)
                break
            except :
                pass
        while True:
            try:
                l=randint(0,7)
                c=randint(0,7)
                d=randint(0,3)
                #print (l,c,d," C ")
                self.placeC(l,c,d,3)
                break
            except :
                pass

        while True:
            try:
                l=randint(0,7)
                c=randint(0,7)
                d=randint(0,3)
                #print (l,c,d,"D")
                self.placeD(l,c,d,2)
                break
            except :
                pass


