from colorama import  Fore,Style ,Style
import colorama 

print(Fore.RED+'Tudo bem'+Fore.MAGENTA+'Tudo lime')
print(Style.RESET_ALL) #reset all colors
#  colorama with ASSCI
# print('\033[31m' + 'some red text')
# print('\033[39m') # reset all colors

import sys
import time

# point by point
msg = "Loading"

print(msg, end="")

for _ in range(10):
    print(end=".")
    sys.stdout.flush()
    time.sleep(1)
print()

# Or all char by char
i = 10
msg = "Loading" + "." * i

for char in msg:
    print(end=char)
    sys.stdout.flush()
    time.sleep(1)
print()