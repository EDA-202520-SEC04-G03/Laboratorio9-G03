# priority_queue.py

from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def new_heap(is_min_pq=True):
    queue = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": default_compare_lower_value if is_min_pq else default_compare_higher_value
    }
    al.add_last(queue["elements"], None)
    return queue

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    return my_heap["size"] == 0

def swim(my_heap, pos):
    elements = my_heap["elements"]
    cmp_function = my_heap["cmp_function"]

    while pos > 1:
        parent_pos = pos // 2
        
        child_node = al.get_element(elements, pos)
        father_node = al.get_element(elements, parent_pos)
        
        if not cmp_function(father_node, child_node):
            al.exchange(elements, pos, parent_pos)
            pos = parent_pos
        else:
            pos = 0 

    return my_heap

def insert(my_heap, priority, value):
    new_entry = pqe.new_pq_entry(priority, value)
    al.add_last(my_heap["elements"], new_entry)
    my_heap["size"] += 1
    new_pos = my_heap["size"]
    my_heap = swim(my_heap, new_pos)
    return my_heap