# -*- coding:utf-8 -*-

from nltk.tokenize import TweetTokenizer
from StanfordDependencyParser import StanfordDependencyParserTest


class Generalizer(object):

    def __init__(self):

        self.__source = ["jumpys over"]
        self.__dpt = StanfordDependencyParserTest()
        return

    def generalize(self,sentence):

        chunks, nonchunks = self.getChunk(sentence)
        dependencyInfo = self.__dpt.getDepandencyTreeInfo(sentence)
        # print dependencyInfo

        for idx in nonchunks:
            subString = nonchunks.get(idx)
            # get center word
            centerWord = ''
            centerIdx = 1000
            tknzr = TweetTokenizer()

            for word in tknzr.tokenize(subString):
                tmpIdx = dependencyInfo.index(word)
                if tmpIdx<centerIdx:
                    centerIdx = tmpIdx
                    centerWord = word

            nonchunks[idx] = centerWord
            # change word to its generalized word
        keys = []
        keys.extend(chunks.keys())
        keys.extend(nonchunks.keys())

        # print chunks.keys()
        # print nonchunks.keys()
        keys.sort()
        # print keys

        res = str()
        for key in keys:
            if chunks.has_key(key):
                res += chunks.get(key) + ' '
            else:
                res += nonchunks.get(key) + ' '

        return res

    def getChunk(self,sentence):

        chunks = dict()# idx,subString
        chunks[1] = 'jumpys over'

        nonchunks = dict()
        nonchunks[0] = 'the quick brown fox'
        nonchunks[2] = 'a lazy dog'
        return chunks, nonchunks

if __name__ == '__main__':

    generalizer = Generalizer()
    sentence = "the quick brown fox jumpys over a lazy dog"
    print sentence
    print generalizer.generalize(sentence)
