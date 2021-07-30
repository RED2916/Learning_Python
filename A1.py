# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:56:02 2021

@author: 57553
"""
import re
import timeit
# from testrandomcase import randomcase

human_number = 0
man_number = 0
woman_number = 0
n = 0
man_finished = [0 for i in range(0,n)]
woman_choice = [0 for i in range(0,n)]

# transfer char list into number list 
def deal_char(char_list):
    number_list = []
    for i in range(0,len(char_list)):
         number_list.append( int(char_list[i]) )
    return number_list

#deal input into acceptable data type
def deal_input(input_all_split):
    length = len(input_all_split)
    global human_number
    global woman_number
    global man_number
    human_number = length - 4
    woman_number = human_number // 2
    man_number = human_number - woman_number
    
    man_list_temp = [[]for i in range(man_number)]
    woman_list_temp = [[]for i in range(woman_number)]
    
    #print(man_number,woman_number,human_number)
    
    temp1 = 0
    temp2 = 0
    for i in range(4,length):
        temp = deal_char(re.findall("\d+", input_all_split[i]))
        del temp[0]
        if( i%2 == 0 ):
            man_list_temp[temp1] = []+temp
            temp1 = temp1 + 1
        else:
            woman_list_temp[temp2] = []+temp
            temp2 = temp2 + 1
    return man_list_temp,woman_list_temp

def man_index_trans( man_index ):
    man_real_index = (man_index + 1)//2 - 1
    return man_real_index

def woman_index_trans(woman_index):
    woman_real_index = woman_index // 2 - 1
    return woman_real_index

# create the inverse list of woman, the largest number represent the strongest willing
def inverse_list(woman_list_input):
    woman_inverse_output = [[0 for i in range(0,n)] for j in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            temp = man_index_trans(woman_list_input[i][j])
            woman_inverse_output[i][temp] = n - j
    return woman_inverse_output
    
def choice_empty_man( man_finished_input ):
    for i in range(0,n): 
        if( man_finished_input[i] == -1 ):
            break
    return i

# man propose to woman
def man_propose(man_index_input,woman_index_input,woman_inverse):
    global woman_choice
    global man_finished
    if( woman_choice[woman_index_input] == -1 ):
        # success and kick out none
        man_finished[man_index_input] = woman_index_input
        woman_choice[woman_index_input] = man_index_input
        # print(man_finished,woman_choice)
        return 1
    elif( woman_inverse[woman_index_input][man_index_input] > woman_inverse[woman_index_input][woman_choice[woman_index_input]] ):
        # success and kick out someone
        man_finished[woman_choice[woman_index_input]] = -1
        man_finished[man_index_input] = woman_index_input
        woman_choice[woman_index_input] = man_index_input
        # print(man_finished,woman_choice)
        return 0
    else:
        # fail
        return -1

def inverse_real_index(man_real_index,woman_real_index):
    man_index = man_real_index*2 + 1
    woman_index = (woman_real_index+1) * 2
    return man_index,woman_index

def show_output(man_finished):
    for i in range(0,n):
        man,woman=inverse_real_index(i, man_finished[i])
        print(man,woman)

def main():
    #get input
    # input_all = input();
    # input_all_split = input_all.split("\n")
    input_all = input();
    input_all_split = input_all.split("\n")
    global n
    global man_finished
    global woman_choice
    # n = int(re.findall("\d+",input_all_split[2])[0])
    n = filter(str.isdigit,input_all_split[2])
    n = int("".join(n))
    man_finished = [-1 for i in range(0,n)]
    woman_choice = [-1 for i in range(0,n)]
    
    man_list,woman_list=deal_input(input_all_split)
    
    execute_number = 0
    woman_inverse = inverse_list(woman_list)
    
    # matching
    while( execute_number < n ):
        man_empty = choice_empty_man( man_finished )
        # print(man_empty,man_finished)
        for i in range(0,n):
            man_target = woman_index_trans(man_list[man_empty][i])
            # print(man_list[man_empty],man_target)
            test_output = man_propose(man_empty, man_target, woman_inverse)
            if( test_output == 1 ):
                execute_number = execute_number + 1
                break
            elif( test_output == 0 ):
                break
    # print(man_finished)
    show_output(man_finished)

        
        

if __name__ == '__main__':
     # start = timeit.default_timer()
     main()
     # print(timeit.default_timer()-start)