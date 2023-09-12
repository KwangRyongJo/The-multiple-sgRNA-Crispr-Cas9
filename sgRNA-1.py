# generate pascal triangle numbers
row=[1]
for i in range(int(input("What's the number? "))): # int(input("What's the number? "))   
    print(row) # (*row, sep=", "), remove bracket in list
    newrow=[]
    newrow.append(row[0])
    for i in range(len(row)-1):
        newrow.append(row[i]+row[i+1])
    newrow.append(row[-1])
    row=newrow