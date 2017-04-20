#!/usr/bin/env python3

'''some functions for dealing with the binary data'''

def read_all(fn):
    '''read the entire dataset into a list'''
    data = []
    with open(fn, 'rb') as f:
        pixel = f.read(3)
        while pixel:
            data.append(from_bytes3(pixel))
            pixel=f.read(3)
    return data

def from_bytes3(b):
    '''3 bytes => 24 bit integer => x, y, and color'''
    i = int.from_bytes(b, 'little')
    return from_int24(i)

def from_int24(i):
    '''24 bit integer to x, y, and color'''
    return i >> 14 & 1023, i >> 4 & 1023, i & 15

def to_bytes3(x, y, c):
    '''x, y, and color to a 3 bytes'''
    return to_int24(x,y,c).to_bytes(3, 'little')

def to_int24(x, y, c):
    '''x, y and color to a 24 bit integer'''
    return (x << 14) + (y << 4) + c




