#import array as a
a=[0,1,2,3,4,5,6,7,8,9]
print("Normal Array:-->")
for i in range(-len(a),-1,2):
    #print(i)
    print(a[i])
print("Reverse Array:-->")
for j in range(-1,-len(a),-2):
    #print(j)
    print(a[j])