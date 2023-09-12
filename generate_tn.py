""" Generate pascal triangle numbers and save it as csv / excel """

import csv
with open("triangle_numbers.csv", "w", encoding="utf8") as csvfile:
    row=[1]
    for i in range(int(input("What's the number? "))):               
        newrow=[]
        newrow.append(row[0])
        for i in range(len(row)-1):
            newrow.append(row[i]+row[i+1])            
        newrow.append(row[-1])        
        row=newrow
        csvfile.write(str(row)[1:-1]) # [1:-1], Remove square brackets from list 
        # using str() + list slicing 
        csvfile.write('\n') # write rows line by line

# read specific lines only (here 16th line)
tn_file = open("triangle_numbers.csv", "r", encoding="utf8")
lines = tn_file.readlines()
# # for i in lines:
# #     i = int(input("Show specific lines :  "))
# #     print(lines[i])
# #     if i >= 16:
# #         tn_file.close()
# print(lines[3]) 
# print(lines[7]) 
# print(lines[11]) 
# print(lines[15]) 
# tn_file.close() 

# save
with open("tn.csv", "w", encoding="utf8") as csvfile:    
    csvfile.write("one sgRNA :," + str(lines[3]))
    csvfile.write("two sgRNAs :," + str(lines[7]))
    csvfile.write("three sgRNAs :," + str(lines[11]))
    csvfile.write("four sgRNAs :," + str(lines[15]))    

# # convert csv to xlsx
import pyexcel # pip install pyexcel pyexcel-xlsx
sheet = pyexcel.get_sheet(file_name="tn.csv", delimiter=",")
sheet.save_as("tn.xlsx")