text=input()
count=0

for i in text:
    if i in "aieouAEIOU":
        count +=1
print(count)        
