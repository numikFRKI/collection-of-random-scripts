import sys
import time
import random

speed = 80
def write(text):
    for letter in text: 
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)
    print('')



write("welcome KekGPT")
input(">> ")
print("thinking...")
time.sleep(3)

if input == input:
    write('shut the fuck up.')
else: #lol
    print("how did you get here?")

sys.exit()