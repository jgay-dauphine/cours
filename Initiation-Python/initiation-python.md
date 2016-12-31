class: center, middle

# Introduction à Python

.left[Intervenant : Jean-Christophe Gay]

.left[Mail : jean-christophe.gay@dauphine.fr]

.left[Bureau : B038]

---

name: plan

# Plan du cours

1. [Introduction](#Introduction)
2. [Premiers pas avec Python](#fisrtSteps)
3. Structures de données
4. Nombres Aléatoires
5. Chaînes de caractères
6. Parsing Web
7. Gestion de Documents
8. Automatisation de tâches
9. Préparation des Projets 

---

name: Introduction

# Introduction

Jean-Christophe Gay : 
* Responsable du Pôle Infrastructure et Intégration
* RSSI de l'université Paris-Dauphine
* Docteur en Informatique

Expérience :
* 5 ans de développement en laboratoire
* 5 ans de développement pour l'Université Paris-Dauphine

---

# Déroulé du cours

* aaa
* bbb
* ccc

---

# Notes et examens

Réalisation d'un projet au choix dans une liste. Le projet sera l'unique moyen 
d'évaluation de ce cours.

---

name: firstSteps

# Premiers pas en Python


- Pourquoi Python ?
--

- Python 2.7.13 ?7?
- Python 3.6.0 ???
--

- Installation
--

- Lancer Python et le quitter
---

name: whyPython

# Premiers pas en Python

.left-column[
### Pourquoi Python ?
]
.right-column[
- Nous vivons dans un monde d'information
- Il y a beaucoup trop d'informations disponible à un moment donné
- Il faut un moyen de réduire l'information, particulièrement l'information financière
]
---

# Premiers pas en Python

.left-column[
### Pourquoi Python ?
]
.right-column[
- Python est gratuit ;
- Python est puissant, flexible et simple à apprendre ;
- Python est plus adapté au Big Data que R ;
- Python se compose de nombreux modules.
]
---
name: PythonVersion

# Premiers pas en Python

.left-column[
### Pourquoi Python ?
### Version de Python ?
]
.right-column[
- Il existe deux versions concurrentes de python : 2.7 et 3.6
- Les différences majeures sont :
 - print 'Hello World' fonctionne en version 2 mais pas en 3
 - les divisions entières sont différentes
 - plus sur
   [http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)
- Pour ce cours les différences ne seront pas très importantes.
]

---
name: InstallingPython

# Premiers pas en python

.left-column[
### Pourquoi Python ?
### Version de Python ?
### Installation de Python
]
.right-column[
Mettre ici quelques notes sur l'installation de Python, 1 slide, 2 images max
ce n'est pas le but du cours
## Procédure d'installation :
- Se rendre sur le site de Python : [www.python.org](www.python.org)
- Section "Download" puis "Windows"
- Choisir l'installer qui convient
]
---

name: InstallingPython

# Premiers pas en python

.left-column[
### Pourquoi Python ?
### Version de Python ?
### Installation de Python
]
.right-column[
Mettre ici quelques notes sur l'installation de Python, 1 slide, 2 images max
ce n'est pas le but du cours
## Procédure d'installation :
- Se rendre sur le site de Python : [www.continuum.io](www.continuum.io)
- Section "Download" puis "Windows"
- Choisir l'installer qui convient
]
---
name: fisrtLaunch

Mettre sur deux colonnes des examples de lancement et de quittage de Python
Avec quelques exemples comme 2+2 ou encore ln(1)

---

name: secondLaunch

# Une première approche

Texte du livre...

```python
>>> 100 / (1 + 0.1)
90.9090909090909090
>>>
```

---

# Une première erreure

Que se passe-t-il la fois prochaine ??
```python
>>> 100 / (1+0.1)^2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
* TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>>
```
En Python il faut utiliser '\*\*' et non '^' pour les puissances.

---

# Attention à la case !

```python
>>> x=2
>>> X
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'X' is not defined
>>>
```
--


Lorsque l'on nomme des variables ou des fonctions il faut faire attention à la
case que l'on utilise. En effet Python est sensible à la case.

---

# Type des variables

En Python les variables n'ont pas de type propre. Elles ont le type de la
valeur qu'elles contiennent.

```python
>>> x = 2
>>> x
2
* >>> # x est un entier
>>> x="aa"
>>> x
'aa'
* >>> # x est une chaîne de caractères
>>>
```

---

name: findingHelp

# Trouver de l'aide

Facile : on en demande

```python
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help>
```
---
count: false

# Trouver de l'aide

```python
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                if                  print
as                  else                import              raise
assert              except              in                  return
break               exec                is                  try
class               finally             lambda              while
continue            for                 not                 with
def                 from                or                  yield
del                 global              pass                

help> 
```
---
# Trouver de l'aide en ligne

* Google + Stackoverflow
* Python Site
* Tutoriels divers...

---

# Version de Python

* Avec un terminal :
** python --version
** python -V
* Avec Python
```python
>>> import sys
>>> print sys.version
2.7.12 (default, Nov 19 2016, 06:48:10)
[GCC 5.4.0 20160609]
```

---

# Exercices

* Trouver l'aire d'un disque de diamètre 10 cm ;
* Trouver la longueur de la diagonale d'un carré de côté 1 ;
* Quelle est la circonférence d'un champs trapézoidal dont les côté font 127
  mètres chacuns ?

---

count: false

# Solutions

```python
>>> aire=3.141592653*10**2
>>> aire
314.1592653
>>>
```
--

```python
>>> diag=2**0.5
>>> diag
1.4142135623730951
```

```python
>>> 127 + 127 + 127 + 127
508
```

---

# Utilisation de Python comme d'une calculatrice

# Introduction aux modules

# Premier code depuis un fichier

# Fonctions classes et méthodes

# Automate the boring stuff with python

# A la marge :
Git
GitHub

---

# Bibliographie

* Python for Finance, Yuxin Yan, PACK, date ?
* Automate the boring stuff with Python
* Python for Finance, O'Reilly
* Mettre au moins un autre livre

# Some Code Inside

Code:

```python
def add(a,b):
    return a + b
```

---
count: false

# Some Code Inside

Code:

```python
def add(a,b):
*   return a + b
```

Notice the return statement

---

# Display and Inline

1. This is an inline integral: `\(\int_a^bf(x)dx\)`
2. More `\(x={a \over b}\)` formulae.

Display formula:

$$e^{i\pi} + 1 = 0$$

 
