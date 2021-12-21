import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
    #TOKENIZATION
from nltk.tokenize import word_tokenize, sent_tokenize
sentence = "Hello I am Atharva. I am pursuing engineering from PICT."
sentence_token = sent_tokenize(sentence)
word_token = word_tokenize(sentence)

#STOP WORDS
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print(stop_words)

filtered_sentence = []

for w in word_token:
        if w not in stop_words:
            filtered_sentence.append(w)
        

print(filtered_sentence)

#STEMMING
from nltk.stem import PorterStemmer
ps = PorterStemmer() 
stemmed_sentence = []
for w in filtered_sentence:
    stemmed_words = (ps.stem(w))
    stemmed_sentence.append(stemmed_words)
    

#LEMMATIZATION
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lemmatized_sentence = []
for w in filtered_sentence:
    lemmatized_words = lemmatizer.lemmatize(w)
    lemmatized_sentence.append(lemmatized_words)
    
print(lemmatized_sentence)
#PARTS OF SPEECH TAGGING
from nltk import pos_tag    
pos_word = pos_tag(filtered_sentence)


#Syntactic parsing is a technique by which segmented, tokenized, and part-of-speech tagged text is 
# assigned a structure that reveals the relationships between tokens governed by syntax rules,
#  e.g. by grammars.


import stanfordnlp
stanfordnlp.download('en')
chunker = nltk.RegexpParser(""" 
                       NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases 
                       P: {<IN>}               #To extract Prepositions 
                       V: {<V.*>}              #To extract Verbs 
                       PP: {<P> <NP>}          #To extract Prepostional Phrases 
                       VP: {<V> <NP|PP>*}      #To extarct Verb Phrases 
                       """) 

output = chunker.parse(pos_word) 

print(output)