# question 1
test_list = [{4, 5, 6, 1}, {6, 4, 1, 5}, {1, 3, 4, 3}, {1, 4, 3}, {7, 8, 9}]
list1=[]
for i in test_list:
   if i in list1:
        print(i,"is duplicate")
   else:
       list1.append(i)
print("list after eliminating the duplicates:",list1)


# question 3

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9,5,4]
count=0
list1=[]
for i in a:
    for j in b:
        if i==j:
            if i not in list1:
                list1.append(i)
                count = count + 1
            else:
                continue
if count>0:
    print(f"the 2 lists have {count} elements as common")
else:
    print("no elements common")


#question 2

n=int(input("enter the number of inputs"))
list1=[]
count=0
str1=""
length=len(str1)
vowels=['a','e','i','o','u']
print("enter the inputs")
for i in range(n):
    test=input()
    list1.append(test)
for i in list1:
    for char in i:
        str1=str1+char
        length=length+1
        if char in vowels:
            count=count+1
            if count==3 and length==3:
                print("happy")
                break
        else:
            length=0
            count=0
if count==0:
    print("sad")




#question 4

arr = [[1, 2, 2, 4, 3, 6],
              [5, 1, 3, 4],
              [9, 5, 7, 1],
              [2, 4, 1, 3]]
set_test=set(arr[0])
for i in arr[1:]:
    set_test.update(i)
print(list(set_test))


#question 5


dict={}
res=True
key_to_remove=[]
for i in str1:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
common_val = max(list(dict.values()), key=list(dict.values()).count)
for i in dict:
    if dict[i]>common_val or dict[i]<common_val:
        dict[i] -=1
        if dict[i]==0:
            key_to_remove.append(i)
for key in key_to_remove:
    dict.pop(key, None)
temp=list(dict.values())[0]
for i in dict:
    if dict[i]!=temp:
        res=False
        break
print(res)
