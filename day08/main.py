#!/bin/env/python3
from copy import deepcopy
import math

def read_input(file_path):
    with open(file_path, 'r') as file:
        # return [char for char in  ]
        lines = [line.strip() for line in file.readlines()]
        data = []
        for line in lines:
            fields=[int(a.strip()) for a in line.split(',')]
            data.append({'circuit' : -1, 'pos': tuple(fields)})
        return data
    
def distance(list_a,list_b):
    x = list_a[0] - list_b[0]
    y = list_a[1] - list_b[1]
    z = list_a[2] - list_b[2]
    return math.sqrt(x**2 + y ** 2 + z ** 2)
    
def generate_connection_pairs(_data, n_pairs):
    data = deepcopy(_data)
    pairs=[]
    size = len(data)
    circuits = []
    n_circuit = 0
    n_connections = 0 
    last_min_dist = 0
    while n_connections < n_pairs:
        print(f'{n_connections=}')
        min_dist = 1e9 
        selected_pair = None
        for i in range(size):            
            for j in range(i,size):
                if i == j:
                    continue
                juntion_i = data[i]
                juntion_j = data[j]
                dist = distance(juntion_i['pos'],juntion_j['pos'])
                if dist < min_dist and dist > last_min_dist: 
                    min_dist = dist
                    selected_pair = (juntion_i, juntion_j)
        
        juntion_i , juntion_j = selected_pair
        last_min_dist = min_dist
        n_connections+=1

        if juntion_i['circuit'] != -1 and juntion_j['circuit'] == -1: 
            juntion_j['circuit'] = juntion_i['circuit']
        elif juntion_j['circuit'] != -1 and juntion_i['circuit'] == -1:
            juntion_i['circuit'] = juntion_j['circuit']
        elif juntion_i['circuit'] == -1 and juntion_j['circuit'] == -1:
            juntion_i['circuit'] = n_circuit
            juntion_j['circuit'] = n_circuit
            n_circuit+=1
        elif juntion_i['circuit'] == juntion_j['circuit']:
            pass
        else: 
            print('mix_groups')
            appended_circuit = juntion_i['circuit'] 
            removed_circuit = juntion_j['circuit']
            for juntion in data:
                if juntion['circuit'] == removed_circuit:
                    juntion['circuit'] = appended_circuit

    return data

def all_1_circuit(data):
    circuits = data[0]['circuit']
    for junction in data:
        if junction['circuit'] != circuits:
            return False
    return True

def generate_connection_pairs2(_data, n_pairs):
    data = deepcopy(_data)
    pairs=[]
    size = len(data)
    circuits = []
    n_circuit = 0
    n_connections = 0 
    last_min_dist = 0
    selected_pair = None
    while n_connections < n_pairs or not all_1_circuit(data) :
        print(f'{n_connections=}')
        min_dist = 1e9 
        selected_pair = None
        for i in range(size):            
            for j in range(i,size):
                if i == j:
                    continue
                juntion_i = data[i]
                juntion_j = data[j]
                dist = distance(juntion_i['pos'],juntion_j['pos'])
                if dist < min_dist and dist > last_min_dist: 
                    min_dist = dist
                    selected_pair = (juntion_i, juntion_j)
        
        juntion_i , juntion_j = selected_pair
        last_min_dist = min_dist
        n_connections+=1

        if juntion_i['circuit'] != -1 and juntion_j['circuit'] == -1: 
            juntion_j['circuit'] = juntion_i['circuit']
        elif juntion_j['circuit'] != -1 and juntion_i['circuit'] == -1:
            juntion_i['circuit'] = juntion_j['circuit']
        elif juntion_i['circuit'] == -1 and juntion_j['circuit'] == -1:
            juntion_i['circuit'] = n_circuit
            juntion_j['circuit'] = n_circuit
            n_circuit+=1
        elif juntion_i['circuit'] == juntion_j['circuit']:
            pass
        else: 
            print('mix_groups')
            appended_circuit = juntion_i['circuit'] 
            removed_circuit = juntion_j['circuit']
            for juntion in data:
                if juntion['circuit'] == removed_circuit:
                    juntion['circuit'] = appended_circuit
    print(f'Part2 code={selected_pair[0]['pos'][0] * selected_pair[1]['pos'][0] }')
    return data

def group_by_circuit(juntion_data):
    circuits={}
    for juntion in juntion_data:
        if circuits.get(juntion['circuit']) is None:
            circuits[juntion['circuit']] = []
        circuits[juntion['circuit']].append(juntion)
    return circuits

    

def multiply(list):
    out = 1
    for number in list:
        out *= number
    return out
if __name__ == "__main__":
    # part 1 
    
    # filename, n_connections ='inputs/example1.txt', 10
    filename, n_connections ='inputs/input.txt', 1000

    input_data = read_input(filename)
    data_dict = generate_connection_pairs(input_data, n_connections)
    circuits = group_by_circuit(data_dict)
    circuit_lengths=[]
    for id, circuit in circuits.items():
        
        if id != -1 :
            circuit_lengths.append(len(circuit))
            print(circuit)
    
    circuit_lengths.sort(reverse=True)
    print(circuit_lengths[:3])
# 
    code =  multiply(circuit_lengths[:3])
    print(f'Part1 {code=}')
        
    # part 2 
    code =  0
    data_dict = generate_connection_pairs2(input_data, n_connections)
    