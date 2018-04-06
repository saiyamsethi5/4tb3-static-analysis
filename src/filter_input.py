import collections

from organized_dict import organized_dict

# Dictionary of supported symbols and their appropriate outputs
optimized_symbs = ['if', 'else', 'for', '*']

class filter_input:
    code_dict = organized_dict(collections.OrderedDict())  # dictionary of line : code
    filtered_dict = organized_dict(collections.OrderedDict())  #dictionary of filtered code

    def __init__(self, code_dict):
        self.code_dict = code_dict

    def filter_keywords(self):

        for keys in self.code_dict:
            for symbs in optimized_symbs:
                if (symbs in self.code_dict [keys]):
                    self.filtered_dict [keys] = self.code_dict [keys]

        return (self.filtered_dict)