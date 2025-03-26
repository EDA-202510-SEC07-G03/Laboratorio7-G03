from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al
import DataStructures.Map.map_functions as map
import DataStructures.Map.map_entry as ent
import random as m

def new_map(num_elements, load_factor, prime=109345121):
    my_map = sl.new_list()
    my_map["prime"] = prime
    my_map["capacity"] = map.next_prime(num_elements/load_factor)
    my_map["scale"] = 1
    my_map["shift"] = 0
    my_map["table"] = al.new_list()
    for i in range(my_map["capacity"]):
        al.add_last(my_map["table"], sl.new_list())
    my_map["current_factor"] = 0
    my_map["limit_factor"] = load_factor
    my_map["size"] = 0
    return my_map

def put(my_map,key,value):
    hash = map.hash_value(my_map, key)
    if key == my_map["table"]["elements"][hash][]
    sl.add_last(my_map["table"]["elements"][hash],value)
    my_map["size"] += 1
    #if my_map["size"]/my_map["capacity"] > my_map["limit_factor"]:
    #    rehash(my_map)
    return my_map