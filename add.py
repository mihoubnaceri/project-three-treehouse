import datetime
import re
import csv
import helpers
import os
from datetime import datetime


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Task:
    def print_statement(self, value):
        print("Title : {}".format(helpers.my_dict[value][0]))
        print("Date : {}".format(helpers.my_dict[value][1]))
        print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
        print("Notes :{} ".format(helpers.my_dict[value][3]))

    def add_task(self):
        """
        Asks user for task,name date minutes spent and notes
        and adds a new row in csv file
        """
        name = input("Task Name : ")
        clear()
        date = helpers.add_date()[0]
        minutes = input("Number of minutes spent on {} Task ".format(name))
        clear()
        notes = input("Any Notes to add this is (optional )")
        clear()
        with open("log.csv", "a") as csvfile:
            taskwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            taskwriter.writerow([name, date, minutes, notes])

    def search_date(self):
        """
        Searches through csv file and finds if text is in the row
        and fives it back
        """
        if helpers.read_csv() != "empty":
            counter = 1
            date = helpers.add_date()[0]
            for value in helpers.my_dict.keys():
                if date in helpers.my_dict[value]:
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))
                    print("{} out of {}".format(counter, helpers.find_counts(date)))
                    ask = input("[N]ext    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter += 1
                    elif ask.lower() == "r":
                        break

            else:
                input("No more entriies press enter to go back to menu")
                clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()

    def search_minutes(self):
        """
        Searches through csv file and finds if minutes is in the row
        and gives it back
        """
        if helpers.read_csv() != "empty":
            minutes = input("Type in Number of minutes spent on task to search for it ")
            counter = 1
            for value in helpers.my_dict.keys():
                if minutes in helpers.my_dict[value]:
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))
                    print("{} out of {}".format(counter, helpers.find_counts(minutes)))
                    ask = input("[N]ext [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter += 1
                    elif ask.lower() == "r":
                        break

            else:
                input("No more entriies press enter to go back to menu")
                clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()

    def search_text(self):
        """
        Searches through csv file and finds if text is in the row
        and fives it back
        """
        if helpers.read_csv() != "empty":
            text = input("Type in text to search  ")
            counter = 1
            for value in helpers.my_dict.keys():
                if text in helpers.my_dict[value][0] or text in helpers.my_dict[value][3]:
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))
                    print("{} out of {}".format(counter, helpers.find_counts(text)))
                    ask = input("[N]ext       [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter += 1
                    elif ask.lower() == "r":
                        break
            else:
                input("No more entriies press enter to go back to menu")
                clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()

    def search_pattern(self):
        """
        Searches through csv file and finds if regex pattern matches is in the row
        and gives it back
        """
        if helpers.read_csv() != "empty":
            string = ""
            with open("log.csv") as log:
                spamreader = csv.reader(log, delimiter=',', quotechar='|')
                for row in spamreader:
                    string += ', '.join(row)

            pattern = input("Type in your Regular Expressions ")
            string_pattern = r"{}".format(pattern)
            pattern1 = re.compile(pattern)
            search = re.findall(string_pattern, string)
            counter = 1
            for value in helpers.my_dict.keys():
                if pattern1.match(helpers.my_dict[value][0]) or pattern1.match(helpers.my_dict[value][3]):
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))

                    print("{} out of {}".format(counter, helpers.find_counts(pattern1)))
                    ask = input("[N]ext  [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter += 1
                        continue
                    elif ask.lower() == "r":
                        break
            else:
                input(" You have no entries press return to go back to menu")
                clear()
        else:
            input("press return ")
            clear()

    def range_dates(self):
        """
        Searches through csv file and finds all tasks between two dates
        and gives it back
        """
        if helpers.read_csv() != "empty":
            counter = 1
            first_date = helpers.add_date()[1]
            print("Now second Date")
            second_date = helpers.add_date()[1]
            for value in helpers.my_dict.keys():
                if first_date <= datetime.strptime(helpers.my_dict[value][1], "%m/%d/%Y") <= second_date:
                    self.print_statement(value)
                    print("{} out of {}".format(counter, helpers.find_range(first_date, second_date)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter += 1
                    elif ask.lower() == "r":
                        break
            else:
                input("No more entriies press enter to go back to menu")
                clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()
