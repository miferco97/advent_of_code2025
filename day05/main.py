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

class Range():
    def __init__(self, lower, higher):
        self.lower = lower
        self.higher = higher

    def has_inside(self, id):
        return test_in_range(id,[self.lower,self.higher])

    def __repr__(self):
        return f'{self.lower}-{self.higher}'

    def __len__(self):
        return self.higher - self.lower + 1

        
    
if __name__ == "__main__":
    # id_ranges, ids = read_input('inputs/input.txt')
    id_ranges, ids = read_input('inputs/example1.txt')

    # part 1 
    code = 0
    for id in ids:
        for id_range in id_ranges:
            if test_in_range(id,id_range):
                code += 1
                # print(f'{id=} within {id_range=}')
                break
    
    print(f'Part1 {code=}')
        
    # part 2 
    valid_ranges = []

    for lower, higher in id_ranges:
        lower_within , higher_within = None, None
        for i, valid_range in enumerate(valid_ranges):
            if valid_range.has_inside(lower):
                lower_within = (i, valid_range)

            elif valid_range.has_inside(higher):
                higher_within = (i, valid_range)


        if not lower_within and not higher_within:
                # create a new range
                new_range = Range(lower,higher)

                ## add it sorted within the valid_ranges if it encloses any range in between remove them before inserting
                min_index, max_index = 0 , 0
                for index, rang in enumerate(valid_ranges):
                    if rang.lower < lower:
                        min_index = index+1
                    if rang.higher < higher:
                        max_index = index+1
                
                if  max_index < min_index:
                    raise Exception('not possible')
                elif max_index == min_index:
                    valid_ranges.insert(min_index,new_range)
                else:
                    indexes=list(range(min_index,max_index))
                    indexes.reverse()
                    for index in indexes:
                        valid_ranges.pop(index)
                    valid_ranges.insert(indexes[-1],new_range)

                continue
        
        if lower_within and higher_within:

            index_lower, range_lower = lower_within
            index_higher, range_higher = higher_within
            new_range = Range(range_lower.lower,range_higher.higher)

            lower_index_to_remove=min(index_higher,index_lower)
            higher_index_to_remove=max(index_higher,index_lower)

            ids_to_remove = list(range(lower_index_to_remove,higher_index_to_remove+1))
            if len(ids_to_remove) > 2:
                print(f'{ids_to_remove=}')

            ids_to_remove.reverse()
            for i in  ids_to_remove:
                valid_ranges.pop(i)
                
            valid_ranges.insert(ids_to_remove[-1],new_range)
            continue

        if lower_within:
            index, lower_range = lower_within
            if higher > lower_range.higher:
                lower_range.higher = higher
        
        if higher_within:
            index, higher_range = higher_within
            if lower < higher_range.lower:
                higher_range.lower = lower
        
    
    # print(f'{valid_ranges=}')

    code = sum([len(x) for x in valid_ranges ])

    print(f'Part2 {code=}')