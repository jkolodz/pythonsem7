import csv

class Animal:
    def __init__(self,name,size,color):
        self.name=name
        self.size=size
        self.color=color

def print_file():
    with open('data.csv', "r") as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for row in csv_read:
            print(row)


def add_row():
    while 1:
        try:
            name, size, color = input("write name, size, color\n").split()
            break
        except ValueError:
            print("try again\n")

    with open('data.csv', 'a', newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([name, size, color])


def remove_row():
    animal_list=[]
    with open('data.csv', 'r') as read:
        for row in csv.reader(read):
            animal_list.append(row)

    while 1:
        try:
            name, size, color = input("write name, size, color to delete\n").split()
            break
        except ValueError:
            print("try again\n")

    with open('data.csv', 'w',  newline='\n') as out:
        writer = csv.writer(out)
        for row in animal_list:
            if row != [name, size, color]:
                writer.writerow(row)


if __name__ == '__main__':
    while 1:
        print_file()
        status = input("exit, add or remove?\n")
        if status == "exit":
            break
        elif status == "add":
            add_row()
        elif status == "remove":
            remove_row()
        else:
            print("bad command, try again\n")

