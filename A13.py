import sys
# import timeit
# from testrandomcase import randomcase

man_dic = {}
woman_dic = {}
seq = 1

for line in sys.stdin:
# for line in randomcase(n=1000):
    if line == "\n":
        break
    line = line.split()
    if( line[0] == '#' ):#if there is #
        continue
    if( line[0] == 'n' ):
        n = int(line[2])
    else:
        temp = list(map(int,line[1:]))
        #do not use int(), it is too slow
        if( seq % 2): #man          
            man_dic.update({seq:temp})
        else: #woman
            # because of the eager for speed, do not care about bug of n = 0
            woman_dic.update({seq:temp})
        seq = seq + 1

# t1 = timeit.default_timer()

# print(man_dic,woman_dic)
man_empty_list = [ x for x in range(1,n*2,2)]
man_finished = {}
woman_choice = {}
# matching
while( man_empty_list ):
    man_empty = man_empty_list[0]
    man_target = man_dic[man_empty].pop(0)
    woman_pref = woman_dic[man_target].index(man_empty)
    if( woman_choice.get(man_target) == None ):
        # success and kick out none
        man_finished[man_empty] = man_target
        woman_choice[man_target] = woman_pref
        man_empty_list.pop(0)
    elif( woman_pref < woman_choice[man_target] ):
        # success and kick out someone
        woman_loved_before = woman_choice[man_target]
        man_kick_out = woman_dic[man_target][woman_loved_before]
        man_empty_list.append(man_kick_out)
        man_finished[man_empty] = man_target
        woman_choice[man_target] = woman_pref
        man_empty_list.pop(0)
    # print(man_finished) 

for line in man_finished.items():
    print(line[0],line[1])

# print(timeit.default_timer()-t1)
