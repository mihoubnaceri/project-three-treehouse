import datetime
import re
import csv
import pytz
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
with open("log.csv") as csvfile:
    data = csvfile.read()
class Task:


    def __init__(self):
        self.my_dict = {}
    def read_csv(self):

        with open("log.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.my_dict[row[0]] = row[:]
        return self.my_dict


    def add_task(self):
        name = input("Task Name : ")
        clear()
        while True:

            date = input("when is yout meeting ? Pleas use MM/DD/YYYY HH:MM FORMAT ")
            try:
                local_date =datetime.datetime.strptime(date, "%m/%d/%Y")
            except ValueError:
                print("{} aint a valid format for date ".format(date))
            else:
                clear()
                break
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
        self.read_csv()
        while True:
            date = input("Type in date to search Pleas use MM/DD/YYYY HH:MM FORMAT ")
            try:
                local_date =datetime.datetime.strptime(date, "%m/%d/%Y")
            except ValueError:
                print("{} aint a valid format for date ".format(date))
            else:
                for value in self.my_dict.keys():
                    #print(value)
                    if date in self.my_dict[value] :
                        print("Title : {}".format(self.my_dict[value][0]))
                        print("Date : {}".format(self.my_dict[value][1]))
                        print("Minuest Spent : {}".format(self.my_dict[value][2]))
                        print("Notes :{} ".format(self.my_dict[value][3]))
                        ask = input("[N]ext    [E]dit    [R]eturn menu ")
                        clear()
                        if ask.lower() == "n":
                            continue
                break
        input("No more entriies press enter to go back to menu")
        clear()
    def search_minutes(self):
        self.read_csv()

        minutes = input ("Type in Number of minutes spent on task to search for it ")
        for value in self.my_dict.keys():
            #print(value)
            if minutes in self.my_dict[value] :
                print("Title : {}".format(self.my_dict[value][0]))
                print("Date : {}".format(self.my_dict[value][1]))
                print("Minuest Spent : {}".format(self.my_dict[value][2]))
                print("Notes :{} ".format(self.my_dict[value][3]))
                ask = input("[N]ext    [E]dit    [R]eturn menu ")
                clear()
                if ask.lower() == "n":
                    continue
        input("No more entriies press enter to go back to menu")
        clear()


    def search_text(self):
        self.read_csv()
        text = input("Type in text to Search for either task name or a matching Word in notes ")
        for value in self.my_dict.keys():
                    #print(value)
            if text in self.my_dict[value] or text in self.my_dict[value][3] :
                print("Title : {}".format(self.my_dict[value][0]))
                print("Date : {}".format(self.my_dict[value][1]))
                print("Minuest Spent : {}".format(self.my_dict[value][2]))
                print("Notes :{} ".format(self.my_dict[value][3]))
                ask = input("[N]ext    [E]dit    [R]eturn menu ")
                clear()
                if ask.lower() == "n":
                    continue
        input("No more entriies press enter to go back to menu")
        clear()

    def search_pattern(self):
        self.read_csv()
        string = ""
        with open("log.csv") as log:

             spamreader = csv.reader(log, delimiter=',', quotechar='|')
             for row in spamreader:
                 string += ', '.join(row)

        pattern = input("Type in your Regular Expressions ")
        string_pattern = r"{}".format(pattern)
        pattern1 = re.compile(pattern)
        search = re.findall(string_pattern,string)
        for value in self.my_dict.keys():
                    #print(value)
            if pattern1.match(self.my_dict[value][0]) or pattern1.match(self.my_dict[value][3])  :
                print("Title : {}".format(self.my_dict[value][0]))
                print("Date : {}".format(self.my_dict[value][1]))
                print("Minuest Spent : {}".format(self.my_dict[value][2]))
                print("Notes :{} ".format(self.my_dict[value][3]))
                ask = input("[N]ext    [E]dit    [R]eturn menu ")
                clear()
                if ask.lower() == "n":
                    continue
        clear()









        #print(self.dates)
        #while True:
            #input("Type in date of Task you are looking for")
