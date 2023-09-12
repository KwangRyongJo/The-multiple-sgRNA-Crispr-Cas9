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
    z1 = df.a + df.b + df.c + df.d,
    z2 = df.e + df.f + df.g + df.h,
    z3 = df.i + df.j + df.k + df.l,
    z4 = df.m + df.n + df.o + df.p,
    y1 = df.a + df.e + df.i + df.m,
    y2 = df.b + df.f + df.j + df.n,
    y3 = df.c + df.g + df.k + df.o,
    y4 = df.d + df.h + df.l + df.p
    )
#save as csv
df1.to_csv('foo-3.csv')

# select rows without '0' values 
# in columns z1, z2, z3 and z4
# filter only tetra-allelic mutations
df2 = read_csv('foo-3.csv')
df3 = df2.loc[
    (df2['z1'] != 0) & 
    (df2['z2'] != 0) & 
    (df2['z3'] != 0) & 
    (df2['z4'] != 0)
    ]
#save as csv
#df3.to_csv('foo-4.csv')

count_row_4 = df3.shape[0]  # gives number of row count
#print("tetra-allelic events in the 4 sgRNA system = ", count_row_4)

# # convert csv to xlsx
# import pyexcel 
# sheet = pyexcel.get_sheet(file_name="foo-4.csv", delimiter=",")
# sheet.save_as("foo-4.xlsx")

# # calculate probability and save it
# with open("probability-1.txt", "w") as report_file:
#         report_file.write("----------- {} sgRNA / tetraploid ---------- "\
#             .format(4))
#         report_file.write("\ntetra-allelic events : {:{}{}}".\
#             format(count_row_4, '>', 20))
#         report_file.write("\ntotal event combinations : {:{}{}}".\
#             format(count_row, '>', 16))
#         report_file.write("\nprobability : {:{}{}.{}}".\
#             format(count_row_4 / count_row, '>', 28, 2)) 
#         report_file.write("\n------------------------------------------- ")

# calculate probability and save it
print("{0} / {1} = {2:.2f}".format(count_row_4, count_row, count_row_4 / count_row))   

# nums = []
# nums.append(count_row_4)
# nums.append(count_row)
# nums.append(nums[0] / nums[1])
# #print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# print("----------- {} sgRNA / tetraploid ---------- "\
#             .format(4))
# print("\ntetra-allelic events : {:{}{}}".\
#             format(nums[0], '>', 20))
# print("\ntotal event combinations : {:{}{}}".\
#             format(nums[1], '>', 16))            
# print("\nprobability : {:{}{}.{}}".\
#             format(nums[2], '>', 28, 2))
# print("\n------------------------------------------- ")