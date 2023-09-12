from event_combinations import x, count_row

if x == 16:
    from module_44 import count_row_4
    print(" ------------ 4 sgRNA / tetraploid ------------ ")
    
    print("tetra-allelic events : {:{}{}}".format(count_row_4, '>', 24))
    print("total event combinations : {:{}{}}".format(count_row, '>', 20))
    
    # txt1 = "tetra-allelic events : "
    # log1 = txt1.ljust(30)
    # print(log1, count_row_4)
    # txt2 = "total event combinations : "
    # log2 = txt2.ljust(30)
    # print(log2, count_row)    
    # #print("probability : {0:>30}".format(count_row_4 / count_row)) 
    # #print("probability : {:.2f}".format(count_row_4 / count_row))
    print("probability : {:{}{}.{}}".format(count_row_4 / count_row, ">", 33, 2))
    # https://pyformat.info/
    print(" ---------------------------------------------- ") 

elif x == 12:
    from module_43 import count_row_3
    print(" ------------ 3 sgRNA / tetraploid ------------ ")
    print("tetra-allelic events : {:{}{}}".format(count_row_3, '>', 24))
    print("total event combinations : {:{}{}}".format(count_row, '>', 20))    
    print('probability : {:{}{}.{}}'.format(count_row_3 / count_row, '>', 33, 2))
    print(" ---------------------------------------------- ")  

elif x == 8:
    from module_42 import count_row_2
    print(" ------------ 2 sgRNA / tetraploid ------------ ")
    # print("tetra-allelic events : ", count_row_2)
    # print("total event combinations : ", count_row)
    # print("probability : {:.2f}".format(count_row_2 / count_row))  
    print("tetra-allelic events : {:{}{}}".format(count_row_2, '>', 24))
    print("total event combinations : {:{}{}}".format(count_row, '>', 20))    
    print('probability : {:{}{}.{}}'.format(count_row_2 / count_row, '>', 33, 2))
    print(" ---------------------------------------------- ") 

elif x == 4:
    from module_41 import count_row_1
    print(" ------------ 1 sgRNA / tetraploid ------------ ")
    # print("tetra-allelic events : ", count_row_1)
    # print("total event combinations : ", count_row)
    # print("probability : {:.2f}".format(count_row_1 / count_row))   
    print("tetra-allelic events : {:{}{}}".format(count_row_1, '>', 24))
    print("total event combinations : {:{}{}}".format(count_row, '>', 20))    
    print('probability : {:{}{}.{}}'.format(count_row_1 / count_row, '>', 33, 2))     
    print(" ---------------------------------------------- ")    
else:
    print()

# import numpy as np
# import pandas as pd
# import itertools
# from pandas import read_csv

# with open(" probability.txt", "w", encoding="utf8") as report_file:
#     if i == int(m / 4):
#         report_file.write(" ---------- {} sgRNA / tetraploid ---------- ".format(i))
#         report_file.write("\ntetra-allelic events : ", count_row(i))
#         report_file.write("\ntotal event combinations : ", count_row)
#         report_file.write("\nprobability : {:.2f}".format(count_row(i) / count_row))
#         report_file.write("\n ------------------------------------------ ")


# #if i == int(m / 4):
# for i in range(1, 4):
#     with open(" probability.txt", "w", encoding="utf8") as report_file:
#         report_file.write(" ---------- {} sgRNA / tetraploid ---------- ".format((i))
#         report_file.write("\ntetra-allelic events : ", (count_row(i))
#         report_file.write("\ntotal event combinations : ", count_row)
#         report_file.write("\nprobability : {:.2f}".format(count_row(i) / count_row))
#         report_file.write("\n ------------------------------------------ ")

# if x == 16:
#     print(" ---------- 4 sgRNA / tetraploid ---------- ")
#     print("tetra-allelic events : ", count_row_4)
#     print("total event combinations : ", count_row)
#     print("probability : {:.2f}".format(count_row_4 / count_row))
#     print(" ------------------------------------------ ") 

# for i in range(1, int(m / 4)):
#     with open(str(i) + " probability.txt", "w", encoding="utf8") as report_file:
#         report_file.write(" ---------- {} sgRNA / tetraploid ---------- ".format(i))
#         report_file.write("\ntetra-allelic events : ", count_row)
#         report_file.write("\total event combinations : ", count_row(i))
#         report_file.write("\nprobability : {:.2f}".format(count_row(i) / count_row))
#         report_file.write("\n ------------------------------------------ ")

    
# elif x == 12:
#     print(" ---------- 4 sgRNA / tetraploid ---------- ")
#     print("tetra-allelic events : ", count_row_3)
#     print("total event combinations : ", count_row)
#     print("probability : {:.2f}".format(count_row_3 / count_row))
#     print(" ------------------------------------------ ")  

# elif x == 8:
#     print(" ---------- 4 sgRNA / tetraploid ---------- ")
#     print("tetra-allelic events : ", count_row_2)
#     print("total event combinations : ", count_row)
#     print("probability : {:.2f}".format(count_row_2 / count_row))  
#     print(" ------------------------------------------ ") 

# elif x == 4:
#     print(" ---------- 4 sgRNA / tetraploid ---------- ")
#     print("tetra-allelic events : ", count_row_1)
#     print("total event combinations : ", count_row)
#     print("probability : {:.2f}".format(count_row_1 / count_row))       
#     print(" ------------------------------------------ ")    
# else:
#     print()
# # # save
# # with open("probability.txt", "w", encoding="utf8") as csvfile:    
# #     csvfile.write("one sgRNA :," + str(lines[3]))
# #     csvfile.write("two sgRNAs :," + str(lines[7]))
# #     csvfile.write("three sgRNAs :," + str(lines[11]))
# #     csvfile.write("four sgRNAs :," + str(lines[15]))    