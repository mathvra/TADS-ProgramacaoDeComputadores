A, B, C, D = map(int, input().split())

if (A + B) > C and (B+C) > A and (A+C) > B:
    print("S")
elif (A + B) > D and (B+D) > A and (A+D) > B:
    print("S")
elif (A + D) > C and (D+C) > A and (A+C) > D:
    print("S")
elif (B + D) > C and (D+C) > B and (B+C) > D:
    print("S")
else:
    print("N")
