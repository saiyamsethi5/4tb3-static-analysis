import collections

class organized_dict(collections.OrderedDict):

    def next_key(self, code_dict, key):
        items = list(code_dict.items())
        #print (items)

        for tuples in items:
            if (key == tuples[0]):
                indexOf = items.index(tuples)
                break;

        return (items[indexOf + 1])

