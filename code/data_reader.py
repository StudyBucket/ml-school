# encoding: utf8
# this file is the data reader class

import codecs


class DataReader:
    
    # this is the constructor of the DataReader class. It makes the
    # corpus file available to the class
    def __init__(self, path_to_conll):
        self.corpus_file = codecs.open(path_to_conll,'r','utf8').readlines()
   
    def read_corpus(self):

        ###############
        # PREPARATION #
        # & VARIABLES #
        ###############

        # go through every line of the annotated corpus,
        # clean it from surrounding newlines
        # and put it into the list "rn_stripped_lines"
        rn_stripped_lines = [line.strip("\r\n") for line in self.corpus_file]

        # corpus is a list
        # it represents all the information we need to extract the features
        # corpus is filled with the segments, which are filled with
        # sentences and their tokens
        corpus = []
        # segment is a dictionary that is appended to corpus when filled
        segment = {}
        # for the case that the corpus does not contain seg annotation:
        # only one segment called "==="
        # "===" marks the end of a segment
        segment["segment_id"]="==="
        # sents_in_segment is is a list with sents that is appended to the
        # dictionary segments (with key "sents": segment["sents"]) when filled
        sents_in_segment = list()
        # sent_dic is a dictionary that is appended to "sents_in_segment" when filled
        # it contains two keys: "sents" and "len"
        # "sents" contains a sentence
        # "len" contains the length of a sentence
        sent_dic = {}
        # initialize that the values are integers and lists
        sent_dic["len"] = int()
        sent_dic["sent"] = list()
        # word-dic is a dictionary for every word in a sent that
        # contains the surface, pos and lemma of a word.
        word_dict = {}


        # the following loop aims to find an ending of a specific 'part' (sentence or segments)
        # segments end with the marker "===B", "===T" etc.
        # sentences end with an empty line
        # if the loop finds an empty line, it adds the sent_dic to the segment dictionary
        # if the loop finds the marker "===", it adds the segment dictionary to the corpus list
        for line in rn_stripped_lines:

            ##################
            # FILL CORPUS    #
            # WITH SEGMENTS  #
            ##################

            if "===" in line:
                # If a line equals to a segment marker (e.g. "===B"),
                # this id is set to the segment_id (1st key of the segment
                # dictionary)
                # the next loop strips the "===" from the Segment-ID
                if "===" in line:
                    segment_id = line.strip()
                # fill the segment dictionary with two keys
                # segment_id e.g. B, T, ...
                # sents with the sentences
                segment["segment_id"] = segment_id
                # All sentences are appended to the segment (as 2nd key
                # of the dictionary: segment["sents"])
                segment["sents"] = sents_in_segment
                # we have every information we need about the segment
                # so we append the segment to the corpus list
                corpus.append(segment)
                #Since the segment is complete, we start a new
                #empty segment dictionary
                sents_in_segment = list()
                segment = {}

            ##################
            # FILL SEGMENTS  #
            # WITH SENTENCES #
            ##################

            elif line == '':
                # first we add the length of the sentence to the corresponding key
                sent_dic["len"] = len(sent_dic["sent"])

                sents_in_segment.append(sent_dic)
                # Since the sentence is complete
                # we start a new empty sentence dictionary
                sent_dic = {}
                sent_dic["len"] = int()
                sent_dic["sent"] = list()

            ##################
            # FILL SENTENCES  #
            # WITH WORDS     #
            ##################

            else:
                # the CoNLL-format is tab seperated
                # we split by the tabs to get a list of the three informations
                # first item is SURFACE (the word itself)
                # second item is the PART OF SPEECH TAG
                # third item is the LEMMA
                splitted_line = line.split("\t")
                # add SURFACE, POS and LEMMA to word_dic
                word_dict['surface'] = splitted_line[0]
                word_dict['pos'] = splitted_line[1]
                word_dict['lemma'] = splitted_line[2]
                # this reader can also transform test data without label (has yet 
                # to be predicted)
                # if there is no annotation, give back "NA"
                if len(splitted_line) ==4:
                    word_dict['annotation'] = splitted_line[3]
                else:
                    word_dict['annotation'] = "NA"
                # append the word_dict to the sentence dictionary
                sent_dic["sent"].append(word_dict)
                # Since the word dictionary has all the information about the token
                # we start a new empty word dictionary
                word_dict={}
        if sents_in_segment !=[]:
            segment["sents"] = sents_in_segment
            corpus.append(segment)
        
        #############################################################################
        # Since the corpus list has a very difficult data-structure to loop,        #
        # we try to return only a simpled version of it.                            #
        # The classifier wants to label only words, not sentences as a whole.       #
        # So we make a list corpus_simple where every item is a dictionary with     #
        # the information we need: SURFACE, POS, LEMMA, SEGMENT-ID,                 #
        # the ANNOTATION,                                                           #
        # SENTENCE-ID (counts the sentences in a segment)                           #
        # WORD-ID (counts the words in a sentence), SENTENCE LENGTH.                #
        #############################################################################

        # open the a list for the corpus_simple
        corpus_simple = list()
        # start the counter for the sentences and words
        sent_label = 1
        word_label = 1

        # this goes through the corpus we filled in the functions above
        # and fills the corpus_simple
        for segment in corpus:
            segment_value = segment["segment_id"]
            for sent_dic in segment["sents"]:
                for token_dic in sent_dic["sent"]:
                    token_dic["segment_id"] = segment_value
                    token_dic["sent_id"] = sent_label
                    token_dic["word_id"] = word_label
                    token_dic["sent_len"] = sent_dic["len"]
                    corpus_simple.append(token_dic)
                    word_label += 1
                word_label = 1
                sent_label += 1

        # we return the corpus simple
        # however if you want to use the other data structure return corpus instead corpus_simple
        return corpus_simple

