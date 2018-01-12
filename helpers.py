

from datetime import datetime
import csv

def add_date():
    while True:
        date = input("Type in date to search Pleas use MM/DD/YYYY HH:MM FORMAT ")
        try:
            local_date =datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            print("{} aint a valid format for date ".format(date))
        else:
            return (date,local_date)
def find_range(first,second):
    result  =0
    for value in my_dict.keys():
        if first <= datetime.strptime(my_dict[value][1],"%m/%d/%Y")<= second :
            result+=1
    return result

def find_counts(text):
    result = 0
    result1 = 0
    for value in my_dict.keys():
                    #print(value)
        if isinstance(text,str):

            if text in my_dict[value] or text in my_dict[value][3] or text in my_dict[value][0] :
                result+=1

        else:
            if text.match(my_dict[value][0]) or text.match(my_dict[value][3]):
                result +=1
    return result
my_dict ={}
def read_csv():
    output = None

    try:
        with open("log.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    my_dict[row[0]] = row[:]
                except IndexError:
                    output = "empty"

    except FileNotFoundError:
        input("File not found type return to addan entry to make the file")
        return "empty"
    return my_dict

def print_statements(value):
    dictation = read_csv()

    print("Title : {}".format(dictation[value][0]))
    print("Date : {}".format(dictation[value][1]))
    print("Minuest Spent : {}".format(dictation[value][2]))
    print("Notes :{} ".format(dictation[value][3]))



def looping_dict(data):
    if read_csv() != "empty":
        dictation = read_csv()

        counter = 1
        for value in dictation.keys():
            if isinstance(data,str):
                    #print(value)
                if data in dictation[value][0] or data in dictation[value][3] :
                    print_statements(value)
                    print("{} out of {}".format(counter,find_counts(data)))
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")

                    if ask.lower() == "n":
                        counter+=1
            else:
                if data.match(dictation[value][0]) or data.match(dictation[value][3]) :
                    print_statements(value)
                    ask = input("[N]ext    [E]dit    [R]eturn menu ")

                    if ask.lower() == "n":
                        counter+=1
        input("No more entriies press enter to go back to menu")

    else:
        input(" You have no entries press return to go back to menu")
