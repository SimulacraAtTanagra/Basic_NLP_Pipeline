# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:32:08 2019

@author: shane
"""

def import_statement():
    global nltk
    import nltk
    from nltk import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import LancasterStemmer, WordNetLemmatizer
    from bs4 import BeautifulSoup
    global textract
    import textract
    global spacy
    import spacy
    from spacy.lang.en import English
    nltk.download('wordnet')
    from nltk.corpus import wordnet as wn
    nltk.download('stopwords')
    en_stop = set(nltk.corpus.stopwords.words('english'))
    global random
    import random
    global gensim
    import gensim
    from gensim import corpora
    global pandas
    import pandas
    global os
    global math
    import os
    import math
    global PyPDF2
    import PyPDF2
    global mobi
    from mobi import Mobi
    global wikipedia
    import wikipedia
    from wikipedia import search as wse
    from wikipedia import summary as wsu
    global wikipediaapi
    import wikipediaapi
    
def strip_html(text):                   #this function strips xml/ html coding to make clean text
    soup = BeautifulSoup(text, "html")
    return soup.get_text()

def epub_to_text(x):
    text = textract.process(x)              #textcract does the heavy lift
    text = strip_html(text)                #now we have a clean string of the entire book
    return(text,x)
def pdf_to_text(x):
    text = []
    with open(x,'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            text.append(pageObj.extractText())
            text = [item for sublist in text for item in sublist]
    return(text,x)
def corpus_processing(text,x):
    #this step tokenizes the contents of the book into individual words without doing anything else
    corpus= []
    for w in nltk.word_tokenize(text):
        corpus.append(w.lower())
    sent_corpus = []
    for s in nltk.sent_tokenize(text):
        sent_corpus.append(s)
    bag_of_words = list(set(corpus))
    words_per_sent = len(corpus)/len(sent_corpus)
    total_words = len(corpus)
    df = pandas.DataFrame().astype('object')    
    df[df.shape[1]]= text               #df.shape[1] allows to change this section without renumbering
    df[df.shape[1]]= [corpus]
    df[df.shape[1]]= [sent_corpus]
    df[df.shape[1]]= [bag_of_words]
    df[df.shape[1]]= words_per_sent
    df[df.shape[1]]= total_words
    df[df.shape[1]]= str(x)
    return(df)


#end tokenizer segment


def main():
    df = pandas.DataFrame().astype('object')                #makes it so things can be stored in df that are lists
    directory = os.fsencode(directory_in_str)           #defines directory as indicated string
    os.chdir(directory)                                 #navigate to directory specified
    for file in os.listdir(directory):                  #iterates over all the files here
        filename = os.fsdecode(file)                    #specifies filename from file
        if filename.endswith(".epub"):                  #isolates epub for further action
            try:
                df = df.append(corpus_processing(epub_to_text(filename)),ignore_index=True)  #appends results of function to df
            except:
                print(filename,"produced an error. Continuing.")        #or lets you know it couldn't
        elif filename.endswith(".pdf"):                  #isolates epub for further action
            try:
                df = df.append(corpus_processing(pdf_to_text(filename)),ignore_index=True)  #appends results of function to df
            except:
                print(filename,"produced an error. Continuing.")        #or lets you know it couldn't

        else:
            continue
    else:
        df.to_csv('summaryoutput.csv',index=False)      #writes dataframe to csv file to save memory

directory_in_str = 'C:\\Users\\shane\\Desktop\\books'
import_statement()
main()

wiki_wiki = wikipediaapi.Wikipedia('en')
termlist = ['einstein','richard nixon','polar bear']
def wikireport(list):
    for term in list:
        try:
            page_py = wiki_wiki.page(wse(term)[0])
            print(page_py.fullurl)
        except:
            print(term,"page not found")
