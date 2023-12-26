#!/usr/bin/python3
#asci values
start = ord('a')
end = ord('z')

#loop through and prrint
for asciiValue in range(start, end + 1):
    print('{:c}'.format(asciiValue), end=' ')
