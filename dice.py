import random
#x= 'y'


def dice():
  import random

  print("\nWelcome to dice game!")
  print("\n-Brought to you by WALL-3")
  print(
  "\n   _______",
  "\n  /\ o o o\ ",
  '\n /o \ o o o\_______',
  '\n<    >------>   o /|',
  '\n \ o/  o   /_____/o|',
  '\n  \/______/     |oo|',
  '\n        |   o   |o/',
  '\n        |_______|/')
  #art by R. Shawn Butler
  #https://www.asciiart.eu/miscellaneous/dice
  #enter to roll
  
  #ask for player names and store
  name1 = input("\nWhat is player 1's name: ")
  name2 = input("\nWhat is player 2's name: ")
  
  #ask person to press enter to roll again
  input("\n" + name1.capitalize() + " press enter to roll!")
  
  #roll
  name1Score = random.randint(1, 6)
  
  
  #if statments for player 1
  if name1Score == 1:
      print("\n┌─────────┐",
          "\n│         │",
          "\n│    ●    │",
          "\n│         │",
          "\n└─────────┘",)
      print("\n", name1.capitalize(), "you rolled a 1!")
  elif name1Score == 2:
      print("\n┌─────────┐",
          "\n│  ●      │",
          "\n│         │",
          "\n│      ●  │",
          "\n└─────────┘",)
      print("\n", name1.capitalize(), "you rolled a 2!")
  elif name1Score == 3:
      print("\n┌─────────┐",
          "\n│  ●      │",
          "\n│    ●    │",
          "\n│      ●  │",
          "\n└─────────┘",)
      print("\n", name1.capitalize(), "you rolled a 3!")
  elif name1Score == 4:
      print(
          "\n┌─────────┐",
          "\n│  ●   ●  │",
          "\n│         │",
          "\n│  ●   ●  │",
          "\n└─────────┘",)
      print("\n", name1.capitalize(), "you rolled a 4!")
  elif name1Score == 5:
      print("\n┌─────────┐",
          "\n│  ●   ●  │",
          "\n│    ●    │",
          "\n│  ●   ●  │",
          "\n└─────────┘")
      print("\n", name1.capitalize(), "you rolled a 5!")
  
  else:
        print("\n┌─────────┐",
          "\n│  ●   ●  │",
          "\n│  ●   ●  │",
          "\n│  ●   ●  │",
          "\n└─────────┘",)
        print("\n", name1.capitalize(), "you rolled a 6!")
      
  
  
  
  #ask to preess enter to roll
  input("\n" + name2.capitalize() + " press enter to roll!")
  
  #roll player 2
  name2Score = random.randint(1, 6)
  
  #if for player 2
  if name2Score == 1:
      print("\n┌─────────┐",
          "\n│         │",
          "\n│    ●    │",
          "\n│         │",
          "\n└─────────┘",)
      print("\n", name2, "you rolled a 1!")
  elif name2Score == 2:
      print("\n┌─────────┐",
          "\n│  ●      │",
          "\n│         │",
          "\n│      ●  │",
          "\n└─────────┘",)
      print("\n", name2, "you rolled a 2!")
  elif name2Score == 3:
      print("\n┌─────────┐",
          "\n│  ●      │",
          "\n│    ●    │",
          "\n│      ●  │",
          "\n└─────────┘",)
      print("\n", name2, "you rolled a 3!")
  elif name2Score == 4:
      print(
          "\n┌─────────┐",
          "\n│  ●   ●  │",
          "\n│         │",
          "\n│  ●   ●  │",
          "\n└─────────┘",)
      print("\n" ,name2, "you rolled a 4!")
  elif name2Score == 5:
      print("\n┌─────────┐",
          "\n│  ●   ●  │",
          "\n│    ●    │",
          "\n│  ●   ●  │",
          "\n└─────────┘")
      print("\n", name2, "you rolled a 5!")
  
  else: 
        print("\n┌─────────┐",
          "\n│  ●   ●  │",
          "\n│  ●   ●  │",
          "\n│  ●   ●  │",
          "\n└─────────┘",)
        print("\n", name2, "you rolled a 6!")
  
  #define score variables
  score1 = 0
  score2 = 0
  
  #decide who wins
  if name1Score > name2Score:
      print("\n" + name1.capitalize(), "you win!")
      score1 += 1 
  elif name2Score > name1Score:
      print("\n" + name2.capitalize(), "you win!")
      score2 += 1
      # name1Score == name2Score
  else:
     print("\nIt's a tie!")
    
  #display scores
  print(score1)
  print(score2)
dice() 


#play multiple times

#for i = 0


