alphabets = "a b c b c d"
list1=alphabets.split()
print(list1)

dictOut={}
index =0
for item,value in enumerate(list1):
    if value not in dictOut.values():
        dictOut[index] = value
        index +=1
        
    

print(dictOut)



