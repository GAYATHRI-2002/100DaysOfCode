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




