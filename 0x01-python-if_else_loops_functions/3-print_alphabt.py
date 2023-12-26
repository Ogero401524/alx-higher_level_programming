#!/usr/bin/python3
# ascii valuse
st = ord('a')
ed = ord('z')
# loop and print
for i in range(st, ed + 1):
    if chr(i) not in {'q', 'e'}:
        print('{:c}'.format(i), end='')
