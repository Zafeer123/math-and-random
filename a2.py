dict = {'Codingal':2,'is':2,'the':2,'best':2,'for':2,'coding':1}
print("The original dictionary is:",dict)
k=2
res=0
for key in dict:
    if dict[key]==k:
        res+=1
print("The frequency of 2 is",str(res))
