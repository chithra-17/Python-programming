text = input("Enter Number: ")
checked=""
for i in text:
    if i not in checked:
        print(i, ":" ,text.count(i))
        checked +=i