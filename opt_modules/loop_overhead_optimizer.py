import collections
from organized_dict import organized_dict

class loop_overhead_optimizer:
    code_dict = organized_dict(collections.OrderedDict())  # dictionary of line : code

    def __init__(self, code_dict):
        self.code_dict = code_dict

    def search_for_optimization(self):
        for keys in self.code_dict:
            if ('for' in self.code_dict[keys] and 'range' in self.code_dict[keys]):
                print("For loop overhead can be optimized by using negative while on line: " + str(keys) + " - " + str(self.code_dict[keys]))
                break