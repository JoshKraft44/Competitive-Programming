# ACM Contest Scoring
# https://open.kattis.com/problems/acm

correct = 0
total_time = 0 
counter = 0
incorrect_list = []
def solve_problem():
        line = input()
        if (line != "-1"):   
            time, question, boolean = line.strip().split() 
            time = int(time)
            if (boolean == "right"): 
                global correct, total_time, counter
                for i in incorrect_list:
                    if i == question:
                        counter += 1
                total_time += (counter * 20)
                counter = 0
                correct += 1
                total_time += time
                solve_problem()
            else: 
                incorrect_list.append(question)
                solve_problem()  
        else:         
            print(correct, total_time)


solve_problem()