from DataStructures.List import array_list as al
import DataStructures.Map.map_functions as map
import DataStructures.Map.map_entry as ent
import random as m

def new_map(num_elements, load_factor, prime=109345121):
    my_table =  al.new_list()
    my_table["prime"] = prime
    my_table["capacity"] = map.next_prime(num_elements/load_factor)
    my_table["scale"] = m.randint(1, prime - 1)
    my_table["shift"] = m.randint(0, prime - 1)
    my_table["table"] = al.new_list()
    for i in range(my_table["capacity"]):
        al.add_last(my_table["table"],ent.new_map_entry(None,None))
        my_table["table"]["size"] += 1
    my_table["current_factor"] = 0
    my_table["limit_factor"] =  load_factor
    return my_table
