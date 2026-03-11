num = int(input("Enter Number: "))
count=0
while num > 0:
    num=num // 10
    count += 1
print("Digits =",count)