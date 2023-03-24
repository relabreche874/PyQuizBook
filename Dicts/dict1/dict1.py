import collections
def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    return dict(zip(keys, values))

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    return collections.ChainMap(d1, d2)
    # return d1 | d2


def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    return {i: d1 for i in lst}


def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    return {i: datadict[i] for i in keylist}

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for k in keylist:
        datadict.pop(k)

    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    pass

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    pass