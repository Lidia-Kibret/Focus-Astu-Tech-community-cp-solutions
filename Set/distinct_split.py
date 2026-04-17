t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    r = [0]*n
    st = set()

    # right distinct
    for i in range(n-1, -1, -1):
        st.add(s[i])
        r[i] = len(st)

    st = set()
    ans = 0

    # try splits
    for i in range(n-1):
        st.add(s[i])
        ans = max(ans, len(st) + r[i+1])

    print(ans)