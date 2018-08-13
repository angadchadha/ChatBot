import spacy
from spacy.symbols import nsubj, VERB
import wikipediaapi

intro = print("\nI am a bot who tells the date of the things.\nDon't forget to put 'when' before the question.\n ")
while True:
    h = ""
    l1 = []
    i = 0
    o = 0
    word = input("Ask me a question: ")
    nlp  = spacy.load('en')
    doc = nlp(word)
    ncs = doc.noun_chunks
    entities = doc.ents
    sentences = doc.sents

    verbs = []

    for n in ncs:
            print("\nthe target subject is: ",n)
            h = str(n).replace("the", "")
    for n in sentences:
        print("the question type: ",n[0])
        print("the question details: ",n[1],n[5])




    wiki_wiki = wikipediaapi.Wikipedia('en')

    page_py = wiki_wiki.page(h)
    doc1 = nlp(page_py.summary)
    entities1 = doc1.ents
    if page_py.exists():
        for n in entities1:
                if n.label_ == "DATE":
                    i+=1
                    if i < 5:
                        l1 += n
        if len(l1) > 1:
            if l1[0] < l1[1]:
                print (l1[0])
        else:
            print(l1[0])
    else:
        print("Sorry,I didn't understand the question.\nPlease make sure you have put 'when' before the question.")
