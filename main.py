#import cmd
#import textwrap
import sys
import os
import time


#welcome message
print("Welcome to Group 3 walls Game")

#define while loop variable
x= 'y'

#run program class
def run():

  #waits to clear screen
  time.sleep(10)
  #clears screen
  os.system('clear')

  #print and retrive option
  print("\nSelect one option below")
  start = int(input('1. Dice\n2. Magic 8 ball\n3. kings\n4. exit\n'))

  #ifs
  if start == 1:
    exec(open("dice.py").read())
  elif start == 2:
    exec(open("magic8ball.py").read())
  elif start == 3:
    exec(open("kings.py").read())
  elif start == 4:
    print("goodbye")
    sys.exit()
    
  
    
#ends class
run()

#runs class while varible is true
while x == 'y':
  run()

'''
def menuChoice():
  print('1: Dice')
  print('2: Magic 8 Ball')
  print('3: Quit')
  choice= int(input('What would you like to do?'))
  while int(choice) < 1 or int(choice) > 3:
    print('That is not a valid choice.')
    print('Please enter a number between 1 and 3:')
    choice=input()
  return choice
menuChoice()

option = menuChoice()
print(option)
while option != 3:
  if option == 1:
    exec(open("dice.py").read())
  elif option ==2:
    exec(open("magic8ball.py").read())
  else:
    print("goodbye")
    sys.exit()
    '''