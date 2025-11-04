try:
    file = open("data.txt")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("Not found")