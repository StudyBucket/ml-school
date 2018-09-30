#this file is used to train a final model on the entire training corpus,
#it downloads the unlabeled test files and sends the results back to our
#webservice

from data_reader import DataReader
from feature_extractor import FeatureExtractor
from trainer import NBTrainer,DTTrainer
import requests
import sys
import codecs
import re

#call with python train_final_and_test.py traindata corpustype teamname

# CUTER base url
cuter_url = 'https://clarin09.ims.uni-stuttgart.de/cuter'

# check no. commandline arguments
if len(sys.argv) != 4:
    sys.exit('\nUnzulaessige Anzahl von Parametern beim Aufruf von test.py: ' +
             str(len(sys.argv)-1) + '\n' +
             'Beispielaufruf:\n' +
             'python test.py ../data/Parzival_train.tsv MHD TeamOne\n')

#name of the team for the submission
teamname = sys.argv[3]
teamname = re.sub("[^A-Za-z0-9_\-]",'',teamname)
#_-9azAZ

# server file name
serverFilename = ''
if sys.argv[2] == "MHD":
    serverFilename = "parzival"
elif sys.argv[2] == "W":
    serverFilename = "werther"
elif sys.argv[2] == "BTD":
    serverFilename = "bundestag"
else:
    print("No valid text type. Exiting.")
    sys.exit(1)

#give the training corpus as frist argument to the script
corpus = DataReader(sys.argv[1]).read_corpus()

#give the test type (MHD, BTD, W) you have trained on



#send file to CUTER

#full_url = cuter_url+"/submit/"+serverFilename+'/'+teamname
#r = requests.post(full_url, data=pred_srv, headers={u'Content-type':u'text/plain; charset=utf8'})

count = 0
while count < 10:

    #print all tokens for these first two segments
    tokens_with_features = FeatureExtractor().extract_features(corpus)


    #train the classifier
    #trainer = NBTrainer(tokens_with_features)
    trainer = DTTrainer(tokens_with_features)

    response = requests.get(cuter_url + '/test/' + serverFilename)
    test = response.text

    #write the testfile to file
    outfile = codecs.open("test_"+sys.argv[2]+".conll",'w','utf8')
    outfile.write(test)
    outfile.close()

    testcorpus = DataReader("test_"+sys.argv[2]+".conll").read_corpus()
    test_features=FeatureExtractor().extract_features(testcorpus)

    #write prediction to file
    predicted = codecs.open("test_"+sys.argv[2]+"."+teamname+".predicted",'w','utf8')
    pred_srv = ''
    for feature_vec in test_features:
        pred=trainer.classifier.classify(feature_vec[0])
        s = feature_vec[0]['word']+'\t'+pred+'\n'
        predicted.write(s)
        pred_srv += pred+'\n'

    predicted.close()
    
    full_url = cuter_url+"/submit/"+serverFilename+'/'+teamname+str(count)
    r = requests.post(full_url, data=pred_srv, headers={u'Content-type':u'text/plain; charset=utf8'})
    count += 1

print count
print("Upload successful!")
print(r.status_code)
print(r.text)
