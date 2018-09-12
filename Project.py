import spacy
from spacy.symbols import nsubj, VERB
import wikipedia

class ChatBot:
    intro = print("\nI am a bot who tells the date of the things.\nDon't forget to put 'when' before the question.\n ")
    def chat():
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

            for n in doc:
                if n.dep_ == "advmod":
                    print ("the question type: ", n)
                if n.dep_ == "nsubj" or n.dep_ == "ccomp":
                    print ("the question details: ", n)


            try:
                page_py = wikipedia.page(h)
                doc1 = nlp(page_py.summary)
                entities1 = doc1.ents

            except wikipedia.exceptions.PageError:
                print("Wikipedia page does not exist! Try again.")
                exit(1)

            oldest=0
            for n in entities1:
                if n.label_ == "DATE":
                    l1.append(n);
                    if l1[i] < l1[oldest]:
                        oldest=i

            print(l1[oldest])
    if __name__ == '__main__':
        chat()
