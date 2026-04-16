# Needed some help on this one.

import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    out = []

    while idx < len(data):
        n = int(data[idx]); m = int(data[idx+1]); idx += 2

        ea = [0]*m; eb = [0]*m; ew = [0]*m
        for i in range(m):
            ea[i] = int(data[idx]) - 1; eb[i] = int(data[idx+1]) - 1; ew[i] = int(data[idx+2])
            idx += 3

        order = sorted(range(m), key=lambda i: ew[i])

        # kruskal's - inlined find + union for speed
        par = list(range(n))
        rnk = [0]*n

        adj_to = [[] for _ in range(n)]
        adj_w = [[] for _ in range(n)]
        mst_sum = 0
        mst_max = 0
        cnt = 0
        nma = []; nmb = []; nmw = []

        for i in order:
            a, b, w = ea[i], eb[i], ew[i]
            # inline find(a)
            x = a
            while par[x] != x: x = par[x]
            ra = x
            x = a
            while par[x] != ra: par[x], x = ra, par[x]
            # inline find(b)
            x = b
            while par[x] != x: x = par[x]
            rb = x
            x = b
            while par[x] != rb: par[x], x = rb, par[x]

            if ra != rb:
                if rnk[ra] < rnk[rb]: ra, rb = rb, ra
                par[rb] = ra
                if rnk[ra] == rnk[rb]: rnk[ra] += 1
                adj_to[a].append(b); adj_w[a].append(w)
                adj_to[b].append(a); adj_w[b].append(w)
                mst_sum += w
                if w > mst_max: mst_max = w
                cnt += 1
            else:
                nma.append(a); nmb.append(b); nmw.append(w)

        if cnt != n - 1:
            out.append("disconnected")
            continue

        # BFS to get tree parent, depth, max edge to parent
        tree_par = [-1]*n
        dep = [0]*n
        mtp = [0]*n  # max_to_parent
        vis = bytearray(n)
        vis[0] = 1
        q = [0]
        head = 0
        while head < len(q):
            u = q[head]; head += 1
            at = adj_to[u]; aw = adj_w[u]
            for i in range(len(at)):
                v = at[i]
                if not vis[v]:
                    vis[v] = 1
                    tree_par[v] = u
                    dep[v] = dep[u] + 1
                    mtp[v] = aw[i]
                    q.append(v)

        best = mst_sum - 2 * mst_max

        # for each non-mst edge with w >= mst_max, walk up to LCA tracking max edge
        for qi in range(len(nma)):
            w = nmw[qi]
            if w < mst_max:
                continue
            x, y = nma[qi], nmb[qi]
            res = 0
            dx, dy = dep[x], dep[y]
            if dx < dy:
                x, y = y, x
                dx, dy = dy, dx
            while dx > dy:
                e = mtp[x]
                if e > res: res = e
                x = tree_par[x]
                dx -= 1
            while x != y:
                e = mtp[x]
                if e > res: res = e
                e = mtp[y]
                if e > res: res = e
                x = tree_par[x]
                y = tree_par[y]

            candidate = mst_sum - res - w
            if candidate < best:
                best = candidate

        out.append(str(best))

    sys.stdout.write("\n".join(out) + "\n")

main()

# first att: just built MST and did mst_sum - max_edge, but that's wrong
# because the MST itself isn't always optimal, sometimes you want a heavier max edge
# in a non-MST spanning tree to get a bigger subtracion
#
# second att: brute force - try every edge as the longest, rebuild each time
# to greedily fill in the rest of the tree. correct but O(m^2) so TLE
#
# third?: build MST once, then for each non-MST edge with w >= mst_max,
# figure out what it costs to swap it in by walking up to LCA on the tree
# to find the heaviest edge on the path it would replace.
# cost = mst_sum - max_on_path(u,v) - w
# Thanks chatGPT, still too slow. 
