#count vowels
name="chithra"
count=0
vowel=['a','e','i','o','u']
for i in name:
    if i in vowel:
        count+=1
print(count)

#count digits
num=1234567
count=0
while num>0:
    num=num // 10
    count+=1
print(count)

#palindrome of the num
num1=int(input())
rev=0
while num1>0:
    digit=num%10      
    rev=rev*10+digit 
    num1=num//10

if num1==rev:
    print("palindrome")
else:
    print("not palindrome")

#fibonacci
num2=int(input("Enter the value:"))
a=0
b=1

for i in range(num2):
    print(a)
    c=a+b
    a=b #1
    b=c #2



