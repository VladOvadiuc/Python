def mainMenu():
    n=input("Choose user menu interface: menu or command :  ")
    if n=="menu" :
        from UI_menu_based import start
    elif n=="command" :
        from UI_command_based import start
    else :
        print("invalid command")

mainMenu()
