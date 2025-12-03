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
        try:
            post_num=max_value*10+max_post
        except:
            post_num=0
        value = max([pre_num,post_num])
        values.append(value)

    code=sum(values)
    print(f'Part1 {code=}')
        
    # part 2 

    code = 0
    n_batteries = 12

    def find_max(number,n_chars):
        number_str = str(number)
        number_length = len(number_str)
        swap_index = number_length-n_chars+1
        number_front = number[0:swap_index]
        # print(f'{number=}, length:{number_length}, {number_front=}')

        max_value = max(number_front)
        index = number_str.find(max_value)
        left_number = number_str[index+1:]
        return max_value, left_number

    for line in input_data:
        final_number = ''
        number=line
        while(len(final_number)<n_batteries):
            new_char, rest = find_max(number,n_batteries-len(final_number))
            # print(f'{new_char=},{rest=}')
            final_number = final_number + new_char
            number=rest

        print(f'{final_number=}')
        code += int(final_number)

    print(f'Part2 {code=}')