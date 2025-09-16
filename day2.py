#factorial using iterative and recursive
def fact_iter(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
def fact_recur(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact_recur(num - 1)

num = int(input("enter a number: "))
inp = input("Enter the choice 1:itera/2:recur: ")

if inp == "1":
    print("The result is : ",fact_iter(num))
elif inp == "2":
    print("The result is : ",fact_recur(num))

#fibanocci series

def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

n = int(input("number: "))
for i in range(n):
    print(fib_recursive(i), end=" ")
#fib_iter(n)





