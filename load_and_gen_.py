import numpy as np
import pickle
import pandas as pd
import random
import tweepy
import time

class MarkovGenLoad:

    def __init__(self, dictpath, msg_len):
        """
        :param dictpath:
        """

        self.dictpath = dictpath
        self.msg_len = msg_len

    def load_model(self):
        """

        :return:
        """
        with open(self.dictpath, 'rb') as dictpath:
            self.model = pickle.load(dictpath)
        return self.model

    def generate_text(self, model):
        state = random.choice(list(model))
        out = list(state)
        for i in range(self.msg_len):
            out.extend(random.choices(list(model[state]), model[state].values()))
            state = state[1:] + out[-1]
        msg = ''.join(out)
        return msg


def main():

    mar = MarkovGenLoad('songdict.pkl', 120)
    model = mar.load_model()
    #consumer_key, consumer_secret, access_token, access_token_secret = mar.tweetgen()
    auth = tweepy.OAuthHandler("XXXXXXXXXXXX", "XXXXXXXXXXXXX")
    auth.set_access_token("XXXXX-XXXXXXXXXXX", "XXXXXXXXXXXXXX")
    api = tweepy.API(auth)
    for i in range(10):
        text = mar.generate_text(model)
        print(text)
        api.update_status(status=  text )


if __name__ == "__main__":

    main()
