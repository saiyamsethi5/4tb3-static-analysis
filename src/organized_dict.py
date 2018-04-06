#organized_dict.py
#Final Project - Group Number: 10
#Requirements: wrapper on top of the OrderedDict class - used for creating the next_key function

import collections

class organized_dict(collections.OrderedDict):
    #Returns the next key in a provided ordered dictionary
    def next_key(self, code_dict, key):
        items = list(code_dict.items())
        #print (items)

        for tuples in items:
            try:
                if (key == tuples[0]):
                    indexOf = items.index(tuples)
                    return (items[indexOf + 1])
            except IndexError:
                return ""



