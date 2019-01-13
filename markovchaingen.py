import os
from pprint import pprint
import json
import codecs
import re
from collections import defaultdict, Counter
import random
import sys
import pandas as pd


class MarkovChainGen:

    def __init__(self, state_len, msg_len, filepath):
        
        """
        :param state_len:
        :param msg_len:
        :param datafile:
        """

        self.state_len = state_len
        self.msg_len = msg_len
        self.filepath = filepath

    def load_dataset(self):
        self.textfile = pd.read_csv(self.filepath, sep = "|")['title']
        return self.textfile

    def preprocess(self):
        self.textfile = self.load_dataset()
        self.textfile = [x for x in self.textfile if len(x) > 3]
        self.textfile = ' '.join(re.sub('[^A-za-z]', ' ', el) for el in self.textfile)
        return self.textfile

    def build_dict(self):

        model = defaultdict(Counter)
        for i in range(len(self.textfile) - self.state_len):
            state = self.textfile[i:i + self.state_len]
            nstate = self.textfile[i + self.state_len]
            model[state][nstate] += 1

        return model

    def generate_text(self, model):
        state = random.choice(list(model))
        out = list(state)
        for i in range(self.msg_len):
            out.extend(random.choices(list(model[state]), model[state].values()))
            state = state[1:] + out[-1]
        msg = ''.join(out)
        return msg


if __name__ == '__main__':

