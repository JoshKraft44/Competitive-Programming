## Gave up on this one. 


import sys

input = sys.stdin.readline


def solve_case(n, m, raw_edges):
    edges = []
    for idx, (u, v, w) in enumerate(raw_edges):
        edges.append((w, u - 1, v - 1, idx))

    edges.sort()

    max_nodes = 2 * n + 5

    # DSU for Kruskal reconstruction tree
    uf = list(range(max_nodes))

    def find(x):
        while uf[x] != x:
            uf[x] = uf[uf[x]]
            x = uf[x]
        return x

    # reconstruction tree data
    tree_parent = [-1] * max_nodes
    tree_weight = [0] * max_nodes
    children = [[] for _ in range(max_nodes)]

    next_node = n
    comps = n
    mst_weight = 0

    # after finishing each weight group, store:
    # group_total[g] = MST/MSF weight using all edges up to this group
    # group_connected[g] = whether graph is connected after this group
    group_total = []
    group_connected = []
    edge_group = [0] * m

    i = 0
    group_id = 0
    while i < m:
        j = i
        w = edges[i][0]
        while j < m and edges[j][0] == w:
            j += 1

        for k in range(i, j):
            _, u, v, original_idx = edges[k]
            ru = find(u)
            rv = find(v)
            if ru != rv:
                new_node = next_node
                next_node += 1

                tree_weight[new_node] = w
                children[new_node].append(ru)
                children[new_node].append(rv)
                tree_parent[ru] = new_node
                tree_parent[rv] = new_node

                uf[ru] = new_node
                uf[rv] = new_node
                uf[new_node] = new_node

                mst_weight += w
                comps -= 1

        connected_now = (comps == 1)
        total_now = mst_weight

        for k in range(i, j):
            _, _, _, original_idx = edges[k]
            edge_group[original_idx] = group_id

        group_total.append(total_now)
        group_connected.append(connected_now)

        group_id += 1
        i = j

    if comps != 1:
        return "disconnected"

    root = find(0)
    total_nodes = next_node

    # Binary lifting on reconstruction tree
    LOG = (total_nodes).bit_length()
    up = [[-1] * total_nodes for _ in range(LOG)]
    depth = [0] * total_nodes

    stack = [root]
    order = [root]

    while stack:
        node = stack.pop()
        for ch in children[node]:
            depth[ch] = depth[node] + 1
            up[0][ch] = node
            stack.append(ch)
            order.append(ch)

    for b in range(1, LOG):
        prev = up[b - 1]
        curr = up[b]
        for v in range(total_nodes):
            p = prev[v]
            curr[v] = -1 if p == -1 else prev[p]

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a

        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                a = up[bit][a]
            diff >>= 1
            bit += 1

        if a == b:
            return a

        for bit in range(LOG - 1, -1, -1):
            if up[bit][a] != up[bit][b]:
                a = up[bit][a]
                b = up[bit][b]

        return up[0][a]

    best = float("inf")

    for original_idx, (u1, v1, w) in enumerate(raw_edges):
        g = edge_group[original_idx]
        if not group_connected[g]:
            continue

        u = u1 - 1
        v = v1 - 1

        ancestor = lca(u, v)
        c = tree_weight[ancestor]

        candidate = group_total[g] - c - w
        if candidate < best:
            best = candidate

    return str(best)


def main():
    out = []

    while True:
        line = input().split()
        if not line:
            break

        n, m = map(int, line)
        raw_edges = [tuple(map(int, input().split())) for _ in range(m)]
        out.append(solve_case(n, m, raw_edges))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

