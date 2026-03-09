# Islands in the Data Stream
# https://open.kattis.com/problems/islandsinthedatastream

num_inputs = int(input())

try: 
    for _ in range(num_inputs): 
        data_stream = list(map(int, input().split()))
        index = data_stream[0]
        data_stream = data_stream[1:]
        islands = 0

        for section in range(1, len(data_stream) - 1):
            current_min = data_stream[section]
            for j in range(section, len(data_stream) - 1):
                current_min = min(current_min, data_stream[j])
                if current_min > data_stream[section - 1] and current_min > data_stream[j + 1]:
                    islands += 1

        print(index, islands)
except EOFError: 
    pass