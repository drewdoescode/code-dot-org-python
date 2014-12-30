"""Stage 11: Puzzle 7 of 11

Here's a program to draw a spiral Make a new program using counter loop
and your `draw_square()` function instead of the long way.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level65')
z = zombie


for counter in range(25,61,5):
    z.fd(counter)
    z.rt()

zombie.check()
