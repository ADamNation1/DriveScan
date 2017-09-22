import sys

dirList = []

dirList.append(input("Enter directory you wish to scan: "))
while True:
    multiple = input("Another one? (Press enter to contine without.)")
    if multiple == "":
        break;
    else:
        dirList.append(multiple)


print("Directories to scan...")
for i in dirList:
    print(i)

proceed = input("Proceed? Y/N: ")
if proceed.lower() == "n":
    print("Exiting...")
    sys.exit()
print("processing...")
