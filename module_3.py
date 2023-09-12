from event_combinations import df, x, count_row
import numpy as np
import pandas as pd
import itertools
from pandas import read_csv

#df = pd.read_csv('foo-2.csv')
# sum of events per chromosome 
# (z1 for chrI, z2 for chrII, z3 for chrIII and z4 for chrIV)
# sum of events per TS(target site)
# (y1 for TS1, y2 for TS2, y3 for TS3 and y4 for TS4)
df1 = df.assign(
    z1 = df.a + df.b + df.c,
    z2 = df.d + df.e + df.f,
    z3 = df.g + df.h + df.i,
    z4 = df.j + df.k + df.l,
    y1 = df.a + df.d + df.g + df.j,
    y2 = df.b + df.e + df.h + df.k,
    y3 = df.c + df.f + df.i + df.l    
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

count_row_3 = df3.shape[0]  # gives number of row count
#print("tetra-allelic events in the 3 sgRNA system = ", count_row_3)

# # convert csv to xlsx
# import pyexcel 
# sheet = pyexcel.get_sheet(file_name="foo-4.csv", delimiter=",")
# sheet.save_as("foo-4.xlsx")

# calculate probability and save it
with open("probability-2.txt", "w") as report_file:
        report_file.write("----------- {} sgRNA / tetraploid ---------- "\
            .format(3))
        report_file.write("\ntetra-allelic events : {:{}{}}".\
            format(count_row_3, '>', 20))
        report_file.write("\ntotal event combinations : {:{}{}}".\
            format(count_row, '>', 16))
        report_file.write("\nprobability : {:{}{}.{}}".\
            format(count_row_3 / count_row, '>', 28, 2)) 
        report_file.write("\n------------------------------------------- ")