list1 = []

list_size = int(input("Enter the total number of list needs to enter: "))

for i in range(list_size):
    user_input = input()
    list1.append(int(user_input))

print(list1)