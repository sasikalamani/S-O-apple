import csv
import random
import pickle
from collections import Counter
import nltk


#creating dictionary that maps question and answer information
quesAns = dict()
ansQues = dict()
ansScore = dict()
ansUser = dict()
with open('QuestionId_AnswererId.csv', 'rb') as csvfile1:
    reader1 = csv.reader(csvfile1)
    for row in reader1:
        ques = row[1]
        ans = row[2]
        user = row[3]
        score = row[4]
        if(ques not in quesAns):
            quesAns[ques] = [ans]
        else: quesAns[ques] += [ans]
        ansScore[ans] = score
        ansUser[ans] = user
        ansQues[ans] = ques

#questions that have 5 or more questions
qmore5 = []
for key in quesAns:
    if(len(quesAns[key]) >= 5):
        qmore5.append(key)

#2908 questions with more than 5 answers
#20130 answers to these questions

allQues = []

cnt = 0
quesTag = dict()
with open('apple-tags.csv', 'rb') as csvfile1:
    reader1 = csv.reader(csvfile1)
    for row in reader1:
        if(row[0] in qmore5):
            quesTag[row[0]] = row[1]

#creating a dictionary that maps the question id to its tags
answers = []
for key in quesTag:
    allQues.append(key)
    answers += quesAns[key]
    quesTag[key] = quesTag[key][1:]
    tags = quesTag[key]
    quesTag[key] = quesTag[key][:(len(tags)- 1)]
for key in quesTag:
    quesTag[key] = quesTag[key].split('><')

#splitting the test/train 
test = list()
train = list()
random.seed(2)
ranNum = random.sample(range(2853), 580)
for i in range(2853):
    if (i in ranNum): 
        test.append(allQues[i])
    else:
        train.append(allQues[i])


trainAns = []
for key in train:
    trainAns = trainAns + quesAns[key]

trainUser = []
trainScore = []
for ta in trainAns:
    trainUser.append(ansUser[ta])
    trainScore.append(int(ansScore[ta]))

testDict = dict()
testAns = []
for key in test:
    testAns = testAns + quesAns[key]
    testDict[key] = quesAns[key]


testUser = []
testScore = []
for ta in testAns:
    testUser.append(ansUser[ta])
    testScore.append(int(ansScore[ta]))

#assigns score for the classification problem
#negative scores are 0, scores above 500 are 101
#between 1-500, each section of 5 is given a score
def scorize(scores):
    for i in range (len(scores)):
        if(scores[i]<0):
            scores[i] = 0
        elif (scores[i]>500):
            scores[i] = 101
        else:
            while(scores[i] % 5 != 0):
                scores[i] += 1
            num = scores[i] // 5
            scores[i] = num
    return scores

trainScore = scorize(trainScore)
testScore = scorize(testScore)


#creates a list of questions based on number of times it was answered
#also creates a list of answerers
answerers = []
questions = []
for ans in answers:
    user = ansUser[ans]
    if(user not in answerers):
        answerers.append(user)
    questions.append(ansQues[ans])

#maps each unique user to an index
def mapUser(someList):
    userDict = Counter()
    usrs = 0
    for i in range(len(someList)):
       word = someList[i]
       if(word not in userDict):
        userDict[word] = usrs
        usrs += 1
    return userDict


userDict = mapUser(answerers)

#print(len(userDict)) 11909
cnt = Counter()
num = 0
for key in quesTag:
    for i in range(len(quesTag[key])):
        word = quesTag[key][i]
        num += 1
        cnt[word.lower()]+= 1
#len = 667

index = dict()
i = 0
for k in cnt.keys():
    index[k] = i
    i+=1

#creating the input matrices
trainIn = [ ([0] * 12576) for row in range(len(trainScore)) ]
testIn = [ ([0] * 12576) for row in range(len(testScore)) ]

trainQues = []
for ans in trainAns:
    trainQues.append(ansQues[ans])

testQues = []
for ans in testAns:
    testQues.append(ansQues[ans])

#one hot encoding of both the tags and the answerer
for i in range(len(trainQues)):
    ques = trainQues[i]
    for j in range(len(quesTag[ques])):
        word = quesTag[ques][j]
        num = index[word.lower()]
        trainIn[i][num] = 1
        usr = trainUser[i]
        num2 = userDict[usr] + 667
        trainIn[i][num2] = 1


for i in range(len(testQues)):
    ques = testQues[i]
    for j in range(len(quesTag[ques])):
        word = quesTag[ques][j]
        num = index[word.lower()]
        testIn[i][num] = 1
        usr = testUser[i]
        num2 = userDict[usr] + 667
        testIn[i][num2] = 1


def inout():
    return trainIn, testIn, trainScore, testScore


def ques():
    return testQues

#dictionary that maps the question to the scores of its answers
for key in testDict:
    for i in range(len(testDict[key])):
        testDict[key][i] = int(ansScore[testDict[key][i]])

def dict():
    return testDict
