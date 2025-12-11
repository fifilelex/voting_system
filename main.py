from src.io.io_manager import IOManager
from src.io.MenuManager import *
from src.services.elections import Election
from tests.test import sample_test_data


#MENU

def main():
    election = Election("wybory prezydenckie", 2045)
    io = IOManager()
    sample_test_data(election)
    running = True
    subrunning = False
    while running:
        action = call_menu_handler(io, election)
        if action == "next":
            subrunning = True
            while subrunning:
                subaction = call_submenu_handler(io, election)
                if subaction == "back":
                    subrunning = False
                else:
                    pass
        else:
            pass


main()



