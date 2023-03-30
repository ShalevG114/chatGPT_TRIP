import openai
import os
import datetime
import planning_service

start_input = input("Would you like to plan a new trip? Yes / No\n")

dest_list=("LONDON", "CHINA", "ISRAEL")

if start_input.upper() == "YES" or start_input.upper() == "Y":  
  destination = input("Ok! Where would you like to go?\n")
  if destination.upper() in dest_list:
    print("Great! Let's start planning your trip to", destination)
  else: 
    print("No data found on", destination)
  
else:
  print("Ok, maybe another time!")