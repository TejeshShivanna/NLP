# -*- coding: utf-8 -*-
import pickle
from sys import argv
script, fileName = argv
try:
    inputFile = open(fileName)
    transitionCount = {}
    emissionCount = {}
    tagCount = {}
    distinctTags = set()
    wordTags = {}
    lineCount = 0
    for line in inputFile:
        lineCount += 1
        prev = '<S>'
        for observation in line.split():
            word = observation[:len(observation) - 3]
            tag = observation[len(observation) - 2:]
            if word not in wordTags:
                lst = set()
                lst.add(tag)
                wordTags[word] = lst
            else:
                lst = wordTags[word]
                if tag not in lst:
                    lst.add(tag)
                    wordTags[word] = lst
            distinctTags.add(tag)
            if tag not in tagCount:
                tagCount[tag] = 1.0
            else:
                tagCount[tag] += 1.0
            transition = ''.join([prev, ' ', tag])
            emission = ''.join([tag, ' ', word])
            if transition not in transitionCount:
                transitionCount[transition] = 1.0
            else:
                transitionCount[transition] += 1.0

            if emission not in emissionCount:
                emissionCount[emission] = 1.0
            else:
                emissionCount[emission] += 1.0
            prev = tag
        lineEnd = ''.join([prev, ' ', '</S>'])
        if lineEnd not in transitionCount:
            transitionCount[lineEnd] = 1.0
        else:
            transitionCount[lineEnd] += 1.0
    for tag1 in distinctTags:
        start = ''.join(['<S>', ' ', tag1])
        end = ''.join([tag1, ' ', '</S>'])
        if start not in transitionCount:
            transitionCount[start] = 0
        if end not in transitionCount:
            transitionCount[end] = 0
        for tag2 in distinctTags:
            tagSequence = ''.join([tag1, ' ', tag2])
            if tagSequence not in transitionCount:
                transitionCount[tagSequence] = 0

    distinctTags.add('<S>')
    distinctTags.add('</S>')
    tagCount['<S>'] = lineCount
    outputFile = open('hmmmodel.txt', 'w')
    pickle.dump([transitionCount, emissionCount, tagCount, distinctTags, wordTags], outputFile)
    outputFile.close()
except Exception, ex:
    print ex
    print 'error'