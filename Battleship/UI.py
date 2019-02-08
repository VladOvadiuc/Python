from game import *
class UI:
    def __init__(self):
        self.__pGame=Game()
        self.__cGame=Game()
        self.__cTarget=Game()
    def gameUI(self):
        print ("Start Game ")

        while True:
            try:
                print("Let's place the battleship ")
                l=int(input("Give line : "))
                c=int(input("Give column : "))
                d=input("Give direction : u(p) / d(own) / l(eft) / r(ight)")
                self.__pGame.placeB(l,c,d,4)
                break
            except Exception as ex:
                print(ex)

        while True:
            try:
                print("Let's place the cruiser ")
                l=int(input("Give line : "))
                c=int(input("Give column : "))
                d=input("Give direction : u(p) / d(own) / l(eft) / r(ight)")
                self.__pGame.placeC(l,c,d,3)
                break
            except Exception as ex:
                print (ex)
        while True:
            try:
                print("Let's place the destroyer ")
                l=int(input("Give line : "))
                c=int(input("Give column : "))
                d=input("Give direction : u(p) / d(own) / l(eft) / r(ight)")
                self.__pGame.placeD(l,c,d,2)
                break
            except Exception as ex:
                print (ex)
        print (str(self.__pGame))

        self.__cGame.autoPlace()
        #print(str(self.__cGame))

        player=True
        while self.__cGame.isWon()==False and self.__pGame.isWon()==False:
            if player:
                try:
                    c = input("Give column : ")
                    l = int(input("Give line : "))
                    s=self.__cGame.player(l,ord(c)-65)
                    if s=="x":
                        self.__cTarget.setX(l,ord(c)-65)
                    else:
                        self.__cTarget.setC(l,ord(c)-65)
                    player=False
                    print ("\n Computer board \n")
                    print(str(self.__cTarget))
                    #print (str(self.__cGame))
                except Exception as e:
                    print (e)

            else:
                s=self.__pGame.computer()
                player=True
                print ("PLAYER board \n")
                print (str(self.__pGame))

        if self.__cGame.isWon():
            print ("Player WON ")
        if self.__pGame.isWon():
            print ("Computer Won")



ui=UI()
ui.gameUI()