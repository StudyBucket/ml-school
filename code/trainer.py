# this class trains a classifier and returns it
from __future__ import unicode_literals
import nltk
import codecs
import time
import os

###################################################
# Trainer Class using the Decision Tree Algorithm #
# Contains also a function to access accuracy and #
# errors.                                         #
###################################################

class DTTrainer:
    
    def __init__(self,train_features):
        #train the classifier right at its initialization
        print("  Decision Tree Classifier initialized")
        train_features_without_word,words= self.make_wordfree_feature_dict(train_features)
        self.classifier = self.train(train_features_without_word)

    def make_wordfree_feature_dict(self,train_features):
        words=[]
        train_features_ww=[]
        for tup in train_features:
            features={}
            for f in tup[0]:
                if f=="word":
                    words.append(tup[0]["word"])
                else:
                    features[f]=tup[0][f]
            train_features_ww.append((features,tup[1]))
        return train_features_ww,words

    #use the nltk implementation of the Decision Tree algorithm to train 
    def train(self,train_features):
        
        classifier =nltk.DecisionTreeClassifier.train(train_features)
        return classifier
    
    #calculate and return the accuracy on the develooment set
    def return_accuracy(self,dev_features):
        dev_features_without_word,words=self.make_wordfree_feature_dict(dev_features)
        corr_with_MB=0
        for word in dev_features_without_word:
            if word[1]=="O":
                corr_with_MB+=1
        BL_accuracy= float(corr_with_MB)/len(dev_features_without_word)
        return nltk.classify.accuracy(self.classifier, dev_features_without_word),BL_accuracy

    # pretty print decision tree
    #def pretty_format()
    
    #print the following info to the screen and write to log file:
    # accuracy
    # the incorrectly classified words along with the gold label and the predicted label
    def analyze_classifier(self,bestclassifier,dev_features):
        try:
            os.makedirs('logs')
        except OSError:
            pass
        logname="logs/log.decisiontree"+time.strftime('%Y-%m-%d-%H-%M-%S')+".txt"
        logfile = codecs.open(logname,'w','utf8')
        dev_features_without_word,words=self.make_wordfree_feature_dict(dev_features)
        corr_with_MB=0
        for word in dev_features_without_word:
            if word[1]=="O":
                corr_with_MB+=1
        BL_accuracy= float(corr_with_MB)/len(dev_features_without_word)
        errors = []
        i=0
        #for each token in the develooment set
        for i,tok in enumerate(dev_features_without_word):
            #word
            word = words[i]
            #gold label
            tag =  tok[1]
            #predicted label
            guess = bestclassifier.classify(tok[0])
            
            #if the gold label is not the same as the predicted label
            if guess != tag:
                errors.append( (tag, guess, word) )
        print("===================================================")
        print("Summary best classifier")
        print("in total there are "+str(len(dev_features_without_word))+ " words in the development set")
        print("out of which your classifier mislabeled "+str(len(errors)))
        print("and correctly labeled "+str(len(dev_features_without_word)-len(errors)))
        print("this is an accuracy of "+str(self.return_accuracy(dev_features)[0]))
        print("if I labeled all words as non-entity, I would reach an accuracy of "+str(BL_accuracy))
        print("you find an overview of the errors in "+logname)
        logfile.write("in total there are "+str(len(dev_features_without_word))+ " words in the development set\r\n")
        logfile.write("out of which your classifier mislabeled "+str(len(errors))+'\r\n\r\n')
        logfile.write("If I had labeled all words as non-entity, I would have mislabeled "+str(len(dev_features_without_word)-corr_with_MB)+'\r\n\r\n')        
        logfile.write("The following features have been used:\n\n")
        features=''
        for f in dev_features_without_word[0][0]:
            features+=f+'\r\n'
        logfile.write(features+'\r\n\r\n')

        # print decision tree
        logfile.write('Decision tree:\r\n' + str(bestclassifier) + '\r\n\r\n')
        
        #print/write all the errors
        for (tag, guess, word) in sorted(errors):
           
            logfile.write('correct={:<8} guess={:<8s} word={:<30}\r\n'.format(tag, guess, word))
        logfile.close()
        
        

###################################################
# Trainer Class using the Naive Bayes Algorithm #
# Contains also a function to access accuracy and #
# errors.                                         #
###################################################
        
class NBTrainer:

    def __init__(self,train_features):
        #train the classifier right at its initialization
        print("  Naive Bayes Classifier initialized")
        train_features_without_word,words= self.make_wordfree_feature_dict(train_features)
        self.classifier = self.train(train_features_without_word)

    def make_wordfree_feature_dict(self,train_features):
            words=[]
            train_features_ww=[]
            for tup in train_features:
                features={}
                for f in tup[0]:
                    if f=="word":
                        words.append(tup[0]["word"])
                    else:
                        features[f]=tup[0][f]
                train_features_ww.append((features,tup[1]))
            return train_features_ww,words


     #use the nltk implementation of the Naive Bayes algorithm to train
    def train(self,train_features):
        classifier = nltk.NaiveBayesClassifier.train(train_features)
        return classifier
       
    def return_accuracy(self,dev_features):
        dev_features_without_word,words=self.make_wordfree_feature_dict(dev_features)
        corr_with_MB=0
        for word in dev_features_without_word:
            if word[1]=="O":
                corr_with_MB+=1
        BL_accuracy= float(corr_with_MB)/len(dev_features_without_word)
        return nltk.classify.accuracy(self.classifier, dev_features_without_word),BL_accuracy
        
    #print the following info to the screen and write to log file:
    # accuracy
    # the incorrectly classified words along with the gold label and the predicted label
    def analyze_classifier(self,bestclassifier,dev_features):
        try:
            os.makedirs('logs')
        except OSError:
            pass
        logname="logs/log.naivebayes"+time.strftime('%Y-%m-%d-%H-%M-%S')+".txt"
        logfile = codecs.open(logname,'w','utf8')
        
        #log the features that were most informative for the alogrithm to make the decision
        #it give the two labels it had to make a decision between the probability distribution of 
        #the feature 1 for class1 and feature value for class2
        logfile.write("Most informative features:\r\n\r\n")
        #bestclassifier.show_most_informative_features(5)
        n=10
        cpdist = bestclassifier._feature_probdist
        for (fname, fval) in bestclassifier.most_informative_features(n):
            def labelprob(l):
                return cpdist[l, fname].prob(fval)

            labels = sorted([l for l in bestclassifier._labels
                             if fval in cpdist[l, fname].samples()],
                            key=labelprob)
            if len(labels) == 1:
                continue
            l0 = labels[0]
            l1 = labels[-1]
            if cpdist[l0, fname].prob(fval) == 0:
                ratio = 'INF'
            else:
                ratio = '%8.1f' % (cpdist[l1, fname].prob(fval) /
                                   cpdist[l0, fname].prob(fval))
            logfile.write('%24s = %-14r %6s : %-6s = %s : 1.0\r\n\r\n\r\n' %
                   (fname, fval, ("%s" % l1)[:6], ("%s" % l0)[:6], ratio))
      
        dev_features_without_word,words=self.make_wordfree_feature_dict(dev_features)
        corr_with_MB=0
        for word in dev_features_without_word:
            if word[1]=="O":
                corr_with_MB+=1
        BL_accuracy= float(corr_with_MB)/len(dev_features_without_word)
        errors = []
        i=0
        #for each token in the develooment set
        for i,tok in enumerate(dev_features_without_word):
            #word
            word = words[i]
            #gold label
            tag =  tok[1]
            #predicted label
            guess = bestclassifier.classify(tok[0])
            
            #if the gold label is not the same as the predicted label
            if guess != tag:
                errors.append( (tag, guess, word) )
        #print/write the information
        print("===================================================")
        print("Summary best classifier")
        print("in total there are "+str(len(dev_features_without_word))+ " words in the development set")
        print("out of which your classifier mislabeled "+str(len(errors)))
        print("and correctly labeled "+str(len(dev_features_without_word)-len(errors)))
        print("this is an accuracy of "+str(self.return_accuracy(dev_features)[0]))
        print("if I labeled all words as non-entity, I would reach an accuracy of "+str(BL_accuracy))
        print("you find an overview of the errors in "+logname)
        logfile.write("in total there are "+str(len(dev_features_without_word))+ " words in the development set\r\n")
        logfile.write("out of which your classifier mislabeled "+str(len(errors))+'\r\n\r\n')
        logfile.write("If I had labeled all words as non-entity, I would have mislabeled "+str(len(dev_features_without_word)-corr_with_MB)+'\r\n\r\n')        
        logfile.write("The following features have been used:\n\n")
        features=''
        for f in dev_features_without_word[0][0]:
            features+=f+'\r\n'
        logfile.write(features+'\r\n\r\n')
        #print/write all the errors
        for (tag, guess, word) in sorted(errors):
           
            logfile.write('correct={:<8} guess={:<8s} word={:<30}\r\n'.format(tag, guess, word))
        logfile.close()
        
