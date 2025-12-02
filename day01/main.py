#!/bin/env/python3

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    # part 1 

    input_data = read_input('input.txt')

    code=0
    value = 50
    for line in input_data:
        action = line[0]
        number = line[1:]
        # print(f'{action} : {number}')
        if action == 'R':
            value += int(number)
        elif action == 'L':
            value -= int(number)
        else:
            raise Exception('no valid action')
        value = value % 100
        if value == 0:
            code += 1

    print(f'Part1 {code=}')
        
    # part 2 

    code=0
    value = 50
    for line in input_data:
        action = line[0]
        number = line[1:]
        # print(f'{action} : {number}')
        if action == 'R':
            value += int(number)
        elif action == 'L':
            value -= int(number)
        else:
            raise Exception('no valid action')
        value = value % 100
        if value == 0:
            code += 1

    print(f'Part1 {code=}')




