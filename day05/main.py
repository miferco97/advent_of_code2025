#!/bin/env/python3
from copy import deepcopy

def read_input(file_path):
    with open(file_path, 'r') as file:
        # return [char for char in  ]
        ranges=[]
        ids=[]
        skip=False
        for line in file.readlines():
            content = line.strip()
            if not content:
                skip=True
                continue
            if not skip:
                x , y = content.split('-') 
                ranges.append([int(x),int(y)])
            else:
                ids.append(int(content))

        return ranges, ids

def test_in_range( id, id_range):
    lower, higher = id_range
    if id < lower or id > higher:
        return False
    return True

if __name__ == "__main__":
    id_ranges, ids = read_input('inputs/input.txt')
    # id_ranges, ids = read_input('inputs/example1.txt')

    print(f'{id_ranges=}, {ids=}')

    # part 1 
    code = 0
    for id in ids:
        for id_range in id_ranges:
            if test_in_range(id,id_range):
                code += 1
                print(f'{id=} within {id_range=}')
                break

    
    print(f'Part1 {code=}')
        
    # part 2 
    code = 0
    print(f'Part2 {code=}')