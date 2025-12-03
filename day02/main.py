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
    # part 2 

    ids = []
    value=0

    def get_dividers(n_chars):
        dividers=[]
        for i in range(1,n_chars):
            if n_chars % i == 0:
                dividers.append(i)
        return dividers
    
    def get_substrings(number,n_char):
        substrings = []
        string = str(number)
        for i in range (len(string)//n_char): 
            begin_index = i * n_char
            end_index= begin_index + n_char
            substrings.append(string[begin_index:end_index])
        return substrings

    def check_repetition(number, n_chars) -> bool:
        substrings = get_substrings(elem, divider)
        if len(substrings) < 2:
            return False 
        # print(f'{elem=},{divider=},{substrings=}')
        ref = substrings[0]
        for pattern in substrings[1:]:
            if pattern != ref:
                return False
        return True


    for orig,end in input_data:
        for elem in range(int(orig),int(end)+1):
            n_chars = len(str(elem))
            for divider in get_dividers(n_chars):
                if check_repetition(elem,n_chars):
                    # print(f'Repetition within {elem=}')
                    ids.append(elem)
                    break # to avoid counting the same number multiple times

    code=sum(ids)

    print(f'Part2 {code=}')

        


