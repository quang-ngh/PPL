def comprehension_flatten(lst):

    return [x for one_lst in lst for x in one_lst]

def recursive_flatten(lst):

    if len(lst) == 0:
        return []
    else:
        return lst[0] + recursive_flatten(lst[1:])

def high_order_flatten(lst):

    return list(map(comprehension_flatten(lst), lst))


input = [[1,2,3], ['a','b','c'], [1.1, 2.1, 3.1]]

print("Comprehension: {}".format(comprehension_flatten(input)))
print("Recursive: {}".format(recursive_flatten(input)))
print("High order: {}".format(high_order_flatten(input)))
