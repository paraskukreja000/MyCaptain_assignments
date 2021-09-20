name = input("Enter your file name: ")
extension = name.split(".")

if str(extension[-1]) == "py":
    print("Extension name is: python")
else:
    print("File name is: " + str(extension[-1]))