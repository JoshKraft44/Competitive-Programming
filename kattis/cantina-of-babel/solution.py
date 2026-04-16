import sys
from collections import defaultdict

num_characters = int(sys.stdin.readline())

graph = defaultdict(list)
rev_graph = defaultdict(list)
char_spoken = {}

for _ in range(num_characters):
    all_info = sys.stdin.readline().split()
    name = all_info[0]
    spoken = all_info[1]
    understood = list(all_info[2:])
    char_spoken[name] = spoken
    for lang in understood:
        graph[lang].append(spoken)
        rev_graph[spoken].append(lang)
    graph[spoken].append(spoken)
    rev_graph[spoken].append(spoken)

all_langs = set(graph.keys()) | set(rev_graph.keys())

visited = set()
finish_order = []

def dfs(node, adj, vis, result):
    stack = [(node, False)]
    while stack:
        v, done = stack.pop()
        if done:
            result.append(v)
            continue
        if v in vis:
            continue
        vis.add(v)
        stack.append((v, True))
        for neighbour in adj[v]:
            if neighbour not in vis:
                stack.append((neighbour, False))

for lang in all_langs:
    if lang not in visited:
        dfs(lang, graph, visited, finish_order)

visited2 = set()
components = []

for lang in reversed(finish_order):
    if lang not in visited2:
        comp = []
        dfs(lang, rev_graph, visited2, comp)
        components.append(set(comp))

max_group = 0
for comp in components:
    size = sum(1 for name in char_spoken if char_spoken[name] in comp)
    max_group = max(max_group, size)

print(num_characters - max_group)
