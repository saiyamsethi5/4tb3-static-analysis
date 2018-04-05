#nested_for_optimizer.py
#Final Project - Group Number: 10
#Requirements: identifies nested for loops and returns optimized output message

import collections

from output_message import output_message

from src.organized_dict import organized_dict


class nested_for_optimizer:
    code_dict = organized_dict(collections.OrderedDict())  # ordered dictionary containing line : code

    def __init__(self, code_dict):
        self.code_dict = code_dict

    #function that goes through the filtered dictionary and searches for a nested for - calls output message on find
    def search_for_optimization(self):
        for keys in self.code_dict:
            if ('for' in self.code_dict[keys] and 'range' in self.code_dict[keys]):
                # Found an if statement - now check if the next input stream is an else
                next_tuple = (self.code_dict.next_key(self.code_dict, keys))
                if ('for' in next_tuple[1] and 'range' in next_tuple[1]):
                    output_message.nested_for_msg(int(str(keys)), str(self.code_dict[keys]), next_tuple[1])
                    continue   #Found nested for loop - break out to avoid reading another for loop that is not nested