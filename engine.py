import networkx as nx
import pandas as pd
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

class SynEngine:

    stop = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    dt = {'from' : str, 'to' : str, 'val' : float}
    dsim = pd.read_csv("./bap.csv", dtype = dt, quotechar="'", escapechar = '\\', )

    def __init__(self, phrase, word):

        self.phrase = {i for i in phrase.lower().split() if i not in SynEngine.stop}

        self.word = word

        self.synonyms = {j.replace('_', ' ') for i in wn.synsets(word) for j in i.lemma_names()} - {self.word}
        self.synonyms = {i for i in self.synonyms if SynEngine.lemmatizer.lemmatize(i) != SynEngine.lemmatizer.lemmatize(self.word)}

        self.graph = nx.DiGraph()

        self.words = self.phrase | {word} | self.synonyms
        #self.graph.add_nodes_from(words)

        sim = SynEngine.dsim[(SynEngine.dsim['from'].isin(self.words)) & (SynEngine.dsim['to'].isin(self.words))]
        self.graph.add_nodes_from(set(sim.values[:,0])|set(sim.values[:,1]))

        for i, j, v in sim.values:
            if not self.graph.has_edge(j,i) and not self.graph.has_edge(i,j):
                self.graph.add_edge(i,j,weight=v)
            if self.graph.has_edge(j,i) and self.graph[j][i]['weight'] < v:
#                print(i,j,v)
#                print(self.graph.has_edge(j,i), self.graph.has_edge(j,i), self.graph.has_edge(i,j))
                self.graph.add_edge(i,j,weight=v)
                self.graph.remove_edge(j,i)

#        [self.graph.add_edge(i,j,weight=v) for i, j, v in sim.values\
#            if ((self.graph.has_edge(j,i) and self.graph[j][i]['weight'] < v)\
#            or (not self.graph.has_edge(j,i) and not self.graph.has_edge(i,j)))]

    def getSyn(self):
        d = {k : nx.pagerank(self.graph)[k] for k in self.graph.nodes() if k in self.synonyms}
        return [(k,d[k]) for k in sorted(d, key=d.get, reverse=True)]
