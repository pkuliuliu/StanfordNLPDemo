# -*- coding:utf-8 -*-
import os
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.parse import stanford


class StanfordParserTest(object):

    def __init__(self):
        self.parser = stanford.StanfordParser(model_path = "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

    def parse(self,sentence):
        tknzr = TweetTokenizer()
        res = self.parser.parse([' '.join(tknzr.tokenize(sentence))])
        return res

    def draw(self,sentence):
        res = self.parse(sentence)
        for elem in res:
            # print sentence
            elem.draw()

if __name__ == '__main__':
    sp = StanfordParserTest()
    sp.draw("The quick brown fox jumps over a lazy dog")


