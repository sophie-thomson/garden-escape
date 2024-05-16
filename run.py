# Write your code to expect a terminal of 80 characters wide and 24 rows high

from pyfiglet import figlet_format
from colorama import Fore, Back, Style
import story_text as st

def get_player_name():
  """
  Function to get gamer name from user. Will capitalise whatever name the user 
  enters.
  """
  user_name = input("Please enter your chosen player name: \n\n").capitalize()
  player = user_name
  
  print(Fore.YELLOW + f"\nGood luck {player}!\n")  
  return player

def start_adventure():
  print(Fore.CYAN +"You will need your wits about you if you are going to make it out alive!\n")
  print(Fore.WHITE + st.INTRO_TEXT)

  start_choice = input(Fore.YELLOW + "Are you ready? y / n : \n")
  

def run_spider_story():
  print(st.SPIDER_TEXT)
  print("Do you:\n")
  print(Fore.MAGENTA + st.SPIDER_OPTION_A)
  print(Fore.CYAN + st.SPIDER_OPTION_B)

  get_spider_choice()
  
def get_spider_choice():
  """
  Function to get choice input from user.
  Run a while loop to collect a valid entry of a or b from the user 
  via the terminal. The loop will repeatedly request data, until it is valid.
  """
  while True:
    print(Fore.WHITE + "Choose wisely...\n")
    spider_choice = input(Fore.YELLOW + "Enter a or b: \n").lower() 
    if validate_story_choice(spider_choice): #spider_choice is the data that we want to check
      print("Choice is valid!")
      break # if the choice is valid (True) the break command stops the while loop
  return spider_choice

def run_spider_choice():

  player_choice_1 = get_spider_choice()
  if player_choice_1 == a:
    print(Fore.WHITE + st.SPIDER_OPTION_A_TEXT)
  else:
    print(Fore.WHITE + st.SPIDER_OPTION_B_TEXT)
  
  import spider

def validate_story_choice(value):
  """
  Validates if the player enters a story choice value that is either 'a' or 'b'.
  Inside the try, raises a ValueError if the player enters a value that is not a or b.
  """
  try:
    if value not in ["a", "b"]:
     raise ValueError(Fore.RED + f"A single letter 'a' or 'b' is required. You entered '{value}'.")
  except ValueError as e:
    print(Fore.RED + f"Invalid entry. {e} \nPlease try again.")
    return False #if error is raised, returns False
    
  return True #if function runs without any errors, then returns True 

def validate_restart_choice():
  pass

def main():
  get_player_name()
  start_adventure()
  run_spider_story()
  run_spider_choice()

  # Title text to see before any functionality
print("       A choose-your-own adventure story created by Sophie Thomson:")
print(Fore.RED + figlet_format("    G A R D E N\n    E S C A P E", font = "slant"))
print(Style.RESET_ALL + "           H o n e y   I   S h r u n k   T h e   C o d e r !")

print(Fore.YELLOW +r"""
                                                            *{*}*
                                                           **{*}**           
   d*b                                                      *{*}*            
   d*b         )*(                                            |              
   d*b        (***)                                           |              
    |           |                                           \ | /            
   \|/         \|/                                           \|/            """)
print(Fore.GREEN + r"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(Style.RESET_ALL)
main()



