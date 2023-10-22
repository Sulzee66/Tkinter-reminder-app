def s_e(list):
    smallest=list[0]
    for i in list:
        if i < smallest:
            smallest=i
    return list.index(smallest)                 #returns the smallest element's index

def SelectionSort(list):
    newlist=[]
    for i in range(len(list)):
        nextInsert=s_e(list)
        newlist.append(list[nextInsert])
        list.pop(nextInsert)
    return newlist


list1=[9,2,2,3,4,1,73,66]
print(SelectionSort(list1))