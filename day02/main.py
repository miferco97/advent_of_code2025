#!/bin/env/python3

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        if len(lines) != 1:
            raise Exception('input is malformed')
        fields = [line.strip() for line in lines[0].split(',')]
        return [ field.split('-') for field in fields]

if __name__ == "__main__":

    input_data = read_input('inputs/input.txt')
    # input_data = read_input('inputs/example1.txt')

    # part 1 
    ids = []
    value=0
    for orig,end in input_data:
        for elem in range(int(orig),int(end)+1):
            n_chars = len(str(elem))
            if n_chars %2 != 0:
                continue
            
            first = elem // (10 ** (n_chars//2))
            second  = elem % (10 ** (n_chars//2))
            if first == second:
                ids.append(int(elem))
    code=sum(ids)
            
    print(f'Part1 {code=}')
    # print(f'Part2 {code=}')
        


