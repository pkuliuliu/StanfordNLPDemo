# -*- coding:utf-8 -*-
from nltk.tokenize import TweetTokenizer
from nltk.tag.stanford import StanfordPOSTagger


class PosTaggerTest(object):

    def __init__(self):
        self.eng_tagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')

    def tag(self,sentence):
        tknzr = TweetTokenizer()
        res = self.eng_tagger.tag([' '.join(tknzr.tokenize(sentence))])
        return res

    def show(self,sentence):
        res = dict(self.tag(sentence))
        for key in res:
            # print sentence
            print key,"\t",res[key]

if __name__ == '__main__':
    pt = PosTaggerTest()
    pt.show("The quick brown xiaoming jumps over a lazy dog")


