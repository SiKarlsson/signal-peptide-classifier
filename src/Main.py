import SampleParser
import Classifier
import ResultPrinter
import Constants
from decimal import Decimal
import sys

def main():
    """Main handler for running the experiments.

    Command line args:
        1: The organism to run the experiments on.

    """
    positiveSamples, negativeSamples = SampleParser.parseTrainingSamples()
    print "Number of positive training samples: " + str(len(positiveSamples))
    print "Number of negative training samples: " + str(len(negativeSamples))
    organism = sys.argv[1]
    methods = ('SVM', 'NB')
    pos = []
    neg = []

    for sign in ['pos', 'neg']:
        for i in range(0, len(methods)):
            classifier, count = Classifier.train(positiveSamples, negativeSamples, methods[i])
            seqs = SampleParser.readFile(Constants.getTestData(organism, sign))
            if sign == 'pos':
                print "Number of positive testing samples: " + " " + str(len(seqs))
            else:
                print "Number of negative testing samples: " + " " + str(len(seqs))

            predicted = Classifier.predict(classifier, seqs, count)
            incorrect = 0
            correct = 0
            for p in predicted:
                if sign == "pos":
                    if p == 1:
                        correct = correct + 1
                    elif p == 0:
                        incorrect = incorrect + 1
                elif sign == "neg":
                    if p == 0:
                        correct = correct + 1
                    elif p == 1:
                        incorrect = incorrect + 1
            if sign == "pos":
                pos.append(Decimal(correct)/Decimal(correct+incorrect))
            elif sign == "neg":
                neg.append(Decimal(correct)/Decimal(correct+incorrect))

    tot = []
    for i in range(0, len(methods)):
        tot.append((pos[i] + neg[i]) / Decimal(2))

    print "--- SUMMARY ---"
    for i in range(0, len(methods)):
        print "--- RESULTS for " + str(methods[i] + " ---")
        print "Positive: " + str(pos[i])
        print "Negative: " + str(neg[i])
        print "Total: " + str(tot[i])
    ResultPrinter.plot(pos, neg, tot, methods, organism)


if __name__ == "__main__":
    main()
