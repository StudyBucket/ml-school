# this is where the features are extracted

# -*- coding: utf-8 -*-

import codecs
import random

class FeatureExtractor:

	# this is the constructor of the FeatureExtractor class
    def __init__(self):
        pass


	# THIS IS WHERE THE DIFFERENT FEATURE EXTRACTION FUNCTIONS ARE CALLED #
	# here you can change which features should be used by simply changing the function calls (commenting the line out)
    def extract_features(self,corpus):
		# featureset is a list
	    # a possible, exemplary output of the featureset list might look like this:
        #[({"surface": dog, "word_length": 3, "pos": NN, "lemma": dog, "segment_id": '===T', ...}, B-EntityPER)
		# {"surface": barks, "word_length": 5, "pos": VB, "lemma": bark, "segment_id": '===T', ...}, label)
		# {"surface": loudly, "word_length": 6, "pos": RB, "lemma": loud, "segment_id": '===T', ...}, label) ...]
        # where {{"surface": dog, "word_length": 3, "pos": ....} stands for one words features along with its label (in test case, label is e.g. X (dummy label))

        featureset = list()

		# this for-loop loops through every token in the dictionary of the corpus while at the same time indexing it
		# it then appends the dictionary and the annotation/label of the word to the featureset list (as seen above in the example)
        for index, token_dic in enumerate(corpus):
                    featureset.append(({"word":token_dic["surface"]},token_dic['annotation']))


                ####################################################################################
				# THIS IS WHERE ALL THE DIFFERENT POSSIBLE FEATURE EXTRACTION FUNCTIONS ARE CALLED #
				# COMMENT THEM IN OR OUT DEPENDING ON WHICH FEATURES YOU FIND USEFUL			   #
				####################################################################################

                    # structure of feature function for example of the feature "capitalized":
                    # -1 calls the last word that has been appended to the featureset
                    # 0 accesses the dictionary which is the first element of the tupel
                    # "capitalized" is the feature name

                    #featureset[-1][0]["pos"] = self.pos(token_dic)
                    #featureset[-1][0]["surface"] = self.surface(token_dic)
                    #featureset[-1][0]["surface_backwards"] = self.surface_backwards(token_dic)
                    #featureset[-1][0]["surface_every_second"] = self.surface_every_second(token_dic)
                    #featureset[-1][0]["word_length"] = self.word_length(token_dic)
                    #featureset[-1][0]["pos_first_character"] = self.pos_first_character(token_dic)
                    ##featureset[-1][0]["lemma"] = self.lemma(token_dic)
                    ##featureset[-1][0]["lemma_backwards"] = self.lemma_backwards(token_dic)
                    ##featureset[-1][0]["lemma_every_second"] = self.lemma_every_second(token_dic)
                    #featureset[-1][0]["segment_id"] = self.segment_id(token_dic)
                    #featureset[-1][0]["sent_id"] = self.sent_id(token_dic)
                    #featureset[-1][0]["word_id"] = self.word_id(token_dic)
                    #featureset[-1][0]["next_word"] = self.next_word(index, corpus)
                    #featureset[-1][0]["next_verb_in_sent"] = self.next_verb_in_sent(index, corpus)
                    #featureset[-1][0]["next_verb_in_sent_distance"] = self.next_verb_in_sent_distance(index, corpus)
                    #featureset[-1][0]["previous_verb_in_sent"] = self.previous_verb_in_sent(index, corpus)
                    #featureset[-1][0]["previous_verb_in_sent_distance"] = self.previous_verb_in_sent_distance(index, corpus)
                    #featureset[-1][0]["next_complete_verb_in_sent"] = self.next_complete_verb_in_sent(index, corpus)
                    #featureset[-1][0]["next_complete_verb_in_sent_distance"] = self.next_complete_verb_in_sent_distance(index, corpus)
                    #featureset[-1][0]["previous_complete_verb_in_sent"] = self.previous_complete_verb_in_sent(index, corpus)
                    #featureset[-1][0]["previous_complete_verb_in_sent_distance"] = self.previous_complete_verb_in_sent_distance(index, corpus)
                    #featureset[-1][0]["previous_word"] = self.previous_word(index, corpus)
                    ##featureset[-1][0]["next_lemma"] = self.next_lemma(index, corpus)
                    ##featureset[-1][0]["previous_lemma"] = self.previous_lemma(index, corpus)
                    #featureset[-1][0]["next_pos"] = self.next_pos(index, corpus)
                    #featureset[-1][0]["previous_pos"] = self.previous_pos(index, corpus)
                    #featureset[-1][0]["find_word_in_sentence74"] = self.find_word_in_sentence74(token_dic)
                    #featureset[-1][0]["contains_dot"] = self.contains_dot(token_dic)
                    #featureset[-1][0]["contains_dash"] = self.contains_dash(token_dic)
                    #featureset[-1][0]["only_vowels"] = self.only_vowels(token_dic)
                    #featureset[-1][0]["only_non_vowels"] = self.only_non_vowels(token_dic)
                    #featureset[-1][0]["sent_length"] = self.sent_length(token_dic)
                    #featureset[-1][0]["more_than_5_chars"] = self.more_than_5_chars(token_dic)
                    #featureset[-1][0]["word_is_ascii"] = self.word_is_ascii(token_dic)
                    #featureset[-1][0]["capitalized"] = self.capitalized(token_dic)
                    #featureset[-1][0]["previous_word_capitalized"] = self.previous_word_capitalized(index, corpus)
                    #featureset[-1][0]["next_word_capitalized"] = self.next_word_capitalized(index, corpus)
                    #featureset[-1][0]["fifth_word"] = self.fifth_word(index, corpus)
                    #featureset[-1][0]["all_upper_case"] = self.all_upper_case(token_dic)
                    #featureset[-1][0]["previous_word_all_upper_case"] = self.previous_word_all_upper_case(index, corpus)
                    #featureset[-1][0]["next_word_all_upper_case"] = self.next_word_all_upper_case(index, corpus)
                    #featureset[-1][0]["suffix"] = self.suffix(token_dic)
                    #featureset[-1][0]["suffix_2"] = self.suffix_2(token_dic)
                    #featureset[-1][0]["suffix_3"] = self.suffix_3(token_dic)
                    #featureset[-1][0]["all_digits"] = self.all_digits(token_dic)
                    #featureset[-1][0]["find_Mensch"] = self.find_Mensch(token_dic)


                    if (random.random() < 0.7):
                        featureset[-1][0]["lemma"] = self.lemma(token_dic)

                    if (random.random() < 0.6):
                        featureset[-1][0]["lemma_backwards"] = self.lemma_backwards(token_dic)

                    if (random.random() < 0.5):
                        featureset[-1][0]["lemma_every_second"] = self.lemma_every_second(token_dic)

                    if (random.random() < 0.5):
                        featureset[-1][0]["next_lemma"] = self.next_lemma(index, corpus)

                    if (random.random() < 0.5):
                        featureset[-1][0]["previous_lemma"] = self.previous_lemma(index, corpus)

                    if (random.random() < 0.5):
                        featureset[-1][0]["pos"] = self.pos(token_dic)

                    if (random.random() < 0.5):
                        featureset[-1][0]["next_pos"] = self.next_pos(index, corpus)

                    if (random.random() < 0.5):
                        featureset[-1][0]["previous_pos"] = self.previous_pos(index, corpus)

                    if (random.random() < 0.5):
                        featureset[-1][0]["next_word"] = self.next_word(index, corpus)

                    if (random.random() < 0.5):
                        featureset[-1][0]["previous_word_capitalized"] = self.previous_word_capitalized(index, corpus)

                    if (random.random() < 0.5):
                        featureset[-1][0]["next_word_capitalized"] = self.next_word_capitalized(index, corpus)
        return featureset


	#####################################################################
	# THESE ARE ALL THE DIFFERENT POSSIBLE FEATURE EXTRACTION FUNCTIONS #
	#####################################################################

	# This function returns the part of speech tag of the word
    def pos(self, word_dic):
        return word_dic["pos"]


	# This function returns the word itself
    def surface(self, word_dic):
        return word_dic["surface"]

    # This function returns the word backwards
    def surface_backwards(self, word_dic):
        return word_dic["surface"][::-1]

    # This function returns every second letter of the word
    def surface_every_second(self, word_dic):
        return word_dic["surface"][::2]


    #This function returns the first character of the pos-tag
    def pos_first_character(self, word_dic):
        return word_dic["pos"][:1]

	# This function returns the lemma of the word
    def lemma(self, word_dic):
        return word_dic["lemma"]

    # This function returns the lemma backwards
    def lemma_backwards(self, word_dic):
        return word_dic["lemma"][::-1]

    # This function returns every second letter of the lemma
    def lemma_every_second(self, word_dic):
        return word_dic["lemma"][::2]

	# This function returns the length of the word
    def word_length(self, word_dic):
        return len(word_dic["surface"])

	# This function returns the segment_id of the segment the word occurs in
    def segment_id(self, word_dic):
        return word_dic["segment_id"]

	# This function returns the sentence_id of the sentence the word occurs in
    def sent_id(self, word_dic):
        return word_dic["sent_id"]

	# This function returns the word_id of the word itself
    def word_id(self, word_dic):
        return word_dic["word_id"]

	# This function returns the next word which follows the word itself
	# if there is no following word (e.g. when the word itself is already the last word) the function returns "None"
    def next_word(self, index, corpus):
        try:
            if corpus[index+1]["sent_id"] == corpus[index]["sent_id"]:
                return corpus[index+1]["surface"]
        except IndexError:
            return None

    # This function returns the next verb within a sentence.
    # If there is no following verb, the function returns "None"
    def next_verb_in_sent(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        ind = index+1

        try:
            while corpus[ind]["sent_id"] == index_sent_id:
                if corpus[ind]["pos"].startswith("V"):
                    return corpus[ind]["surface"]
                ind += 1
            return None
        except IndexError:
            return None

    # This function returns the distance to the next verb within a sentence.
    # If there is no following verb, the function returns "None"
    def next_verb_in_sent_distance(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        next = 1

        try:
            while corpus[index + next]["sent_id"] == index_sent_id:
                if corpus[index + next]["pos"].startswith("V"):
                    return next
                next += 1
            return None
        except IndexError:
            return None


    # This function returns the previous verb within a sentence.
    # If there is no previous verb, the function returns "None"
    def previous_verb_in_sent(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        ind = index-1

        try:
            while corpus[ind]["sent_id"] == index_sent_id:
                if corpus[ind]["pos"].startswith("V"):
                    return corpus[ind]["surface"]
                ind += -1
            return None

        except IndexError:
            return None

    # This function returns the distance to the previous verb within a sentence.
    # If there is no previous verb, the function returns "None"
    def previous_verb_in_sent_distance(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        before = 1

        try:
            while corpus[index - before]["sent_id"] == index_sent_id:
                if corpus[index - before]["pos"].startswith("V"):
                    return before
                before += 1
            return None

        except IndexError:
            return None

    # This function returns only the next complete verb (VVFIN) within a sentence.
    # If there is no following complete verb, the function returns "None"
    def next_complete_verb_in_sent(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        ind = index + 1

        try:
            while corpus[ind]["sent_id"] == index_sent_id:
                if corpus[ind]["pos"].startswith("VVFIN"):
                    return corpus[ind]["surface"]
                ind += 1
            return None
        except IndexError:
            return None

    # This function returns the distance to the next complete verb (VVFIN) within a sentence.
    # If there is no following complete verb, the function returns "None"
    def next_complete_verb_in_sent_distance(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        next = 1

        try:
            while corpus[index + next]["sent_id"] == index_sent_id:
                if corpus[index + next]["pos"].startswith("VVFIN"):
                    return next
                next += 1
            return None
        except IndexError:
            return None

    # This function returns the previous complete verb (VVFIN) within a sentence.
    # If there is no previous complete verb, the function returns "None"
    def previous_complete_verb_in_sent(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        ind = index - 1

        try:
            while corpus[ind]["sent_id"] == index_sent_id:
                if corpus[ind]["pos"].startswith("VVFIN"):
                    return corpus[ind]["surface"]
                ind += -1
            return None

        except IndexError:
            return None

    # This function returns the distance to the previous complete verb (VVFIN) within a sentence.
    # If there is no previous complete verb, the function returns "None"
    def previous_complete_verb_in_sent_distance(self, index, corpus):
        index_sent_id = corpus[index]["sent_id"]
        before = 1

        try:
            while corpus[index - before]["sent_id"] == index_sent_id:
                if corpus[index - before]["pos"].startswith("VVFIN"):
                    return before
                before += 1
            return None

        except IndexError:
            return None

	# This function returns the previous word which preceeds the word itself
	# if there is no previous word (e.g. when the word itself is the first word) the function returns "None"
    def previous_word(self, index, corpus):
        if corpus[index-1]["sent_id"] == corpus[index]["sent_id"]:
             return corpus[index-1]["surface"]
        else:
            return None

	# This function returns the lemma of the following word
	# if there is no following lemma (e.g. when there is no following word) the function returns "None"
    def next_lemma(self, index, corpus):
        try:
            if corpus[index+1]["sent_id"] == corpus[index]["sent_id"]:
                return corpus[index+1]["lemma"]
        except IndexError:
            return None

	# This function returns the lemma of the previous word
	# if there is no previous lemma (e.g. when there is no previous word) the function returns "None"
    def previous_lemma(self, index, corpus):
        if corpus[index-1]["sent_id"] == corpus[index]["sent_id"]:
             return corpus[index-1]["lemma"]
        else:
             return None

	# This function returns the part of speech tag of the following word
	# if there is no following part of speech tag (e.g. when there is no following word) the function returns "None"
    def next_pos(self, index, corpus):
        try:
            if corpus[index+1]["sent_id"] == corpus[index]["sent_id"]:
                return corpus[index+1]["pos"]
        except IndexError:
            return None

	# This function returns the part of the speech tag of the previous word
	# if there is no previous part of speech tag (e.g. when there is no previous word) the function returns "None"
    def previous_pos(self, index, corpus):
        if corpus[index-1]["sent_id"] == corpus[index]["sent_id"]:
             return corpus[index-1]["pos"]
        else:
             return None

    # This function returns "True" if the word "ist" occurs in the 74th sentence, "False" otherwise
    def find_word_in_sentence74(self, word_dic):
        if word_dic["sent_id"] == 74:
            if "ist" in word_dic["surface"]:
                return True
            else:
                return False
        else:
            return False


	# This function returns "True" if the word contains a dot, "False" otherwise
    def contains_dot(self, word_dic):
        if "." in word_dic["surface"]:
            return True
        else:
             return False

	# This function returns "True" if the word contains a dash, "False" otherwise
    def contains_dash(self, word_dic):
        if "-" in word_dic["surface"]:
            return True
        else:
            return False

    # This functions returns only the vowels of a word
    def only_vowels(self, word_dic):
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        string_only_vowels = "".join([string for string in word_dic["surface"] if string in vowels])
        return string_only_vowels

    #This functions returns only non-vowels of a word (consonants, non literal-characters can be included)
    def only_non_vowels(self, word_dic):
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        string_only_non_vowels = "".join([string for string in word_dic["surface"] if string not in vowels])
        return string_only_non_vowels

	# This function returns the length of the sentence the word occurs in
    def sent_length(self, word_dic):
        return word_dic["sent_len"]

	# This function returns "True" if the word consists of more than five characters, "False" otherwise
    def more_than_5_chars(self, word_dic):
        if len(word_dic["surface"]) > 5:
           return True
        else:
            return False

	# This function returns "True" if the word only consists of ASCII-characters, "False" otherwise
    def word_is_ascii(self, word_dic):
        return all(ord(char) < 128 for char in word_dic["surface"])

	# This function returns "True" if the word starts with a capital letter, "False" otherwise
    def capitalized(self, word_dic):
        if word_dic["surface"][0].isupper():
            return True
        else:
            return False

    # This function returns "True" if the previous word starts with a capital letter, "False" otherwise
    def previous_word_capitalized(self, index, corpus):
        if corpus[index-1]["sent_id"] == corpus[index]["sent_id"]:
            if corpus[index-1]["surface"][0].isupper():
                return True
            else:
                return False

	# This function returns "True" if the next word starts with a capital letter, "False" otherwise
	# if there is no following word (e.g. when the word itself is already the last word) the function returns "None"
    def next_word_capitalized(self, index, corpus):
        try:
            if corpus[index+1]["sent_id"] == corpus[index]["sent_id"]:
                if corpus[index+1]["surface"][0].isupper():
                    return True
                else:
                    return False
        except IndexError:
            return None

    # This function returns the fifth word of the corpus
    def fifth_word(self, index, corpus):
        return corpus[5]["surface"]

	# This function returns "True" if the word only consists of capitalized letters, "False" otherwise
    def all_upper_case(self, word_dic):
        if word_dic["surface"].isupper():
            return True
        else:
            return False

    # This function returns "True" if the previous word only consists of capitalized letters, "False" otherwise
	# if there is no previous word (e.g. when the word itself is the first word) the function returns "None"
    def previous_word_all_upper_case(self, index, corpus):
        if corpus[index-1]["sent_id"] == corpus[index]["sent_id"]:
            if corpus[index-1]["surface"].isupper():
                return True
            else:
                return False

	# This function returns "True" if the next word only consists of capitalized letters, "False" otherwise
	# if there is no following word (e.g. when the word itself is already the last word) the function returns "None"
    def next_word_all_upper_case(self, index, corpus):
        try:
            if corpus[index+1]["sent_id"] == corpus[index]["sent_id"]:
                if corpus[index+1]["surface"].isupper():
                    return True
                else:
                    return False
        except IndexError:
            return None

	# This function returns "True" if one of the suffixes are found at the end of the word, "False" otherwise
    def suffix(self, word_dic):
        suffix = "ung", "ling", "heit", "schaft", "keit"
        if word_dic["surface"].endswith(suffix):
            return True
        else:
            return False

    # This suffix-function returns the last two characters of a word
    def suffix_2(self, word_dic):
        return word_dic["surface"][-2:]

    # This suffix-function returns the last three characters of a word
    def suffix_3(self, word_dic):
        return word_dic["surface"][-3:]

	# This function returns "True" if the word only consists of numbers, "False" otherwise
    def all_digits(self, word_dic):
        if word_dic["surface"].isdigit():
            return True
        else:
            return False

   # This function returns the word_id of the word "Mensch", "None" if the word "Mensch" does not occur in the sentence
    def find_Mensch(self, word_dic):
        if "Mensch" in word_dic["surface"]:
            return word_dic["word_id"]
        else:
            return None
