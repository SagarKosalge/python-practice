# 1)
# a= int(input("first: "))
# b= int(input("second: "))
# if a > b:
#     print(a)
# elif a==b:
#     print("Both are equal")
# else:
#     print(b)
# 2)
# Gender= input("what is your gender")
# if Gender == "M":
#     print('Hello Mr')
# else:
#     print("Hello Ms")
# 3)
# no = int(input("number"))
# if no % 2 ==0 :
#     print(f"{no} is even number")
# else:
#     print(f"{no} is an odd no")
# 4)
# Name = input("what is you name?: ")
# age = int(input("What is your age: "))
# if age >= 18:
#     print(f"{Name} can vote.")
# else:
#     print(f"{Name} can not vote.")

# 5)
# year = int(input("what is year"))
# if year % 4 == 0:
#     if  year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

# 6)
# letter = input("enter letter: ")
# if letter.lower() in "aeiou":
#     print("letter is vowel.")
# else:
#     print("letter is consonent.")

# 7)
# n = int(input("type no: "))
# for _ in range(1, n+1):
#     print(_)

# 8)
# n = int(input("number: "))
# for _ in range(n,0,-1):
#     print(_)

# 9)
# n = int(input("Write number: "))
# for _ in range(1,11):
#     print(n*_)

# 10)
# n = int(input("Write number: "))
# z=0
# for  i in range(1, n+1):
#     z= z+i
# print(z)

#  11)
# N = int(input("Write number: "))
# z=1
# for i in range(N,0,-1):
#     z=z*i
# print(z)

# 12)

# N = int(input("Write number: "))
# for i in range(1,N+1):
#     if N % i == 0:
#         print(f"{i} is factor of {N}.")
#     else:
#         print(f"{i} is not factor of {N}.")

# 13)
# N = int(input("Write number: "))
# x=0
# for i in range(1,N):
#     if N % i == 0: 
#         x = x + i
# if x == N:
#     print(f"{N} is perfect no.")
# else:
#     print(f"{N} is not perfect no.")

# 14)
# N = int(input("Write number: "))
# if N == 2 and N== 1:
#    print(f"{N} is not a prime no")
# else:
#     count=0
#     for i in range(1,N+1):
#         if N % i == 0:
#             count+=1
#     if count == 2 :
#         print(f"{N} is prime no.")
#     else:
#         print(f"{N} is composite no.")

# 15) by using str
# N = input("Write number: ")
# x= len(N)
# for i in range(0,x):
#     print(int(N[i]))

# N = int(input("Write number: "))
# while N<100:
#     print(N%10)
#     print(int((N-(N%10))/10))
#     break

# Better solution
# N = int(input("Write number: "))
# while N!=0:
#     print(N%10)
#     N=N//10

    
      




# 16)
# N = (input("Write number: "))
# x= len(N)
# for i in range(0,x):
#     if N[i]== N[i-len(N)]:
#         print(f"{N} is pallindromic number.")
#         break
#     else:
#         print(f"{N} is not pallindromic number.")

# Better solution 
# N = int(input("Write number: "))
# a=0
# copy=N
# while N>0:
#     a=(a*10)+(N%10)
#     N=N//10
# if copy==a:
#     print(f"{copy} is pallindromic number.")
# else:
#     print(f"{copy} is not pallindromic number.")




    
