# def sum(list):
#     if list ==[]:
#         return 0
#     else:
#         return list[0] + sum(list[1:])          #Trying to write a recursive function for the sum function
# def count(list):
#     if list ==[]:
#         return 0
#     else:
#         return 1 + count(list[1:])
# def max(list):
#     if len(list)==2:
#         return list[0] if list[0] > list[1] else list[1]
#     else:
        
# list1=[1,2,3,4,5,6,7,8,9,10,11]
# print("The sum of the",count(list1),"numbers above is",sum(list1))
rty=int(input("Input your numbers:"))
count=0
for i in rty:
    count+=1

print('There are ',count,' number of numbers')