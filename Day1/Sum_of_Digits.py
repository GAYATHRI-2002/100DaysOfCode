num = int(input("enter a number: "))
sum = 0
while num != 0:
    last = num % 10
    sum += last
    num = num// 10

print("The sum of the number is: ", sum)