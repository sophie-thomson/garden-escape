from colorama import Fore


def story_separator():
    """
    Creates an ASCII art strip used to demarcate different sections of 
    narrative and improve spacing for better user experience.
    """
    print(Fore.YELLOW + "             (*)                  (*)           \
     (*)     (*)        (*)")
    print(Fore.GREEN + "             ~|~                  ~|~            \
    ~|~     ~|~        ~|~")
    print(Fore.GREEN + "||||||||||||||||||||||||||||||||||||||||||||||||||\
|||||||||||||||||||||||||")
