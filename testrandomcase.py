# -*- coding: utf-8 -*-

"""Random test case generator.

Randomly creates test cases for the stable matching problem presented in
COMPSCI 320 Assignment 1.

Assignment specification:
https://canvas.auckland.ac.nz/courses/60521/assignments/235860

Usage:
    1. put this file in the same directory/folder as your assignment solution
    2. import this file in your assignment solution
        `from testrandomcase import randomcase`
"""

import random


def randomcase(n=25):
    """Return randomly generated test case for the stable matching problem.

    Test cases are formatted as a list of strings, where each string is an
    input line ending with \n.
    """
    proposers = [str(2*i + 1) for i in range(n)]
    proposees = [str(2*i + 2) for i in range(n)]
    rankings = []
    for i in range(n):
        rankings.append(proposees.copy()) # proposer with proposee ranking
        rankings.append(proposers.copy()) # proposee with proposer ranking
    for ranking in rankings:
        random.shuffle(ranking)
    lines = [
        f"# Random instance for Gale-Shapley, n = {n}\n",
        "#\n",
        f"n = {n}\n",
        "#\n"
    ]
    for i in range(2*n):
        lines.append(f"{i+1}: {' '.join(rankings[i])}\n")
    return lines
