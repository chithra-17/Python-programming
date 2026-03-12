# reverse words in python

text=input("Input: ")
words=text.split()
rev=words[::-1]
output=" ".join(rev)

print("Output:",output)