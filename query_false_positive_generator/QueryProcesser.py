import Vars as vr


# doc_vector is one doc vector - like DOC1
def is_false_positive(elem_list, doc_vector):
    ret = True
    for elem in elem_list:
        ret = ret and (elem in doc_vector)
    #print(elem, doc_vector, elem not in doc_vector)
    return not ret


# hash represents the particular hash of the document
def match_hash(elem_list, hash_dict, doc_hash):
    all_elem_hash = 0
    for elem in elem_list:
        all_elem_hash |= hash_dict[elem]
    return (all_elem_hash & doc_hash) > 0


# hash_dict represents the particular hash function dictionary
# doc_list represents the list of all documents
# doc_hash_list represents the hash for each document for corresponding hash_dict
def get_query_false_positives(query, hash_dict, doc_list, doc_hash_list):
    fp = 0
    for elem_list in query:
        for doc_number in range(len(doc_list)):
            if match_hash(elem_list, hash_dict, doc_hash_list[doc_number]) and is_false_positive(elem_list,
                                                                                                 doc_list[doc_number]):
                fp += 1
    #print(query, hash_dict, doc_hash_list, fp)
    return fp


# hash_dict represents the particular hash function dictionary
# doc_list represents the list of all documents
# doc_hash_list represents the hash for each document for corresponding hash_dict
def get_false_positives_for_all_queries(all_queries, hash_dict, doc_list, doc_hash_list):
    total_fp = 0
    for query in all_queries:
        total_fp += get_query_false_positives(query, hash_dict, doc_list, doc_hash_list)
    print(hash_dict, doc_hash_list, total_fp)
    return total_fp