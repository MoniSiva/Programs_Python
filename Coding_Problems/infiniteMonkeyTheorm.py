"""
Infinite Monkey Theorem
    The theorem states that a monkey hitting keys at random on a typewriter keyboard for an
    infinite amount of time will almost surely type a given text.
    We replace a monkey with a Python function and determine the time required and the ways for
    generating the input string.

"""
import random

#Function to generate the random string for monkey typing
def generateRandomString(strlen):
    stringOfCharacters = "abcdefghijklmnopqrstuvwxyz "
    resultString = ""
    for i in range(strlen):
        resultString += stringOfCharacters[random.randrange(27)]
    return resultString

#Function to compute the similarity of the strings
def scoreCompute(inputString, generatedString):
    number = 0
    for i in range(len(inputString)):
        if inputString[i] == generatedString[i]:
            number += 1
    return number / len(inputString)


def main():
    inputString = input("Enter the string to be checked:")    # Input String
    generatedString = generateRandomString(len(inputString))
    bestScore = 0
    result_score = scoreCompute(inputString, generatedString)

    #Printing all the possible strings with increasing matching score
    while result_score < 1:
        if result_score > bestScore:
            print("Generated String is {} with score {} ".format(generatedString,result_score))
            bestScore = result_score
        generatedString = generateRandomString(len(inputString))
        result_score = scoreCompute(inputString, generatedString)

    #Loop breaks with matching score more than 1 where the two string matches with more similarity.

main()