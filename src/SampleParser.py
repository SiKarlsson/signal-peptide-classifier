import os
import sys
import random
from Bio import SeqIO
import Constants

def parseTrainingSamples():
    pos_path = Constants.positiveSamplesPath
    neg_path = Constants.negativeSamplesPath
    return _parseSample(pos_path), _parseSample(neg_path)

def readFile(filename):
    try:
        c = 0
        sequences = list()
        records = list(SeqIO.parse(filename, "fasta"))
        for record in records:
            sequence = str(record.seq.split('#')[0])
            if (_checkSequence(sequence) and c < 3400):
                c = c + 1
                sequences.append(sequence)
        return sequences
    except :
        sys.exit("Error reading file " + filename)


def _parseSample(path):
    samples = list()
    for dir in os.listdir(path):
        sample_dir = os.path.join(path, dir)
        for file in os.listdir(sample_dir):
            samples = samples + readFile(os.path.join(sample_dir, file))
    return samples

def _checkSequence(sequence):
    if len(sequence) < 20 or _countUniqueChars(sequence) > 22 or sequence == 'Sequenceunavailable':
        return False
    else:
        return True

def _countUniqueChars(s):
    unique = []
    for c in s[::]:
        if c not in unique:
            unique.append(c)
    return len(unique)

def produceRandomSequence(n):
    sequences = []
    for i in range(0, n):
        l = 100
        a = ("R", "H", "K", "D", "E", "S", "T", "N", "Q", "C", "U", "G", "P", "A", "V", "I", "L", "M", "F", "Y", "W")
        lineLength = 80
        s = ""
        for x in range(1, int(l)+1):
            s = s + random.choice(a)
        sequences.append(s)
    return sequences
