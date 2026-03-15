import zipfile
from utils.display_banner import display_banner, clear_screen
from utils.help import display_help

def manage_input():
## Function used to manage user input
    try:
        while True:
            user_input_value = input("archsolve > ").strip()

            # Check for exit commands
            if user_input_value.lower() in ("exit", "quit", "q"):
                print("\n[!] Exiting Archivum Solver...\n")
                quit()

            elif user_input_value.lower() == "clear":
                display_banner() #if user enter clear console is cleared and banner is reprinted
    
            elif user_input_value.lower() in ("help" , "man"):
                display_help() #displays help 

            # if input is not a command gives an error
            elif user_input_value:
                print(f"[!] Command '{user_input_value}' not found")

    except KeyboardInterrupt:
        print("\n[!] Exiting Archivum Solver...\n")

def main():

    display_banner()
    manage_input()


if __name__ == "__main__":
    main()
