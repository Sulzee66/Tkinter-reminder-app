tdlist={
    1:"Do Amao Assignment",
    2:"Get my daily login bonus in efootball",
    3:"Go to cafe",
    4:"Go to Faculty for project submission",
    5:"Watch NFO vs MNU"
}
tdlist.update({2:"Buy data"})
print(tdlist)
# tdlist[6]="Buy fruits to break"
# print(tdlist)
td = input("to do list: ")
tdlist.update({7: td})
print(tdlist)