import sys 
from collections import defaultdict

numFlights  = int(sys.stdin.readline())
flights = []
output = defaultdict(list)
counter = 0

for i in range(numFlights): 

    flight_info = list(map(int, sys.stdin.readline().split()))
    for j in range(len(flight_info)):
        if flight_info[j] != -1: 
            counter += 1
            output[i+1].append((j+1, flight_info[j]))



for i in range(numFlights):
    sorted(output[i])

print(counter)

for key, value_list in output.items():
    for item in value_list:
        print(key, item[0], item[1])

