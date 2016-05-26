# import statements
import string
from collections import Counter
from sys import argv
import os
import pickle

# global variables
vocabularyList = []
documentsCountDict = {'positivetruthful': 0, 'positivedeceptive': 0, 'negativetruthful': 0, 'negativedeceptive': 0}
priorProbabilityDict = {'positivetruthfulclass': 0.0, 'positivedeceptiveclass': 0.0, 'negativetruthfulclass': 0.0,
                        'negativedeceptiveclass': 0.0}
positivetruthfuldict = {}
positivedeceptivedict = {}
negativetruthfuldict = {}
negativedeceptivedict = {}
totalUniqueWords = 0
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


def writeToFile(fileName, pt, pd, nt, nd):
    outFile = open(fileName, 'w')
    dumpList = [pt, pd, nt, nd, priorProbabilityDict['positivetruthfulclass'],
                priorProbabilityDict['positivedeceptiveclass'], priorProbabilityDict['negativetruthfulclass'],
                priorProbabilityDict['negativedeceptiveclass']]
    pickle.dump(dumpList, outFile)
    outFile.close()


# Method to get prior probailty of all classes
def GetPriorProbability(documentsCountDict):
    priorProbabilityDict['positivetruthfulclass'] = (float)(documentsCountDict['positivetruthful']) / (float)(
            documentsCountDict['positivetruthful'] + documentsCountDict['positivedeceptive'] + documentsCountDict[
                'negativetruthful'] + documentsCountDict['negativedeceptive'])
    priorProbabilityDict['positivedeceptiveclass'] = (float)(documentsCountDict['positivedeceptive']) / (float)(
            documentsCountDict['positivetruthful'] + documentsCountDict['positivedeceptive'] + documentsCountDict[
                'negativetruthful'] + documentsCountDict['negativedeceptive'])
    priorProbabilityDict['negativetruthfulclass'] = (float)(documentsCountDict['negativetruthful']) / (float)(
            documentsCountDict['positivetruthful'] + documentsCountDict['positivedeceptive'] + documentsCountDict[
                'negativetruthful'] + documentsCountDict['negativedeceptive'])
    priorProbabilityDict['negativedeceptiveclass'] = (float)(documentsCountDict['negativedeceptive']) / (float)(
            documentsCountDict['positivetruthful'] + documentsCountDict['positivedeceptive'] + documentsCountDict[
                'negativetruthful'] + documentsCountDict['negativedeceptive'])


# Method to get Conditional Probabilty of a given class
def GetConditonalProbability(classDict, vocabulary, totalUniqueWordsCount):
    condDict = {}
    wordCountInClass = 0
    for key in classDict:
        wordCountInClass = wordCountInClass + classDict[key]
    denominator = float(wordCountInClass + totalUniqueWordsCount)
    for key in vocabulary:
        value = classDict.get(key)
        if (value == None):
            condDict[key] = 1 / denominator
        else:
            condDict[key] = (classDict[key] + 1) / denominator
    return condDict


# Method to parse the given text file and update the 4 dictionaries
def ParseTextFile(filename):
    global stopwords
    global documentsCountDict
    with open(filename, 'r') as myfile:
        line = myfile.read().replace('\n', '')

    line = line.translate(string.maketrans("", ""), string.punctuation)
    line = line.lower().strip()
    # filter(lambda x: x.isalpha(), line)
    tokens = line.split(' ')
    tokens = [x for x in tokens if x.isalpha()]
    tokens = filter(None, tokens)
    oldDict = Counter(tokens)
    currDict = dict(
            (key, value)
            for key, value in oldDict.iteritems()
            if key not in set(stopwords)
    )
    if filename.find('positive') != -1 and filename.find('truthful') != -1:
        documentsCountDict['positivetruthful'] = documentsCountDict['positivetruthful'] + 1
        for item in currDict:
            if item in positivetruthfuldict:
                positivetruthfuldict[item] = positivetruthfuldict[item] + 1
            else:
                positivetruthfuldict[item] = 1

    if filename.find('positive') != -1 and filename.find('deceptive') != -1:
        documentsCountDict['positivedeceptive'] = documentsCountDict['positivedeceptive'] + 1
        for item in currDict:
            if item in positivedeceptivedict:
                positivedeceptivedict[item] = positivedeceptivedict[item] + 1
            else:
                positivedeceptivedict[item] = 1

    if filename.find('negative') != -1 and filename.find('truthful') != -1:
        documentsCountDict['negativetruthful'] = documentsCountDict['negativetruthful'] + 1
        for item in currDict:
            if item in negativetruthfuldict:
                negativetruthfuldict[item] = negativetruthfuldict[item] + 1
            else:
                negativetruthfuldict[item] = 1
    if filename.find('negative') != -1 and filename.find('deceptive') != -1:
        documentsCountDict['negativedeceptive'] = documentsCountDict['negativedeceptive'] + 1
        for item in currDict:
            if item in negativedeceptivedict:
                negativedeceptivedict[item] = negativedeceptivedict[item] + 1
            else:
                negativedeceptivedict[item] = 1


# Program starts here
try:
    tempDict = {}
    for dirName, subdirList, fileList in os.walk(argv[1]):
        if dirName.find('fold1') == -1:
            for fname in fileList:
                if fname.endswith(".txt"):
                    if (fname == "README.txt"):
                        continue
                    fn = os.path.join(dirName, fname)
                    ParseTextFile(fn)

    tempDict.update(positivetruthfuldict)
    tempDict.update(positivedeceptivedict)
    tempDict.update(negativetruthfuldict)
    tempDict.update(negativedeceptivedict)
    GetPriorProbability(documentsCountDict)
    for word in tempDict:
        vocabularyList.append(word)
    totalUniqueWords = len(vocabularyList)
    condpositivetruthful = GetConditonalProbability(positivetruthfuldict, vocabularyList, totalUniqueWords)
    condpositivedeceptive = GetConditonalProbability(positivedeceptivedict, vocabularyList, totalUniqueWords)
    condnegativetruthful = GetConditonalProbability(negativetruthfuldict, vocabularyList, totalUniqueWords)
    condnegativedeceptive = GetConditonalProbability(negativedeceptivedict, vocabularyList, totalUniqueWords)
    writeToFile('nbmodel.txt', condpositivetruthful, condpositivedeceptive, condnegativetruthful, condnegativedeceptive)
except Exception, e:
    print 'error'
