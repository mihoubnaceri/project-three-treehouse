import datetime
import re
import csv
import pytz
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Task:


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
        with open("log.csv","a") as csvfile:
            taskwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            taskwriter.writerow([name,date,minutes,notes])
