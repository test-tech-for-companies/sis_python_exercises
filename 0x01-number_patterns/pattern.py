#!/usr/bin/env python3
"""
print_pattern module
"""

def print_pattern(num) -> None:
    """
    Print a pattern of numbers from 1 to n.
    """

    i, j = 0, 0
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    yellow = "\033[33m"
    cyan = "\033[36m"
    white = "\033[37m"
    reset = "\033[0m"

    # First upper half of the pattern
    i = num
    while i >= 1:
        # First inner part of upper half RED= red left
        j = num
        while j > i:
            print(f"{red}{j}{reset}", end=" ")
            j -= 1
        
        # Second inner part of upper half BLU= blue half
        j = 1
        while j <= (i * 2 - 1):
            print(f"{blue}{i}{reset}", end=" ")
            j += 1

        # Third inner part of upper half GRN= green right
        j = i + 1
        while j <= num:
            print(f"{green}{j}{reset}", end=" ")
            j += 1
        
        print()
        i -= 1
    
    
    # Second lower half of the pattern
    i = 1
    while i < num:        
        # First inner part of lower half YEL = yellow left
        j = num
        while j > i:
            print(f"{yellow}{j}{reset}", end=" ")
            j -= 1

        # Second inner part of lower half CYN = almost green half
        j = 1
        while j <= (i * 2 - 1):
            print(f"{cyan}{i + 1}{reset}", end=" ")
            j += 1

        # Third inner part of lower half WHT = white  right
        j = i + 1
        while j <= num:
            print(f"{white}{j}{reset}", end=" ")
            j += 1

        print()
        i += 1
