# -*- coding: utf-8 -*-
import math
import pickle
import time
from sys import argv
script, fileName = argv

transitionCount = {}
emissionCount = {}
tagCount = {}
distinctTags = {}
wordTags = {}


#read from hmmmodel.txt
def readFromModel():
    global transitionCount
    global emissionCount
    global distinctTags
    global tagCount
    global wordTags
    inputfile = open('hmmmodel.txt', 'r')
    transitionCount, emissionCount, tagCount, distinctTags, wordTags  = pickle.load(inputfile)
    inputfile.close()


def printOutput(tags, newline):
    tags.reverse()
    output = []
    #wordsInSentence = newline.split()
    for i in range(0, len(tags), 1):
        output.append(''.join([newline[i], '/', tags[i]]))
    outputFile.write(' '.join(output))
    outputFile.write('\n')


try:
    #starttime = time.time()
    readFromModel()
    vocabSize = float(len(distinctTags))
    devFile = open(fileName, 'r')
    outputFile = open('hmmoutput.txt', 'w')
    #forward step
    for newline in devFile:
        words = newline.split(" ")
        words = words[:len(words)-1]
        words.append('.')
        sentenceLength = len(words)
        best_score = {}
        best_edge = {}
        best_score['0 <S>'] = 0
        best_edge['0 <S>'] = None
        for i in range(0, sentenceLength, 1):
            if words[i] in wordTags:
                lst = wordTags[words[i]]
            else:
                lst = distinctTags
            for prev in distinctTags:
                tran = ''.join([repr(i), ' ', prev])
                for next in lst:
                    prevnext = ''.join([prev, ' ', next])
                    if tran in best_score and prevnext in transitionCount:
                        tVal = ((transitionCount[prevnext]+1)/(tagCount[prev]+vocabSize))
                        nextword = ''.join([next, ' ', words[i]])
                        if nextword in emissionCount:
                            emVal = (emissionCount[nextword]/(tagCount[prev]+vocabSize))
                        else:
                            emVal = 1
                        score = best_score[tran] - math.log(tVal) - math.log(emVal)
                        trannext = ''.join([repr((i+1)), ' ', next])
                        if trannext not in best_score or best_score[trannext] > score:
                            best_score[trannext] = score
                            best_edge[trannext] = tran
        next = '</S>'
        for prev in distinctTags:
            tran = ''.join([repr(i), ' ', prev])
            prevnext = ''.join([prev, ' ', next])
            if tran in best_score and prevnext in transitionCount:
                tVal = ((transitionCount[prevnext]+1)/(tagCount[prev]+vocabSize))
                score = best_score[tran] - math.log(tVal)
                trannext = ''.join([repr((i+1)), ' ', next])
                if trannext not in best_score or best_score[trannext] > score:
                    best_score[trannext] = score
                    best_edge[trannext] = tran

        #backward step
        tags = []
        ls = list(wordTags[words[i]])
        tags.append(ls[0])
        next_edge = best_edge[''.join([repr(i+1), ' ', '</S>'])]
        while next_edge != "0 <S>":
            edge = next_edge.split(' ')
            tags.append(edge[1])
            next_edge = best_edge[next_edge]
        printOutput(tags, words)
    devFile.close()
    outputFile.close()
    #print time.time() - starttime
except Exception, ex:
    print ex
    print 'error'