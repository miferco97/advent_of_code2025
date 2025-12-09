#!/bin/env/python3
from copy import deepcopy

def read_input(file_path):
    with open(file_path, 'r') as file:
        # return [char for char in  ]
        data=[]
        for line in file.readlines():
            data.append([int(x.strip()) for x in line.split(',')])
        return data


class CharMatrix():

    def __init__(self, data):
        self.n_rows = len(data)
        self.n_cols = len(data[0])
        self.data=data
    
    def __str__(self):
        out=''
        for row in self.data:
            fields = ''.join(row)
            out=out+fields+'\n'
        return out
    
    def at(self,i,j):
        return self.data[i][j]
    
    def set(self,value,i,j):
        self.data[i][j] = value
    
def compute_area(tile1,tile2):
    #print(tile1 ,tile2)
    min_x = min(tile1[0],tile2[0])
    min_y = min(tile1[1],tile2[1])
    max_x = max(tile1[0],tile2[0])
    max_y = max(tile1[1],tile2[1])

    x = max_x - min_x + 1
    y = max_y - min_y + 1 
    # print (f'{x=} , {y=}, area={x*y}')
    return x * y

def find_max(tile_list):
    max_value = 0 
    largest_tile = 0
    for i in range(len(tile_list)):
        for j in range(i,len(tile_list)):
            if i == j: 
                continue
            area = compute_area(tile_list[i], tile_list[j])
            if area > max_value:
                max_value = area
                largest_tile = (tile_list[i],tile_list[j])
    return max_value

if __name__ == "__main__":
    # part 1 
    input_data = read_input('inputs/input.txt')
    #input_data = read_input('inputs/example1.txt')
    #print(input_data)
    assert(compute_area( [2,5] , [9,7]) == 24)
    assert(compute_area( [7,1] , [11,7]) == 35)
    assert(compute_area( [7,3] , [2,3]) == 6)

    code = find_max(input_data)
    print(f'Part1 {code=}')
        
    # part 2 
    code = 0
    print(f'Part2 {code=}')