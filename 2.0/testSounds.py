import os
from time import sleep

accept = "accept.mp3"
error = "error.mp3"
os.system("mpg123 " + accept)
sleep(2)
os.system("mpg123 " + error)
