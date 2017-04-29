# Synonymie et thésaurus distributionnels

André Nasturas et Benjamin Loglisci

------

Ce dépôt contient les codes sources de l'application de proposition de synonymes en fonction du contexte que nous avons réalisé dans le cadre du projet du cours de Traitement Automatisé du Langage naturel (TAL) du master Données Apprentissage et Connaissances (DAC) de l'Université Pierre et Marie Curie (UPMC).

## Prérequis

### Base de données

Une base de données de relations sémantiques orientés entre les mots est nécessaire à l'utilisation de ce programme. En raison de son poids important, nous l'avons stocké en dehors du dépôt de code sources.

Il s'agit d'un fichier CSV de 326.44 Mo que nous avons constitué en traitant une base déjà existante obtenue dans [un autre projet GitHub](https://github.com/hltfbk/Excitement-Open-Platform/wiki/English-Knowledge-Resources).

Ce fichier peut être téléchargé directement sur [Dropbox](https://www.dropbox.com/s/868k526d983qqdm/bap.csv?dl=0).

### Dépendances Python

Ce programme fonctionne sous Python 3. Il requiert les paquets suivants :

*	nltk
    -   corpus.stopwords
    -   corpus.wordnet
    -   stem.WordNetLemmatizer
*	pandas
*	networkx
*	matplotlib

## Utilisation

Exécuter le client :

```
    python3 client.py
```

Le programme s'exécute dans la console de manière interactive. Il est demandé  à l'utilisateur de taper un mot, puis une phrase contextualisant le mot. Le programme proposera ensuite les synonymes trouvés, dans l'ordre décroissant de probabilité, accompagné de leur score PageRank, ainsi que l'affichage du graphe des relations de synonymie tel que construit par l'algorithme implémenté.
