def generate_doc_hash(doc_vector, hash_dict):
    doc_hash = 0
    for elem in doc_vector:
        doc_hash |= hash_dict[elem]
    return doc_hash


def generate_all_doc_hash(doc_list, hash_dict):
    return [generate_doc_hash(doc, hash_dict) for doc in doc_list]