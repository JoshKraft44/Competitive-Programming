# Veeva Systems Technical Interview Prep  

class Solution:
    def numberToWords (num: int) -> str:

        dict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"} 
        count = 0
        list = []
        num_str = str(num) 
        digits = []
        word = "" 
        things = []
        section = ""
        if num == 0: 
            return "Zero"

        for i in range(len(num_str)):
            list.append(num_str[i])
            count += 1


        while count > 0: 
            if count > 9: 
                things.append(dict[int(list[0])] + " Billion ")
                del list[0]
                count -= 1
                continue

            if count > 6: 
                if count == 9: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    check = int(str(list[1]) + str(list[2]))
                    if check > 19: 
                        if str(list[2]) == "0":
                            section = dict[int(list[0])] + " Hundred " + dict[int(list[1] + "0")] + " Million "
                        else: 
                            section = dict[int(list[0])] + " Hundred " + dict[int(list[1] + "0")] + " " + dict[int(list[2])] + " Million "
                        things.append(section)
                        count -= 3
                        del list[0:3]
                    else:
                        if check == 0:
                            section = dict[int(list[0])] + " Hundred Million "
                        else:
                            section = dict[int(list[0])] + " Hundred " + dict[check] + " Million "
                        things.append(section)
                        count -= 3
                        del list[0:3]


                elif count == 8: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    check = int(str(list[0]) + str(list[1]))
                    if check == 0: 
                        count -= 2
                    if check > 19: 
                        if str(list[1]) == "0":
                            section = dict[int(list[0] + "0")] + " Million"
                        else: 
                            section = dict[int(list[0] + "0")] + " " + dict[int(list[1])] + " Million "
                        things.append(section)
                        count -= 2
                        del list[0:2]
                    else: 
                        things.append(dict[check] + " Million ")
                        count -= 2
                        del list[0:2]
                elif count == 7: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    section = dict[int(list[0])] + " Million "
                    things.append(section)
                    count -= 1
                    del list[0]
                    continue



            if count > 3: 
                if count == 6: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    check = int(str(list[1]) + str(list[2]))
                    if check > 19: 
                        if str(list[2]) == "0":
                            section = dict[int(list[0])] + " Hundred " + dict[int(list[1] + "0")] + " Thousand"
                        else: 
                            section = dict[int(list[0])] + " Hundred " + dict[int(list[1] + "0")] + " " + dict[int(list[2])] + " Thousand "
                        things.append(section) 
                        count -= 3
                        del list[0:3]
                    else: 
                        if check == 0: 
                            section = dict[int(list[0])] + " Hundred Thousand"
                        else: 
                            section = dict[int(list[0])] + " Hundred " + dict[check] + " Thousand "
                        things.append(section)
                        count -= 3
                        del list[0:3]


                elif count == 5: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    check = int(str(list[0]) + str(list[1]))
                    if check > 19: 
                        if str(list[1]) == "0": 
                            section = dict[int(list[0] + "0")] + " Thousand" 
                        else: 
                            section = dict[int(list[0] + "0")] + " " + dict[int(list[1])] + " Thousand " 
                        things.append(section)
                        count -= 2
                        del list[0:2]
                    else: 
                        things.append(dict[check] + " Thousand ")
                        count -= 2
                        del list[0:2]
                elif count == 4: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    section = dict[int(list[0])] + " Thousand"
                    things.append(section)
                    count -= 1
                    del list[0]
                    continue


            if count > 0: 
                if count == 3: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    check = int(str(list[1]) + str(list[2]))
                    if check > 19: 
                        if str(list[2]) == "0": 
                            section = dict[int(list[0])] + " Hundred " + dict[int(list[1] + "0")]  
                        else: 
                            section = dict[int(list[0])] + " Hundred " + dict[int(list[1] + "0")] + " " + dict[int(list[2])]     
                    else: 
                        if check == 0: 
                            section = dict[int(list[0])] + " Hundred"
                        else: 
                            section = dict[int(list[0])] + " Hundred " + dict[check]
                    count -= 3
                    things.append(section)   
                elif count == 2: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    check = (int(list[0]) * 10) + int(list[1])
                    if check > 19: 
                        if int(list[1]) == 0:
                            section = dict[int(list[0]) * 10]
                        else: 
                            section = dict[int(list[0]) * 10] + " " + dict[int(list[1])]
                        things.append(section)
                        count -= 2
                    else: 
                        things.append(dict[check])
                        count -= 2
                elif count == 1: 
                    check1 = int(str(list[0]))
                    if check1 == 0:
                        count -= 1
                        del list[0]
                        continue
                    section = dict[int(list[0])]
                    things.append(section)
                    count -= 1
                    
        word = " ".join(part.strip() for part in things)
        return word