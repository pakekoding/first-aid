#Original source: Python Typing Text Effect - www.101computing.net/python-typing-text-effect/

import time,os,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")

for line in open("[your-own-motivational-text-file].txt", "r"):
  typingPrint(line)