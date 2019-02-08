from functions import *
from datetime import *
date=datetime.now()
d=date.day

def testAddExpense():
    assert addExpense( [[13,50,'food']],[4,'water'])  == [[13,50,'food'],[5,4,'water']]
    assert addExpense([[18,50,'food']],[10,'transport'])==[[18,50,'food'],[5,10,'transport']]
    assert addExpense([[1,50,'food']],[4,'water'])==[[1,50,'food'],[5,4,'water']]

def testInsertExpense():

    assert insertExpense([[13,50,'food']],[25,4,'water'])==[[13,50,'food'],[25,4,'water']]
    assert insertExpense([[18,50,'food']],[30,10,'transport'])==[[18,50,'food'],[30,10,'transport']]
    assert insertExpense([[1,50,'food']],[6,4,'water'])==[[1,50,'food'],[98,4,'water']]

def testFindDay():
    assert findDay ([[1, 65, 'water'],[15, 230, 'gym'],[19, 55, 'food']],1)==0
    assert findDay ([[22, 180, 'food'],[15, 54, 'gas'],[14, 90, 'rent']],14)==2
    assert findDay ([[12, 20, 'clothes'],[15, 230, 'transport'],[14, 90, 'food']],30)==-1
    assert findDay ([[19,45, 'food'],[29,4500, 'service'],[6,5, 'donuts'],[4,50, 'water']],29)==1
    assert findDay ([[5,12,'ticket'],[2,20,'gas'],[25,350,'gym'],[30,56,'others']],8)==-1


def testRemoveDayExpense():
    assert removeDayExpense([[18, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food']],[15])==[[18, 20, 'food'],[14, 90, 'food']]
    assert removeDayExpense([[1, 20, 'net'],[15, 230, 'gas'],[14, 90, 'food']],[14])==[[1, 20, 'net'],[15, 230, 'gas']]
    assert removeDayExpense([[3,45,'net'],[28,66,'clothes'],[17,450,'rent'],[20,43,'gym']],[20])==[[3,45,'net'],[28,66,'clothes'],[17,450,'rent']]
    assert removeDayExpense([[5,12,'ticket'],[2,20,'gas'],[25,350,'gym'],[30,56,'others']],[31])==[[5,12,'ticket'],[2,20,'gas'],[25,350,'gym'],[30,56,'others']]
    assert removeDayExpense([[19,45, 'food'],[29,4500, 'service'],[6,5, 'donuts'],[4,50, 'water']],[19])==[[29,4500, 'service'],[6,5, 'donuts'],[4,50, 'water']]
    
def testRemove():
    assert remove([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food']],[14,15])==[[1, 20, 'food']]
    assert remove([[1, 20, 'food'],[6, 520, 'others'],[15, 230, 'transport'],[14, 90, 'food']],[1,10])==[[15, 230, 'transport'],[14, 90, 'food']]
    assert remove([[19,45, 'food'],[29,4500, 'service'],[6,5, 'donuts'],[4,50, 'water']],[1,20])==[[29,4500, 'service']]
    assert remove([[3,45,'net'],[28,66,'clothes'],[17,450,'rent'],[20,43,'gym']],[1,30])==[]
    assert remove([[12,250,'electricity'],[24,150,'bills'],[3,5,'transport'],[19,25,'taxi']],[10,20])==[[24,150,'bills'],[3,5,'transport']]
        
def testRemoveCategory():
    assert removeCategory([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food']],['food']==[[15, 230, 'transport']])
    assert removeCategory([[1, 20, 'food'],[6, 520, 'others'],[15, 230, 'transport'],[14, 90, 'food']],['transport']==[[1, 20, 'food'],[6, 520, 'others'],[14, 90, 'food']])

def testListCategory():
    assert listCategory([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food']],['food'])==[[1, 20, 'food'],[14, 90, 'food']]
    assert listCategory ([[13,45,'rent'],[1,50,'transport'],[4,450,'gas']],['gas'])==[[4,450,'gas']]
    assert listCategory([[12,250,'electricity'],[24,150,'bills'],[3,5,'transport'],[19,25,'taxi']],['bills'])==[[24,150,'bills']]
    assert listCategory([[18,50,'food'],[13,50,'transport'],[1,20,'food'],[1,100,'transport']],['food'])==[[18,50,'food'],[1,20,'food']]
    assert listCategory([[1, 20, 'food'], [6, 520, 'others'], [15, 230, 'transport'], [14, 90, 'food']], ['net']) == []

def testListCategoryValue():
    assert listCategoryValue([[1, 20, 'food'], [15, 230, 'transport'], [14, 90, 'food']], ['food','>',7]) == [[1, 20, 'food'],[14, 90, 'food']]
    assert listCategoryValue([[13, 45, 'rent'], [1, 50, 'transport'], [4, 450, 'gas']], ['gas','>',100]) == [[4, 450, 'gas']]
    assert listCategoryValue([[1, 20, 'food'], [6, 520, 'others'], [15, 230, 'transport'], [14, 90, 'food']], ['transport','>',50]) ==[[15, 230, 'transport']]
    assert listCategoryValue([[12,250,'electricity'],[24,150,'bills'],[3,5,'transport'],[19,25,'taxi']],['bills','=',150])==[[24,150,'bills']]
    assert listCategoryValue([],['food','>',0])==[]
 
def testSumm():
    assert summ([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food']],['food'])==110
    assert summ([[1, 20, 'food'],[6, 520, 'others'],[15, 230, 'transport'],[14, 90, 'food']],['others'])==520
    assert summ([[12,250,'electricity'],[24,150,'bills'],[3,5,'transport'],[19,25,'bills']],['bills'])==175
    assert summ([],['food'])==0
    assert summ([[5,12,'ticket'],[2,20,'gas'],[25,350,'gym'],[30,56,'others']],['food'])==0

def testSumMax():
    assert sumMax([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food']])==(15, 230)
    assert sumMax([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food'],[6, 520, 'others']])==(6, 520)
    assert sumMax([[12,250,'electricity'],[24,150,'bills'],[3,5,'transport'],[19,25,'bills']])==(12,250)
    assert sumMax([[12,50,'net'],[24,15,'bills'],[13,151,'food'],[19,25,'bills']])==(13,151)
    assert sumMax([])==(0,0)

def testSortDay():
    assert sortDay([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food'],[6, 520, 'others']],[1])==[[1, 20, 'food']]
    assert sortDay([[1,23,'food'],[1,4,'transport'],[1,15,'water'],[1,78,'taxi'],[1,2,'donut']],[1])==[[1,2,'donut'],[1,4,'transport'],[1,15,'water'],[1,23,'food'],[1,78,'taxi']]
    assert sortDay([[1,23,'food'],[1,4,'transport'],[1,15,'water'],[1,78,'taxi'],[1,2,'donut']],[2])==[]
    assert sortDay([],[2])==[]
    assert sortDay([[12,1000,'rent'],[12,50,'net'],[13,89,'food'],[12,5,'taxi']],[12])==[[12,5,'taxi'],[12,50,'net'],[12,1000,'rent']]


def testSortCat():
    assert sortCat([[1, 540, 'food'], [15, 230, 'transport'], [14, 90, 'food']],['food'])==[[14, 90, 'food'],[1, 540, 'food']]
    assert sortCat([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food'],[6, 520, 'others']],['transport'])==[[15, 230, 'transport']]
    assert sortCat([[1, 20, 'food'],[15, 230, 'transport'],[14, 90, 'food'],[6, 520, 'others']],['net'])==[]
    assert sortCat([],['net'])==[]
    assert sortCat([[12,250,'electricity'],[24,150,'bills'],[3,5,'transport'],[19,25,'taxi']],['bills'])==[[24,150,'bills']]


def testFilterCategory():
    assert filterCategory([[1, 540, 'food'], [15, 230, 'transport'], [14, 90, 'food']],['food'])==[[1, 540, 'food'],[14, 90, 'food']]
    assert filterCategory([[1, 20, 'water'], [1, 54, 'others'], [14, 90, 'food'], [6, 520, 'others']], ['others']) == [[1, 54, 'others'],[6, 520, 'others']]
    assert filterCategory([[1, 20, 'food'], [15, 230, 'transport'], [14, 90, 'food'], [6, 520, 'others']], ['net']) == []
    assert filterCategory([], ['net']) == []
    assert filterCategory([[12, 250, 'electricity'], [24, 150, 'bills'], [3, 5, 'transport'], [19, 25, 'taxi']],['bills']) == [[24, 150, 'bills']]

def testFilterCategoryValue():
    assert filterCategoryValue([[1, 540, 'food'], [15, 230, 'transport'], [14, 90, 'food']], ['food','>',100]) == [[1, 540, 'food']]
    assert filterCategoryValue([[1, 20, 'water'], [1, 54, 'others'], [14, 90, 'food'], [6, 520, 'others']], ['others','>',100]) == [[6, 520, 'others']]
    assert filterCategoryValue([[1, 20, 'food'], [15, 230, 'transport'], [14, 90, 'food'], [6, 520, 'others']],['net','=',50]) == []
    assert filterCategoryValue([], ['water','>',10]) == []
    assert filterCategoryValue([[12, 250, 'electricity'],[24, 150, 'bills'], [3, 5, 'transport'], [19, 25, 'taxi']],['bills','=',150]) == [[24, 150, 'bills']]

