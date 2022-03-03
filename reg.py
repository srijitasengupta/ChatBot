import nltk
from nltk.corpus import wordnet
import re

list_words=['hello','describe','role','website','help', 'operate','refund','located','add','view','buy']

dict_syn={}

for word in list_words:
    #print(word)
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            synonyms.append(lem.name())
    #print(set(synonyms))
    dict_syn[word]=set(synonyms)
#print(dict_syn)
keywords={}

keywords['greet']=[]

for synonym in list(dict_syn['hello']):
    keywords['greet'].append('.*\\b'+synonym+'\\b.*')

keywords['about_chatbot']=[]
keywords['about_chatbot'].append('.*who.*you.*')
for synonym in list(dict_syn['describe']):
    keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*')

keywords['role']=[]
for synonym in list(dict_syn['role']):
    keywords['role'].append('.*\\b'+synonym+'\\b.*')

keywords['about_site']=[]
for synonym in list(dict_syn['website']):
    keywords['about_site'].append('.*\\b'+synonym+'\\b.*')

keywords['site_functionality']=[]
for synonym in list(dict_syn['help']):
    keywords['site_functionality'].append('.*\\b'+synonym+'\\b.*')

keywords['add_books']=[]
for synonym in list(dict_syn['add']):
    keywords['add_books'].append('.*\\b'+synonym+'\\b.*')

keywords['view_books']=[]
for synonym in list(dict_syn['view']):
    keywords['view_books'].append('.*\\b'+synonym+'\\b.*')

keywords['buy_books']=[]
for synonym in list(dict_syn['buy']):
    keywords['buy_books'].append('.*\\b'+synonym+'\\b.*')

keywords['add_bookname']=[]
keywords['add_bookname'].append('.*\\b'+"bookname is"+'\\b.*')

keywords['add_authorname']=[]
keywords['add_authorname'].append('.*\\b'+"authorname is"+'\\b.*')

keywords['buy_bookname']=[]
keywords['buy_bookname'].append('.*\\b'+"buybook"+'\\b.*')
patterns={}

for intent, keys in keywords.items():
    patterns[intent]=re.compile('|'.join(keys))
#print(patterns)