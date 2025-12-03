#!/bin/env/python3

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    # part 1 

    input_data = read_input('inputs/input.txt')
    # input_data = read_input('inputs/example1.txt')

    values = []
    # find pivot
    for line in input_data:

        numbers =[int(number) for number in line ]
        max_value=max(numbers)
        index = line.find(f'{max_value}')
        # print(f'{line}: {max_value=} at {index=}')


        max_pre = max(numbers[:index]) if index!=0 else None
        max_post = max(numbers[index+1:]) if index!=(len(numbers)-1) else None

        try:
            pre_num=max_pre*10+max_value
        except:
            pre_num=0
        # print(f'{line}: {max_value=} at {index=}')
        try:
            post_num=max_value*10+max_post
        except:
            post_num=0
        value = max([pre_num,post_num])
        # print(f'{max_pre=} {max_post=}')
        # print(f'{value=}')
        values.append(value)

    code=sum(values)
    print(f'Part1 {code=}')
        
    # part 2 

    code=0
    print(f'Part2 {code=}')
     




