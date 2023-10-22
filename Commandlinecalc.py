print("This is a command line calculator")
# try:
x=int(input())      #input the first value
char =input()       #Input the desired sign operation
y= int(input())     #input the second value

if (char== "+"):
  result =x+y         #the addition operation
  print(result)
elif (char== "-"):
  result =x-y          #the subtraction operation
  print(result)
elif (char== "*"):
  result =x*y          #the multiplication operation
  print(result)
elif (char== "/"):
  result =x/y          #the division operation
  print(result)
# except ValueError:
  # print("Error! can only take numerical values not string")
    