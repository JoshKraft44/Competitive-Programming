row_count = 0
my_list = []
invalid = False
count = 0

for _ in range(8): 
    row_count += 1
    board_row = input().strip()
    for i in range(len(board_row)):
        if (board_row[i] == "*"): 
            my_list.append([row_count, i+ 1])
            count += 1

if count != 8:
    invalid = True

else: 
    for a in range(len(my_list)): 
        for b in range(a + 1, len(my_list)): 
            s1, s2 = my_list[a]
            s3, s4 = my_list[b]
            if s1 == s3 or s2 == s4:
                invalid = True
            if abs(s1 - s3) == abs(s2 - s4): 
                invalid = True
            

if invalid == False: 
    print("valid")
else: print("invalid")

