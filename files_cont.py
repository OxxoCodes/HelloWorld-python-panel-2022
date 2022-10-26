with open("myfile.txt", "w") as myFile:
    myFile.write("This is another test!")

with open("myfile.txt", "r") as myFile:
    contents = myFile.read()

print(contents)