from xml.dom.expatbuilder import parseString


## Think SLICING for many of these.

def create_list_from_tuple(t):
    """
    This function takes a tuple of elements and returns a list containing those elements of the tuple.
    """
    return list(t)
    
def drop_last(lst):
    """
    This function takes a list and returns a list with the last item removed.
    """
    return lst[:-1]


def drop_first_two(lst):
    """
    This function takes a list and returns a list with the first two items removed.
    """
    return lst[2:]

def drop_mangle(lst):
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """
    return lst[2:-1]

def add_item_front(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """
    lst.insert(0, a)
    return lst

    # return [a] + lst
def add_item_end(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """
    lst.append(a)
    return lst

    # return lst + [a]

def add_list_to_list(lsta, lstb):
    """
    This function takes two lists and appends one to the other,
    returning a list
    """
    return lsta + lstb

def list_and_list_to_tuple(lsta, lstb):
    """
    This function takes two lists and returns a tuple containing the two lists
    """
    return lsta,lstb

    # return tuple([lsta, lstb])

def list_and_list_to_list(lsta, lstb):
    """
    This function takes two lists and returns a list containing the two lists
    """
    return [lsta, lstb]

##
##
##

def list_from_range(n):
    """
    This function returns list with 0..n as integers in a list
    """
    return list(range(n))

def list_from_range2(n, m):
    """
    This function returns list with n..m (without m) as integers in a list
    """
    return list(range(n,m))

def list_from_range3(n, m):
    """
    This function returns list with n..m (including m(!)) as integers in a list
    """
    return list(range(n, m + 1))

def list_from_range4(n, m):
    """
    This function returns list with n..m (WITHOUT n and including m) as integers in a list
    """
    return list(range(n + 1, m + 1))

def list_from_range_by(n, step):
    """
    This function returns list with 0..n as integers by step in a list
    (read the test)
    """
    return list(range(0, n, step))

def rev_list(lst):
    """
    This function returns list which is a reverse of the argument list
    (read the test)
    """
    return lst[::-1]
  
def concat_list_indexwise(lst1, lst2):
    """
    Write a program to add two lists index-wise. 
    Create a new list that contains the 0th index item from both the list, 
    then the 1st index item, and so on till the last element. 
    Any leftover items will get added at the end of the new list.
    """
    return list(zip(lst1, lst2))

def square_each_item(lst):
    """
    This function returns list which each item in argument list has been squared
    (read the test)
    """
    return lst ** 2

def remove_empty_strs(lst):
     """
     Remove empty strings from the list of strings
     """
     pass


def remove_item_from(lst, aaa):
    """
    Remove all occurrences of a specific item from a list.
    """
    pass

def leave_item_in(lst, aaa):
    """
    Leave all occurrences of a specific item in a list.
    """
    pass

def length_of(lst):
    """
    return the length of the list
    """
    pass