import saved_var as sv

def one():
    title = [];date = [];location = [];description = [];capacity = []
    print("\n__Search for Upcoming Events__")
    contents = read_contents("Event.txt")

    for content in contents[1:]:
        content = content.split('|')
        if len(content) < 9: continue
        title.append(content[0])
        date.append(content[1])
        location.append(content[2])
        description.append(content[3])
        capacity.append(content[4])

    print("\nID | Title               ")
    print("-" * 23)
    for i in range(len(title)):
        print(f"{i + 1:<3}|{title[i]:<20}")
        print("-" * 23)

    confirm = input(
        "\nDo you want to search the details of events? If yes, press ENTER; else type NO: ").lower()
    if confirm == "no":
        return "back"


    while True:
        try:
            event_id = int(input("Enter the ID number (1-{}): ".format(len(title))))
            if event_id not in range(1, len(title) + 1):
                print("out of range")
                continue
            break
        except ValueError:
            print("you shall enter number")

    index = event_id - 1
    print('\n')
    print("ID | Title              | Date          | Location           | Description             | Capacity")
    print("-" * 110)
    print(
        f"{event_id:<3}|{title[index]:<20}|{date[index]:<15}|{location[index]:<20}|{description[index]:<25}|{capacity[index]}")
    print("-" * 110)
    return "back"

def two():
    print("\n__Register for an event__")
    confirm = input("Do you want to register for upcoming events? If yes, press ENTER; else type NO: ").lower()
    if confirm == "no":
        return "back"

    title = []
    contents = read_contents("Event.txt")
    for i in range(1, len(contents)):
        content = contents[i].split('|')
        if len(content) < 7:
            continue
        title.append(content[0])

    if title != []:
        print("______Event______")
        for i in range(len(title)):
            print(f"{i + 1}. {title[i]}")
    elif title == []:
        print("no event exist...")
        return "back"

    while True:
        choice = input("Select the title you want to register for: ")
        if not choice.isdigit(): print("you shall enter number"); continue

        choice = int(choice) - 1
        if choice not in range(len(title)): print("out of range"); continue
        break

    title = title[choice]
    for i in range(len(contents)):
        content = contents[i].split('|')
        if content[0] == title:
            if sv.user_id in content[6].split(':'):
                print("you have registered for this event")
                return "back"
            elif len(content[6].split(':')) >= int(content[4]):
                print("Event has full")
                return "back"
            print('\n')
            print(
                "Title               | Date          | Location            | Description               | Capacity")
            print("-" * 110)
            print(f"{content[0]:<20}|{content[1]:<15}|{content[2]:<20}|{content[3]:<25}|{content[4]}")
            print("-" * 110)

    confirm = input("Are you sure to register for upcoming events? Enter YES to confirm...").lower()
    if confirm != "yes":
        return "back"

    eventContents = read_contents("Event.txt")
    with open("Event.txt", "w") as file:
        file.write(eventContents[0])
        for i in range(1, len(eventContents)):
            eventContent = eventContents[i].split('|')
            if len(eventContent) < 9:continue
            elif eventContent[0] == title:
                attend = eventContent[6].split(':')
                attend.append(sv.user_id)
                eventContent[6] = ':'.join(attend)
                eventContents[i] = '|'.join(eventContent)
            file.write('\n'+eventContents[i])

    return "back"

def three():
    print("__Cancel Registration__")
    confirm = input("Do you want to cancel registration for upcoming events? If yes, press ENTER; else type NO: ").lower()
    if confirm == "no":
        return "back"
    title = []

    contents = read_contents("Event.txt")
    for i in range(1, len(contents)):
        content = contents[i].split('|')
        if len(content) < 7:
            continue
        elif sv.user_id in content[6].split(':'):
            title.append(content[0])

    if title != []:
        print("______Event______")
        for i in range(len(title)):
            print(f"{i + 1}. {title[i]}")
    elif title == []:
        print("no event exist...")
        return "back"

    while True:
        choice = input("Select the title you want to cancel: ")
        if not choice.isdigit(): print("you shall enter number"); continue

        choice = int(choice) - 1
        if choice not in range(len(title)): print("out of range"); continue
        break

    title = title[choice]
    confirm = input(f"Do you sure you want to cancel registration for {title} events? Enter \'yes\' to confirm...").lower()
    if confirm != "yes":
        return "back"

    eventContents = read_contents("Event.txt")
    with open("Event.txt", "w") as file:
        file.write(eventContents[0])
        for i in range(1, len(eventContents)):
            eventContent = eventContents[i].split('|')
            if len(eventContent) < 9:continue
            elif eventContent[0] == title:
                attend = eventContent[6].split(':')
                attend.remove(sv.user_id)
                eventContent[6] = ':'.join(attend)
                eventContents[i] = '|'.join(eventContent[0])
            file.write('\n'+eventContents[i])

def four():
    title = [];date = [];location = [];description = [];capacity = []
    print("\n__View Personal Event Calendar__")
    confirm = input(
        "\nDo you want to view personal event calender? If yes, press ENTER; else type NO: ").lower()
    if confirm == "no":
        return "back"
    with open('Event.txt', 'r') as file:
        contents = file.read().split('\n')

    for c in contents[1:]:
        content = c.split('|')
        if len(content) < 9: continue
        if sv.user_id in content[6].split(':'):
            title.append(content[0])
            date.append(content[1])
            location.append(content[2])
            description.append(content[3])
            capacity.append(content[4])

    if title == []:
        print("no personal event exist...")
        return "back"
    
    #sort by date
    for k in range(len(date)):
        date_select = date[k].split('/')
        for j in range(k, len(date)):
            date_compare = date[j].split('/')
            check = [int(date_select[2]) > int(date_compare[2]),    #compare year
                     int(date_select[2]) == int(date_compare[2]) and int(date_select[1]) > int(date_compare[1]),    #compare month
                     int(date_select[2]) == int(date_compare[2]) and int(date_select[1]) == int(date_compare[1]) and int(date_select[0]) > int(date_compare[0])]    #compare date
            if any(check):
                y = date[j];date[j] = date[k];date[k] = y
                y = title[j];title[j] = title[k];title[k] = y
                y = location[j];location[j] = location[k];location[k] = y
                y = description[j];description[j] = description[k];description[k] = y
                y = capacity[j];capacity[j] = capacity[k];capacity[k] = y

    print("\nID | Title               | Date")
    print("-" * 43)
    for k in range(len(title)):
        print(f"{k + 1:<3}|{title[k]:<20}|{date[k]}")
    print('-'*43)
    print("1. View event details")
    print("2. View calender")
    print("3. undo")
    while True:
        choice = input(":")
        if not choice.isdigit(): print("invalid input");continue
        elif int(choice) not in range(1, 4):print("out of range");continue
        break


    if choice == '1':
        while True:
            eventIndex = input("Choose a title to view, no to undo:").lower()
            if eventIndex == 'no':return "back"
            elif not eventIndex.isdigit():print("unavailable input");continue
            elif int(eventIndex) not in range(1, len(title)+1): print("out of range");continue
            index = int(eventIndex) - 1
            print('\n')
            print("ID | Title              | Date          | Location           | Description             | Capacity")
            print("-" * 110)
            print(
                f"{eventIndex:<3}|{title[index]:<20}|{date[index]:<15}|{location[index]:<20}|{description[index]:<25}|{capacity[index]}")
            print("-" * 110)
            continue
    elif choice == '2':
        i=0; history = [-1]
        while True:
            if i >= len(date):
                print("That\'s all Event")
                i-=1
            elif i < 0:
                print("This is first Event")
                i+=1
            if history[-1]!=i:history.append(i)

            eventDate = date[i].split("/")
            month = eventDate[1]
            year = eventDate[2]
            calender = getCalender(int(month), int(year))
            addDay = []
            addEvent = []
            for g in range(i, len(date)):
                anotherDate = date[g].split("/")
                if anotherDate[1] == month and anotherDate[2] == year:
                    addDay.append(int(anotherDate[0]))
                    addEvent.append(title[g])
                    i+=1
            j=0

            monthMatch = {1: "January",2: "February",3: "March",4: "April",5: "May",6: "June",7: "July",8: "August",9: "September",10: "October",11: "November",
                          12: "December"}
            length = 0
            for t in title:
                if len(t) > length: length = len(t)
            print(f"{year} year")
            print(monthMatch[int(month)])
            print(" Sut"+" "*length+"| mon"+" "*length+"| Tue"+" "*length+"| Wen"+" "*length+"| Thu"+" "*length+"| Fri"+" "*length+"|Sun")
            for y in range(6):
                next_layer = [[""]*7];pnl = False
                for x in range(7):
                    if j == len(addDay) or not calender[y][x].isdigit() :
                        pass
                    elif int(calender[y][x]) == addDay[j]:
                        dateNum = int(calender[y][x])
                        calender[y][x] += ": " + addEvent[j]
                        j+=1
                        k = 0
                        for i in range(j, len(addDay)):
                            if dateNum == addDay[i]:
                                while(True):
                                    try:
                                        next_layer[k][x] += ": " + addEvent[j]
                                        k+=1
                                        break
                                    except:
                                        next_layer.append([""]*7)
                                        continue
                                pnl = True
                                j+=1
                                i+=1

                    print(calender[y][x], " "*(length+3-len(calender[y][x])), "|", end = "")
                print()
                if pnl:
                    for k in range(len(next_layer)):
                        for h in range(7):
                            print(" " * (len(str(dateNum))-1), next_layer[k][h], " " * (length + 3  - len(next_layer[k][h])), end="|")
                        print()

            print("1. next")
            print("2. previous")
            print("3. view")
            print("4. undo")
            while True:
                choice = input(":")

                if choice == "1":pass
                elif choice == "2":
                    history.pop()
                    i = history[-1]
                elif choice == "3":
                    while True:
                        eventIndex = input("Choose a date to view Event (no to undo): ").lower()
                        if eventIndex == 'no':
                            break
                        elif not eventIndex.isdigit():
                            print("unavailable input");continue
                        elif int(eventIndex) not in addDay:
                            print("out of range");continue

                        index = []
                        for i in range(len(addDay)):
                            if int(addDay[i]) == int(eventIndex) :
                                index.append(i)
                        choice = 0
                        if len(index) > 1:
                            for g in range(len(index)):
                                print(f"{g+1}. {addEvent[index[g]]}")
                            while True:
                                choice = input("Enter a choice")
                                if not choice.isdigit():
                                    print("invalid value")
                                    continue
                                choice = int(choice) - 1
                                if choice not in range(len(index)):
                                    print("out of range")
                                    continue
                                break
                        for i in range(len(title)):
                            if title[i] == addEvent[index[choice]]:
                                print('\n')
                                print(
                                    "ID | Title              | Date          | Location           | Description             | Capacity")
                                print("-" * 110)
                                print(
                                    f"{eventIndex:<3}|{title[i]:<20}|{date[i]:<15}|{location[i]:<20}|{description[i]:<25}|{capacity[i]}")
                                print("-" * 110)

                elif choice == "4":return "back"
                else :
                    print("invalid input")
                    continue
                break

    elif choice == '3':return "back"




def read_contents(fileName = 'waiting_Event.txt'):
    with open(fileName, 'r') as f:
        contents = f.read().split('\n')
    return contents


def getCalender(month, year):
    row = [[""] * 7, [""] * 7, [""] * 7, [""] * 7, [""] * 7, [""] * 7]
    defaultDate = [1, 1, 1]
    defaultWeek = 5
    defaultWeek -= 1

    increasementOfWeek = defaultWeek
    big = year
    small = defaultDate[2]
    increasementOfWeek = increasementOfWeek + big - small + int((big - small) / 4)
    if increasementOfWeek > 6: increasementOfWeek = increasementOfWeek - 7 * int(increasementOfWeek / 7)

    days = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
            2: 28, 4: 30, 6: 30, 9: 30, 11: 30}
    if year % 4 == 0: days[2] = 29

    for i in range(month-1):
        if days[i + 1] == 31:
            increasementOfWeek += 3
        elif days[i + 1] == 30:
            increasementOfWeek += 2
        elif days[i + 1] == 29:
            increasementOfWeek += 1
        if increasementOfWeek > 6: increasementOfWeek -= 7

    increasementOfWeek+=3       #adjust some deviation
    stratDate = 1
    dueDate = days[month]

    y = 0
    for i in range(stratDate - 1, dueDate):
        x = i + increasementOfWeek
        while True:
            if x > 6: x -= 7;continue
            break
        row[y][x] = f"{i + 1}"
        if x == 6: y += 1
    return row