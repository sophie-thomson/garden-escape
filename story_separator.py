from colorama import Fore


def story_separator():
    """
    Creates ASCII art to demarcate different sections of narrative and improve
    spacing for better user experience.
    """
    print(Fore.RED + "          (*)                 (*)            \
    (*)     (*)         (*)")
    print(Fore.GREEN + r"""           |                   |                  |
   |       |          |        |   |        |     |      ||           |  |
   |       |  |      ||      | |   |      | ||    |      |||     |    || |
  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
  """)
