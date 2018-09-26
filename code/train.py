# this file is called by the participants in order to train and test a model in cross-validation 
# setting. This is the development script

# -*- coding: utf-8 -*-

from data_reader import DataReader
from feature_extractor import FeatureExtractor
from trainer import NBTrainer,DTTrainer
import requests
import os

if not os.path.isdir("logs"):
    os.makedirs("logs")

#THIS IS WHERE THE INPUT IS DEFINED AND READ#

#calls a function from DataReader here
#reads in the annotated corpus
#change the path to the desired input corpus here:
#platfrom-independent:
#corpus = DataReader(os.path.join('..','data','Parzival_train.tsv')).read_corpus()
#on Windows this looks slightly different:
# corpus = DataReader("..\data\Parzival_train.tsv").read_corpus()
corpus = DataReader("../data/Parzival_train.tsv").read_corpus()

#THIS IS WHERE THE FEATURES ARE EXTRACTED#

#the annotated corpus is send to the FeatureExtractor
#different feature extraction functions are called here
#in order to change which features are used, open feature_extractor.py and change the 
#function calls
tokens_with_features = FeatureExtractor().extract_features(corpus)


##THIS IS WHERE THE MACHINE LEARNING STARTS##
#before we start training we don't have an accuracy value, thus 0
accuracy=0

#train in cross validation, test if the accuracy is higher then before, if yes, save the classifier and overwrite the accuracy
#determine crossvalidation set sizes
num_folds = 3
subset_size = int(len(tokens_with_features)/num_folds)
print("Train classifier in "+str(num_folds)+"-fold crossvalidation setting")
#train a classifier for each crossvalidation fold
for i in range(num_folds):
    print("Train fold number "+str(i+1))
    #make crossvalidation set test and train
    testcv = tokens_with_features[i*subset_size:][:subset_size]
    traincv = tokens_with_features[:i*subset_size] + tokens_with_features[(i+1)*subset_size:]

    #THIS IS WHERE YOU CAN CHANGE THE ML ALGORITHM#
    #change this line for another ML algorithm (remove the # infront of a line to uncomment)
    #DTTrainer is the trainer for a Decision Tree classifier
    #NBTrainer is the trainer for a Naive Bayes classifier
    #
    trainer = DTTrainer(traincv)
    #trainer = NBTrainer(traincv)
    
    #here the accuracy of the resulting algorithm is calculated
    acc,BL_acc= trainer.return_accuracy(testcv)
    
    print("  The classifier reaches an accuracy of "+str(acc))
    print("  If I labeled all words as non-entity, the accuracy would be "+str(BL_acc))
    #if the accuracy is higher than for the previous classifiers, store the best classifier
    #print(trainer.classifier)
    #print(trainer.classifier.pretty_format())
    #print(trainer.classifier.pseudocode())

    if acc > accuracy:
        #store the accuracy
        accuracy = acc
        #classifier is now the current classifier
        classifier = trainer.classifier
        besttrainer =trainer
        #keep the test set that belonged to this crossvalidation fold
        testset=testcv

#give detailed analysis of the best classifier
besttrainer.analyze_classifier(classifier,testset)


