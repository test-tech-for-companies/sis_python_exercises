#!/usr/bin/env python3
"""
Entry point module
"""


print_pattern = __import__('pattern').print_pattern

print(f"-------------------->  n: 4")
print_pattern(4)
print(f"-------------------->  n: 2")
print_pattern(2)
print(f"-------------------->  n: 5")
print_pattern(5)
print(f"-------------------->  n: 7")
print_pattern(7)
