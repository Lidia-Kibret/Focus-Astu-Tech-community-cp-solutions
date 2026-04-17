S = input()
if len(S) == 8 and S[0].isupper() and S[-1].isupper() and S[1:7].isdigit():
    print("Yes" if 100000 <= int(S[1:7]) <= 999999 else "No")
else:
    print("No")
    