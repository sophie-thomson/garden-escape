from pyfiglet import figlet_format
from colorama import Fore, Back, Style
import story_text as st
import importlib


def get_player_name():
  """
  Function to get gamer name from user. Will capitalise whatever name the user 
  enters.
  """
  user_name = input(" Please enter your chosen player name: \n").capitalize()
  player = user_name
  
  print(Fore.YELLOW + f"\n Good luck {player}!\n")  
  return player


def start_adventure():
  """
  Displays the intro text for the beginning of the story and prompts player to confirm they
  are ready to start the choose-your-own adventure.
  """
  print(Fore.CYAN +" You will need your wits about you if you are going to make it out alive!")
  print(Fore.WHITE + st.INTRO_TEXT)
  # no input validation required. As long as they press enter the next function in main() runs
  start_prompt = input(Fore.YELLOW + f" Are you ready? Press enter to continue... \n")  
  

def get_story_choice():
  """
  Function to get story choice input from user.
  Run a while loop to collect a valid entry of a or b from the user via the terminal. 
  The loop will repeatedly request data, until it is valid.
  """
  while True:
    print(Fore.WHITE + " Choose wisely...\n")
    story_choice = input(Fore.YELLOW + " Enter a or b: \n").lower() 
    if validate_story_choice(story_choice): #story_choice is the data that we want to check
      break # if the choice is valid (True) the break command stops the while loop
    
  return story_choice
  

def validate_story_choice(value):
  """
  Validates if the player enters a story choice value that is either 'a' or 'b'.
  Inside the try, raises a ValueError if the player enters a value that is not a or b.
  """
  try:
    if value not in ["a", "b"]:
     raise ValueError(Fore.RED + f"A single letter 'a' or 'b' is required. You entered '{value}'.")
  except ValueError as e:
    print(Fore.RED + f" Invalid entry. {e} \nPlease try again.")
    return False #if error is raised, returns False
    
  return True #if function runs without any errors, then returns True


def display_spider_story():
  """
  Displays narrative text from story_text file to set the scene for spider section.
  Displays options for player to choose between to direct the narrative and runs the 
  display_spider_story_choices function for the player to make their choice.
  """
  print(Fore.WHITE + st.SPIDER_TEXT)
  print(" Do you:\n")
  print(Fore.MAGENTA + st.SPIDER_OPTION_A)
  print(Fore.CYAN + st.SPIDER_OPTION_B)

  display_spider_story_choices()


def display_spider_story_choices():
  """
  Runs get_story_choice function for player to enter their chosen story option and 
  for the choice to be validated (validate_story_choice).

  If valid, the choice is returned to this function for the program to display the 
  next block of story text depending on the chosen outcome along with some ASCII art.
  """
  player_choice = get_story_choice()
  if player_choice == "a":
    import spider # displays spider ASCII Art
    print(Fore.WHITE + st.SPIDER_OPTION_A_TEXT)
    progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")
    display_nested_spider_choices()
  else:
    import spider # displays spider ASCII Art
    print(Fore.WHITE + st.SPIDER_OPTION_B_TEXT)
    progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")
  

def display_nested_spider_choices():
  """
  Runs get_story_choice function for player to enter their chosen story option and 
  for the choice to be validated (validate_story_choice).

  If valid, the choice is returned to this function for the program to display the 
  next block of story text depending on the chosen outcome along with some ASCII art.
  """
  print(Fore.WHITE + st.NESTED_SPIDER_OPTIONS_TEXT)
  print(Fore.MAGENTA + st.SPIDER_OPTION_A2)
  print(Fore.CYAN + st.SPIDER_OPTION_B2)

  player_choice = get_story_choice()
  if player_choice == "a":
    print(Fore.WHITE + st.SPIDER_OPTION_A2_TEXT)
  else:
    print(Fore.WHITE + st.SPIDER_OPTION_B2_TEXT)
    
  progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")


def display_centipede_story():
  """
  Displays narrative text from story_text file to set the scene for centipede section.
  Displays options for player to choose between to direct the narrative and runs the 
  display_centipede_story_choices function for the player to make their choice.
  """
  print(Fore.WHITE + st.CENTIPEDE_STORY_TEXT)
  progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")

  display_centipede_story_choices()


def display_centipede_story_choices():
  """
  Runs get_story_choice function for player to enter their chosen story option and 
  for the choice to be validated (validate_story_choice).

  If valid, the choice is returned to this function for the program to display the 
  next block of story text depending on the chosen outcome along with some ASCII art.
  """
  print(Fore.WHITE + st.CENTIPEDE_OPTIONS_TEXT)
  print(Fore.MAGENTA + st.CENTIPEDE_OPTION_A)
  print(Fore.CYAN + st.CENTIPEDE_OPTION_B)

  player_choice = get_story_choice()
  import centipede # displays centipede ASCII Art
  if player_choice == "a":
    print(Fore.WHITE + st.CENTIPEDE_OPTION_A_TEXT)
    game_over ()
  else:
    print(Fore.WHITE + st.CENTIPEDE_OPTION_B_TEXT)
    
  progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")


def display_rake_story():
  """
  Displays narrative text from story_text file to set the scene for rake section.
  Displays options for player to choose between to direct the narrative and runs the 
  display_spider_story_choices function for the player to make their choice.
  """
  print(Fore.WHITE + st.RAKE_STORY_TEXT)
  progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")

  display_rake_story_choices()


def display_rake_story_choices():
  """
  Runs get_story_choice function for player to enter their chosen story option and 
  for the choice to be validated (validate_story_choice).

  If valid, the choice is returned to this function for the program to display the 
  next block of story text depending on the chosen outcome along with some ASCII art.
  """
  print(Fore.WHITE + st.RAKE_OPTIONS_TEXT)
  print(Fore.MAGENTA + st.RAKE_OPTION_A)
  print(Fore.CYAN + st.RAKE_OPTION_B)

  player_choice = get_story_choice()
  import rake # displays centipede ASCII Art
  if player_choice == "a":
    print(Fore.WHITE + st.RAKE_OPTION_A_TEXT)
    game_over ()
  else:
    print(Fore.WHITE + st.RAKE_OPTION_B_TEXT)
    
  progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")

def display_nested_rake_choices():
  """
  Runs get_story_choice function for player to enter their chosen story option and 
  for the choice to be validated (validate_story_choice).

  If valid, the choice is returned to this function for the program to display the 
  next block of story text depending on the chosen outcome along with some ASCII art.
  """
  print(Fore.WHITE + st.NESTED_RAKE_OPTIONS_TEXT)
  print(Fore.MAGENTA + st.RAKE_OPTION_A2)
  print(Fore.CYAN + st.RAKE_OPTION_B2)

  player_choice = get_story_choice()
  if player_choice == "a":
    print(Fore.WHITE + st.RAKE_OPTION_A2_TEXT)
  else:
    print(Fore.WHITE + st.RAKE_OPTION_B2_TEXT)
    
  progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")


def game_over():
  """
  Displays game over title and invites the player to choose whether to start again
  or finish the game at that point.

  Choosing to finish the game includes an exit() function to stop the program from
  continuing to run the next block of code in main().
  """
  print(Fore.RED + figlet_format("G A M E  O V E R", font = "slant"))
  player_restart_choice = get_restart_choice()

  if player_restart_choice == "y":
    importlib.reload(title) # reloads main title ASCII Art
    main() # re-starts the game from the beginning
  else:
    print(Fore.WHITE + "               T h a n k   y o u   f o r   p l a y i n g !\n\n")
    exit() # exits the program


def get_restart_choice():
  """
  Function to get choice input from user.
  Run a while loop to collect a valid entry of y or n from the user 
  via the terminal. The loop will repeatedly request data, until it is valid.
  """
  while True:
    print(Fore.WHITE + " Better luck next time!\n Would you like to start again?\n")
    restart_choice = input(Fore.YELLOW + " Enter y or n: \n").lower()
    if validate_restart_choice(restart_choice): #restart_choice is the data that we want to check
      break # if the choice is valid (True) the break command stops the while loop
    
  return restart_choice


def validate_restart_choice(value):
  """
  Validates if the player enters a story choice value that is either 'a' or 'b'.
  Inside the try, raises a ValueError if the player enters a value that is not a or b.
  """
  try:
    if value not in ["y", "n"]:
     raise ValueError(Fore.RED + f"A single letter 'y' or 'n' is required. You entered '{value}'.")
  except ValueError as e:
    print(Fore.RED + f" Invalid entry. {e} \nPlease try again.")
    return False #if error is raised, returns False
    
  return True #if function runs without any errors, then returns True


def main():
  player = get_player_name()
  start_adventure()
  display_spider_story()
  display_centipede_story()
  display_rake_story()
  
  
  










  # Title text to see before any functionality
import title # displays main title ASCII Art
main()



