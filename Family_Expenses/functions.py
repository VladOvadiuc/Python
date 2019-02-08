from datetime import *
    #date=datetime.now()
    #print (date.day)
from test_init import *


def addExpenseCommand(expenseList,cmd):
    '''
        Adds or inserts an expense to the list
        In:-the expense list and the commands
        out :- the updated list
    '''
    if len(cmd)==2 :
        expenseList=addExpense(expenseList,cmd)
    elif len(cmd)==3:
        expenseList=insertExpense(expenseList,cmd)
    else :
        raise ValueError("Invlaid input")
    return expenseList

def insertExpense(expenseList,cmd):
    '''
        Inserting an expense to a given day
        In:-the expense list and the commands
        out :- the updated list
    '''
    day = int(cmd[0])
    if len(cmd) < 3:
        raise ValueError("Invlaid input")
    elif  day < 1 or day > 30:
        raise ValueError("Invlaid input")
    else:
        expense = (int(cmd[0]), int(cmd[1]),cmd[2])
        expenseList.append(expense)
    return expenseList
    
def addExpense(expenseList,cmd):
    '''
        Adding an expense to the curent day
        In:-the expense list and the commands
        out :- the updated list
    '''
    date=datetime.now()
    day=date.day
    #if len(cmd[0]) == 0 or cmd[0].isalpha() or len(cmd[1]) == 0 or cmd[1].isdigit():
        #print("Invalid input. Expense was not added")
    #else:
    expense = (day, int(cmd[0]),cmd[1])
    expenseList.append(expense)
    return expenseList


def removeExpenseCommand (expenseList,cmd):
    '''
        The remove command choose what to remove from the list by the type and the numbers of params
        In:-the expense list and the commands
        out :- the updated list
    '''
    if len(cmd)==2 :
        expenseList=remove(expenseList,cmd)
    elif len(cmd)==1 and cmd[0].isdigit():
        expenseList =removeDayExpense(expenseList,cmd)
    elif len(cmd)==1 and cmd[0].isalpha():
        expenseList=removeCategory(expenseList,cmd)
    return expenseList

def findDay(expenseList,day):
    '''
        in: the expenses list and a given day
        out :a position  or -1 if the day is in expenseList or not
    '''
    pos = -1
    for i in range(0, len(expenseList)):
        d=expenseList[i]
        if d[0] == day:
            pos = i
    return pos


def removeDayExpense(expenseList,cmd):
    '''
        removes a day from the list
        in: the list and the parameter (day)
        out: the updated list without that day
    '''
    day=int(cmd[0])
    pos = findDay(expenseList,day) # searches the day in the list
    while pos != -1: #while the day is in list, remove it
        expenseList.pop(pos)
        pos = findDay(expenseList,day)
    return expenseList

def findDayToDay(expenseList,day1,day2):
    '''
            in: the expenses list and 2 days
            out :a position  or -1 if in the list exists a day between day1 and day2
    '''
    pos = -1
    for i in range(0, len(expenseList)):
        d=expenseList[i]
        if d[0] >= day1 and d[0]<=day2:
            pos = i
    return pos
    
def remove(expenseList,cmd):
    '''
            removes some days from the list
            in: the list and 2 days as parameter
            out: the updated list without those days
    '''
    #if len(cmd[0]) == 0 or len(cmd[1]) == 0 :
        #print("Invalid input. Expense was not added")
    day1=int(cmd[0])
    day2=int(cmd[1])
    pos=findDayToDay(expenseList,day1,day2) # searches the day in the list
    while pos!= -1: #while the day is in list, remove it
        expenseList.pop(pos)
        pos=findDayToDay(expenseList,day1,day2)
    return expenseList

def findCategory(expenseList,cat):
    '''
                in: the expenses list and a category
                out :a position  or -1 if in the list exists that category
    '''
    pos = -1
    for i in range(0, len(expenseList)):
        d = expenseList[i]
        if d[2] == cat:
            pos = i
    return pos

def removeCategory(expenseList,cmd):
    '''
        removes a category from the list
        in: the list and the parameter (category)
        out: the updated list without that category
    '''
    cat=cmd[0]
    pos = findCategory(expenseList, cat) # searches the category in the list
    while pos != -1: #while the category is in list, remove it
        expenseList.pop(pos)
        pos = findCategory(expenseList, cat)
    return expenseList

def listCommand(expenseList,cmd):
    '''
        the list command choose what list to print
        in: expense list
        out: the whole list or a list that satisfies some properties
    '''
    if len(cmd)==0:
        return expenseList
    if len(cmd)==1:
        return(listCategory(expenseList,cmd))
    if len(cmd)==3:
        return(listCategoryValue(expenseList,cmd))

def listCategory(expenseList,cmd):
    '''
        from the list, selects only the expenses that have the given category
        and makes a second list 
        in: the expense list and the command
        out: the second list
    '''
    cat=cmd[0]
    result=[]
    for i in range(len(expenseList)):
        d=expenseList[i]
        if str(d[2]) == cat:
            result.append(d)
    return result
            
def listCategoryValue(expenseList,cmd):
    '''
        from the list, selects only the expenses that have the given category and the given value
        and makes a second list 
        in: the expense list and the command
        out: the second list
    '''
    cat=str(cmd[0])
    sign=str(cmd[1])
    value=int(cmd[2])
    result=[]
    for i in range(0,len(expenseList)):
        d=expenseList[i]
        if d[2] == cat:
            if sign== "<" and d[1] < value:
                result.append(d)
            elif sign== "=" and d[1] == value:
                result.append(d)
            elif sign== ">" and d[1] > value:
                result.append(d)
    return result
        
def summ (expenseList,cmd):
    '''
        sums the amount of money spent on a given category
        in: the expense list and the category
        out: the sum of money spent on that category
    '''
    cat=str(cmd[0])
    sume=0
    for i in range(0,len(expenseList)):
        d=expenseList[i]
        if d[2] == cat:
            sume=sume+d[1]
    return sume
def sumMax(expenseList):
    '''
        finds the day with the maximum expenses
        in : the expense list 
        out: the day and the maximum amount of money spent
    '''
    sume=0
    sMax=0
    dMax=0
    for i in range(0,len(expenseList)):
        d=expenseList[i]
        sume=d[1]
        for j in range (i+1,len(expenseList)):
            e=expenseList[j]
            if d[0]==e[0]:
                sume=sume+e[1]
        if sume>sMax:
            sMax=sume
            dMax=d[0]
    return dMax,sMax

def sortCommand(expenseList,cmd):

    lst=[]
    if len(cmd)>1:
        return False
    elif cmd[0].isdigit():
        lst=sortDay(expenseList,cmd)
    elif cmd[0].isalpha():
        lst=sortCat(expenseList,cmd)
    return lst

def sortDay(expenseList,cmd):
    '''
    
        write the total daily expenses in ascending order by amount of money spent.
        in: the expense list and a given day
        out: the expenses on that day, in ascending order
    '''
    day=int(cmd[0])
    lst=[]
    
    for i in range(0,len(expenseList)):
        d=expenseList[i]
        if d[0]==day:
            lst.append(d)
    lst=sorted(lst,key=lambda price:price[1])
    return lst
def sortCat(expenseList,cmd):
    '''
        write the daily expenses for the given category in ascending order by amount of money spent.
        in: the expense list and a given category
        out: the expenses on that category, in ascending order 
    '''
    cat=str(cmd[0])
    lst=[]
    
    for i in range(0,len(expenseList)):
        d=expenseList[i]
        if d[2]==cat:
            lst.append(d)
    lst=sorted(lst,key=lambda price:price[1])
    return lst

def filterCommand(expenseList,cmd):
    if len(cmd)==1:
        expenseList=filterCategory(expenseList,cmd)
    if len(cmd)==3:
        expenseList=filterCategoryValue(expenseList,cmd)
    return expenseList

def filterCategory(expenseList,cmd):
    '''
    
        – keep only expenses in a given category
        in: the expense list and a given category
        out: the updated list, wich contains only the expenses with that category
    '''
    cat=cmd[0]
    result=[]
    for i in range(len(expenseList)):
        d=expenseList[i]
        if str(d[2]) == cat:
            result.append(d)
    expenseList=result
    return expenseList
            
def filterCategoryValue(expenseList,cmd):
    '''

            – keep only expenses in a given category
            in: the expense list, a given category and the value
            out: the updated list, wich contains only the expenses with that category and the value with the property
    '''
    cat=str(cmd[0])
    sign=str(cmd[1])
    value=int(cmd[2])
    result=[]
    for i in range(0,len(expenseList)):
        d=expenseList[i]
        if d[2] == cat:
            if sign== "<" and d[1] < value:
                result.append(d)
            elif sign== "=" and d[1] == value:
                result.append(d)
            elif sign== ">" and d[1] > value:
                result.append(d)
    expenseList=result
    return expenseList

def undo(undoList):
    '''
        undo – the last operation that has modified program data will be reversed. 
        in: the expenselist
        out: the expense list with the last operation reversed
    '''
    vector=undoList[len(undoList)-1]
    del undoList[len(undoList)-1]
    return vector,undoList














    
    
    
