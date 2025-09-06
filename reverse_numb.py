#anass exercise reverse number
#methode 1
# n=int(input())
# n_string=str(n)
# reverse_numb=''
# for i in n_string:
#     reverse_numb=i+reverse_numb
# print(int(reverse_numb))

#methode 2
# n=int(input())
# s=0
# while n>0:
#     rest = n % 10   # 123 rest will be 3 
#     n = n // 10
#     s= s*10 + rest
# print (s)


# methode 3
n=int(input())
print(int(str(n)[::-1]))

