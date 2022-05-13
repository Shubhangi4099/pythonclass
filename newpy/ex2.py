import os

from pdb import Restart
import as 
Restart = input ('do you have restart your computer ? (yes/no):')
if Restart == "no":
    exit()
    else:
        os.system('shutdown/r/t 1')