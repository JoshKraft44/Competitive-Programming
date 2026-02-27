# Pachyderm Peanut Packing
# https://open.kattis.com/problems/pachydermpeanutpacking

def get_boxes():
    global first_x_array
    global first_y_array
    global second_x_array
    global second_y_array
    global numBoxes
    global numPeanuts
    global box_size_array
    text = ""

    first_x_array = []
    second_x_array = []
    first_y_array = []
    second_y_array = []
    box_size_array = []

    numBoxes = int(input())
    if numBoxes == 0:
        exit()
    for i in range(numBoxes):
        global boxSize
        x1, y1, x2, y2, boxSize = input().split()
        x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])
        first_x_array.append(x1)
        first_y_array.append(y1)
        second_x_array.append(x2)
        second_y_array.append(y2)
        box_size_array.append(boxSize)
    return first_x_array, first_y_array, second_x_array, second_y_array, box_size_array, numBoxes

def get_peanuts(first_x_array, first_y_array, second_x_array, second_y_array, box_size_array, numBoxes):
    numPeanuts = int(input())
    for i in range(numPeanuts):
        x, y, peanutSize = input().split()
        x = float(x)
        y = float(y)
        text = "floor"

        for j in range(numBoxes):
            if x >= first_x_array[j] and x <= second_x_array[j] and \
            y >= first_y_array[j] and y <= second_y_array[j]:
                if box_size_array[j] == peanutSize: 
                    text = "correct"
                else: 
                    text = box_size_array[j]
                break
            
        print(peanutSize, text) 
                
while True: 
    first_x_array, first_y_array, second_x_array, second_y_array, box_size_array, numBoxes = get_boxes()
    get_peanuts(first_x_array, first_y_array, second_x_array, second_y_array, box_size_array, numBoxes)
