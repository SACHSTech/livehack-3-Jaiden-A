'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	a program that allows you to enter the distance you drove until you pass 100 km

Author:	Adhvaryu.J

Created:	03/03/2021
------------------------------------------------------------------------------
'''

print("******  Welcome to the DoorDash Distance Tracker  ******")
print("")

print("** Travel Log **")
total = 0
days = 0

# get the distance travelled until they reach 100km
while total <= 100:
  distance_travelled = int(input("Enter the distance travelled for the day: "))

  # compute the days it took and average km per day
  total = total + distance_travelled
  days = days + 1
  average = total/days 

# output the amount of days it took to drive 100km
print("")
print("** Summary **")
print("It took " + str(days) + " days to surpass 100km driven.")
print("The average distance driven per day is " + str(average) + "km")