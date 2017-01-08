import os

trainingDataId = "dec16"
testDataId = "jan17"

positiveSamplesPath = os.getcwd() + "/../data/training_data/"+ trainingDataId +"/" + "positive_examples"
negativeSamplesPath = os.getcwd() + "/../data/training_data/"+ trainingDataId +"/" + "negative_examples"

def getTestData(organism, sign):
    """Returns the path to the test data.

    Args:
        organism (str): Which organism to get the path to.
        sign (str): Either 'pos' or 'neg', based on which samples is wanted.

    Returns:
        The path to the test data for the given organism with the given sign.

    """
    return os.getcwd() + "/../data/test_data/"+ testDataId +"/" + organism + "/" + sign
