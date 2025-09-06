n = int(input())
integer_list = list(map(int, input().split()))
if len(integer_list) != n:
    print("Error: Number of integers does not match the specified count.")
else:
    t = tuple(integer_list)
    print(hash(t))