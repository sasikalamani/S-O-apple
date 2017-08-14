import prepold
import MLP

(testDict) = prepold.dict()
print(testDict)
print("hi")

sortedDict = dict()
for key in testDict:
    x = testDict[key]
    index = [0]*len(x)
    for i in range(len(x)):
        index[x.index(max(x))] = i
        x[x.index(max(x))] = min(x)-1
    sortedDict[key] = index
print(sortedDict)

testQuestions = prepold.ques()

(output) = MLP.test_mlp()

outputDict = dict()
for i in range(len(output)):
    ques = testQuestions[i]
    if(ques not in outputDict):
        outputDict[ques] = [output[i]]
    else: outputDict[ques] += [output[i]]


outputSorted = dict()
for key in outputDict:
    x = outputDict[key]
    index = [0]*len(x)
    for i in range(len(x)):
        index[x.index(max(x))] = i
        x[x.index(max(x))] = min(x)-1
    outputSorted[key] = index


final = 0
for ques in outputSorted:
    x = outputSorted[ques]
    num = x.index(0)
    y = sortedDict[ques]
    num2 = y[num]
    prob = (num2) + 1
    final += (1/float(prob))
print(final/(float(580)))