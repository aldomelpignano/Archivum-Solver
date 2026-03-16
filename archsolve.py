import zipfile

from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

history = InMemoryHistory()

import shlex
import os

from utils.display_banner import display_banner, clear_screen
from utils.help import display_help
from utils.extract import extract_command

def manage_input():
## Function used to manage user input
    try:
        while True:
            user_input_value = prompt("archsolve > ", history=history).strip()

            # Check for exit commands
            if user_input_value.lower() in ("exit", "quit", "q"):
                print("\n[!] Exiting Archivum Solver...\n")
                exit(0)

            ## COMMANDS


            elif user_input_value.lower() == "clear":
                display_banner() #if user enter clear console is cleared and banner is reprinted
    
            elif user_input_value.lower() in ("help" , "man"):
                display_help() #displays help
 
            elif user_input_value.lower().startswith("extract"):
                extract_command(user_input_value)
            
            ## ERROR MANAGMENT
            # if input is not a command gives an error
            elif user_input_value:
                print(f"[!] Command '{user_input_value}' not found")

    except KeyboardInterrupt:
        print("\n[!] Exiting Archivum Solver...\n")
        exit(0)

def main():

    display_banner()
    manage_input()


if __name__ == "__main__":
    main()
