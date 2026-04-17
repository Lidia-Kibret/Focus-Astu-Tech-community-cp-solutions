n, k = map(int, input().split())
m = list(map(int, input().split()))

d = {}
cur = 0


for i in range(k):
    if m[i] not in d:
        cur += 1
        d[m[i]] = 0
    d[m[i]] += 1

ans = cur


for i in range(k, n):
    d[m[i]] = d.get(m[i], 0) + 1
    if d[m[i]] == 1:
        cur += 1

    d[m[i-k]] -= 1
    if d[m[i-k]] == 0:
        cur -= 1

    ans = max(ans, cur)

print(ans)