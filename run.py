from pyfiglet import figlet_format
from colorama import Fore, Back, Style
import story_text as st
import story_separator as ss
import importlib


def get_player_name():
  """
  Function to get gamer name from user. Will capitalise whatever name the user 
  enters.
  """
  while True:
    user_name = input(Fore.WHITE + " Please enter your chosen player name: \n").capitalize()
    player = user_name
    if validate_player_name(player): #player is the data that we want to check
      break # if the name is valid (True) the break command stops the while loop
  
  print(Fore.YELLOW + f"\n Good luck {player}!\n")
  return player


def validate_player_name(name):
  """
  Checks that the player enters at least one character as a name, but also checks
  that the length of the name is no more than 16 characters so it will fit on the
  congratulations window if they make it to the end.

  The name can be anything they want, so there is no validation to check if they
  have entered any sybmols or numbers.
  """
  try:
    length = len(name)
    if length < 1 or length > 16:
      raise ValueError(Fore.RED +
        f"Name must be between 1 - 16 characters, your name has {length} characters"
      )
  except ValueError as e:
    print(Fore.RED + f"Invalid data: {e}, please try again.\n")
    return False #if error is raised, returns False
    
  return True #if function runs without any errors, then returns True 


def start_adventure(player_name):
  """
  Displays the intro text for the beginning of the story and prompts player to confirm they
  are ready to start the choose-your-own adventure.
  """
  print(Fore.CYAN +" You will need your wits about you if you are going to make it out alive!")
  print(Fore.WHITE + st.INTRO_TEXT)
  # no input validation required. As long as they press enter the next function in main() runs
  start_prompt = input(Fore.YELLOW + f" Are you ready {player_name}? Press enter to continue... \n")

  

def get_story_choice():
  """
  Function to get story choice input from user.
  Run a while loop to collect a valid entry of a or b from the user via the terminal. 
  The loop will repeatedly request data, until it is valid.
  """
  while True:
    print(Fore.WHITE + Style.NORMAL + f" Choose wisely...\n")
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
  ss.story_separator()
  print(Fore.WHITE + st.SPIDER_TEXT)
  print(" Do you:\n")
  print(Fore.MAGENTA + Style.BRIGHT + st.SPIDER_OPTION_A)
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
  ss.story_separator()
  print(Fore.WHITE + st.NESTED_SPIDER_OPTIONS_TEXT)
  print(Fore.MAGENTA + Style.BRIGHT + st.SPIDER_OPTION_A2)
  print(Fore.CYAN + st.SPIDER_OPTION_B2)

  player_choice = get_story_choice()
  
  if player_choice == "a":
    ss.story_separator()
    print(Fore.WHITE + st.SPIDER_OPTION_A2_TEXT)
  else:
    ss.story_separator()
    print(Fore.WHITE + st.SPIDER_OPTION_B2_TEXT)
    
  progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")


def display_centipede_story():
  """
  Displays narrative text from story_text file to set the scene for centipede section.
  Displays options for player to choose between to direct the narrative and runs the 
  display_centipede_story_choices function for the player to make their choice.
  """
  ss.story_separator()
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
  ss.story_separator()
  print(Fore.WHITE + st.CENTIPEDE_OPTIONS_TEXT)
  print(Fore.MAGENTA + Style.BRIGHT + st.CENTIPEDE_OPTION_A)
  print(Fore.CYAN + st.CENTIPEDE_OPTION_B)

  player_choice = get_story_choice()
  import centipede # displays centipede ASCII Art
  if player_choice == "a":
    print(Fore.WHITE + st.CENTIPEDE_OPTION_A_TEXT)
    progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")
    ss.story_separator()
    print(Fore.WHITE + st.CENTIPEDE_GAME_OVER_TEXT)
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
  ss.story_separator()
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
  ss.story_separator()
  print(Fore.WHITE + st.RAKE_OPTIONS_TEXT)
  print(Fore.MAGENTA + Style.BRIGHT + st.RAKE_OPTION_A)
  print(Fore.CYAN + st.RAKE_OPTION_B)

  player_choice = get_story_choice()
  import rake # displays centipede ASCII Art
  if player_choice == "a":
    print(Fore.WHITE + st.RAKE_OPTION_A_TEXT)
    progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")
    ss.story_separator()
    print(Fore.WHITE + st.RAKE_GAME_OVER_TEXT)
    game_over ()
  else:
    print(Fore.WHITE + st.RAKE_OPTION_B_TEXT)
    progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")
    display_nested_rake_choices()
  

def display_nested_rake_choices():
  """
  Runs get_story_choice function for player to enter their chosen story option and 
  for the choice to be validated (validate_story_choice).

  If valid, the choice is returned to this function for the program to display the 
  next block of story text depending on the chosen outcome along with some ASCII art.
  """
  print(Fore.WHITE + st.NESTED_RAKE_OPTIONS_TEXT)
  print(Fore.MAGENTA + Style.BRIGHT + st.RAKE_OPTION_A2)
  print(Fore.CYAN + st.RAKE_OPTION_B2)

  player_choice = get_story_choice()
  if player_choice == "a":
    print(Fore.WHITE + st.RAKE_OPTION_A2_TEXT)
    progress_prompt = input(Fore.YELLOW + " Press enter to continue... \n")
    print(Fore.WHITE + st.END_TEXT)
    # print(Fore.YELLOW + figlet_format("   Congratulations!", font = "small"))
    # print("             Y o u   E s c a p e d   T h e   G a r d e n !\n\n")
    # print(Fore.WHITE + "               T h a n k   Y o u   F o r   P l a y i n g !\n\n")
    # exit() # exits the program
  else:
    print(Fore.WHITE + st.RAKE_OPTION_B2_TEXT)
    game_over()


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
    print(Fore.WHITE + "               T h a n k   Y o u   F o r   P l a y i n g !\n\n")
    exit() # exits the program


def get_restart_choice():
  """
  Function to get choice input from user.
  Run a while loop to collect a valid entry of y or n from the user 
  via the terminal. The loop will repeatedly request data, until it is valid.
  """
  while True:
    print(Fore.WHITE + f" Better luck next time!\n\n Would you like to start again?\n")
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
  player_name = get_player_name()
  start_adventure(player_name)
  display_spider_story()
  display_centipede_story()
  display_rake_story()
  print(Fore.YELLOW + figlet_format(f"   Congratulations\n    {player_name}!", font = "small"))
  print(Fore.CYAN +"             Y o u   E s c a p e d   T h e   G a r d e n !\n")
  print(Fore.WHITE + "               T h a n k   Y o u   F o r   P l a y i n g !\n")
  exit() # exits the program


# Title text to see before any functionality
import title # displays main title ASCII Art
main()



