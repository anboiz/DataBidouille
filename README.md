# DataBidouille

DataBidouille est une série d'exercices destinée à faire découvrir les manipulations de base de données sous forme de tableaux à l'aide de Python à des débutants.

## Comment utiliser DataBidouille
TODO

## Python

Python est un langage de programmation créé en 1991 par Guido van Rossum. Publié sous licence libre (*Python Software Foundation License*), il est réputé dans le monde de l'enseignement comme étant une bonne initiation aux concepts de base de la programmation.

Au delà de l'aspect, pédagogique, Python se caractérise également par une communauté très active fournissant de nombreux outils - eux aussi la plupart du temps sous licences libres - notamment dans la manipulation, le traitement de données ainsi que l'intelligence artificielle. Très utilisé, par les grandes entreprises du numérique, celles-ci contribuent activement au développement de l'écosystème python. De nombreux outils sont mis à disposition par ces sociétés. On peut citer par exemple :
- **TensorFlow**, outil d'apprentissage automatique développé par Google, opensourcé en 2015 ;
- **PyTorch**, outil d'apprentissage automatique développé par Meta, publié pour la première fois en 2016 et donné à la Linux Fondation en 2022 ;
- **OpenCV**, spécialisé dans le traitement et la reconnaissance d'image, développé initialement par Intel, publié depuis 2000.

### Installation

Bien sûr en premier lieu, il est nécessaire d'installer l'interpréteur Python qui sera à même d'executer les scripts.

Il est possible d'installer l'interpréteur Python directement depuis le site [python.org](https://www.python.org/downloads/).

Toutefois, certaines distributions offrent des outils complémentaires qui seront utiles par la suite. C'est le cas notamment des distributions **conda** qui en plus de permettre d'installer python sans disposer des droits administrateurs sur son poste, offre une gestion simplifié des environnements virtuels (voir plus loin).

L'installation minimale pour **conda**, s'appelle miniconda et sera suffisante pour la plupart des cas d'usage.

Les liens de téléchargement des installateurs pour les différentes plateformes sont disponibles sur le [site officiel de conda](https://docs.conda.io/en/latest/miniconda.html). Laissez-vous guider par les instructions.

> A la fin de l'installation, si vous utilisez un poste qui accède à internet *via* un serveur mandataire (ou *proxy*), il est nécessaire de régler les paramètres de conda afin qu'il puisse également accéder à internet. Pour cela il faut saisir la commande ```conda config```. Puis d'ajouter dans le fichier ```.condarc``` ainsi créé les éléments suivants :
>
> ```yaml
>   proxy_servers:
>       http: http://user:pass@corp.com:8080
>       https: https://user:pass@corp.com:8080
> ```
> En remplaçant les informations par celles correspondant à votre organisation.

### Les bibliothèques logicielles

La bibliothèque standard de Python est très grande, elle offre un large éventail d'outils. Elle peut être complétée par des bibliothèques optionnelles qui apportent des fonctionnalités ou des méthodes de travail complémentaires.

L'installation de ces bibliothèques se fait à l'aide des collections publiques qui permettent leur publication et leur diffusion. 

Par exemple, PyPI le répertoire le plus populaire rassemble à date 440 000 projets

Pour installer ```pandas```, une seule ligne de commande suffit :

```bash
pip install pandas
```

ou

```bash
conda install pandas
```

Les bibliothèques les plus utiles dans pour la manipulation de données vont être (entre autres) :

- **pandas** : permettant la manipulation et l'analyse des données. Elle propose en particulier des structures de données et des opérations de manipulation de tableaux numériques et de séries temporelles. Pandas est un logiciel libre sous licence BSD2. Son nom est dérivé du terme Panel Data (en français "données de panel", un terme d'économétrie pour les jeux de données qui comprennent des observations sur plusieurs périodes de temps pour les mêmes individus). Son nom est également un jeu de mots sur l'expression "Python Data Analysis". [Plus d'informations](https://fr.wikipedia.org/wiki/Pandas)

- **jupyter** : application web utilisée pour programmer dans plus de 40 langages de programmation, dont Python, Julia, Ruby, R, ou encore Scala. C'est un projet communautaire dont l'objectif est de développer des logiciels libres, des formats ouverts et des services pour l'informatique interactive. Jupyter est une évolution du projet IPython. Jupyter permet de réaliser des calepins ou notebooks, c'est-à-dire des programmes contenant à la fois du texte, simple ou enrichi typographiquement et sémantiquement grace au langage à balises simplifié Markdown, et du code, lignes sources et résultats d'exécution. Ces calepins sont notamment utilisés en science des données pour explorer et analyser des données. [Plus d'informations](https://fr.wikipedia.org/wiki/Jupyter)

### Les environnements virtuels

Les programmes Python utilisent souvent des paquets et modules qui ne font pas partie de la bibliothèque standard. Ils nécessitent aussi, parfois, une version spécifique d'une bibliothèque, par exemple parce qu'un certain bogue a été corrigé ou encore que le programme a été implémenté en utilisant une version obsolète de l'interface de cette bibliothèque.

Cela signifie qu'il n'est pas toujours possible, pour une installation unique de Python, de couvrir tous les besoins de toutes les applications. Basiquement, si une application A dépend de la version 1.0 d'un module et qu'une application B dépend de la version 2.0, ces dépendances entrent en conflit et installer la version 1.0 ou 2.0 laisse une des deux applications incapable de fonctionner.

La solution est de créer un environnement virtuel, un dossier auto-suffisant qui contient une installation de Python pour une version particulière de Python ainsi que des paquets additionnels.

Différentes applications peuvent alors utiliser des environnements virtuels différents. Pour résoudre l'exemple précédent où il existe un conflit de dépendances, l'application A a son environnement virtuel avec la version 1.0 installée pendant que l'application B a un autre environnement virtuel avec la version 2.0. Si l'application B requiert que la bibliothèque soit mise à jour à la version 3.0, cela n'affecte pas l'environnement de A.

Pour créer un environnement virtuel avec conda :

```bash
conda create --name mon_environnement python=3.7
```
Cette commande crée un environnement appelé ```mon_environnement```, autour de la version ```3.7``` de python.

Une fois l'environnement crée, il est possible de l'activer avec la commande :
```bash
conda activate mon_environnement
```

## L'environnement de développement intégré (IDE)

Développer un script peut être fait directement dans un éditeur de texte, toutefois, avoir recours à un environnement de développement intégré va offrir des outils pour faciliter le développement :
- un éditeur de texte spécialisé dans le développement : coloration syntaxique, indentation du code, autocomplétion
- une interface pour le gestionnaire de version
- un débogueur pour executer le code ligne par ligne etc.

Certains IDE sont spécialisé pour un langage de programmation donné, d'autres sont plus généraliste.

Pour Python les IDE les plus connus sont :
- PyCharm
- Spyder
- Visual Studio Code

C'est ce dernier que je vous conseille d'utiliser.

### VSCode/VSCodium
Visual Studio Code (VSCode pour les intimes), est un IDE développé dont le code source est public (et sous licence MIT). Toutefois, le logiciel diffusé par Microsoft, VSCode, s'il est gratuit est dans une licence propriétaire et intègre des fonctionnalité de télémétrie.

C'est la raison pour laquelle, la communauté open-source a décidé de re-compiler le code fourni par Microsoft et de distribuer programme sous une licence réellement open-source (MIT). Ce produit s'appelle VSCodium.

Ainsi bien qu'ils aient les mêmes fonctionnalités, les différences en termes de licence font que seul VSCodium fait partie du socle interministériel de logiciels libres (SILL).[Plus d'informations](https://sill.etalab.gouv.fr/)


### L'installation

[Lien de téléchargement](https://github.com/VSCodium/vscodium/releases).
Choisir le paquet *"VSCodiumUserSetup"* ia32 ou x64 suivant votre version de windows.

### Les extensions
TODO

## Fonctionnement général : script vs calepin (notebook)
TODO

## Liste des exercices :

- [X] Charger des données (Lire un fichier, un ensemble de fichiers, les concaténer)
- [ ] Écrire des données sur le disque TODO
- [ ] Filtrer les données (Extraire des données correspondant à une partie de l'ensemble de départ) TODO
- [ ] Créer de nouvelles colonnes (Ajouter des colonnes à nos tableaux de données) TODO
- [ ] Réaliser une jointure (Lier les informations de deux tableaux) TODO
- [ ] Réaliser des regroupements TODO
