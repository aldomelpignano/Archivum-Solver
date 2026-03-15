import zipfile
from utils.display_banner import display_banner
from utils.help import print_help

def manage_input():
## Function used to manage user input
    try:
        while True:
            user_input_value = input("archsolve > ").strip()

            # Check for exit commands
            if user_input_value.lower() in ("exit", "quit", "q"):
                print("\n[!] Exiting Archivum Solver...\n")
                quit()

    
            elif user_input_value.lower() in ("help" , "man"):
                print_help()

            # Qui puoi aggiungere altre logiche, ad esempio aprire zip

    except KeyboardInterrupt:
        print("\n[!] Exiting Archivum Solver...\n")

def main():
    display_banner()

    manage_input()


if __name__ == "__main__":
    main()
