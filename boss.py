import os, platform, time, sys
try:
    import requests
except:
    os.system('pip install requests')
print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mCh>
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m6>
    from PROJECT1 import menu
    menu()
elif bit == '32bit':
    from PROJECT2 import menu
    menu()
