#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys
import os
from itertools import izip
from collections import defaultdict
from collections import Counter

clipCount = defaultdict(float)
totalCount = defaultdict(float)
r = 0.0
c = 0.0

def generatengram(sentence, n):
    words = sentence.split()
    if (n == 1):
        return words
    ngramlist = []
    for i in range(len(words) - 1):
        word = []
        for j in range(n):
            if ((i + j) < len(words)):
                word.append(words[i + j])
        if (len(word) == n):
            ngramlist.append(' '.join(word))
    return ngramlist

def calculatePrecision(candidate, reference, n):
    global c
    global r
    referencelengths = []
    referencengrams = []
    candidateLength = len(candidate.split())
    candidatengrams = generatengram(candidate, n)

    if type(reference) is tuple:
        for referenceSentence in reference:
            referenceSentence = referenceSentence.rstrip()
            referencelengths.append(len(referenceSentence.split()))
            ngramlist = generatengram(referenceSentence, n)
            for item in ngramlist:
                referencengrams.append(item)
    else:
        referenceSentence = reference.rstrip()
        referencelengths.append(len(referenceSentence.split()))
        ngramlist = generatengram(referenceSentence, n)
        for item in ngramlist:
            referencengrams.append(item)

    r += min(referencelengths, key=lambda x: abs(candidateLength - x))
    c += candidateLength
    referenceCounter = Counter(referencengrams)
    candidateCounter = Counter(candidatengrams)

    for item in candidateCounter:
        cCount = rCount = 0.0
        cCount = candidateCounter[item]
        rCount = referenceCounter[item]
        totalCount[n] += cCount
        clipCount[n] += min(cCount, rCount)


try:
    candidateFile = open(sys.argv[1], 'rb')
    referenceName = sys.argv[2]
    if '.txt' in referenceName:
        referenceFile = open(referenceName, 'rb')
        for candidateLine, referenceLine in izip(candidateFile, referenceFile):
            for n in range(1, 5):
                calculatePrecision(candidateLine.rstrip(), referenceLine.rstrip(), n)
    else:
        for root, dirs, files in os.walk(referenceName):
            referencefiles = [open(''.join([referenceName, file]), 'rb') for file in files if file.endswith('.txt')]
            candidateLines = []
            for candidateLine in candidateFile:
                candidateLines.append(candidateLine.rstrip())
            linenumber = 0
            for referencelines in izip(*referencefiles):
                for n in range(1, 5):
                    calculatePrecision(candidateLines[linenumber], referencelines, n)
                linenumber += 1

    candidateFile.close()
    logprecision = 0.0

    for i in range(1, 5):
      logprecision += math.log(clipCount[i] / totalCount[i])

    bleuscore = math.exp(((0.25)*logprecision) + min(1 - r / c, 0))
    outputfile = open('bleu_out.txt', 'w')
    outputfile.write(str(bleuscore))
    outputfile.close()
except Exception, ex:
    print ex