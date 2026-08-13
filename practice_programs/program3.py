text="apple banana apple orange banana"

dit=text.split(" ")
dit2={}

for ch in dit:
    if ch not in dit2:
        dit2[ch]=1
    else:
        dit2[ch]+=1

print(dit2)