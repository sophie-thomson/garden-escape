
# Garden Escape: Honey I Shrunk the Coder!

Garden Escape: Honey I Shrunk the Coder! is a fun choose-your-own adventure story game where you play the role of a tiny software developer who has to make a series of key decisions to choose the direction of the narrative and try to survive until the end of the story.

Can you fight your way through your jungle-sized garden, past giant creepy crawlies and garden tools back to the safety of your kitchen? Choose from the options presented to you as you progress through the story and follow the prompts on screen to see if you can make it home and escape the garden.

The story includes references that will appeal to developers, but is equally fun and easy to understand if you have no coding experience at all.

This terminal-based project is coded in Python and is designed to view on a laptop / desktop computer screen. It will not display correctly on a mobile.

The live site can be found here: https://garden-escape-185db543c454.herokuapp.com/

![Multi-device mockup](docs/readme-images/multi-device-mockup.png)

## Features

### Game Title (title.py)

***Title Text***

- 'Garden Escape' displayed in large text to provide clear heading to mark the beginning of the story and to give an impression of a big adventure ahead. 
- Colour red used to indicate danger and risk
- 'Honey I Shrunk the Coder!' in default font, but with spacing between letters to stand out from regular text and appear larger to work visually alongside main title text.
- 'Garden Escape' text created using [pyfiglet 1.0.2](https://pypi.org/project/pyfiglet/) library imported from Python Package Index (PyPI) with ['slant'](http://www.figlet.org/examples.html) font. 
- Red text colour created using [Colorama 0.4.6](https://pypi.org/project/colorama/) library imported from PyPI.

***ASCII Art***
- A garden themed strip of ASCII art to help set the scene alongside the title text.
- Different coloured output created using Colorama’s constant shorthand for ANSI escape sequences.

***Enter Name: input()***
- The player is invited to enter a name for their story character.
- The name must be at least 1 character long, but less than 16 characters so it fits in the final congratulations window at the end of the story.
- The entered name is passed through validation function validate_player_name() and if it does not pass validation then an error message is displayed to the player with a prompt to try again.
- The error message is in red text to highlight that there is problem that needs attention.

![Screenshot of title on desktop](docs/readme-images/title.png)
![Screenshot of title with name entered and error messages](docs/readme-images/player-name-errors.png)

### Introduction

***Good Luck Message***

- 

***Intro Text***

- story_text.py
- 

***Start Game: input()***

- progress_prompt.py

![Screenshot of Introduction with Good Luck message and Start Game prompt]()

***Functions Used (run.py)***

- 
- 
- 

### Spider Section

***Story Text***

- 

***Options Text***

- 
- 

![Screenshot of Spider Section with story options]()
![Screenshot of ]()

***Player Choice: input()***

- 
- 

![Screenshot of Player Choice input with error messages]()

***Nested Spider Options***

- 


![Screenshot of Nested Spider Options]()

### Centipede Section

***Story Text***

- 

***Options Text***

- 
- 

![Screenshot of Centipede Section with story options]()
![Screenshot of ]()

***Player Choice: input()***

- 
- 

![Screenshot of Player Choice input with error messages]()

### Rake Section

***Story Text***

- 

***Options Text***

- 
- 

![Screenshot of Centipede Section with story options]()
![Screenshot of ]()

***Player Choice: input()***

- 
- 

![Screenshot of Player Choice input with error messages]()

***Nested Rake Options***

- 

![Screenshot of Nested Rake Options]()

### Game Over

***Game Over Text***
- 

![Screenshot of Game Over Screen]()

***Restart Game: input()***

- 

![Screenshot of Player Choice input with error messages]()

***End Credits***

- 

![Screenshot of End Credits]()

### Game Completion

***Congratulations Text***

- 

***Congratulations Text***

- 

![Screenshot of Congratulations Screen]()

### Existing Features

- CRUD Functionality (Create, Read, Update, Delete)
- Error Handling
- Heroku Deployment
- All content written and presented to fit on window of 80 characters wide x 24 lines high.
- 

### Future Features
To expand on this project, there are a number of features that could be added to enhance player enjoyment and functionality:
- 
- The option to 
 
## Design

### Planning Process

***Story Writing***

- ChatGPT

***Logic Mapping***

- A flow diagram following the story narrative .

![Screenshot of Flow Diagram]()


### Building in Python

***Process***

- Incremental Coding
- 

***Data Model***

- 

***List of Functions***

- get name and validation
- display story choices
- continue choice
- Separate py files

***Imported Libraries***

- pyfiglet
- 

***ASCII Art***

- Designed using raw print data
- Colorama
- Separate py files

![Screenshot of spider ASCII Art]()
![Screenshot of centipede ASCII Art]()
![Screenshot of rake ASCII Art]()
![Screenshot of story_separator ASCII Art]()
![Screenshot of game_over separator ASCII Art]()

### Layout and Styling

- All content written and presented to fit on window of 80 characters wide x 24 lines high.
- Consistent use of colours for repeating elements to improve user experience and readability:
    - White: Narrative text
    - Yellow: Call to attention for player to interact with game
    - Cyan and Magenta: Used to highlight story options to choose from
    - Red: Used to highlight important information such as error messages and main titles
- Story separator
- Game over separator

## Testing

### Logic Flow

***Method of Testing***

- 

***Results***

- 
- 


### Validation and Error Handling

- 
- 

### ASCII Art Loading

***Method of Testing***

- 

***Results***

- 

### Script Functionality

***Method of Testing***

- 

***Results***

- 
        
### Validator Testing

- PYTHON
    -  No errors were found when passing through the Pep8 Validator [CI Python Linter](https://pep8ci.herokuapp.com/)

![Screenshot of Python validation results for run.py]()
![Screenshot of Python validation results for story_text.py]()
![Screenshot of Python validation results for centipede.py]()
![Screenshot of Python validation results for game_over_separator.py]()
![Screenshot of Python validation results for progress_prompt.py]()
![Screenshot of Python validation results for rake.py]()
![Screenshot of Python validation results for spider.py]()
![Screenshot of Python validation results for story_separator.py]()
![Screenshot of Python validation results for title.py]()

- GitPod Problems
    - No problems detected within the Gitpod Garden-Escape workspace

### Unfixed Bugs

- On occassion there is some residual code from the title text or ascii art that is not cleared by the os.system("clear") function. This issue is inconsistent and does not affect the user experience as it is not visible unless the player chooses to scroll up on the terminal window. I have not been able to identify a reason for this issue, but as it does not impact the intended functionality and use of the program I have kept the title text and ascii art in the program.
- No other bugs.

## Deployment

### Gitpod Version Control
This site was created using the Gitpod cloud development environment before being pushed through to a dedicated repository on Github.

The following commands were used througout development to push the code through to the Github repo:

- **git add .** - This command was used to add any tracked files to the staging area.
- **git commit -m "Commit message."** - This command was used to create a snapshot of the staged area with a short description.
- **git push** - This command was used to push the committed changes from the current branch to the remote repository on Github.

### Deployment

The finished program was initially hosted within a repository on Github, and then this Github repository was connected with Heroku, the site through which the final project was deployed.

***How to Deploy to Heroku***

The steps to deploy to Heroku are as follows:
- 
- 
- 
- 

## Credits

### Content

***Data Model***

- [Portal Hunt](https://github.com/JackLamb99/portal-hunt/) by Jack Lamb was referred to as an example of how to structure the story narrative data (story_text.py) ready to be imported and used in run.py. 

No code was taken from Jack's project, but it was useful for considering a suitable data model. 

***Python***

- The CI walkthrough project 'Love Sandwiches' was used as a reference example when building the error handling functions; validate_player_name() and validate_story_choice()
- A tutorial on [YouTube ' How to create ASCII art text in Python'](https://youtu.be/Y0QiBbI3MWs) was used as guidance on how to import and use pyfiglet library to create the title and game over text
- Guidance on [Geeks for Geeks](https://www.geeksforgeeks.org/python-docstrings/) was used as reference for best practice when writing docstrings
- Guidance on [Python Morsels](https://www.pythonmorsels.com/breaking-long-lines-code-python/) was used as reference for breaking up long lines of code to fit within the 80 character constraints 
- A World Class Tech Ed tutorial on [YouTube](https://www.youtube.com/watch?v=z8yw9gUJaHo) was used as a reference when creating my own ASCII art
- Guidance on [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/) was used as reference for how to clear the screen in python using os.system("clear")
- The code in a [StackOverflow discussion](https://stackoverflow.com/questions/1254370/reimport-a-module-while-interactive) was adapted to enable the title content to be re-imported if the player chooses to re-start the game.
- 
- 

## Code & Technology
 The following code, platforms and apps were used in the creation of this program:
 - Python - The program is written in Python code and is run within a Python Terminal.
 - [Stack Overflow](https://stackoverflow.com/) - used as a reference for possible syntax of Python code.
 - [Geek for Geeks](https://www.geeksforgeeks.org/) - used for guidance on best practice and syntax. 
 - [Gitpod](https://gitpod.io/) - Cloud development environment used to write and preview code before committing.
 - [Github](https://github.com/) - Github hosts the Garden Escape: Honey I Shrunk the Coder! repository and connects to Heroku where the site is deployed.
 - [Heroku](https://dashboard.heroku.com/apps) - a cloud-based Platform as a Service (PaaS) that Garden Escape is deployed through
 - [Lucidchart](https://www.lucidchart.com/pages/) - used to create flow diagram to map out program logic
 - [ChatGPT](https://chatgpt.com/) - used to generate initial ideas for narrative structure and what choose-your-own adventure options might look like
 - Google Docs - used to write out story narrative, building on some parts of the content provided by ChatGPT
 - [pyfiglet (PyPI)](https://pypi.org/project/pyfiglet/) - used to generate the ASCII Art text for the game title, game over and congratulations text
 - [Colorama (PyPI)](https://pypi.org/project/colorama/) - used to change colour of output within the Python terminal
 - Import of [os](https://docs.python.org/3/library/os.html) built-in operating system library - used for clear screen function to help with styling and readability
 - Import of [importlib](https://docs.python.org/3/library/importlib.html) built-in import implementation library - used to reimport function to enable player to re-start from the beginning of the game.
