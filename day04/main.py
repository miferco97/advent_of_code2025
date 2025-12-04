#!/bin/env/python3
from copy import deepcopy

def read_input(file_path):
    with open(file_path, 'r') as file:
        # return [char for char in  ]
        lines = [line.strip() for line in file.readlines()]
        data=[]
        for line in lines:
            data.append([char for char in line])
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
    
    def count_adjacents(self,row,column):
        count = 0
        for i in range(row-1,row+2):
            for j in range(column-1,column+2):
                if i == row and j==column:
                    continue
                if i < 0 or i>=self.n_rows:
                    continue
                if j < 0 or j>=self.n_cols:
                    continue
                # print(f'{i},{j}')
                if self.data[i][j] == '@':
                    count+=1
        return count
    
    def at(self,i,j):
        return self.data[i][j]
    
    def set(self,value,i,j):
        self.data[i][j] = value
    

def remove_rolls(initial_matrix):
    removed=0
    new_matrix = deepcopy(initial_matrix)

    for i in range(matrix.n_rows):
        for j in range(matrix.n_cols):
            data = matrix.at(i,j)
            if data == '@':
                if matrix.count_adjacents(i,j) < 4:
                    removed += 1
                    new_matrix.set('.',i,j)

    return new_matrix, removed

if __name__ == "__main__":
    # part 1 
    input_data = read_input('inputs/input.txt')
    # input_data = read_input('inputs/example1.txt')
    matrix = CharMatrix(input_data)
    _ , code = remove_rolls(matrix) 
    print(f'Part1 {code=}')
        
    # part 2 
    code = 0
    changed=True
    while changed:
        matrix , removed = remove_rolls(matrix)
        if not removed:
            break
        code += removed
    print(f'Part2 {code=}')