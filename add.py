import datetime
import re
import csv
import helpers
import os
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Task:
    def print_statement(self,value):
        print("Title : {}".format(helpers.my_dict[value][0]))
        print("Date : {}".format(helpers.my_dict[value][1]))
        print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
        print("Notes :{} ".format(helpers.my_dict[value][3]))


    def add_task(self):
        name = input("Task Name : ")
        clear()
        date = helpers.add_date()[0]
        minutes = input("Number of minutes spent on {} Task ".format(name))
        clear()
        notes = input("Any Notes to add this is (optional )")
        clear()
        #self.my_dict[name] = [name,date,minutes,notes]

        with open("log.csv","a") as csvfile:
            taskwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            taskwriter.writerow([name,date,minutes,notes])
    def search_date(self):
        if helpers.read_csv() != "empty":
            counter = 1
            date = helpers.add_date()[0]
            for value in helpers.my_dict.keys():
                        #print(value)
                if date in helpers.my_dict[value] :
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))
                    print("{} out of {}".format(counter,helpers.find_counts(date)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter+=1


            input("No more entriies press enter to go back to menu")
            clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()
    def search_minutes(self):
        if helpers.read_csv() != "empty":

            minutes = input ("Type in Number of minutes spent on task to search for it ")
            counter = 1
            for value in helpers.my_dict.keys():
                #print(value)
                if minutes in helpers.my_dict[value] :
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))
                    print("{} out of {}".format(counter,helpers.find_counts(minutes)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter+=1

            input("No more entriies press enter to go back to menu")
            clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()
    def search_text(self):
        if helpers.read_csv() != "empty":

            text = input ("Type in text to search  ")
            counter = 1
            for value in helpers.my_dict.keys():
                #print(value)
                if text in helpers.my_dict[value][0] or text in helpers.my_dict[value][3] :
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))
                    print("{} out of {}".format(counter,helpers.find_counts(text)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter+=1
            input("No more entriies press enter to go back to menu")
            clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()

    def search_pattern(self):
        if helpers.read_csv() != "empty":
            string = ""
            with open("log.csv") as log:

                 spamreader = csv.reader(log, delimiter=',', quotechar='|')
                 for row in spamreader:
                     string += ', '.join(row)

            pattern = input("Type in your Regular Expressions ")
            string_pattern = r"{}".format(pattern)
            pattern1 = re.compile(pattern)
            search = re.findall(string_pattern,string)
            counter = 1
            for value in helpers.my_dict.keys():
                        #print(value)
                if pattern1.match(helpers.my_dict[value][0]) or pattern1.match(helpers.my_dict[value][3])  :
                    print("Title : {}".format(helpers.my_dict[value][0]))
                    print("Date : {}".format(helpers.my_dict[value][1]))
                    print("Minuest Spent : {}".format(helpers.my_dict[value][2]))
                    print("Notes :{} ".format(helpers.my_dict[value][3]))

                    print("{} out of {}".format(counter,helpers.find_counts(pattern1)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter+=1
                        continue
            clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()


    def range_dates(self):
        
        if helpers.read_csv() != "empty":
            counter = 1
            first_date = helpers.add_date()[1]
            print("Now second Date")
            second_date = helpers.add_date()[1]
            #datetime.strptime('12', '%M %d %Y ')
            for value in helpers.my_dict.keys():
                        #print(value)
                if first_date <= datetime.strptime(helpers.my_dict[value][1],"%m/%d/%Y")<= second_date :
                    self.print_statement(value)
                    print("{} out of {}".format(counter,helpers.find_range(first_date,second_date)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter+=1
                    elif ask.lower()== "b":
                        self.print_statement(value)

            input("No more entriies press enter to go back to menu")
            clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()
