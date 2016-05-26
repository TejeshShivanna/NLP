# import statements
import string
from collections import Counter
from sys import argv
import os
import pickle
import math

# global variables
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone',
             'along',
             'already',
             'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another',
             'any',
             'anyhow', 'anyone', 'anything',
             'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes',
             'becoming', 'been', 'before', 'beforehand',
             'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but',
             'by',
             'call', 'can', 'cannot', 'cant', 'co', 'computer',
             'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during',
             'each',
             'eg', 'eight', 'either', 'eleven', 'else',
             'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere',
             'except', 'few', 'fifteen', 'fify', 'fill', 'find',
             'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full',
             'further', 'get', 'give', 'go', 'had', 'has', 'hasnt',
             'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herse"', 'him',
             'himse"', 'his', 'how', 'however', 'hundred', 'i',
             'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itse"', 'keep', 'last',
             'latter',
             'latterly', 'least', 'less', 'ltd', 'made', 'many',
             'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much',
             'must', 'my', 'myse"', 'name', 'namely', 'neither',
             'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now',
             'nowhere', 'of', 'off', 'often', 'on', 'once', 'one',
             'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own',
             'part',
             'per', 'perhaps', 'please', 'put', 'rather', 're',
             'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side',
             'since', 'sincere', 'six', 'sixty', 'so', 'some',
             'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take',
             'ten', 'than', 'that', 'the', 'their', 'them',
             'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon',
             'these',
             'they', 'thick', 'thin', 'third', 'this',
             'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top',
             'toward',
             'towards', 'twelve', 'twenty', 'two', 'un',
             'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever',
             'when',
             'whence', 'whenever', 'where', 'whereafter',
             'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who',
             'whoever', 'whole', 'whom', 'whose', 'why', 'will',
             'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves']


def PositiveTruthfulClass(priorprobofclass, vocabList, condpositivetruthful):
    priorProb = math.log(priorprobofclass)
    try:
        for word in vocabList:
            if word in condpositivetruthful:
                val = 0.0
                for i in range(0, vocabList[word]):
                    val = val + math.log(condpositivetruthful[word])
                priorProb = priorProb + val
    except Exception, e:
        pass
    return priorProb


def PositiveDeceptiveClass(priorprobofclass, vocabList, condpositivedeceptive):
    priorProb = math.log(priorprobofclass)
    try:
        for word in vocabList:
            if word in condpositivedeceptive:
                val = 0.0
                for i in range(0, vocabList[word]):
                    val = val + math.log(condpositivedeceptive[word])
                priorProb = priorProb + val
    except Exception, e:
        pass
    return priorProb


def NegativeTruthfulClass(priorprobofclass, vocabList, condnegativetruthful):
    priorProb = math.log(priorprobofclass)
    try:
        for word in vocabList:
            if word in condnegativetruthful:
                val = 0.0
                for i in range(0, vocabList[word]):
                    val = val + math.log(condnegativetruthful[word])
                priorProb = priorProb + val
    except Exception, e:
        pass
    return priorProb


def NegativeDeceptiveClass(priorprobofclass, vocabList, condnegativedeceptive):
    priorProb = math.log(priorprobofclass)
    try:
        for word in vocabList:
            if word in condnegativedeceptive:
                val = 0.0
                for i in range(0, vocabList[word]):
                    val = val + math.log(condnegativedeceptive[word])
                priorProb = priorProb + val
    except Exception, e:
        pass
    return priorProb


try:
    with open('nbmodel.txt', 'r') as f:
        dumpList = pickle.load(f)

    condpositivetruthful = dumpList[0]
    condpositivedeceptive = dumpList[1]
    condnegativetruthful = dumpList[2]
    condnegativedeceptive = dumpList[3]
    priorPositiveTruthfulClass = dumpList[4]
    priorPositiveDeceptiveClass = dumpList[5]
    priorNegativeTruthFulClass = dumpList[6]
    priorNegativeDeceptiveClass = dumpList[7]
    filePaths = []
    for dirName, subdirList, fileList in os.walk(argv[1]):
        for fname in fileList:
             if fname.endswith(".txt"):
                 if (fname == "README.txt"):
                     continue
                 fn = os.path.join(dirName, fname)
                 filePaths.append(fn)
    outFile = open("nboutput.txt", "w")
    for fileName in filePaths:
        with open(fileName, 'r') as myfile:
            line = myfile.read().replace('\n', '')

        line = line.translate(string.maketrans("", ""), string.punctuation)
        line = line.lower().strip()
        tokens = line.split(' ')
        tokens = filter(None, tokens)
        tokens = [x for x in tokens if x.isalpha()]
        oldDict = Counter(tokens)
        currDict = dict(
                (key, value)
                for key, value in oldDict.iteritems()
                if key not in set(stopwords)
        )
        ptclassprob = PositiveTruthfulClass(priorPositiveTruthfulClass, currDict, condpositivetruthful)
        pdclassprob = PositiveDeceptiveClass(priorPositiveDeceptiveClass, currDict,
                                             condpositivedeceptive)
        ntclassprob = NegativeTruthfulClass(priorNegativeTruthFulClass, currDict,
                                            condnegativetruthful)
        ndclassprob = NegativeDeceptiveClass(priorNegativeDeceptiveClass, currDict,
                                             condnegativedeceptive)
        if(pdclassprob>ptclassprob and pdclassprob>ntclassprob and pdclassprob>ndclassprob):
            labela = 'deceptive'
            labelb = 'positive'
        elif(ntclassprob>ptclassprob and ntclassprob>pdclassprob and ntclassprob>ndclassprob):
            labela = 'truthful'
            labelb = 'negative'
        elif(ndclassprob>ptclassprob and ndclassprob>pdclassprob and ndclassprob>ntclassprob):
            labela = 'deceptive'
            labelb = 'negative'
        else:
            labela = 'truthful'
            labelb = 'positive'
        outFile.write(labela + ' ' + labelb + ' ' + fileName + '\n')
    outFile.close()

except Exception, e:
    pass
