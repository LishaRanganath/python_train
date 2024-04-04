a=10
b=5
if a>b:
    print("a is greater")
if a>=b:
    print("a is greater or equal")
if a<b:
    print("b is grater")
if a<=b:
    print("b is greater of equal")
if a==b:
    print("a equals b")


print("a is greater") if a>b else print("b is greater")

# check if the rearranged number is multiple of 5

num="108"
if int(num) % 5 == 0:
    print("multiple of 5")
else:
    if '0' in num or '5' in num:
        print("multiple of 5")
        # for i in range(len(num)):
        #     temp=num[i]
        #     num[i+1]=num[i]
        #     num[i+1]=temp
        #     if int(num)%5==0:
        #         print("multiple of 5")
        #         break
    else:
        print("not a miltiple of 5")


count = 3
while (count > 0):
    print(count)
    count = count - 1
else:
    print("count is 0")


set1={1,2,4,3,5}
set2={4,5,8}
# set1.remove(2)
# set1.discard(2) #discard doesnt give any error when u try to discard any element that i snot present in the set it is opposite in remove
# set1.pop()
print(set2.symmetric_difference(set1))
set1.symmetric_difference_update(set2)
set1={1,2,4,3,5}
set2={4,5,8}
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))

tup1=(1,2,3)
print(set1.union(tup1))# | used instead of .union, it throws an error
#true the boolean value is considered as 1 in set
# a={True,1}
# print(a)
if set1.issubset(set2):
    print("set1 is subset of set2")
else:
    print("set1 is superset of set2")

if set1.issuperset(set2):
    print("set1 is superset of set2")
else:
    print("set1 is subset of set2")

set3={1,2,3,4}
temp=list(set3)
print(set(temp[0:-1]))

dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5}
dict3={'f':6,'g':7}
dict4={}
# print(dict.keys())
# print(dict.values())
# for key,value in dict.items():
#     print(key,value)

dict1.update(dict2)
dict1.update(dict3)
dict4.update(dict1)
print(dict4)






