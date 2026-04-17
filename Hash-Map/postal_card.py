n = int(input())
a = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    s = input().split()

    if s[0] == "2":
        k = int(s[1])
        print(a[k - 1])
    else:
        k = int(s[1])
        x = int(s[2])
        a[k - 1] = x