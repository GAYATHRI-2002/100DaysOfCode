n1 = 0
n2 = 1
series_num = int(input("Enter the number of series needed: "))
print("The series is : ", n1, n2, end=" ")
for i in range(2, series_num):
    n3 = n1 + n2
    print(n3 , end=" ")
    n1 = n2
    n2 = n3

