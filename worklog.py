import os
import sys
from add import Task


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    while True:

        print("Welcome to Your Work Log")
        print("""
    Here is you menu choose one of them :
    a) add a Task
    b) search through tasks
    c) quit
        """)
        user_choice = input("> ")
        clear()
        if user_choice.lower() == "b":
            print("""
    a) Find Task by exact date
    b) Find Task by Range of dates
    c) Find Task by a text search
    d) Find Task by regular Expressions Pattern
    e) Return To main menu
            """)
            ask = input(">")
            clear()
        elif user_choice.lower() == "a":
            mate = Task()
            mate.add_task()
            input("Just added Task press enter to go back to menu")
            clear()
        elif user_choice.lower() == "c":
            clear()
            break
        elif user_choice.lower() == "e":
            clear()
            main()






if __name__ == "__main__":
    main()