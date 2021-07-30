import sys

def inverse_real_index(man_real_index,woman_real_index):
    man_index = man_real_index*2 + 1
    woman_index = (woman_real_index+1) * 2
    return man_index,woman_index


def man_index_trans( man_index ):
    man_real_index = (man_index + 1)//2 - 1
    return man_real_index


def woman_index_trans(woman_index):
    woman_real_index = woman_index // 2 - 1
    return woman_real_index

n = 0
man_list = []
woman_list = []
seq = 1

for line in sys.stdin:
# for line in randomcase(n=1000):
    if line == "\n":
        break
    if( line[0] != '#' ):#if there is no #
        line = line.split()
        if( line[0] == 'n' ):
            n = int(line[2])
        else:
            temp = [ int(x) for x in line[1:] ]
            #do not use int(), it is too slow
            if( seq % 2): #man          
                man_list.append(temp)
                seq = seq + 1
            else: #woman
                # because of the eager for speed, do not care about bug of n = 0
                woman_list.append(temp)
                seq = seq + 1

execute_number = 0
man_finished = [-1]*n
woman_choice = [-1]*n   
# matching
while( execute_number < n ):
    for i in range(0,n): 
        if( man_finished[i] == -1 ):
            man_empty = i
            break
    man_inverse_index = man_empty*2 + 1
    for i in range(0,n):
        man_target = woman_index_trans(man_list[man_empty][i])
        woman_pref = woman_list[man_target].index(man_inverse_index)
        if( woman_choice[man_target] == -1 ):
            # success and kick out none
            man_finished[man_empty] = man_target
            woman_choice[man_target] = woman_pref
            execute_number = execute_number + 1
            break
        elif( woman_pref < woman_choice[man_target] ):
            # success and kick out someone
            man_kick_out = man_index_trans(woman_list[man_target][woman_choice[man_target]])
            man_finished[man_kick_out] = -1
            man_finished[man_empty] = man_target
            woman_choice[man_target] = woman_pref
            break
for i in range(0,n):
    man,woman=inverse_real_index(i, man_finished[i])
    print(man,woman)

# print(timeit.default_timer()-t1)