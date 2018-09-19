import Vars as vr


def add_elem_to_hash_set(hash_set, elem):
    new_hash_set = []
    for set in hash_set:
        for new_hash in range(2, 6, 2):
            new_set_1 = dict(set)
            new_set_1[elem] = new_hash
            new_hash_set.append(new_set_1)
    return new_hash_set


def construct(hash_set, elem_set, index = 0):
    if index == len(elem_set):
        return hash_set
    else:
        return construct(add_elem_to_hash_set(hash_set, elem_set[index]), elem_set, index+1)


def generate_all_hash():
    return construct(vr.BASIC_HASH_SET, vr.ELEM_LIST)

