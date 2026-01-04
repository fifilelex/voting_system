from src.io.io_manager import IOManager
from src.io.MenuManager import *
from src.io.menu import call_menu, call_submenu
from src.services.elections import Election
from src.persistence.json_repository import JsonData
from tests.test import sample_test_data


#MENU

def main():
    election = Election("wybory prezydenckie", 2045)
    io = IOManager()
    data = JsonData()
    sample_test_data(election)
    running = True
    subrunning = False
    while running:
        call_menu()
        action = call_menu_handler(io, election, data)
        if action == MENURESULTS.CONTINUE:
            pass
        elif action == MENURESULTS.BACK:
            pass
        elif action == MENURESULTS.NEXT:
            subrunning = True
            while subrunning:
                call_submenu()
                subaction = call_submenu_handler(io, election)
                if subaction == MENURESULTS.CONTINUE: #everything works, menu reappears
                    pass
                elif subaction == MENURESULTS.BACK:
                    subrunning = False
                elif subaction == MENURESULTS.NEXT: #cant go into next menu, cuz submenu is the lowest one
                    pass
                elif subaction == MENURESULTS.EXIT: #wont ever happen
                    pass
                else: #wrong choice, submenu reappears
                    pass
        elif action == MENURESULTS.EXIT:
            running = False
        else:
            pass


main()



