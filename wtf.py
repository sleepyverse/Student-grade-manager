tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter the number that you want to search"))
i = 0
found = False

while i < len(tup):
    if x == tup[i]:
        print("element found at idx", i)
        found = True
        break
    i += 1

if not found:
    print("element not found")

