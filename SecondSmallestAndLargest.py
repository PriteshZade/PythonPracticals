smallest = float('inf')
second_smallest = float('inf')
largest = float('-inf')
second_largest = float('-inf')

def update_values(elem):
    global smallest, second_smallest, largest, second_largest
    if elem < smallest:
        second_smallest = smallest
        smallest = elem
    elif smallest < elem < second_smallest:
        second_smallest = elem

    if elem > largest:
        second_largest = largest
        largest = elem
    elif largest > elem > second_largest:
        second_largest = elem

def process_collection(L):
    for item in L:
        if isinstance(item, (list, tuple, set)):
            process_collection(item)
        elif isinstance(item, dict):
            process_collection(item.values())
            process_collection(item.keys())
        elif isinstance(item, int):
            update_values(item)

def get_second_smallest_second_largest(L):
    process_collection(L)
    return (second_smallest if second_smallest != float('inf') else None,
            second_largest if second_largest != float('-inf') else None)

result = get_second_smallest_second_largest((7, 8,{7:1}, 2, 6, 4, 3, 12, 89, 4, 7))
print(result) 
