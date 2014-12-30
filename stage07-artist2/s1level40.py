"""Stage 7: Puzzle 6 of 11

Using only 3 lines of code, can you draw a square with edges of 20 pixels?

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level40')
a = artist

a.width = 10
for count in range(4):
    a.fd(19)
    a.rt()

artist.check()
