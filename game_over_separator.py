from colorama import Fore


def game_over_separator():
    """
    Creates an ASCII art strip used to demarcate different sections of 
    narrative and improve spacing for better user experience.
    """
    print(Fore.RED + "             (*)                  (*)           \
     (*)     (*)        (*)")
    print(Fore.RED + "             ~|~                  ~|~            \
    ~|~     ~|~        ~|~")
    print(Fore.RED + "||||||||||||||||||||||||||||||||||||||||||||||||||\
|||||||||||||||||||||||||||||")
