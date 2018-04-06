#if_else_optimizer.py
#Final Project - Group Number: 10
#Requirements: identifies if else statements and returns optimized output message

import collections

from output_message import output_message

from organized_dict import organized_dict


class if_else_optimizer:
    code_dict = organized_dict(collections.OrderedDict())  #dictionary of line : code

    def __init__(self, code_dict):
        self.code_dict = code_dict

    #function that goes through the filtered dictionary and searches for an if else - calls output message on find
    def search_for_optimization(self):
        for keys in self.code_dict:
            if ('if' in self.code_dict [keys]):
                #Found an if statement - now check if the next input stream is an else
                next_tuple = (self.code_dict.next_key(self.code_dict, keys))
                try:
                    if ('else' in next_tuple[1]):
                        output_message.if_else_msg(int(str(keys)), str(self.code_dict[keys]), next_tuple[1])
                        continue   #Found else - break out to avoid reading another if/else that is not nested
                except IndexError:
                    print ("")