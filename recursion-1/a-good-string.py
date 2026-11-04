def solve(s, c):
    n = len(s)

    if n == 1:
        if s[0] == c:
            return 0
        return 1

    mid = n // 2

    a = 0
    b = 0

    for i in range(mid):
        if s[i] != c:
            a += 1

        if s[i + mid] != c:
            b += 1

    x = a + solve(s[mid:], chr(ord(c) + 1))
    y = b + solve(s[:mid], chr(ord(c) + 1))

    return min(x, y)


t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    print(solve(s, 'a'))