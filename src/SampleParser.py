import os
import sys
from Bio import SeqIO
import Constants

def parseTrainingSamples():
    pos_path = Constants.positiveSamplesPath
    neg_path = Constants.negativeSamplesPath
    return _parseSample(pos_path), _parseSample(neg_path)

def readFile(filename):
    try:
        sequences = list()
        records = list(SeqIO.parse(filename, "fasta"))
        for record in records:
            sequence = str(record.seq.split('#')[0])
            if (str(sequence) != 'Sequenceunavailable'):
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
