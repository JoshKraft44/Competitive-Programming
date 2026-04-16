import sys

num_games = int(sys.stdin.readline())


for i in range(num_games): 
    
    board = []
    for i in range(10): 
        row = list(sys.stdin.readline().strip())
        board.append(row) 

print(board)









def DFS(player, graph, captures): 

    pass