import pyautogui #Module to controll keyboard
from random import randint #Module for random numbers
import time #Module to make a break

commands = ["ls", "cat dpkg.log", "touch guenther.txt", "pwd", "mkdir Hallo", "cd Hallo", "cd ", "uname", "w", "uptime", "cp guenther.txt joseph.txt", "rm -r Hallo", "man ls", "q", "grep --help", "head deutsch.txt", "tail deutsch.txt", "wc -l deutsch.txt", "more deutsch.txt", "q", "less deutsch.txt", "q", "apropos less", "rm joseph.txt", "rm guenther.txt", "history", "exit"]

time.sleep(3) #To switch from editor to terminal ot other messagebox

for i in range(len(commands)): #For-loop to run the following commands in the specified duration
	time.sleep(1) #Break for 1sec so that the server comes along
	pyautogui.write(commands[i]) #To write the commands in the command-line
	pyautogui.press("enter") #To execute the command
	