#!/bin/env/python3
from copy import deepcopy


def read_input1(file_path):
    
    data=[]
    ops=[]

    def clean_line(line):
            out =  ''
            line=line.strip()
            blank=False
            for char in line:
                if char == ' ':
                    if blank:
                        continue
                    blank=True
                    out+=','
                else:
                    blank=False
                    out+=char
            return out


    with open(file_path, 'r') as file:
        # return [char for char in  ]
        for line in file.readlines():
            line = clean_line(line)
            if line[0] in ['+','*']:
                ops = [text.strip() for text in line.split(',')]
                break
            data.append([int(number) for number in line.split(',')])

    return data, ops

def restruct_data(data, ops):
    data_in_cols = []

    for j in range(len(data[0])):
        new_col = []
        for i in range(len(data)):
            new_col.append(data[i][j])
        data_in_cols.append(new_col)
    
    return list(zip(data_in_cols,ops))


def read_input2(file_path):
    data=[]
    ops=[]
    # get the content in cols
    with open(file_path, 'r') as file:
        # return [char for char in  ]
        lines= file.readlines()
        data_in_cols=[]
        for j in range(len(lines[0])):
            new_cols=''
            for i in range(len(lines)):
                if j >= len(lines[i]):
                    continue
                new_cols+=lines[i][j]
            data_in_cols.append(new_cols)
    return data_in_cols[:-1]

def process_columns(input):
    ops=[]
    data=[]
    op=None
    numbers_list=[]

    for col in input:
        # print(col)
        if '*' in col:
            op='*'
        elif '+' in col:
            op='+'
        if len(set(col)) == 1 :
            # all are spaces
            # print(f'data {numbers_list} with op {op}')
            ops.append(op)
            data.append(numbers_list.copy())
            numbers_list=[]
            op=None
            continue
        numbers_in_col= col[:-1]
        # print(numbers_in_col)
        number=int(numbers_in_col.strip())
        numbers_list.append(number)
    # print(f'data {numbers_list} with op {op}')
    ops.append(op)
    data.append(numbers_list.copy())

    return zip(data, ops)



def compute_maths(numbers_opt,debug=False):
    results=[]

    for numbers, op in numbers_opt:
        result = 1
        if op == '+':
            result = sum(numbers)
        if op == '*':
            for num in numbers:
                result*=num
        results.append(result)
        if debug:
             print(f'{numbers=} with op {op} = {result}')

    return results 
    
if __name__ == "__main__":
    # input_file = 'inputs/input.txt'
    input_file = 'inputs/example1.txt'

    # part 1 
    numbers, ops = read_input1(input_file)
    numbers_ops = restruct_data(numbers,ops)
    results = compute_maths(numbers_ops)
    code = sum(results)
    print(f'Part1 {code=}')
        
    # part 2 
    numbers= read_input2(input_file)
    # print(numbers)
    numbers_ops = process_columns(numbers)
    results = compute_maths(numbers_ops)
    code = sum(results)
 
    print(f'Part2 {code=}')