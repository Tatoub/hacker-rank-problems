#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    L = []
    N = int(input())
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        if cmd == 'insert':
            i = int(command[1])
            e = int(command[2])
            L.insert(i, e)
        elif cmd == 'print':
            print(L)
        elif cmd == 'remove':
            e = int(command[1])
            L.remove(e)
        elif cmd == 'append':
            e = int(command[1])
            L.append(e)
        elif cmd == 'sort':
            L.sort()
        elif cmd == 'pop':
            L.pop()
        elif cmd == 'reverse':
            L.reverse()
    