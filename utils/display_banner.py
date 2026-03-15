import os

# =========================================
#            Utility Functions
# =========================================

def clear_screen():
    """Clears the terminal screen using ANSI escape codes."""
    print("\033[H\033[J", end="")

def set_color(color_name: str):
    """Sets the text color in the terminal."""

    colors = {
        "GREEN": "\033[0;32m",
        "LIGHT_GREEN": "\033[1;32m"
    }

    print(colors.get(color_name.upper(), "\033[0m"), end="")

def reset_color():
    """Resets the terminal text color to default."""
    print("\033[0m", end="")

# =========================================
#            Display Functions
# =========================================

def display_ascii():
    """Prints the ASCII art banner for the tool."""

    print ("""
    ##############################################################################################################################################################

        .S_SSSs     .S_sSSs      sSSs   .S    S.    .S   .S    S.    .S       S.    .S_SsS_S.           sSSs    sSSs_sSSs    S.       .S    S.     sSSs   .S_sSSs    
    .SS~SSSSS   .SS~YS%%b    d%%SP  .SS    SS.  .SS  .SS    SS.  .SS       SS.  .SS~S*S~SS.         d%%SP   d%%SP~YS%%b   SS.     .SS    SS.   d%%SP  .SS~YS%%b   
    S%S   SSSS  S%S   `S%b  d%S'    S%S    S%S  S%S  S%S    S%S  S%S       S%S  S%S `Y' S%S        d%S'    d%S'     `S%b  S%S     S%S    S%S  d%S'    S%S   `S%b  
    S%S    S%S  S%S    S%S  S%S     S%S    S%S  S%S  S%S    S%S  S%S       S%S  S%S     S%S        S%|     S%S       S%S  S%S     S%S    S%S  S%S     S%S    S%S  
    S%S SSSS%S  S%S    d*S  S&S     S%S SSSS%S  S&S  S&S    S%S  S&S       S&S  S%S     S%S        S&S     S&S       S&S  S&S     S&S    S%S  S&S     S%S    d*S  
    S&S  SSS%S  S&S   .S*S  S&S     S&S  SSS&S  S&S  S&S    S&S  S&S       S&S  S&S     S&S        Y&Ss    S&S       S&S  S&S     S&S    S&S  S&S_Ss  S&S   .S*S  
    S&S    S&S  S&S_sdSSS   S&S     S&S    S&S  S&S  S&S    S&S  S&S       S&S  S&S     S&S        `S&&S   S&S       S&S  S&S     S&S    S&S  S&S~SP  S&S_sdSSS   
    S&S    S&S  S&S~YSY%b   S&S     S&S    S&S  S&S  S&S    S&S  S&S       S&S  S&S     S&S          `S*S  S&S       S&S  S&S     S&S    S&S  S&S     S&S~YSY%b   
    S*S    S&S  S*S   `S%b  S*b     S*S    S*S  S*S  S*b    S*S  S*b       d*S  S*S     S*S           l*S  S*b       d*S  S*b     S*b    S*S  S*b     S*S   `S%b  
    S*S    S*S  S*S    S%S  S*S.    S*S    S*S  S*S  S*S.   S*S  S*S.     .S*S  S*S     S*S          .S*P  S*S.     .S*S  S*S.    S*S.   S*S  S*S.    S*S    S%S  
    S*S    S*S  S*S    S&S   SSSbs  S*S    S*S  S*S   SSSbs_S*S   SSSbs_sdSSS   S*S     S*S        sSS*S    SSSbs_sdSSS    SSSbs   SSSbs_S*S   SSSbs  S*S    S&S  
    SSS    S*S  S*S    SSS    YSSP  SSS    S*S  S*S    YSSP~SSS    YSSP~YSSY    SSS     S*S        YSS'      YSSP~YSSY      YSSP    YSSP~SSS    YSSP  S*S    SSS  
        SP   SP                         SP   SP                                      SP                                                            SP          
        Y    Y                          Y    Y                                       Y                                                             Y                                                                                                                                                       
    
    ##############################################################################################################################################################""")

def display_author_info():
    """Displays author and tool information."""

    tool_name = "Archivum Solver"
    version = "v1.0"
    author = "Aldo Daniele Melpignano"
    github = "https://github.com/aldomelpignano/Archivum-Solver"    

    print(f"""
    #
    #   {tool_name} {version}
    #   Author  : {author}
    #   GitHub  : {github}
    #
    """)

# =========================================
#            Final Function
# =========================================

def display_banner():
    """Main function to display the banner and author info."""

    clear_screen()
    set_color("LIGHT_GREEN")
    display_ascii()
    set_color("GREEN")
    display_author_info()
    reset_color()