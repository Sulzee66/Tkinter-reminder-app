def b_s(list,item):
    low=0
    high=len(list)
    while True:
        mid=int((low + high)*0.5)
        guess=list[mid]
        if guess==item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low= mid + 1
        else:
            print("Not present in the list")
    return list.index(guess)  

t_list=[1,3,5,7,9]
print(b_s(t_list,6))          
        
