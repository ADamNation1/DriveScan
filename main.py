import sys, os

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

for i in dirList:
    for root, dirs, files in os.walk(i, topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


