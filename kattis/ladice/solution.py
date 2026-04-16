import sys
input = sys.stdin.readline

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a == root_b:
        return False

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    return True


n, l = map(int, sys.stdin.readline().split())

parent = []
size = []
used = []
rank = []
output = []

for i in range(l + 1):
    parent.append(i)
    size.append(1)
    used.append(0)
    rank.append(0)


for i in range(n):
    a, b = map(int, input().split())

    if find(a, parent) == find(b, parent):
        current_root = find(b, parent)
    else:
        old_a = size[find(a, parent)]
        old_b = size[find(b, parent)]

        old_used_a = used[find(a, parent)]
        old_used_b = used[find(b, parent)]


        if union(a, b, parent, rank):
            new_root_a = find(a, parent)
            new_root_b = find(b, parent)

            current_root = new_root_a

            combined_size = old_a + old_b
            combined_used = old_used_a + old_used_b

            size[current_root] = combined_size
            used[current_root] = combined_used
        else:
            current_root = find(a, parent)

    spots_taken = used[current_root]
    total_spots = size[current_root]

    if spots_taken < total_spots:
        used[current_root] = used[current_root] + 1
        output.append("LADICA")
    else:
        output.append("SMECE")

for answer in output:
    print(answer)