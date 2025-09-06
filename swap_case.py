def swap_case(s):
    solution=''
    for i in s:
        if i.islower():
            tmp=i.upper()
        else:
            tmp=i.lower()
        solution = solution + tmp
    return solution


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)