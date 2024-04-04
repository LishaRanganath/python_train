def length_of_string():
    string1 = "hello world"
    count = 0
    for i in string1:
        count = count + 1
    print(count)


def biggst_in_list():
    list1 = [1, 3, 5, 8, 2, 3]
    biggest = list1[0]
    for i in list1:
        if i > biggest:
            biggest = i
    print(biggest)


def frequency_chars():
    count = 0
    string1 = "hello world"
    for i in string1:
        if i == " ":
            continue
        else:
            count = count + 1
    print(count)


def add_ing_or_ly():
    string2 = "helloing"
    sub = "ing"
    if len(string2) > 3:
        if sub not in string2:
            string2 = string2 + sub
            print(string2)
        else:
            string2 = string2.replace(sub,"ly")
            print(string2)
    else:
        print(string2)


def common_elements():
    tup1 = (1, 2, 3, 4)
    tup2 = (3, 4, 5, 6)
    for i in tup1:
        for j in tup2:
            if i == j:
                print(i)


def add_to_tupple():
    tup1 = (1, 2, 3, 4)
    tup2 = (3, 4, 5, 6)
    l1 = list(tup1)
    l2 = list(tup2)
    l1.extend(l2)
    print(tuple(l1))


def unpack_tuples():
    tup1 = (1, 2, 3, 4, 5, 6)
    t1 = tup1[0:3]
    t2 = tup1[3:]
    print(t1)
    print(t2)


def list_of_tuples():
    list1 = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11)]
    list2 = []
    for i in list1:
        data = ''
        for j in i:
            data = data + str(j)
        list2.append(data)
    print(list2)


def convert_to_list():
    tup = (3, 4, 5, 6)
    l1 = list(tup)
    l1.clear()
    tup = tuple(l1)
    print(tup)


def add_tuple_to_list():
    list1 = [1, 2, 3]
    tup = (4, 5, 6)
    list1.append(tup)
    for i in list1:
        print(i)


def sort_accord_len():
       list1= ["hi", "programming", "is", "This", "python", "language", "", "", ""]
       length=len(list1[0])
       for i in range(len(list1)):
           for j in range(0,len(list1)-i-1):
               if len(list1[j])>len(list1[j + 1]):
                   temp=list1[j]
                   list1[j]=list1[j+1]
                   list1[j+1]=temp
       print(list1)


def remove_using_pos_indexing():
    tup1=(1,2,3,4,5)
    tup2=tup1[:len(tup1)-1]
    print(tup2)


def diff_between_tuples():
    tup1=(1,2,3,4)
    tup2=(1,4,5,6)
    list1=[]
    for i in tup1:
        if i not in tup2:
            list1.append(i)
    print(tuple(list1))
    list1.clear()
    for i in tup2:
        if i not in tup1:
            list1.append(i)
    print(tuple(list1))

def diff_equals_zero():
    list1=[1, 2, 3, -2, -1,-3]
    list2=[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j]==0:
                if ([list1[i],list1[j]]) not in list2:
                    list2.append([list1[i],list1[j]])
    print(list2)


length_of_string()
biggst_in_list()
common_elements()
add_to_tupple()
frequency_chars()
unpack_tuples()
add_ing_or_ly()
list_of_tuples()
convert_to_list()
add_tuple_to_list()
sort_accord_len()
remove_using_pos_indexing()
diff_between_tuples()
diff_equals_zero()