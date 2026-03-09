# Watering Grass
# https://open.kattis.com/problems/wateringgrass

import math
fileContinues = True
Pass = False


while fileContinues:
    count = 0
    notFinished = True
    sprinkler_list = [] 

    try:
        num_sprinklers, strip_length, width = list(map(int, input().strip().split()))
    except EOFError: 
        fileContinues = False
        break
    halfWidth = width / 2.0

    for i in range(num_sprinklers):
        try: 
            position, radius = list(map(int, input().strip().split()))
        except EOFError: 
            fileContinues = False
            break

        if radius <= halfWidth:
            continue

        length = math.sqrt((radius ** 2) - (halfWidth**2))
        start, finish = position - length, position + length
        sprinkler_list.append((start, finish))
    
    sprinkler_list = sorted(sprinkler_list)

    maximum = 0.0
    distanceCovered = 0.0
    counter = 0


    while notFinished:
        maximumUpdated = False

        while counter < len(sprinkler_list) and sprinkler_list[counter][0] <= distanceCovered:
            if sprinkler_list[counter][1] > maximum:
                maximum = sprinkler_list[counter][1]
                maximumUpdated = True
            counter += 1
    
        if not maximumUpdated:
            print(-1)
            notFinished = False
            break

        distanceCovered = maximum
        count += 1

        if distanceCovered >= strip_length: 
            print(count)
            sprinkler_list = []
            notFinished = False
            break

    

    