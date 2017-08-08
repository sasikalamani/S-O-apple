import prep
import MLP

(testDict) = prep.dict()

sortedDict = dict()
for key in testDict:
    x = testDict[key]
    index = [0]*len(x)
    for i in range(len(x)):
        index[x.index(max(x))] = i
        x[x.index(max(x))] = min(x)-1
    sortedDict[key] = index


testQuestions = prep.ques()

(ranks, output) = MLP.test_mlp()
outputDict = dict()
for i in range(len(output)):
    ques = testQuestions[i]
    if(ques not in outputDict):
        outputDict[ques] = [output[i]]
    else: outputDict[ques] += [output[i]]

outputSorted = dict()
for key in outputDict:
    x = testDict[key]
    index = [0]*len(x)
    for i in range(len(x)):
        index[x.index(max(x))] = i
        x[x.index(max(x))] = min(x)-1
    outputSorted[key] = index

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