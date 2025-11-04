try:
    with open("E:\\PYTHONfull\\100DaysOfCode\\file.txt", "a", encoding="utf-8") as file:
        file.write("Adding a new line.\n")
        file.write("The new line added\n")
except PermissionError:
    print("Permission denied! The file has only read permission.")
except FileNotFoundError:
    print("File not found.")
print("File written successfully")
