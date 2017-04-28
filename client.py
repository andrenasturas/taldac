import sys
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from engine import SynEngine

print("")
print("Synonymie contextuelle")
print("----------------------")
print("")

print("Chargement des dépendances...\t\t\033[92m\033[1mOK\033[0m\n")

while(True):
    print("Lecture de la phrase à analyser.")
    w = input("Tapez le mot dont vous cherchez un synonyme : ")
    s = input("Tapez la phrase de contexte : ")
#    print("Phrase entrée : \033[0;36m" + b + "\033[0m\033[1;36m " + w + "\033[0m\033[0;36m " + e + "\033[0m\n")
    print("Création du graphe...", end="\t")

    t = SynEngine(s, w)

    print("\t\t\t\033[92m\033[1mOK\033[0m\n")

    print("Mot étudié : \033[1;36m " + t.word + "\033[0m")
    print("Contexte : \033[0;36m" + ' '.join(t.phrase) + "\033[0m")

    r = t.getSyn()
    print(str(len(r)) + " synonymes trouvés :")
    if len(r) > 0:
        print("\033[1;32m" + r[0][0] + "\033[0m\t" + str(r[0][1]))
    if len(r) > 1:
        for i in r[1:]:
            print("\033[;1m" + i[0] + "\033[0m\t" + str(i[1]))

    inp = input("Afficher le  graphe ? y/[n] ")
    if len(inp) > 0 and inp[0] == 'y':
        nx.draw_networkx(t.graph)
        plt.show()

    inp = input("Analyser une autre phrase ? [y]/n ")
    if len(inp) > 0 and inp[0] == 'n':
        exit(0)
