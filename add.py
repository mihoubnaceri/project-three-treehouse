import datetime
import re
import csv
import pytz
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Task:
    def __init__(self):
        self.my_dict = {}

    def read_csv(self):
        output = None

        try:
            with open("log.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        self.my_dict[row[0]] = row[:]
                    except IndexError:
                        output = "empty"



        except FileNotFoundError:
            input("File not found type return to addan entry to make the file")
            return "empty"
        return self.my_dict

    def add_date(self):
        while True:
            date = input("Type in date to search Pleas use MM/DD/YYYY HH:MM FORMAT ")
            try:
                local_date =datetime.datetime.strptime(date, "%m/%d/%Y")
            except ValueError:
                print("{} aint a valid format for date ".format(date))
            else:
                return date

    def add_task(self):
        name = input("Task Name : ")
        clear()
        date = self.add_date()
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
        if self.read_csv() != "empty":
            counter = 1
            date = self.add_date()
            for value in self.my_dict.keys():
                        #print(value)
                if date in self.my_dict[value] :
                    print("Title : {}".format(self.my_dict[value][0]))
                    print("Date : {}".format(self.my_dict[value][1]))
                    print("Minuest Spent : {}".format(self.my_dict[value][2]))
                    print("Notes :{} ".format(self.my_dict[value][3]))
                    print("{} out of {}".format(counter,self.find_counts(date)))
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
        if self.read_csv() != "empty":

            minutes = input ("Type in Number of minutes spent on task to search for it ")
            counter = 1
            for value in self.my_dict.keys():
                #print(value)
                if minutes in self.my_dict[value] :
                    print("Title : {}".format(self.my_dict[value][0]))
                    print("Date : {}".format(self.my_dict[value][1]))
                    print("Minuest Spent : {}".format(self.my_dict[value][2]))
                    print("Notes :{} ".format(self.my_dict[value][3]))
                    print("{} out of {}".format(counter,self.find_counts(minutes)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter+=1

            input("No more entriies press enter to go back to menu")
            clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()
    def find_counts(self,text):
        result = 0
        result1 = 0
        for value in self.my_dict.keys():
                    #print(value)
            if isinstance(text,str):

                if text in self.my_dict[value] or text in self.my_dict[value][3] or text in self.my_dict[value][0] :
                    result+=1
            else:
                if text.match(self.my_dict[value][0]) or text.match(self.my_dict[value][3]):
                    result +=1
        return result

    def edit_things(self):

        while True:
            ask = input("""
What do you want to edit :
a) Task name
b) Task Date
c) Minutes Spent
d) Notes
e) Never minde return
""")
            if ask == "a":
                answer = input("> Change name to ")
                self.my_dict[value][0] = answer
            elif ask =="b":
                answer = input("> Change name to ")



    def search_text(self):
        if self.read_csv() != "empty":

            text = input ("Type in text to search  ")
            counter = 1
            for value in self.my_dict.keys():
                #print(value)
                if text in self.my_dict[value][0] or text in self.my_dict[value][3] :
                    print("Title : {}".format(self.my_dict[value][0]))
                    print("Date : {}".format(self.my_dict[value][1]))
                    print("Minuest Spent : {}".format(self.my_dict[value][2]))
                    print("Notes :{} ".format(self.my_dict[value][3]))
                    print("{} out of {}".format(counter,self.find_counts(text)))
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
        if self.read_csv() != "empty":
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
            for value in self.my_dict.keys():
                        #print(value)
                if pattern1.match(self.my_dict[value][0]) or pattern1.match(self.my_dict[value][3])  :
                    print("Title : {}".format(self.my_dict[value][0]))
                    print("Date : {}".format(self.my_dict[value][1]))
                    print("Minuest Spent : {}".format(self.my_dict[value][2]))
                    print("Notes :{} ".format(self.my_dict[value][3]))

                    print("{} out of {}".format(counter,self.find_counts(pattern1)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")
                    clear()
                    if ask.lower() == "n":
                        counter+=1
                        continue
            clear()
        else:
            input(" You have no entries press return to go back to menu")
            clear()
