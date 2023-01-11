#!/usr/bin/python3
import sys
if __name__ == '__main__':
    numarg = len(sys.argv) - 1
    if numarg == 1:
        print('{} argument.'.format(numarg))
    else:
        print('{} arguments.'.format(numarg))
    for i in range(1, numarg + 1):
        print('{}: {}'.format(i, sys.argv[i]))
