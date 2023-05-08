import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from boss1 import menu

    menu()

elif bit == '32bit':

    from boss2 import menu

    menu()
