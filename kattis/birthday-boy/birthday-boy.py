# Birthday Boy
# https://open.kattis.com/problems/birthdayboy

coworkers = int(input())
if (coworkers == 0):
    print("10-28")
    exit()
days = []
difference_array = []
number_array = []
maximum = 0
dates = []

def determine_day(month, day):
    if (month == 2) or (month == 4) or (month == 6) or (month == 8) or (month == 9) or (month == 11): 
        month -= 1
        day += 31
        return determine_day(month, day) 

    elif (month == 5) or (month == 7) or (month == 10) or (month == 12):
        month -= 1
        day += 30
        return determine_day(month, day) 

    elif (month == 3):
        month -= 1
        day += 28
        return determine_day(month, day) 
    
    elif (month == 1):
        return day
    else:
        return day

for i in range(coworkers): 
    name, date = input().strip().split()
    month, day = date[0:2], date[3:5]
    month = int(month)
    day = int(day)
    if (month > 12 or month < 1):
        pass
    if (day < 1): 
        pass
    if (day > 31): 
        pass
    if (month == 4) or (month == 6) or (month == 9) or (month == 11):
        if (day > 30): 
            pass
    if (month == 2): 
        if (day > 28): 
            pass
    days.append(determine_day(month, day))
    days.sort()
    dates.append(date)

wraparound = 365 - days[(len(days) - 1)] + days[0]
difference_array.append(wraparound)
for i in range(len(days)): 
    for j in range(len(days)): 
        if (j == i+1):
                difference = abs(days[i] - days[j])
                difference_array.append(difference)


maximum = max(difference_array)
indices = [i for i in range(len(difference_array)) if difference_array[i] == maximum]
maximums = [days[i] for i in range(len(difference_array)) if difference_array[i] == maximum]
count = len(indices)
if count == 1:
    winning_day = maximums[0]
else:
    october_array = []
    for i in maximums:
        difference = (i - 301) if (i > 301) else (64 + i)
        october_array.append(difference)

    winner = min(october_array)
    winner = october_array.index(winner)
    winning_day = maximums[winner]



found = False
for date in dates:
    month, day = date[0:2], date[3:5]
    month = int(month)
    day = int(day)
    if ((determine_day(month, day)) == winning_day):
        month, day = date[0:2], date[3:5]
        month = int(month)
        day = int(day) - 1
        if (day == 0):
            month = month - 1
            if (month == 0):
                month = 12
                day = 31
            elif (month == 2):
                day = 28
            elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
                day = 30
            else:
                day = 31
        print("0" + str(month) if (month <10) else month, "-", "0" + str(day) if (day < 10) else day, sep = "")
        found = True
        break

if (found == False):
    print("10-28")
