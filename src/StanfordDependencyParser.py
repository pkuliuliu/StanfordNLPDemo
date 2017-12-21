# -*- coding:utf-8 -*-

import os
from nltk.tokenize import TweetTokenizer
from nltk.parse import stanford


class StanfordDependencyParserTest(object):

    def __init__(self):
        self.parser = stanford.StanfordDependencyParser(model_path = "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

    def parse(self,sentence):
        tknzr = TweetTokenizer()
        res = self.parser.parse([' '.join(tknzr.tokenize(sentence))])
        return res

    def draw(self,sentence):
        res = self.parse(sentence)
        for elem in res:
            elem.tree().draw()

    def getDepandencyTreeInfo(self,sentence):
        res = self.parse(sentence)
        return str(res.next().tree())

    def otherInfo(self,sentence):
        res = self.parse(sentence)
        for row in list(res)[0].triples():
            print row
        # print [sentence.tree() for sentence in res]

if __name__ == '__main__':
    sdp = StanfordDependencyParserTest()
    sentence = "The quick brown fox jumps over a lazy dog"
    print sdp.getDepandencyTreeInfo(sentence)
    sdp.draw(sentence)
