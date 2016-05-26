#This Python program will take a string as the first parameter, and write an output file called anagram_out.txt which contains all the anagrams (permutations) of the string, one per line, sorted alphabetically.
import sys
lst = []
def anagram(str, inputstring):
    if len(str) == len(inputstring):
        lst.append(str)
        return
    else:
        for ch in inputstring:
            if ch not in str:
                anagram(str+ch, inputstring)

def writetofile(lst):
    try:
        count = 0
        outfile = open(sys.argv[2], 'w')
        for word in lst:
            outfile.write(word+'\n')
        outfile.close()
    except IOError,e:
        pass

try:
    inputstring = str(sys.argv[1])
    inputstring = inputstring.strip('')
    anagram('', inputstring)
    lst.sort()
    writetofile(lst)

except Exception, e:
    pass
