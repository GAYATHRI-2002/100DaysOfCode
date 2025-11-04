#file = open(r"E:\PYTHONfull\100DaysOfCode\file.txt")
file = open(r"E:\PYTHONfull\100DaysOfCode\file.txt")

for line in file:
    print(line.strip())
file.close()