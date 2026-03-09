

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

    
        