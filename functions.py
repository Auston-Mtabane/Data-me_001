# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    lst.reverse()
    return lst

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    return lst.count(element)

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    c = []
    for key in dct.keys():
        if dct[key] == value:
            c.append(key)
    
    return c

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    lst1 += lst2
    lst1.sort()
    return lst1

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    if len(numbers)< 2 or (len(numbers) == numbers.count(numbers[0])):
        return None
        
    numbers.sort()
    return numbers[-2]

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    str1 = list(str1)
    str2 = list(str2)
    str1.sort()
    str2.sort()
    
    
    return str1 == str2
    


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    c =[]
    for n in nested_list:
        try:
            # if len(n) == 1:
            #     c.append(n[0])
            #     continue
            if len(n):
                c+=flatten_list(n)
        except TypeError:
            c.append(n)
    return c
            
            


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    c = []
    for n in lst:
        if not (n in c):
            c.append(n)
        
    return c

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    c = []
    for n in lst1:
        if n in lst2:
            c.append(n)
    return c

