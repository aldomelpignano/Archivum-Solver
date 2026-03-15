# module used to manage help command 


help_text = """
    ArchivumSolver - Automatically solve password-protected archives (CTF / lab use)
    Many features are under development.

    Usage:
        archivumsolver [options] <archive>

    Options:
        -h, --help              Show this help message and exit
        -w, --wordlist FILE     File with candidate passwords
        -b, --bruteforce        Enable brute-force if wordlist fails
        -l, --length RANGE      Password length for brute-force (e.g., 1-6)
        -r, --recursive         Recursively extract nested archives
        -t, --threads N         Number of threads to use (default: 4)
        -d, --max-depth N       Maximum depth for recursive extraction
        -s, --max-size SIZE     Maximum total size to extract (e.g., 2GB)
        -v, --verbose           Verbose output
        -q, --quiet             Minimal output
        --stats                 Show cracking statistics

"""

def print_help():
    print(help_text)

