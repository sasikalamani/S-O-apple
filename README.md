# S-O-apple

Preprocessing the data:
prep.py    -  preprocesses the entire apple dataset
The dictionary qmore5 contains the questions which have 5 or more questions. The test set is 20% of this dictionary randomly chosen. The train set is 80% of the qmore5 dictionary as well as any other question in the apple dataset with an answer. 

The input features are the tags in one hot encoding as well the answerer in one hot encoding. The input size is 35205.

The output is the score made into a classification problem. There are 102 classes therefore the output size is 102.

To run the preprocessing file, files needed:
QuestionId_AnswererId.csv
apple-tags.csv

run using the command : python prep.py



prepold.py    -  preprocesses a subset of the apple dataset
The dictionary qmore5 contains the questions which have 5 or more questions. The test set is 20% of this dictionary randomly chosen. The train set is 80% of the qmore5 dictionary.

The input features are the tags in one hot encoding as well the answerer in one hot encoding. The input size is 12576.

The output is the score made into a classification problem. There are 102 classes therefore the output size is 102.

To run the preprocessing file, files needed:
QuestionId_AnswererId.csv
apple-tags.csv

run using the command : python prepold.py


preSparse.py    -  preprocesses a subset of the apple dataset
The dictionary qmore5 contains the questions which have 5 or more questions. The test set is 20% of this dictionary randomly chosen. The train set is 80% of the qmore5 dictionary.

There are two input matrices. The input features are the tags in one hot encoding as well the answerer in one hot encoding. The input size 667 for the tags and 11909 of the users.

The output is the score made into a classification problem. There are 102 classes therefore the output size is 102.

To run the preprocessing file, files needed:
QuestionId_AnswererId.csv
apple-tags.csv

run using the command : python prepSparse.py


Neural Nets:
MLP.py     -  a simple multi-layered perceptron
add or remove hidden layers with the hidden layer class
tune the hyper parameters with number of hidden units, learning rate, number of epochs, etc.

Validation set is currently set to be the same as the train set.

Will print the test error for epochs that see a significant change.
In the end, will print the best validation error and test error.

To run the neural net file, files needed:
prep.py or prepold.py depending on the dataset 
logistic_sgd.py (for the logistic regression layer)

run using the command : python MLP.py



sparse_MLP.py    - a mulit-layered perceptron modeled after the Hinton distributed learning paper. The MLP has two separate inputs. 
The second layer is separate distributed encoding of the two inputs. There are multiple combined hidden layers with a final output.

Validation set is currently set to be the same as the train set.

Will print the test error for epochs that see a significant change.
In the end, will print the best validation error and test error.

To run the neural net file, files needed:
prepSparse.py 
logistic_sgd.py (for the logistic regression layer)

run using the command : python sparse_MLP.py


Post-processing:
post.py    - calculates and prints the MRR accuracy for the sparse MLP for the test set

To run the post processing file, files needed:
prepSparse.py
sparse_MLP.py

run using the command : python post.py

postold.py   - calculates and prints the MRR accuracy for the sparse MLP for the test set

To run the post processing file, files needed:
prepold.py or prep.py(depending on the dataset)
MLP.py

run using the command : python postold.py
