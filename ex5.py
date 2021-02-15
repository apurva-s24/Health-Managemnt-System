# Health Management System
# 3 clients - Harry, Rohan, Hammad
# total 6 files...3 file for Diet log and 3 for exercise log
# write a function that when executed takes as input client name
# seated shoulder press
# cable crossover
# one more function to retrieve exercise or food for any client


def getdate():
    import datetime
    return datetime.datetime.now()


client = {1: "Person1", 2: "Person2", 3: "Person3"}
option = {1: "Exercise", 2: "Diet"}


try:

    for key, value in client.items():
        print(f"Press {key} for {value}")

    clientName = int(input("Enter: "))
    print(f"\nSelected Client: {client[clientName]}")

    task = int(input("Press 1 for log\nPress 2 for retrieve\nEnter: "))

    if task == 1:
        print("\n")
        for key, value in option.items():
            print(f"Press {key} for {value}")
        action = int(input("Enter: "))
        print(f"\nSelected Job: {option[action]}")

        f = open(f"{client[clientName]}_{option[action]}.txt", "a")

        more = ""
        while more != "n":
            print(f"\nEnter {option[action]}")
            work = input("Add: ")
            f.write(f"[{str(getdate())} ]: {work} \n")
            more = input("Add more item(y/n): ")
            if more == "y":
                continue
            elif more == "n":
                exit()
            else:
                print("invalid input")
                more = input("Add more item(y/n): ")

        f.close()

    elif task == 2:
        print("\n")
        for key, value in option.items():
            print(f"Press {key} for {value}: ")
        action = int(input("Enter: "))
        print(f"{client[clientName]}-{option[action]} Report: \n")
        f = open(f"{client[clientName]}_{option[action]}.txt")
        print(f.read())
        f.close()

    else:
        print("Invalid Input")

except Exception as e:
    print("Invalid Input")
