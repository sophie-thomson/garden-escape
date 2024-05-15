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
  print(Style.RESET_ALL)
  print(st.INTRO_TEXT)
  return player

def start_adventure():
  print(Fore.CYAN +"You will need your wits about you if you are going to make it out alive!\n")
  print(Style.RESET_ALL)

  start_choice = input("Are you ready? y / n : \n")
  

def run_spider_story():
  import spider
  print(st.SPIDER_TEXT)
  print(Fore.CYAN + "Do you:")
  print(Style.RESET_ALL)
  print(st.SPIDER_OPTIONS)

  get_spider_choice()
  
def get_spider_choice():
  print(Fore.MAGENTA +"Choose wisely...")
  print(Style.RESET_ALL)
  spider_choice = input("Enter a or b: \n") 
  

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
  run_spider_story()

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



