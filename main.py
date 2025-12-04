from src.io.io_manager import *
from src.io.MenuManager import *
from src.services.elections import Election
from tests.test import sample_test_data


#MENU
election = Election("wybory prezydenckie", 2045)
io = IOManager()
sample_test_data(election)
running = True
while running:
    running = call_menu_handler(io, election)



