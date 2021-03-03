'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	a program that asks you to input your wins and losses and puts you in a specific group

Author:	Adhvaryu.J

Created:	03/03/2021
------------------------------------------------------------------------------
'''

print("****** Tournament Tracker ******")
print("")

wins = 0
losses = 0

# get amount of wins and losses and add them up
print("Enter the wins (W) and losses (L) for you team: ")
for i in range(6):
  games_played = str(input(""))
  if games_played == "W":
    wins = wins + 1
  elif games_played == "L":
    losses = losses + 1
  else :
    print("Please enter the values W or L again")

# output results based off wins and losses
if wins == 5 or wins == 6:
  print("Your team is in group 1")
elif wins == 3 or wins == 4:
  print("Your team is in group 2")
elif wins == 1 or wins == 2:
  print("Your team is in group 3")
else :
  print("Your team has been eliminated from the tournament")


  
