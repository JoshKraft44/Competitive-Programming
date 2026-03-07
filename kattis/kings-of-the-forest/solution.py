import heapq
import sys

def solve(): 
    poolSize, years = map(int, input().split())


    karl_year, karl_strength = map(int, input().split())

    moose = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            entry, strength = map(int, line.split())
            moose.append((entry, strength))

    moose = [(karl_year, karl_strength)] + moose

    all_entry_years = [m[0] for m in moose]
    start_year = min(all_entry_years)

    pool = []
    newcomers = {}
    

    for entry, strength in moose: 
        if entry == start_year: 
            heapq.heappush(pool, (-strength, entry))
        else: 
            newcomers[entry] = strength

    for year in range(start_year, start_year + years): 

        if year in newcomers: 
            s = newcomers[year]
            heapq.heappush(pool, (-s, year))


        neg_strength, entry = heapq.heappop(pool)
        winner_strength = -neg_strength

        if winner_strength == karl_strength: 
            print(year)
            return
            
        

    print("unknown")

solve()


