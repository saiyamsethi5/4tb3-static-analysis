import collections
from organized_dict import organized_dict
from output_message import output_message

class if_else_optimizer:
    code_dict = organized_dict(collections.OrderedDict())  #dictionary of line : code

    def __init__(self, code_dict):
        self.code_dict = code_dict

    def search_for_optimization(self):
        for keys in self.code_dict:
            if ('if' in self.code_dict [keys]):
                #Found an if statement - now check if the next input stream is an else
                next_tuple = (self.code_dict.next_key(self.code_dict, keys))
                if ('else' in next_tuple[1]):
                    output_message.if_else_msg(int(str(keys)), str(self.code_dict[keys]), next_tuple[1])