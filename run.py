import sys
import os
import random
import time
from data import people as p
from data import scripts as sc

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def main():
    clear_screen()
    time.sleep(1)
    print("================")
    time.sleep(1)
    clear_screen()
    print("Heaven Or Hell?\n"
          "================")
    time.sleep(1)
    clear_screen()
    print("================\n"
          "Heaven Or Hell?\n"
          "================\n")
    time.sleep(1)
    clear_screen()
    time.sleep(1)
    menu()

def menu():
    clear_screen()
    print("================\n"
          "Heaven Or Hell?\n"
          "================\n")
    print("1. Play")
    print("2. How to play?")
    print("0. Exit")
    choice = user_choice()
    if choice == "1":
        play()
    if choice == "2":
        clear_screen()
        input("Coming Soon!")
        menu()
    if choice == "0":
        clear_screen()
        print("Stopped All Scripts!")
        sys.exit(1)

def play():
    clear_screen()
    print("Name: {}\n"
          "\n"
          "Record:\n"
          "-------------------\n"
          "* {}\n"
          "* {}\n"
          "* {}\n".format(random.choice(p.people), random.choice(sc.s1), random.choice(sc.s2), random.choice(sc.s3)))
    print("\nHeaven Or Hell? or back")
    choice = user_choice()
    if choice == "Heaven":
        input("Sent to Heaven! :)")
        play()
    if choice == "Hell":
        input("Sent to Hell! >:(")
        play()
    if choice == "Back":
        menu()

main()
    
