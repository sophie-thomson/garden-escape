# Write your code to expect a terminal of 80 characters wide and 24 rows high

from pyfiglet import figlet_format
from colorama import Fore, Back, Style
import story_text as story

def get_player_name():
  """
  Function to get gamer name from user. Will capitalise whatever name the user 
  enters.
  """
  user_name = input("Please enter your chosen player name: \n\n").capitalize()
  player = user_name
  
  print(f"\nGood luck {player}!\n")

  return player

def start_adventure():
  print(story.INTRO_TEXT)
  print(Fore.CYAN +"You will need your wits about you if you are going to make it out alive!\n")
  print(Fore.MAGENTA +"Choose wisely...")


def user_choice():
  """
  Function to get choice input from user.
  Run a while loop to collect a valid entry of a or b from the user 
  via the terminal. The loop will repeatedly request data, until it is valid.
  """
  pass

def validate_story_choice():
  """
  Inside the try, raises ValueError if user enters a value that is not a or b.
  """
  try:
    if value != "a" or "b":
      raise ValueError (
        print(f"Only the single letter 'a' or 'b' required, you entered {value}")
      )
  except ValueError as e:
        print(f"Invalid entry: {e}, please try again.\n")
        return False #if error is raised, returns False
    
  return True #if function runs without any errors, then returns True 

def validate_restart_choice():
  pass

def main():
  get_player_name()
  start_adventure()

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



