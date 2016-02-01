import binascii
import sys

reload(sys)
sys.setdefaultencoding('UTF8')
outputlist = []


def fileIO(filename, mode):
    try:
        fopen = open(filename, mode)
        return fopen
    except IOError, e:
        pass


def writetofile(lst):
    try:
        outputfile = fileIO(argv[2], 'w')
        for word in lst:
            outputfile.write(word)
        outputfile.close()
    except IOError, e:
        pass


def onebyteencode(inputstring):
    try:
        defaultstring = ['0', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
        binarystring = '{0:08b}'.format(inputstring)
        for index in range(len(defaultstring) - 1, 0, -1):
            if defaultstring[index] != '0' and defaultstring[index] != '1':
                defaultstring[index] = binarystring[index]
        hexval = hex(int(''.join(defaultstring), 2))
        hexval = hexval[2:]
        if (len(hexval) % 2 != 0):
            hexval = '0a'
        val = binascii.unhexlify(hexval)
        return val
    except Exception, e:
        pass


def twobyteencode(inputstring):
    try:
        defaultstring = ['1', '1', '0', 'x', 'x', 'x', 'x', 'x', '1', '0', 'x', 'x', 'x', 'x', 'x', 'x']
        binarystring = '{0:08b}'.format(inputstring)
        if (len(binarystring) < 11):
            count = 11 - len(binarystring)
            rev = list(binarystring[::-1])
            while count > 0:
                rev.append('0')
                count = count - 1
            binarystring = rev[::-1]
        binaryindex = len(binarystring) - 1
        for index in range(len(defaultstring) - 1, 0, -1):
            if defaultstring[index] != '0' and defaultstring[index] != '1':
                defaultstring[index] = binarystring[binaryindex]
                binaryindex = binaryindex - 1
        hexval = hex(int(''.join(defaultstring), 2))
        hexval = hexval[2:]
        val = binascii.unhexlify(hexval)
        return val
    except Exception, e:
        pass


def threebyteencode(inputstring):
    try:
        defaultstring = ['1', '1', '1', '0', 'x', 'x', 'x', 'x', '1', '0', 'x', 'x', 'x', 'x', 'x', 'x', '1', '0', 'x',
                         'x', 'x', 'x', 'x', 'x']
        binarystring = '{0:08b}'.format(inputstring)
        if (len(binarystring) < 16):
            count = 16 - len(binarystring)
            rev = list(binarystring[::-1])
            while count > 0:
                rev.append('0')
                count = count - 1
            binarystring = rev[::-1]
        binaryindex = len(binarystring) - 1
        for index in range(len(defaultstring) - 1, 0, -1):
            if defaultstring[index] != '0' and defaultstring[index] != '1':
                defaultstring[index] = binarystring[binaryindex]
                binaryindex = binaryindex - 1
        hexval = hex(int(''.join(defaultstring), 2))
        hexval = hexval[2:]
        val = binascii.unhexlify(hexval)
        return val
    except Exception, e:
        pass


try:
    filename = sys.argv[1]
    inputfile = fileIO(filename, 'rb')
    while inputfile:
        str = inputfile.read(2)
        if str != '':
            lst = []
            for ch in str:
                lst.append(ch)
            v = map(lambda x: '%02x' % ord(x), lst)
            v = ''.join(v)
            intval = int(v, 16)
            if (intval < 128):
                outputlist.append(onebyteencode(intval))
            elif (intval < 2048):
                outputlist.append(twobyteencode(intval))
            else:
                outputlist.append(threebyteencode(intval))
        else:
            break
    writetofile(outputlist)
except Exception, e:
    pass
