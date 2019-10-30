# John Jack Lewis
# November - December 3rd, 2018
# jklewis99@gmail.com
# CSC 2280 LC1 - Introduction to Computer Science
# CSC 1980 LC1 - Exploring Computer Science
# Soundboards

# I will practice academic and personal integrity and excellence of character
# and expect the same from others.

from sound_effects_function import sound_effects
from keyboard_function import *
SIZE = 16
FREQUENCY = 44100
N_CHANNELS = 2
BUFFER = 512

def verify_input():
    while True:
        print("Which sound board would you like to play?")
        print("\tEnter 1 for a Sound Effects soundboard.")
        print("\tEnter 2 for a Marimba soundboard.")
        print("Enter your desired soundboard name: ", end='')
        selection = input()
        if selection == '1' or selection == '2':
            return selection
        else:
            print("\n> Invalid input. Please try again.\n")

soundboard_type = verify_input()

print("\nYour soundboard is opening in another window...")
if soundboard_type == '1':
    sound_effects()
else:
    marimba()