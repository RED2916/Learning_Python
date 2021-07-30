# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:24:42 2021

@author: 57553
"""

from collections import deque

def worst_case(n):
    lines = []
    lines.append("# Random instance for Gale-Shapley, n = 5 \n")
    lines.append("# \n")
    lines.append("n = {} \n".format(n))
    lines.append("# \n")
    men = deque()
    women = deque()
    
    for i in range(1, 2 * n + 1):
        if i % 2 == 0:
            women.append(str(i))
        else:
            men.append(str(i))   

    men.rotate(-1) 
    for i in range(1, 2* n + 1):
        
        if i % 2 == 0:
            line = "{}:".format(i)
            for x in men:
                line = line + " " + x
            
            men.rotate(1)
            final_line = line + "\n"
            lines.append(final_line)        
            
        else:
            line = "{}:".format(i)
            for x in women:
                line = line + " " + x 

            women.rotate(-1)
            final_line = line + "\n"
            lines.append(final_line)
    
    return lines

def main():   
    
    lines = worst_case(500)   
    
    f = open("worst_case.txt", "w")
    
    for line in lines:
        f.write(line)

    f.close()

main()