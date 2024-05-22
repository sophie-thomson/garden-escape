from pyfiglet import figlet_format
from colorama import Fore, Style
import story_text as st
import story_separator as ss
import progress_prompt as pp
import importlib
import spider as sp
import title as title
import os


def get_player_name():
    """
    Gets a chosen name from the player and runs validation to check length.

    Uses a while loop to repeatedly request data, until it is valid.
    Will capitalise whatever name the user enters.

    Args:
        None

    Returns:
        str: The chosen name of the player.
    """
    while True:
        user_name = input(Fore.WHITE+" Enter your chosen player name: \n")
        player = user_name.capitalize()  # capitalises name entered by player
        if validate_player_name(player):  # player is the data to check
            break  # if the name is valid, break command stops the while loop
    os.system("clear")  # clears screen to display text at top of window    
    print(Fore.YELLOW + f"\n Good luck {player}!\n")

    return player


def validate_player_name(player_name):
    """
    Checks that the player enters at least one character and no more than 16
    characters to fit on the congratulations window if they get to the end.

    Name can include any characters, numbers and symbols, so there is no
    validation to check if they have entered a str / int / float.

    Raises a ValueError if the player enters a value that is not between 1-16
    characters.

    Args:
        player_name (str): The chosen name entered by the player.

    Returns:
        boolean: True if validation runs with no error.
        boolean: False if ValueError triggered.
    """
    try:
        length = len(player_name)
        if length < 1 or length > 16:  # checks length of name
            raise ValueError(Fore.RED +
                  f"Name must be 1-16 characters. You entered {length}")
    except ValueError as e:
        print(Fore.RED + f"Invalid data: {e}, please try again.\n")

        return False  # if error is raised, returns False

    return True  # if function runs without any errors, then returns True


def start_adventure(player_name):
    """
    Displays the intro text for the beginning of the story.
    Uses an input prompt with player name in f-string to confirm they are
    ready to start the choose-your-own adventure.

    Args:
        player_name (str): The chosen name entered by the player.

    Returns:
        None
    """
    print(Fore.CYAN + " You'll need your wits about you to make it out alive!")
    print(Fore.WHITE + st.INTRO_TEXT)
    # no input validation required. Only hitting enter will continue program
    input(Fore.YELLOW +
          f" Are you ready {player_name}? Press enter to continue... \n")


def get_story_choice():
    """
    Gets story choice input from the player.

    Uses a while loop to collect a valid entry of a or b from the player via
    the terminal. The loop will repeatedly request data, until it is valid.

    Args:
        None

    Returns:
        str: Choice of a or b entered by the player
    """
    while True:
        print(Fore.WHITE + Style.NORMAL + f" Choose wisely...\n")
        story_choice = input(Fore.YELLOW + " Enter a or b: \n").lower()
        if validate_story_choice(story_choice):  # story_choice data to check
            break  # if the choice is valid, break command stops the while loop

    return story_choice


def validate_story_choice(value):
    """
    Checks that the player enters a story choice value that is either a or b.
    Inside the try, raises a ValueError if the player enters a value that is
    not a or b.

    Args:
        value (str): The story_choice (a or b) entered by the player.

    Returns:
        boolean: True if validation runs with no error.
        boolean: False if ValueError triggered.
    """
    try:
        if value not in ["a", "b"]:
            raise ValueError(Fore.RED +
                  f"A letter 'a' or 'b' is required. You entered '{value}'.")
    except ValueError as e:
        print(Fore.RED + f" Invalid entry. {e} \nPlease try again.")

        return False  # if error is raised, returns False

    return True  # if function runs without any errors, then returns True


def display_spider_story():
    """
    Extracts narrative text from story_text file to set the scene for the
    spider section.

    Displays two options (a or b) for player to choose between to direct the
    narrative of the story and runs the display_spider_story_choices function
    (for the player to select and see the outcome of their choice.)
    """
    os.system("clear")  # clears screen to display text at top of window
    ss.story_separator()  # runs story_separator to demarcate narrative blocks
    print(Fore.WHITE + st.SPIDER_STORY_TEXT)
    print(" Do you:\n")
    print(Fore.MAGENTA + Style.BRIGHT + st.SPIDER_OPTION_A)
    print(Fore.CYAN + st.SPIDER_OPTION_B)

    display_spider_story_choices()


def display_spider_story_choices():
    """
    Runs get_story_choice function for player to enter their chosen story
    option and for their choice to be validated (validate_story_choice).

    The validated story_choice is returned to this function and an if/else
    statement displays the relevant block of narrative from the story_text
    file depending on the player's choice of a or b.
    """
    player_choice = get_story_choice()
    os.system("clear")  # clears screen to display text at top of window
    if player_choice == "a":
        sp.spider_ascii()  # displays spider ASCII Art
        print(Fore.WHITE + st.SPIDER_OPTION_A_TEXT)
        pp.progress_prompt()  # adds prompt input to press enter to continue
        display_nested_spider_choices()  # shows nested set of options
    else:
        sp.spider_ascii()  # displays spider ASCII Art
        print(Fore.WHITE + st.SPIDER_OPTION_B_TEXT)
        pp.progress_prompt()  # adds prompt input to press enter to continue


def display_nested_spider_choices():
    """
    Extracts narrative text from story_text and displays a nested set of
    options (a or b) for the player to choose between as a result of their
    first spider story_choice.

    Runs get_story_choice function for player to enter their chosen story
    option from the nested set of story options, and for their choice to
    be validated (validate_story_choice).

    The validated story_choice is returned to this function and an if/else
    statement displays the relevant block of narrative from the story_text
    file depending on the player's choice of a or b.
    """
    os.system("clear")  # clears screen to display text at top of window
    ss.story_separator()
    print(Fore.WHITE + st.NESTED_SPIDER_OPTIONS_TEXT)
    print(Fore.MAGENTA + Style.BRIGHT + st.SPIDER_OPTION_A2)
    print(Fore.CYAN + st.SPIDER_OPTION_B2)

    player_choice = get_story_choice()
    os.system("clear")  # clears screen to display text at top of window
    if player_choice == "a":
        ss.story_separator()
        print(Fore.WHITE + st.SPIDER_OPTION_A2_TEXT)
    else:
        ss.story_separator()
        print(Fore.WHITE + st.SPIDER_OPTION_B2_TEXT)

    pp.progress_prompt()  # adds prompt input to press enter to continue


def display_centipede_story():
    """
    Extracts narrative text from story_text file to set the scene for the
    centipede section.

    Runs the display_centipede_story_choices function for the player to
    view the centipede story choice options.
    """
    os.system("clear")  # clears screen to display text at top of window
    ss.story_separator()
    print(Fore.WHITE + st.CENTIPEDE_STORY_TEXT)
    pp.progress_prompt()  # adds prompt input to press enter to continue

    display_centipede_story_choices()


def display_centipede_story_choices():
    """
    Extracts narrative text from story_text and displays two centipede
    options (a or b) for the player to choose between.

    Runs get_story_choice function for player to enter their chosen story
    option, and for their choice to be validated (validate_story_choice).

    The validated story_choice is returned to this function and an if/else
    statement displays the relevant block of narrative from the story_text
    file or runs the game_over() function depending on the player's choice
    of a or b.
    """
    os.system("clear")  # clears screen to display text at top of window
    ss.story_separator()
    print(Fore.WHITE + st.CENTIPEDE_OPTIONS_TEXT)
    print(Fore.MAGENTA + Style.BRIGHT + st.CENTIPEDE_OPTION_A)
    print(Fore.CYAN + st.CENTIPEDE_OPTION_B)

    player_choice = get_story_choice()
    os.system("clear")  # clears screen to display text at top of window
    import centipede  # displays centipede ASCII Art
    if player_choice == "a":  # checks if player_choice is 'a'
        print(Fore.WHITE + st.CENTIPEDE_OPTION_A_TEXT)
        pp.progress_prompt()  # adds prompt input to press enter to continue
        os.system("clear")  # clears screen to display text at top of window
        print(Fore.WHITE + st.CENTIPEDE_GAME_OVER_TEXT)
        game_over()
    else:
        print(Fore.WHITE + st.CENTIPEDE_OPTION_B_TEXT)
        pp.progress_prompt()  # adds prompt input to press enter to continue


def display_rake_story():
    """
    Extracts narrative text from story_text file to set the scene for the
    rake section.

    Runs the display_rake_story_choices function for the player to view the
    rake story choice options.
    """
    os.system("clear")  # clears screen to display text at top of window
    ss.story_separator()
    print(Fore.WHITE + st.RAKE_STORY_TEXT)
    pp.progress_prompt()  # adds prompt input to press enter to continue

    display_rake_story_choices()


def display_rake_story_choices():
    """
    Extracts narrative text from story_text and displays two rake story
    options (a or b) for the player to choose between.

    Runs get_story_choice function for player to enter their chosen story
    option, and for their choice to be validated (validate_story_choice).

    The validated story_choice is returned to this function and an if/else
    statement displays the relevant block of narrative from the story_text
    file or runs the game_over() function depending on the player's choice
    of a or b.
    """
    os.system("clear")  # clears screen to display text at top of window
    ss.story_separator()
    print(Fore.WHITE + st.RAKE_OPTIONS_TEXT)
    print(Fore.MAGENTA + Style.BRIGHT + st.RAKE_OPTION_A)
    print(Fore.CYAN + st.RAKE_OPTION_B)

    player_choice = get_story_choice()
    os.system("clear")  # clears screen to display text at top of window
    import rake  # displays centipede ASCII Art
    if player_choice == "a":
        print(Fore.WHITE + st.RAKE_OPTION_A_TEXT)
        pp.progress_prompt()  # adds prompt input to press enter to continue
        os.system("clear")  # clears screen to display text at top of window
        print(Fore.WHITE + st.RAKE_GAME_OVER_TEXT)
        game_over()
    else:
        print(Fore.WHITE + st.RAKE_OPTION_B_TEXT)
        pp.progress_prompt()  # adds prompt input to press enter to continue
        display_nested_rake_choices()  # shows second, nested set of options


def display_nested_rake_choices():
    """
    Extracts narrative text from story_text and displays a nested set of
    options (a or b) for the player to choose between as a result of their
    first rake story_choice.

    Runs get_story_choice function for player to enter their chosen story
    option from the nested set of story options, and for their choice to
    be validated (validate_story_choice).

    The validated story_choice is returned to this function and an if/else
    statement displays the relevant block of narrative from the story_text
    file depending on the player's choice of a or b.
    """
    os.system("clear")  # clears screen to display text at top of window
    print(Fore.WHITE + st.NESTED_RAKE_OPTIONS_TEXT)
    print(Fore.MAGENTA + Style.BRIGHT + st.RAKE_OPTION_A2)
    print(Fore.CYAN + st.RAKE_OPTION_B2)

    player_choice = get_story_choice()
    if player_choice == "a":
        print(Fore.WHITE + st.RAKE_OPTION_A2_TEXT)
        pp.progress_prompt()  # adds prompt input to press enter to continue
        print(Fore.WHITE + st.END_TEXT)
    else:
        print(Fore.WHITE + st.RAKE_OPTION_B2_TEXT)
        game_over()


def game_over():
    """
    Displays game over title and invites the player to choose whether to start
    again or finish the game at that point.

    Choosing to finish the game includes an exit() function to stop the program
    from continuing to run the next block of code in main().
    """
    print(Fore.RED + Style.BRIGHT + figlet_format(
        "G A M E  O V E R", font="slant"))
    player_restart_choice = get_restart_choice()

    if player_restart_choice == "y":
        importlib.reload(title)  # reloads main title ASCII Art
        main()  # re-starts the game from the beginning
    else:
        print(Fore.WHITE + Style.NORMAL +
              "               T h a n k   Y o u   F o r   P l a y i n g !\n\n")
        exit()  # exits the program


def get_restart_choice():
    """
    Gets restart choice input from the player (y or n).

    Uses a while loop to collect a valid entry of 'y' or 'n' from the player
    via the terminal. The loop will repeatedly request data, until it is valid.

    Args:
        None

    Returns:
        str: Choice of y or n entered by the player
    """
    while True:
        print(Fore.WHITE + Style.NORMAL + " Better luck next time!\n\n")
        print(" Would you like to start again?\n")
        restart_choice = input(Fore.YELLOW + " Enter y or n: \n").lower()
        if validate_restart_choice(restart_choice):  # restart_choice to check
            break  # if the choice is valid, break command stops the while loop

    return restart_choice


def validate_restart_choice(value):
    """
    Checks that the player enters a story choice value that is either y or n.
    Inside the try, raises a ValueError if the player enters a value that is
    not y or n.

    Args:
        value (str): The story_choice (y or n) entered by the player.

    Returns:
        boolean: True if validation runs with no error.
        boolean: False if ValueError triggered.
    """
    try:
        if value not in ["y", "n"]:
            raise ValueError(Fore.RED +
                  f"A letter 'y' or 'n' is required. You entered '{value}'.")
    except ValueError as e:
        print(Fore.RED + f" Invalid entry. {e} \nPlease try again.")
        return False  # if error is raised, returns False

    return True  # if function runs without any errors, then returns True


def main():
    """
    Runs all of the main program functions in sequence.
    """
    player_name = get_player_name()
    start_adventure(player_name)
    display_spider_story()
    display_centipede_story()
    display_rake_story()
    print(Fore.YELLOW + Style.BRIGHT + figlet_format(
        f"   Congratulations\n    {player_name}!", font="small"))
    print(Fore.CYAN +
          "             Y o u   E s c a p e d   T h e   G a r d e n !\n")
    print(Fore.WHITE + Style.NORMAL +
          "               T h a n k   Y o u   F o r   P l a y i n g\n")
    exit()  # exits the program


main()
