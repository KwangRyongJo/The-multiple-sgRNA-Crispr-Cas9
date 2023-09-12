# generate pascal triangle numbers and save it as csv file
import csv
with open("triangle_numbers.csv", "w", encoding="utf8") as csvfile:
    row=[1]
    for i in range(16):  
        # print(row)    
        # print(*row, sep=", ") # print list without bracket              
        newrow=[]
        newrow.append(row[0])
        for i in range(len(row)-1):
            newrow.append(row[i]+row[i+1])            
        newrow.append(row[-1])        
        row=newrow
        csvfile.write(str(row)[1:-1]) # [1:-1], Remove square brackets from list 
        # using str() + list slicing 
        csvfile.write('\n') # write rows line by line

import pyexcel # pip install pyexcel pyexcel-xlsx
sheet = pyexcel.get_sheet(file_name="triangle_numbers.csv", delimiter=",")
sheet.save_as("triangle_numbers.xlsx")