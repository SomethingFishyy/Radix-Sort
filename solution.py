

def radix_base(values_to_sort, base):
    # validate args
    # -----
    if (values_to_sort is None) or (values_to_sort == []):
        raise ValueError("invalid arguments")
    if (base < 2):
        raise ValueError("invalid arguments")
    
    try:
        for element in values_to_sort:
            element % base
    except:
        raise ValueError("invalid list element")
    # -----

    # debug
    print("vts:", values_to_sort)
    print("base:", base)

    temp_list = [[] for _ in range(base)]
    max_length = max_int_length(values_to_sort)

    for i in range(max_length):
        # add elements to their respective buckets
        for element in values_to_sort:
            temp_element = element
            for n in range(i):
                temp_element = temp_element // base
            place = temp_element % base
            temp_list[place].append(element)

        # concatenate the buckets into one list
        values_to_sort = concat_list_elements(temp_list)
        temp_list = [[] for _ in range(base)]

    return values_to_sort


def concat_list_elements(array):
    new_list = []
    for innerlist in array:
        for ele in innerlist:
            new_list.append(ele)
    return new_list


def max_int_length(array):
    l = 0
    for element in array:
        if len(str(element)) > l:
            l = len(str(element))
    return l

print(radix_base([1011, 110, 101], 2))

        