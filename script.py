n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))
n3 = int(input("enter number 3: "))

largest = 0
a = [n1,n2,n3]

for n in a:
    if n > largest:
        largest = n

print(largest)