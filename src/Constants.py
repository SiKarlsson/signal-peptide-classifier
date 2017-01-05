import os

trainingDataId = "dec16"
testDataId = "jan17"

positiveSamplesPath = os.getcwd() + "/../data/training_data/"+ trainingDataId +"/" + "positive_examples"
negativeSamplesPath = os.getcwd() + "/../data/training_data/"+ trainingDataId +"/" + "negative_examples"

def getTestData(organism, sign):
    return os.getcwd() + "/../data/test_data/"+ testDataId +"/" + organism + "/" + sign
