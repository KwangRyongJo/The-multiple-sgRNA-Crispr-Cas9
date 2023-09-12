""" Produce all possible event combinations in tetraploid / 1 ~ 4 sgRNA """

import numpy as np
import pandas as pd
import itertools
from pandas import read_csv

# generate total event combinations and save into csv    
x = int(input("What's the number? "))              
a = list(itertools.product([0,1], repeat=x))
# tetraploid / 4gRNAs; repeat=16
# tetraploid / 3gRNAs; repeat=12
# tetraploid / 2gRNAs; repeat=8
# tetraploid / 1gRNA; repeat=4
# diploid / 4gRNAs; repeat 8
# diploid / 3gRNAs; repeat 6
# diploid / 2gRNAs; repeat 4
# diploid / 1gRNA; repeat 2
np.savetxt("foo-1.csv", a, delimiter=",", fmt='%d')


# generate all possible one letter strings 
from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 1)]
# print(keywords)
header = keywords[:x]
# print(header)

# put the column header in the dataframe and then save it.
df = pd.read_csv("foo-1.csv", sep = ',', names=header)

#df.to_csv('foo-2.csv')

count_row = df.shape[0]  # gives number of row count
#print("total event combinations = ", count_row)

# # convert csv to xlsx
# import pyexcel 
# sheet = pyexcel.get_sheet(file_name="foo-2.csv", delimiter=",")
# sheet.save_as("foo-2.xlsx")
