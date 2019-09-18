from enum import Enum
class Requested(Enum):
    DUE_DATE = 1
    RELEASE_DATE = 2
    WEIGHT = 3
    PROCESS = 4
    DURATION = 5


if __name__ == '__main__':
    main()

def main():
    userSentence = input()
    transformedSentence = userSentence.lower()
    userSentenceObject = getObject(transformedSentence)
    userSentenceRequest = getRequest(transformedSentence)

def getObject(sentence):
# TODO implement

def getRequest(sentence):
    if "due" in sentence:
        requested = Requested.DUE_DATE
    if "how much" in sentence:
        requested = Requested.WEIGHT
    if "release" in sentence:
        requested = Requested.RELEASE_DATE
    if "how long" in sentence:
        requested = Requested.DURATION
    if

