import math


def radix_base(values_to_sort, base):
    # validate args
    # -----
    if (values_to_sort is None) or (values_to_sort == []):
        raise ValueError("invalid arguments")
    if (base < 2):
        raise ValueError("invalid arguments")
    
    for element in values_to_sort:
        if not isinstance(element, int) or element < 0:
            raise ValueError("invalid list element")
    # -----

    max_val = max(values_to_sort)
    
    max_length = 0
    while max_val > 0:
        max_val = max_val // base
        max_length += 1

    for i in range(max_length):
        # set empty list of buckets for categorization
        buckets = [[] for _ in range(base)]

        # adding elements to their respective buckets
        for element in values_to_sort:
            # calculate where the digit placement is
            place = (element // base**i) % base
            print(element, place, i)

            # add to bucket
            buckets[place].append(element)

        # concatenate the buckets into one list
        values_to_sort = concat_list_elements(buckets)

    return values_to_sort


def concat_list_elements(array):
    new_list = []
    for innerlist in array:
        for ele in innerlist:
            new_list.append(ele)
    return new_list

print(radix_base([1, 9, 8, 7, 4, 5, 6561], 9))