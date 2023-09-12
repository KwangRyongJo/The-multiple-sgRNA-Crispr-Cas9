from event_combinations import df, x, count_row
import numpy as np
import pandas as pd
import itertools
from pandas import read_csv

#df = pd.read_csv('foo-2.csv')
# sum of events per chromosome 
# (z1 for chrI, z2 for chrII, z3 for chrIII and z4 for chrIV)
# sum of events per TS(target site)
# (y1 for TS1)
df1 = df.assign(
    z1 = df.a,
    z2 = df.b,
    z3 = df.c,
    z4 = df.d,
    y1 = df.a + df.b + df.c + df.d          
    )
#save as csv
df1.to_csv('foo-3.csv')

# select rows without '0' values 
# in columns z1, z2, z3 and z4
# filter only tetra-allelic mutations
df2 = pd.read_csv('foo-3.csv')
df3 = df2.loc[
    (df2['z1'] != 0) & 
    (df2['z2'] != 0) & 
    (df2['z3'] != 0) & 
    (df2['z4'] != 0)
    ]
# #save as csv
# df3.to_csv('foo-4.csv')

count_row_1 = df3.shape[0]  # gives number of row count
#print("tetra-allelic events in the 1 sgRNA system = ", count_row_1)

# # convert csv to xlsx
# import pyexcel 
# sheet = pyexcel.get_sheet(file_name="foo-4.csv", delimiter=",")
# sheet.save_as("foo-4.xlsx")

# calculate probability and save it
with open("probability-4.txt", "w") as report_file:
        report_file.write("----------- {} sgRNA / tetraploid ---------- "\
            .format(1))
        report_file.write("\ntetra-allelic events : {:{}{}}"\
            .format(count_row_1, '>', 20))
        report_file.write("\ntotal event combinations : {:{}{}}"\
            .format(count_row, '>', 16))
        report_file.write("\nprobability : {:{}{}.{}}"\
            .format(count_row_1 / count_row, '>', 29, 1)) 
        report_file.write("\n------------------------------------------- ")



# merge .txt files
# https://www.tutorialspoint.com/How-to-merge-multiple-files-into-a-new-file-using-Python
filenames = ['probability-1.txt', 'probability-2.txt', 
             'probability-3.txt', 'probability-4.txt']
with open('mergefile', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:                
                outfile.write(line)
                outfile.write("\n")






