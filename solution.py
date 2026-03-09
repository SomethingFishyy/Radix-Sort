def radix_base(values_to_sort, base):
    # validate args
    # -----
    if (values_to_sort is None) or (values_to_sort == []):
        raise ValueError("invalid arguments")
    if (base < 2):
        raise ValueError("invalid arguments")
    
    for element in values_to_sort:
        if element < 0:
            raise ValueError("invalid list element")
        try:
            element % base
        except (TypeError):
            raise ValueError("invalid list element")
    # -----

    max_length = length_of_largest(values_to_sort)

    for i in range(max_length):
        # set empty list of buckets for categorization
        buckets = [[] for _ in range(base)]

        # adding elements to their respective buckets
        for element in values_to_sort:
            # calculate where the digit placement is
            place = (element // base**i) % base

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


def length_of_largest(array):
    length = 0
    for element in array:
        if len(str(element)) > length:
            length = len(str(element))
    return length

print(radix_base([50, 30, 20, 18, 600, 1, 3], 15))