from functions import *


def readCommand():
    '''
    Read and parse user commands
    input: -
    output: (command, params) tuple, where:
            command is user command
            params are parameters
    '''
    cmd = input("Input option: ")
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
    helpCommand()
    '''
    Entry point into the program
    '''
    expenseList = []

    '''
    We add a few expenses so that we do not start from scratch
    '''
    testInit(expenseList)
    undoList = []

    while True:
        '''
        User input consist of command and parameters
        '''
        cmd = readCommand()
        command = cmd[0]
        params = cmd[1]
        result = []

        '''
        Execute command
        '''
        if command == '1':
            try:
                if (addExpenseCommand(expenseList, params)):
                    undoList.append(expenseList[:])
                else:
                    print("invalid")
            except:
                print ("------ Error------")
        elif command == '2':
            try:
                undoList.append(expenseList[:])
                expenseList = removeExpenseCommand(expenseList, params)
            except:
                print ("------ Error------")

        elif command == '3':
            try:
                showAll(listCommand(expenseList, params))
            except:
                print ("------ Error------")
        elif command == '4':
            try:
                print(summ(expenseList, params))
            except:
                print ("------ Error------")
        elif command == '5':
            try:
                print(sumMax(expenseList))
            except:
                print ("------ Error------")
        elif command == '6':
            try:
                if sortCommand(expenseList,params):
                    showAll(sortCommand(expenseList,params))
                else:
                    print("invalid")
            except:
                print ("------ Error------")
        elif command == '7':
            try:
                undoList.append(expenseList[:])
                expenseList = filterCommand(expenseList, params)
            except:
                print ("------ Error------")
        elif command =='8':
            if(len(undoList)):
                expenseList,undoList=undo(undoList)
        elif command == 'help' or command=='9':
            helpCommand()
        elif command == 'exit' or command=='10':
            break
        else:
            print("Invalid command!")


def showAll(expenseList):
    for i in range(len(expenseList)):
        print (expenseList[i])


def helpCommand():
    print("\n ===================================\n ")
    print("Valid commands:")
    print("\t 1.add ")
    print("\t \t <sum_of_money>, <category>")
    print("\t \t <day>,<sum_of_money>, <category>")
    print("\t 2.remove ")
    print("\t \t <day>")
    print("\t \t <start day> , <end day>")
    print(" \t \t <category>")
    print(" \t 3.list")
    print(" \t \t  all")
    print(" \t \t  <category>")
    print(" \t \t <category>,< | = | >,<value>")
    print("\t 4.sum <category>")
    print ("\t 5.max")
    print("\t 6.sort")
    print("\t \t <day>")
    print("\t \t <category>")
    print("\t 7.filter")
    print("\t \t <category>")
    print("\t \t <category, < | = | >,<val>")
    print("\t 8.undo")
    print(" \t 9.help")
    print("\t 10.exit")
    print("\n ===================================\n ")

start()
