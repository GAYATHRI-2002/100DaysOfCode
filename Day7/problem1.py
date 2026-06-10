"""
Write a function that merges two dictionaries.
If a key exists in both dictionaries, sum their values.
If a key exists in only one, include it as is.
"""
def merge_dictionaries(dict_a, dict_b):
    result = dict_a.copy()
    for key, value in dict_b.items():
        result[key]=result.get(key, 0) + value
    return result

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}
final_ans = merge_dictionaries(dict_a,dict_b)
print(final_ans)