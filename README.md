# DataBidouille

DataBidouille est une série d'exercices destinée à faire découvrir les manipulations de base de données sous forme de tableaux à l'aide de Python à des débutants.

## Python

Python est un langage de programmation créé en 1991 par Guido van Rossum. Publié sous licence libre (*Python Software Foundation License*), il est réputé dans le monde de l'enseignement comme étant une bonne initiation aux concepts de base de la programmation.

Au delà de l'aspect, pédagogique, Python se caractérise également par une communauté très active fournissant de nombreux outils - eux aussi la plupart du temps sous licences libres - notamment dans la manipulation, le traitement de données ainsi que l'intelligence artificielle. Très utilisé, par les grandes entreprises du numérique, celles-ci contribuent activement au développement de l'écosystème python. De nombreux outils sont mis à disposition par ces sociétés. On peut citer par exemple :
- **TensorFlow**, outil d'apprentissage automatique développé par Google, opensourcé en 2015 ;
- **PyTorch**, outil d'apprentissage automatique développé par Meta, publié pour la première fois en 2016 et donné à la Linux Fondation en 2022 ;
- **OpenCV**, spécialisé dans le traitement et la reconnaissance d'image, développé initialement par Intel, publié depuis 2000.

### Installation

Bien sûr en premier lieu, il est nécessaire d'installer l'interpréteur Python qui sera à même d'executer les scripts.

Il est possible d'installer l'interpréteur Python directement depuis le site [python.org](https://www.python.org/downloads/).

Toutefois, certaines distributions offrent des outils complémentaires qui seront utiles par la suite. C'est le cas notamment des distributions **conda** qui en plus de permettre d'installer python sans disposer des droits administrateurs sur son poste, offre une gestion simplifé des environnements virtuels (voir plus loin).

L'installation minimale pour **conda**, s'appelle miniconda et sera suffisante pour la plupart des cas d'usage.

Les liens de téléchargement des installateurs pour les différentes plateformes sont disponibles sur le [site officiel de conda](https://docs.conda.io/en/latest/miniconda.html). Laissez-vous guider par les instructions.

> A la fin de l'installation, si vous utilisez un poste qui accède à internet *via* un serveur mandataire (ou *proxy*), il est nécessaire de régler les paramètres de conda afin qu'il puisse également accéder à internet. Pour celà il faut saisir la commande ```conda config```. Puis d'ajouter dans le fichier ```.condarc``` ainsi créé les éléments suivants :
>
> ```yaml
>   proxy_servers:
>    http: http://user:pass@corp.com:8080
>    https: https://user:pass@corp.com:8080
> ```
> En remplaçant les informations par celles correspondant à votre organisation.

