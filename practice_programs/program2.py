str="programming"
dict={}

for i in str:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

non_repeating=list(dict.items())[0] #or without using list
first_item=next(iter(dict.items()))
print(non_repeating)
print(first_item)
#Note dictionary doesnt support indexing like list
    
    




