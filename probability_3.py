class Multiplex:
    def __init__(self, tetra_allelic_events, total_event_combinations, probability):
        self.tetra_allelic_events = tetra_allelic_events
        self.total_event_combinations = total_event_combinations
        self.probability = probability

    def show_detail(self):
        print(self.tetra_allelic_events, self.total_event_combinations, \
            self.probability)





# from event_combinations import x, count_row

# if x == 16:
#     from module_4 import count_row_4
#     with open("probability.txt", "w") as report_file:
#         report_file.write("------------- {} sgRNA / tetraploid ------------ ".format(4))
#         report_file.write("\ntetra-allelic events : {:{}{}}".format(count_row_4, '>', 24))
#         report_file.write("\ntotal event combinations : {:{}{}}".format(count_row, '>', 20))
#         report_file.write("\nprobability : {:{}{}.{}}".format(count_row_4 / count_row, '>', 33, 2)) 
#         report_file.write("\n----------------------------------------------- ")


# elif x == 12:
#     from module_3 import count_row_3
#     print(" ------------ 3 sgRNA / tetraploid ------------ ")
#     print("tetra-allelic events : {:{}{}}".format(count_row_3, '>', 24))
#     print("total event combinations : {:{}{}}".format(count_row, '>', 20))    
#     print('probability : {:{}{}.{}}'.format(count_row_3 / count_row, '>', 33, 2))
#     print(" ---------------------------------------------- ")  

# elif x == 8:
#     from module_2 import count_row_2
#     print(" ------------ 2 sgRNA / tetraploid ------------ ")
#     print("tetra-allelic events : {:{}{}}".format(count_row_2, '>', 24))
#     print("total event combinations : {:{}{}}".format(count_row, '>', 20))    
#     print('probability : {:{}{}.{}}'.format(count_row_2 / count_row, '>', 33, 2))
#     print(" ---------------------------------------------- ") 

# elif x == 4:
#     from module_1 import count_row_1
#     print(" ------------ 1 sgRNA / tetraploid ------------ ")
#     print("tetra-allelic events : {:{}{}}".format(count_row_1, '>', 24))
#     print("total event combinations : {:{}{}}".format(count_row, '>', 20))    
#     print('probability : {:{}{}.{}}'.format(count_row_1 / count_row, '>', 33, 2))     
#     print(" ---------------------------------------------- ")    
# else:
#     print()