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
        self.data=deepcopy(data)
    
    def __str__(self):
        out=''
        for row in self.data:
            fields = ''.join([str(elem) for elem in row])
            out=out+fields+'\n'
        return out
    
    def __getitem__(self,i,j):
        return self.data[i][j]
    
    def row(self, i):
        return self.data[i]
    
    def cell_exists(self, i , j):
        if i < 0 or i >= self.n_rows:
            return False
        elif j < 0  or  j >= self.n_cols:
            return False
        return True

    def change(self, value, i, j):
        if i < 0 or i >= self.n_rows:
            return False
        elif j < 0  or  j >= self.n_cols:
            return False
        self.data[i][j] = value
        return True
    
    def expand_bottom(self,i,j):
        bottom_coord_i, bottom_coord_j = i+1, j
        if not self.cell_exists(bottom_coord_i,bottom_coord_j):
            return -1
        cell = self.__getitem__(bottom_coord_i,bottom_coord_j)
        if cell == '^':
            self.change('|',bottom_coord_i,bottom_coord_j-1)
            self.change('|',bottom_coord_i,bottom_coord_j+1)
            return 1 
        if cell == '.':
            self.change('|',bottom_coord_i,bottom_coord_j)

        return 0
    
    
    def increase(self,value,i,j):
        if not self.cell_exists(i,j):
            return
        if not isinstance(self.data[i][j], int):
             return
        if not isinstance(value, int):
             return
        
        self.data[i][j] += value
        

    def sum_bottom(self,i,j):
        curr_value = self.data[i][j]
        bottom_coord_i, bottom_coord_j = i+1, j
        if not self.cell_exists(bottom_coord_i,bottom_coord_j):
            return -1
        cell = self.__getitem__(bottom_coord_i,bottom_coord_j)
        if cell == '^':
            self.increase(curr_value,bottom_coord_i,bottom_coord_j-1)
            self.increase(curr_value,bottom_coord_i,bottom_coord_j+1)
            return 1 
        self.increase(curr_value,bottom_coord_i,bottom_coord_j)
        return 0            
    

def propagate_tree(matrix):
    n_splits=0
    for i in range(matrix.n_rows):
        for j, char in enumerate(matrix.row(i)):
            if char == 'S':
                matrix.expand_bottom(i,j)
            if char == '|':
                res = matrix.expand_bottom(i,j)
                if res < 0 :
                    return n_splits
                n_splits+=res
        #print(matrix)


def numberize_matrix(matrix):
    for i in range(matrix.n_rows):
        for j in range(matrix.n_cols):
            char_ = matrix.data[i][j]
            if char_ == 'S':
                matrix.data[i][j] = 1
            elif char_ == '.':
                matrix.data[i][j] = 0
    return matrix

def propagate_matrix(matrix):
    n_splits=0
    for i in range(matrix.n_rows):
        for j, char in enumerate(matrix.row(i)):
            if isinstance(char,int) and char == 0:
                continue

            res = matrix.sum_bottom(i,j)
            if res < 0 :
                return n_splits
            n_splits+=res
        #print(matrix)
   
    
if __name__ == "__main__":
    # part 1 
    filename='inputs/input.txt'

    input_data = read_input(filename)
    matrix = CharMatrix(input_data.copy())
    code =  propagate_tree(matrix)
    print(f'Part1 {code=}')
        
    # part 2 
    matrix = CharMatrix(input_data)
    matrix = numberize_matrix(matrix)
    code = propagate_matrix(matrix)
    code = sum(matrix.row(matrix.n_rows-1))

    print(f'Part2 {code=}')