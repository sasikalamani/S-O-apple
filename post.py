import prepSparse
import sparse_MLP

(testDict) = prepSparse.dict()

#creates a dictionary that replaces the score with
#the its ranking among all the answers for a specific question
sortedDict = dict()
for key in testDict:
    x = testDict[key]
    index = [0]*len(x)
    for i in range(len(x)):
        index[x.index(max(x))] = i
        x[x.index(max(x))] = min(x)-1
    sortedDict[key] = index


testQuestions = prepSparse.ques()

(output) = sparse_MLP.test_mlp()
#creates a dictionary that maps the a question to its
#predicted output of answers
outputDict = dict()
for i in range(len(output)):
    ques = testQuestions[i]
    if(ques not in outputDict):
        outputDict[ques] = [output[i]]
    else: outputDict[ques] += [output[i]]

#sorts the predicted outputs according to rank
outputSorted = dict()
for key in outputDict:
    x = testDict[key]
    index = [0]*len(x)
    for i in range(len(x)):
        index[x.index(max(x))] = i
        x[x.index(max(x))] = min(x)-1
    outputSorted[key] = index

#calculates the MRR accuracy for the test set
final = 0
for ques in testDict:
    x = testDict[ques]
    maxi = max(x)
    num = x.index(maxi)
    y = outputDict[ques]
    maxy = max(y)
    num2 = y.index(maxy)
    prob = (abs(num-num2) + 1)
    final += (1/float(prob))
print(final/(float(580)))