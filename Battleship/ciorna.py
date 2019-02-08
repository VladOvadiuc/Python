import unittest
from game import *
g=Game()
b=Board()
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(g.isWon(),True)
        g.placeB(1,1,"d",4)
        self.assertEqual(g.isWon(), False)
        g.setX(1,1)
        g.setX(2,1)
        self.assertEqual(g.player(4,1),"x")
        g.setX(3,1)
        g.setX(4,1)
        g.setC(3,3)
        b.set(3,3,"-")
        self.assertEqual(b.getSquare(3,3),"-")
        #print (g)
        self.assertEqual(g.isWon(), True)
        self.assertEqual(b.isFree(6,6),True)
        self.assertEqual(b.isNotHit(6, 6), 0)
        self.assertRaises(Exception,b.play,12,32)

if __name__ == '__main__':
    unittest.main()