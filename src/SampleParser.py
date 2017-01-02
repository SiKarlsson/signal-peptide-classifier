import os
import sys
from Bio import SeqIO

def parseTrainingSamples():
    pos_path = os.getcwd() + "/../training_data/" + "positive_examples"
    neg_path = os.getcwd() + "/../training_data/" + "negative_examples"
    return _parseSample(pos_path), _parseSample(neg_path)

def _parseSample(path):
    samples = list()
    for dir in os.listdir(path):
        sample_dir = os.path.join(path, dir)
        for file in os.listdir(sample_dir):
            samples = samples + _readFile(os.path.join(sample_dir, file))
    return samples

def _readFile(filename):
    try:
        sequences = list()
        records = list(SeqIO.parse(filename, "fasta"))
        for record in records:
            sequences.append(record.seq.split('#')[0])
        return sequences
    except :
        sys.exit("Error reading file " + filename)
