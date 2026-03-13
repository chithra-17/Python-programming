text="data engineering data python"
str=text.split()
freq={}

for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for key,values in freq.items():
    print(key,values)