#Most frequent character
text="banana"
freq={}

for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(max(freq, key=freq.get))