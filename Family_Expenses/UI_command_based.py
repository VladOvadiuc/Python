from functions import *


def readCommand():
    '''
    Read and parse user commands
    input: -
    output: (command, params) tuple, where:
            command is user command
            params are parameters
    '''
    cmd = input("command: ")
    '''
    Separate command word and parameters
    '''
    if cmd.find(" ") == -1:
        '''
        No parameters - e.g. help, exit
        '''
        command = cmd
        params = ""
    else:
        
        command = cmd[0:cmd.find(" ")]
        params = cmd[cmd.find(" "):]
        params = params.split(",")
        for i in range(0, len(params)):
            params[i] = params[i].strip()
    return (command, params)


def start():
    '''
    Entry point into the program
    '''
    expenseList = []
    helpCommand()
    '''
    We add a few expenses so that we do not start from scratch
    '''
    testInit(expenseList)
    undoList=[]
    while True:
        '''
        User input consist of command and parameters
        '''
        cmd = readCommand()
        command = cmd[0]
        params = cmd[1]
        result=[]
        #helpCommand()
        '''
        Execute command
        '''
        if command == 'add':
            try:
                undoList.append(expenseList[:])
                expenseList=addExpenseCommand(expenseList,params)
            except ValueError as ve :
                print (ve)
        elif command == 'remove':
             try:
                undoList.append(expenseList[:])
                expenseList=removeExpenseCommand(expenseList, params)
             except:
                print ("------ Error------")
                
        elif command == 'list':
            try:
                showAll(listCommand(expenseList,params))
            except:
               print ("------ Error------")
        elif command == 'sum':
            try:
                print(summ(expenseList,params))
            except:
                print ("------ Error------")
        elif command == 'max':
            try:
                print(sumMax(expenseList))
            except:
               print ("------ Error------")
        elif command == 'sort':
            try:
                if sortCommand(expenseList,params):
                    showAll(sortCommand(expenseList,params))
                else:
                    print("invalid")
            except:
                print ("------ Error------")
        elif command == 'filter':
            try:
                undoList.append(expenseList[:])
                expenseList=filterCommand(expenseList,params)
            except:
                print ("------ Error------")
        elif command =='undo':
            if(len(undoList)):
                expenseList,undoList=undo(undoList)
        elif command == 'help':
            pass
            helpCommand()
        elif command == 'exit':
            break    
        else:
            print("Invalid command!")
def showAll(expenseList):
    for i in range(len(expenseList)):
        print (expenseList[i])





def helpCommand():
    print("\n \n ===================================")
    print("Valid commands:")
    print("\t add ")
    print("\t \t <sum_of_money>, <category>")
    print("\t \t <day>,<sum_of_money>, <category>")
    print("\t remove ")
    print("\t \t <day>")
    print("\t \t <start day> , <end day>")
    print(" \t \t <category>")
    print(" \t list")
    print(" \t \t  all")
    print(" \t \t  <category>")
    print(" \t \t <category>,< | = | >,<value>")
    print("\t sum <category>")
    print ("\t max")
    print("\t sort")
    print("\t \t <day>")
    print("\t \t <category>")
    print("\t filter")
    print("\t \t <category>")
    print("\t \t <category, < | = | >,<val>")
    print(" \t undo")
    print(" \t help")
    print("\t exit")
    print(" ===================================\n \n")


start()
