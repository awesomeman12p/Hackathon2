import random

#print welcome message
print("Welcome to the Magic 8 Ball!")
print(' ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n',
'⣿⣿⣿⣿⣿⣿⣿⡿⠟⣉⣡⣤⣴⣶⣶⣶⣶⣦⣤⣌⣉⠻⢿⣿⣿⣿⣿⣿⣿⣿\n',
'⣿⣿⣿⣿⣿⠟⢁⣴⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿\n',
'⣿⣿⣿⡿⢁⣴⡟⠁⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿\n',
'⣿⣿⡟⢡⣿⠏⠀⠀⢠⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠉⠙⠻⣿⣿⣿⡌⢻⣿⣿\n',
'⣿⣿⠁⣾⠏⠀⠀⣰⣿⣿⣿⣿⣿⡿⠁⠀⠀⢠⡤⠤⣤⠀⠀⠘⢿⣿⣷⠈⣿⣿\n',
'⣿⡇⢰⣿⠀⠀⢰⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠸⣄⣀⣟⠀⠀⠀⠘⣿⣿⡆⢸⣿\n',
'⣿⡇⢸⣿⠀⢠⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⢠⡏⠀⠈⣷⠀⠀⢠⣿⣿⡇⢸⣿\n',
'⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠻⠶⠞⠃⠀⢀⣾⣿⣿⠇⢸⣿\n',
'⣿⣿⡀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⢀⣠⣴⣿⣿⣿⡿⢀⣿⣿\n',
'⣿⣿⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣼⣿⣿\n',
'⣿⣿⣿⣷⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣾⣿⣿⣿\n',
'⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿\n',
'⣿⣿⣿⣿⣿⣿⣿⣷⣦⣉⡙⠛⠻⠿⠿⠿⠿⠟⠛⢋⣉⣴⣾⣿⣿⣿⣿⣿⣿⣿\n',
'⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n')
#from https://emojicombos.com/eight-ball-ascii-art


#ask for input from user
input("Ask a question to the Magic 8 ball. ")
#pick a random prompt
prompt = random.randint(1, 6)
if prompt == 1:
    print("\nThe magic 8 ball says No.")

if prompt == 2:
    print("\nThe magic 8 ball says Yes.")

if prompt == 3:
    print("\nThe magic 8 ball says Maybe.")

if prompt == 4:
    print("\nThe magic 8 ball says Most definitely. ")

if prompt == 5:
    print("\nThe magic 8 ball says You will have to ask again.")

if prompt == 6:
    print("\nThe magic 8 ball says As I see it without a doubt.")

