from colorama import Fore


def progress_prompt():
    """
    Repeatable function to add a prompt for the player to hit enter
    to continue the story.
    """
    input(Fore.YELLOW + " Press enter to continue... \n")
