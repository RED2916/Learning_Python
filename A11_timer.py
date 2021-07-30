# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:08:27 2021

@author: 57553
"""

import sys
from testrandomcase import randomcase
import timeit


def man_index_trans( man_index ):
    man_real_index = (man_index + 1)//2 - 1
    return man_real_index


def woman_index_trans(woman_index):
    woman_real_index = woman_index // 2 - 1
    return woman_real_index

def choice_empty_man( man_finished_input ):
    for i in range(0,n): 
        if( man_finished_input[i] == -1 ):
            break
    return i


        
n = 0
man_list = []
woman_list = []
seq = 1
time_flag = 0
# for line in sys.stdin:
for line in randomcase(n=1000):
    if line == "\n":
        break
    line = line.split()
    if( line[0] != '#' ):#if there is no #
        
        if( line[0] == 'n' ):
            n = int(line[2])
            # print(n)
        else:
            # temp = re.findall("\d+", line)
            temp = [ int(x) for x in line[1:] ]
            if( seq % 2 ): #man          
                man_list.append(temp)
                seq = seq + 1
            else: #woman
                # because of the eager for speed, do not care about bug of n = 0
                woman_list.append(temp)
                seq = seq + 1
    else:
        if(time_flag == 0 ):
            t1 = timeit.default_timer()
            time_flag = 1
        continue
# print(man_list,woman_list)
t2 = timeit.default_timer() - t1
t21 = timeit.default_timer()

# create the inverse list of woman, the largest number represent the strongest willing
woman_inverse = [[0]*n for j in range(0,n)]

t3_1 = timeit.default_timer() - t21

for i in range(0,n):
    for j in range(0,n):
        temp = man_index_trans(woman_list[i][j])
        woman_inverse[i][temp] = n - j
        
t3 = timeit.default_timer() - t21
t31 = timeit.default_timer()

execute_number = 0
man_finished = [-1]*n # []* much faster than in range
woman_choice = [-1]*n 
# man_finished = [-1 for i in range(0,n)]
# woman_choice = [-1 for i in range(0,n)]

t4 = timeit.default_timer() - t31
t41 = timeit.default_timer()

# matching
while( execute_number < n ):
    man_empty = choice_empty_man( man_finished )
    for i in range(0,n):
        man_target = woman_index_trans(man_list[man_empty][i])
        if( woman_choice[man_target] == -1 ):
            # success and kick out none
            man_finished[man_empty] = man_target
            woman_choice[man_target] = man_empty
            execute_number = execute_number + 1
            break
        elif( woman_inverse[man_target][man_empty] > woman_inverse[man_target][woman_choice[man_target]] ):
            # success and kick out someone
            man_finished[woman_choice[man_target]] = -1
            man_finished[man_empty] = man_target
            woman_choice[man_target] = man_empty
            break
        
t5 = timeit.default_timer() - t41
t51 = timeit.default_timer()

# print(man_finished)
for i in range(0,n):
    man = i*2 + 1#unnecessary change
    woman = (man_finished[i]+1) * 2
    print(man,woman)
    

t6 = timeit.default_timer() - t51
t61 = timeit.default_timer()

print("t2",t2)
print("t3",t3)
print("t3_1",t3_1)
print("t4",t4)
print("t5",t5)
print("t6",t6)

t7 = timeit.default_timer() - t61

print("t7",t7)
print(timeit.default_timer()-t1)
