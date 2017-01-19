class: center, middle

# Introduction à Python

.left[Intervenant : Jean-Christophe Gay]

.left[Mail : jean-christophe.gay@dauphine.fr]

.left[Bureau : B038]

---

name: plan

# Plan du cours

1. [Introduction](#Introduction)
2. [Premiers pas avec Python](#firstSteps)
3. [Utilisation de Python en Quelques Lignes](#UsingPythonAsCalculator)
4. [Contrôle de Flux](#FlowControl)
5. [Programmation Fonctionnelle](#Functions)
6. [Réalisation d'un solver de Sudoku](#ProjectSudoku)

???

3. Structures de Données
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
- mail: jean-christophe.gay@dauphine.fr
- Bureau: B038 (de temps en temps et surtout le matin)

Expérience :
- 5 ans de développement en laboratoire
- 5 ans de développement pour l'Université Paris-Dauphine

???

Parler de
- Responsable du Pôle Infrastructure et Intégration
- RSSI de l'université Paris-Dauphine
- Docteur en Informatique


# Notes et examens

Réalisation d'un projet au choix dans une liste. Le projet sera l'unique moyen
d'évaluation de ce cours.

---

name: whatIsPython

# Qu'est-ce que Python ?

Wikipédia :

--
> Python est un **langage de programmation** objet, multi-paradigme et multiplateformes. Il favorise la programmation **impérative structurée, fonctionnelle et orientée objet**. Il est doté d'un **typage dynamique fort**, d'une **gestion automatique de la mémoire** par ramasse-miettes et d'un système de gestion d'**exceptions** ; il est ainsi similaire à Perl, Ruby, Scheme, Smalltalk et Tcl.

--
>
> Le langage Python est placé sous une **licence libre** proche de la licence BSD et fonctionne sur la plupart des plates-formes informatiques, des supercalculateurs aux ordinateurs centraux, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et aussi avec Java ou encore .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser.


???


---

name: firstSteps

# Premiers pas en Python
<br/>
### Pourquoi Python ?
### Version de Python ?
### Installation de Python
### Lancement de l'interpréteur
### Une premiere opération
### On quitte

???

- Pourquoi Python ?

- Python 2.7.13 ?7?
- Python 3.6.0 ???

- Installation

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

## Procédure d'installation :
- Se rendre sur le site de Python : [www.continuum.io](www.continuum.io)
- Section "Download" puis "Windows"
- Choisir l'installer qui convient

]
---
name: fisrtLaunch

# Premiers pas en python

.left-column[
### Lancement de l'interpréteur
]
.right-column[

Dans un "terminal" lancer la commande python.

Cet interpréteur peut être utilisé pour lancer des commandes python et ainsi réaliser des calculs. Nous allons essayer rapidement.

]

---

# Premiers pas en python

.left-column[
### Lancement de l'interpréteur
### Une premiere opération
]
.right-column[

Dans l'interpréteur :

```python
>>> 1 + 1
2
>>> a = 1
>>> print a
1
>>> a + 2
3
```
]

---

# Premiers pas en python

.left-column[
### Lancement de l'interpréteur
### Une premiere opération
### On quitte
]
.right-column[

Dans l'interpréteur :

```python
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> quit()
```
]

---

name: secondLaunch

# Une première utilisation de Python

Si nous estimons qu'un retour de 100€ est attendu au bout d'un an avec
une remise annuelle de 10%. La valeur actuelle d'une rentrée future d'argent
est la suivante :

$$PV = { FV \over (1+R)^n }$$

Dans cette équation PV représente la valeur présente et FV la valeur
future, R est la remise et n le nombre de périodes.

Quelle est la valeur actuelle ?

```python
>>> 100 / (1 + 0.1)
```
---

# Une première utilisation de Python

Si nous estimons qu'un retour de 100€ est attendu au bout d'un an avec
une remise annuelle de 10%. La valeur actuelle d'une rentrée future d'argent
est la suivante :

$$PV = { FV \over (1+R)^n }$$

Dans cette équation PV représente la valeur présente et FV la valeur
future, R est la remise et n le nombre de périodes.

Quelle est la valeur actuelle ?

```python
>>> 100 / (1 + 0.1)
90.9090909090909090
>>>
```

---

# Une première erreure

Que se passe-t-il pour la prochaine période ?
```python
>>> 100 / (1+0.1)^2
```

---

count: false

# Une première erreure

Que se passe-t-il pour la prochaine période ?
```python
>>> 100 / (1+0.1)^2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
* TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>>
```

En Python il faut utiliser '\*\*' et non '^' pour les puissances.

---
count: false
# Une première erreure

Que se passe-t-il pour la prochaine période ?
```python
>>> 100 / (1+0.1)^2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
* TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>>
```

En Python il faut utiliser '\*\*' et non '^' pour les puissances.

```python
>>> 100 / (1+0.1)**2
82.64462809917354
```
---

# Attention à la case !

```python
>>> x=2
>>> X
```

---
count: false
# Attention à la case !

```python
>>> x=2
>>> X
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
*NameError: name 'X' is not defined
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
*>>> # x est un entier
>>> x="aa"
>>> x
'aa'
*>>> # x est une chaîne de caractères
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

# Solutions

- Exercice 1
```python
>>> aire=3.141592653*10**2
>>> aire
314.1592653
>>>
```
--
- Exercice 2
```python
>>> diag=2**0.5
>>> diag
1.4142135623730951
```
--
- Exercice 3
```python
>>> 127 + 127 + 127 + 127
508
```
---

name: UsingPythonAsCalculator
# Utilisation de Python en Quelques Lignes
<br/>
## Jouons avec les variables
## Le module mathématique
## Quelques fonctions utiles
## Les tuples

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
]
.right-column[
* On assigne des valeurs aux variables :
```python
>>> a = 1
>>> aa = 'Salut'
>>> b = 2
>>> a + b
3
```

* Afficher le contenu d'une variable :
```python
>>> a
1
>>> aa
'Salut'
>>> print a
1
>>> print aa
Salut
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
]
.right-column[
* Quelques erreurs :
```python
>>> aaa
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
*NameError: name 'aaa' is not defined
```
```python
>>> sqrt(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
*NameError: name 'sqrt' is not defined
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
]
.right-column[
* Du nommage des variables
```python
>>> # Mauvais exemple
>>> x = 100
>>> y = 0.1
*>>> z = x / ( 1 + y )
>>> print "Le résultat est", z
Le résultat est 90.9090909091
```
```python
>>> # Bon exemple
>>> FV = 100
>>> R = 0.1
*>>> PV = FV / ( 1 + R )
>>> print "Le résultat est", PV
Le résultat est 90.9090909091
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
]
.right-column[
Introspection
```python
>>> dir
['__builtins__', '__doc__', '__name__', '__package__']
```

dir() permet d'accèder à l'ensemble des nom définis à un instant

```python
>>> a = 1
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
```

dir(a) permet d'avoir les fonctions applicable à a :
```python
>>> type(a)
<type 'int'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__cmp__',  ...
'denominator', 'imag', 'numerator', 'real']
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
]
.right-column[
Suppression d'une variable
```python
>>> dir
<built-in function dir>
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> maVariable=1
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'maVariable']
>>> del(maVariable)
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
]
.right-column[
* Les opérations de base
```python
>>> # Addition
>>> 1 + 1
2
>>> # Soustraction
>>> 1 - 2
-1
>>> # Multiplication
>>> 2 * 2
4
>>> # Divisions
>>> 3 / 2
1
>>> 3 / 2.
1.5
>>> 3//2.
1.0
>>> int(2.5)
2
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
]
.right-column[
* Plus de mathématiques, le module
```python
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> import math
>>> dir()
[... , 'math']
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh',
... , 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> math.pow(2,2)
4.0
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
]
.right-column[
* Plus de mathématiques, le module

```python
>>> help(pow)
Help on built-in function pow in module __builtin__:

pow(...)
    pow(x, y[, z]) -> number

    With two arguments, equivalent to x**y.  With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).

>>> pow(3,10,4)
1
>>> 3**10
59049
>>> 59049%4
1

```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
]
.right-column[
* Choisir la précision
```python
>>> 3/7.
0.42857142857142855
>>> payement=3/7.
>>> pay2=round(payement,4)
>>> pay2
0.4286
```
* Mais attention...
```python
>>> payement*pow(10,6)
428571.4285714285
>>> pay2*pow(10,6)
428600.0
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
]
.right-column[
* e, Pi, log et exp
```python
>>> math.e
2.718281828459045
>>> math.pi
3.141592653589793
>>> math.log(math.e)
1.0
>>> math.log(math.exp(2))
2.0
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
### Une note sur import
]
.right-column[
* import math
```python
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> import math
>>> dir()
[..., 'math']
```

* from math import
```python
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> from math import pow
>>> dir()
[..., 'pow']
>>> from math import *
>>> dir()
[..., 'acos', 'acosh', 'asin', 'asinh', 'atan',
..., 'sqrt', 'tan', 'tanh', 'trunc']
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
### Une note sur import
### Fonctions utiles
]
.right-column[
* Affichage : print
```python
>>> import math
>>> print 'Pi =', math.pi
>>> print math.pi
>>> print "Je crois que Pi vaut %f, enfin je crois, \
... ou alors c'est %f ?" % (math.pi,  math.e)
```

* Savoir de quel type est une variable
```python
>>> x = 1
>>> type(x)
>>> x = float(x)
>>> type(x)
>>> if isInstance(x, (int, float)):
... 	print "X est un nombre"
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Jouons avec les variables
### Le module mathématique
### Une note sur import
### Fonctions utiles
]
.right-column[
* Combinaison de chaînes de caractères
```python
>>> a = 'Hello'
>>> b = 'World'
>>> a+b
>>> a+' '+b
>>> print "%s %s" % (a,b)
```

* Strip et upper
```python
>>> x = '  hello '
>>> print x.upper()
>>> print x.capitalize()
>>> print x.strip()
>>> print x.strip().capitalize()
```
]

---

# Utilisation de Python en Quelques Lignes

.left-column[
### Les tuples
]
.right-column[
```python
>>> t = ('JC', 33)
>>> print t
>>> len(t)
>>> t[0]
>>> type(t[1])
>>> type(t)
>>> print "My name is %s and my age is %d." % t
```
]

---

# Exercices

- Comment trouver toutes les fonctions built-in ?
- Convertir 'Cet exercice est facile' en lettres majuscules.
- Nous avons 41 personnes dans la classe. Si nous devons faire des groupes de 3 pour des projets, combien de groupes et combien de personnes dans un groupe non entier ?
- Expliquer le résultat suivant :
```python
>>> x=5.566
>>> round(x,2)
5.57
```
---

# Solutions

- Exercice 4
```python
>>> dir(__builtins__)
```

--
- Exercice 5
```python
>>> s='Cet exercice est facile'.upper()
>>> print s
```

--
- Exercice 6
```python
>>> print 'Avec %d élèves ont peut faire %d \
... groupes de %d personnes et il en restera %d.' % (41,41/3,3,41%3)
Avec 41 élèves ont peut faire 13 groupes de 3 personnes et il en restera 2.
```

---

# Solutions

- Exercice 7
C'est le fonctionnement classique de l'arrondi en mathématique :

Si `\(x-int(x) \lt 0.5\)`<br/>
Alors `\(round(x) = int(x)\)`<br/>
Sinon `\(round(x) = int(x)+1\)`

---
name: FlowControl
# Contrôle de flux

### Les Booléens
### Les Opérateurs Booléen
### Les blocs de code
### If, then, else, elif
---

# Contrôle de flux

.left-column[
### Les Booléens
]
.right-column[
```python
>>> spam = True
>>> spam
True
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> True = 2
  File "<stdin>", line 1
SyntaxError: can't assign to keyword
```
]

---

# Contrôle de flux

.left-column[
### Les Booléens
]
.right-column[
```python
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword
to get more help.

False               def                 if
raise               None                del
import              return              True
elif                in                  try
and                 else                is
while               as                  except
lambda              with                assert
finally             nonlocal            yield
break               for                 not
class               from                or
continue            global              pass
```
]

---

# Contrôle de flux

.left-column[
### Les Booléens
### Les Opérateurs Booléen
]
.right-column[
| Opérateur | Signification|
|:---------:|:------------:|
| == | Égal à |
| != | Différent de |
| < | Inférieur à |
| > | Supérieur à |
| <= | Inférieur ou égal à |
| >= | Supérieur ou égal à |
]

---

# Contrôle de flux

.left-column[
### Les Booléens
### Les Opérateurs Booléen
]
.right-column[
```python
>>> 42 == 42
True
>>> 42 == 99
False
>>> 2 != 3
True
>>> 2 != 2
False
```
]

---

# Contrôle de flux

.left-column[
### Les Booléens
### Les Opérateurs Booléen
]
.right-column[
```python
>>> 'hello' == 'hello'
True
>>> 'hello' == 'Hello'
False
>>> 'dog' != 'cat'
True
>>> True == True
True
>>> True != False
True
>>> 42 == 42.0
True
>>> 42 == '42'
False
```
]

---

# Contrôle de flux

.left-column[
### Les Booléens
### Les Opérateurs Booléen
]
.right-column[
```python
>>> (4 < 5) and (5 < 6)
True
>>> (4 < 5) and (9 < 6)
False
>>> (1 == 2) or (2 == 2)
True
>>> 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True
```
]

---

# Contrôle de flux

.left-column[
### Les Booléens
### Les Opérateurs Booléen
### Les blocs de code
]
.right-column[
L'indentation c'est la vie !

En python les blocs de code sont délimités par l'indentation, ils commencent
en général par ':' et se prolongent tant que l'indentation est présente.

```python
>>> name = 'Mary'
>>> password = 'swordfish'
>>> if name == 'Mary':
...     print('Hello Mary')
...     if password == 'swordfish':
...         print('Access granted.')
...     else:
...         print('Wrong password.')
```
]

---

# Contrôle de flux

.left-column[
### Les Booléens
### Les Opérateurs Booléen
### Les blocs de code
### If, then, else, elif
]
.right-column[
```python
>>> if name == 'Mary':
...     print('Hello Mary')
```
```python
>>> if name == "Mary":
...     print('Hello Mary')
... else:
...     print('Who are you?')
```
```python
>>> name = 'Bob'
>>> age = 5
>>> if name == 'Alice':
...     print('Hi, Alice.')
... elif age < 12:
...     print('You are not Alice, kiddo.')
```
]

---

# Contrôle de flux

.left-column[
### Boucles
]
.right-column[
- Les boucles While
```python
>>> spam = 0
>>> while spam < 5:
...     print('Hello, world.')
...     spam = spam + 1
```
- Break
```python
>>> while True:
...     print('Please type your name.')
...     name = input()
...     if name == 'your name':
...         break
>>> print('Thank you!')
```
]

---

# Contrôle de flux

.left-column[
### Boucles
]
.right-column[
- Continue
```python
>>> while True:
...   print('Who are you?')
...   name = input()
...   if name != 'Joe':
...     continue
...   print('Hello, Joe. What is the password?')
...   password = input()
...   if password == 'swordfish':
...     break
>>> print('Access granted.')
```
]

---

# Contrôle de flux

.left-column[
### Boucles
]
.right-column[
- Les boucles For
```python
>>> print('My name is')
>>> for i in range(5):
...    print('Jimmy Five Times (' + str(i) + ')')
```
```python
  range(stop) -> range object
  range(start, stop[, step]) -> range object

  Return an object that produces a sequence of integers
  from start (inclusive) to stop (exclusive) by step.
  range(i, j) produces i, i+1, i+2, ..., j-1. start
  defaults to 0, and stop is omitted!  range(4)
  produces 0, 1, 2, 3. These are exactly the valid
  indices for a list of 4 elements. When step is given,
  it specifies the increment (or decrement).
```
]

---

# Exercices

- Écrire un code qui affiche 'Hello' si 1 est stocké dans la variable spam,
'Howdy' si 2 est stocké dans spam et 'Greetings' dans tous les autres cas.
- Quelle est la différence entre break et continue ?
- Quelle sont les différences entre range(10), range(0, 10) et range(0, 10, 1)
  ?
- Écrire un programme qui calcule la somme des 20 premiers entiers à l'aide
  d'une boucle for.
- Faire la même chose à l'aide d'une boucle while.
- Faire la même chose.

---

# Solutions

- Exercice 8:
```python
    if spam == 1:
        val = 'Hello'
    elif spam == 2:
        val = 'Howdy'
    else:
        val = 'Greetings'
    print(val)
```
--
- Exercice 9:

Break permet de quitter une boucle, alors que continue permet d'aller
directement à la prochaine itération de la boucle.
--

- Exercice 10:

Absoluement aucune !

---

# Solutions

- Exercice 11:
```python
    somme = 0
    for i in range(1, 21):
        somme += i
    print(somme)
```
--
- Exercice 12:
```python
    somme = 0
    i = 1
    while i < 21:
        somme += i
        i += 1
    print(somme)
```
--
- Exercice 13:
```python
    somme = (20*21)//2
```
---
name: Functions

# Programmation Fonctionnelle

### Une première fonction
### Notre propre module
### Un peu de mathématiques
### Utilisation de notre module

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
]
.right-column[
Wikipédia :
> En informatique, une fonction est une entité informatique qui **encapsule** une
> portion de code (une séquence d'instructions) effectuant un traitement
> spécifique **bien identifié** relativement
> indépendant du reste du programme, et qui peut être **réutilisé** dans le même
> programme, ou dans un autre. Dans ce cas, on range souvent la fonction dans
> une **bibliothèque** pour la rendre disponible à d'autres projets de
> programmation, tout en préservant l'intégrité de son implémentation.
]

???

Ne pas oublier de faire un point sur l'utilisation de l'IDE. Pas de slides mais
il faut faire une démonstration de l'utilisation de l'IDE

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
]
.right-column[
- Définition :
```python
    def maFonction():
        print "Hello World"
```

- Utilisation :
```python
    maFonction()
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
]
.right-column[
- Définition avec des paramètres :
```python
    def hello(name):
        print('Hello ' + name)
```

- Utilisation :
```python
    hello('Alice')
    hello('Bob')
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
]
.right-column[
- Valeurs de retour :
```python
    def getAnswer(answerNumber):
        if answerNumber == 1:
            return "C'est sûr"
        elif answerNumber == 2:
            return "C'est vraisemblable"
        elif answerNumber == 3:
            return "Oui"
        elif answerNumber == 4:
            return "Retentez votre chance"
        elif answerNumber == 5:
            return "Redemandez plus tard"
        elif answerNumber == 6:
            return "Concentrez-vous et redemandez"
        elif answerNumber == 7:
            return "Ma réponse est non"
        elif answerNumber == 8:
            return "Les chances ne sont pas de votre côté"
        elif answerNumber == 9:
            return "Peu vraisemblable"
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
]
.right-column[
- Utilisation :
```python
    import random
    fortune = getAnswer(random.randint(1,9))
    print(fortune)
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
]
.right-column[
- Passage d'arguments et print
```python
    print('Hello')
    print('World')
```
- les arguments nommés ('keywords arguments')
```python
    print('Hello', end=' ')
    print('World')
    print('Hello', 'World')
    print('cats', 'dogs', 'mice', sep=', ', end='.\n')
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
### Portée des variables
]
.right-column[
- On ne peut pas utiliser des variables locales en dehors de leur scope...
```python
    def spam():
        eggs = 31337
        print(str(eggs))
    spam()
    print(eggs)
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
### Portée des variables
]
.right-column[
- On ne peut toujours pas utiliser des variables locales en dehors de leur scope...
```python
    def spam():
        eggs = 31337
        bacon()
        print(eggs)

    def bacon():
        ham = 101
        eggs = 0

    spam()
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
### Portée des variables
]
.right-column[
- Par contre on peut tout à fait utiliser des variables globales dans une
  fonction 
```python
    def spam():
        print(eggs)
    
    eggs = 31337
    spam()
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
### Portée des variables
]
.right-column[
- A ne SURTOUT PAS refaire, mais on peut le faire... 
```python
    def spam():
        eggs = 'spam local'
        print(eggs)

    def bacon():
        eggs = 'bacon local'
        print(eggs)
        spam()
        print(eggs)
    
    eggs = 'global'
    bacon()
```
]

---

# Programmation Fonctionnelle

.left-column[
### Une première fonction
### Portée des variables
]
.right-column[
- L'utilisation de 'global'
```python
    def spam():
        global eggs
        eggs = spam

    eggs = 'global'
    spam()
    print(eggs)
```
]

---
name: OurModule
# Notre propre module

.left-column[
### Une première fonction
### Portée des variables
### Notre propre module
]
.right-column[
- Documentation Python :
> A module is a file containing Python definitions and statements. The file
> name is the module name with the suffix .py appended.
- En fait un module python est simplement un fichier que l'on importe. Le
  fichier contient simplement les fonctions utilisables.
- Exemple :
```python
    >>> import suites
    >>> # Importe le fichier suites.py
    >>> dir(suites)
    ['__name__', 'fib', 'fib2']
```
]

---

# Notre propre module

.left-column[
### Une première fonction
### Portée des variables
### Notre propre module
]
.right-column[
Créons notre module "suites"
```python
    # Un module avec différentes suites

    def fib(n):    # affiche la série de Fibonacci de 1 à n
        a, b = 0, 1
        while b < n:
            print(b, end=' ')
            a, b = b, a+b
        print()

    def fib2(n):   # renvoit la suite de  Fibonacci jusqu'à n
        res = []
        a, b = 0, 1
        while b < n:
            res.append(b)
            a, b = b, a+b
        return res
```
On sauve le fichier suites.py.
]

---

# Notre propre module

.left-column[
### Une première fonction
### Notre propre module
### Utilisation de notre module
]
.right-column[
- Utilisation :
```python
>>> import suites
>>> suites.__name__
'suites'
>>> suites.fib(1000)
1 1 2 3 5 8 13 21 34 55 144 233 377 610 987
```
]

---

# Notre propre module

.left-column[
### Une première fonction
### Notre propre module
### Utilisation de notre module
]
.right-column[
- Rendre le module executable
- Parce que l'on veut tester notre module
- Parce que l'on peut transformer rapidement un module en exécutable
```python
    if __name__ == "__main__":
        import sys
        # Utilisation : python suites.py <rang>
        fib(int(sys.argv[1]))
```
]

---

# Exercices

- Créer un programme cherchant à faire deviner un chiffre. Le joueur a six
  tentatives.
- Ajouter au module suite la suite de Syracuse définie par :
$$u_{n+1} = 
\dfrac{u_n}{2} \mbox{ si } u_n \mbox{ est pair, }
3*u_n+1 \mbox{ sinon.}
$$

---

# Solutions

- Exercice 14:
```python
    # Jeu où l'on doit deviner un nombre

    # imports

    # On demande 6 fois au joueur
        # Si le chiffre est trop bas
        # Si le chiffre est trop haut
        # Sinon on sort

    # Si l'on a trouvé le chiffre
    # Ou pas...
```

---

# Solutions

- Exercice 14:
```python
    # Jeu où l'on doit deviner un nombre
    import random

    secret = random.randint(1,20))
    print('Je penses à un nombre entre 1 et 20.')

    # On demande 6 fois au joueur
    for nombreChoix in range(1,7):
        print('Alors quel nombre ?')
        choix = int(input())
        if choix < secret:
            print('Votre choix est trop petit.') # Si le chiffre est trop bas
        elif choix > secret:
            print('Votre choix est trop grand.') # le chiffre est trop haut
        else:
            break # Sinon on sort

    if choix == secret:
        print('Bien joué.') # Si l'on a trouvé le chiffre
    else:
        print('Pas de chance...') # Ou pas...
```

---

# Solutions

- Exercice 15:
```python
    def syracuse(debut, rang):
        u = debut
        print(u, end=' ')
        for n in range(debut, rang):
            if u % 2 == 0:
                u = u / 2
            else:
                u = 3 * u + 1
            print(u, end=' ')
```
---

# Le Jeu du Pendu

.left-column[
### Concept
]
.right-column[
- Nous allons mettre au point un jeu du pendu
- Règles :
 - Un mot est choisi par l'ordinateur
 - A chaque tour le joueur propose une lettre
 - Si la lettre existe dans le mot elle apparaît
 - Sinon le compteur augmente et le joueur se rapproche de la fin
]

---

# Le Jeu du Pendu

.left-column[
### Concept
### Mise en place
]
.right-column[
```python
    # imports
    # Choisir un mot 
    # tant qu'il reste un tour
        # demander une lettre
        # test de la lettre
        # test victoire
        # incrémentation
```
]

---
name: ProjectSudoku
# Le sudoku

.left-column[
### Règles du jeu
]
.right-column[
Un sudoku classique contient neuf lignes et neuf colonnes, donc 81 cases au
total. Le but du jeu est de remplir ces cases avec des chiffres allant de 1 à 9
en veillant toujours à ce qu'un même chiffre ne figure qu'une seule fois par
colonne, une seule fois par ligne, et une seule fois par carré de neuf cases.

On peut déduire deux règles
- Si une case contient un chiffre, ce chiffre ne peut pas se retrouver dans les
  blocs contenant cette case ;
- Si une case, du fait de la règle précédente, ne peut contenir qu'une seule
  valeur, alors cette valeur doit être affectée à cette case.
]

---

# Le sudoku

.left-column[
### Règles du jeu
### Notations
]
.right-column[
Quelques notations et conventions :
- une grille se compose de 81 **cases** ou **square** ;
- les **colones** (cols) sont numérotés de 1 à 9 ;
- les **lignes** (rows) sont numérotés de A à I ;
- un bloc est un carré de 9 cases tels que definit par le jeu ;
- une **unité** est un ensemble de cases qui s'impactent les unes les autres :
  soit une ligne, soit une colone, soit un bloc ;
- les **pairs** d'une case sont l'ensemble des cases qui sont dans une unité
  commune avec la case considérée.
]

---

# Le sudoku

.left-column[
### Règles du jeu
### Notations
]
.right-column[

Quelques représentations d'une grille :
```python
    A1 A2 A3| A4 A5 A6| A7 A8 A9   
    B1 B2 B3| B4 B5 B6| B7 B8 B9  
    C1 C2 C3| C4 C5 C6| C7 C8 C9 
    --------+---------+--------- 
    D1 D2 D3| D4 D5 D6| D7 D8 D9 
    E1 E2 E3| E4 E5 E6| E7 E8 E9
    F1 F2 F3| F4 F5 F6| F7 F8 F9
    --------+---------+---------
    G1 G2 G3| G4 G5 G6| G7 G8 G9
    H1 H2 H3| H4 H5 H6| H7 H8 H9
    I1 I2 I3| I4 I5 I6| I7 I8 I9
```
]

---

# Le sudoku

.left-column[
### Règles du jeu
### Notations
]
.right-column[
Quelques représentations d'une grille :
```python
     4 1 7 | 3 6 9 | 8 2 5 
     6 3 2 | 1 5 8 | 9 4 7
     9 5 8 | 7 2 4 | 3 1 6 
    -------+-------+-------
     8 2 5 | 4 3 7 | 1 6 9 
     7 9 1 | 5 8 6 | 4 3 2 
     3 4 6 | 9 1 2 | 7 5 8 
    -------+-------+-------
     2 8 9 | 6 4 3 | 5 7 1 
     5 7 3 | 2 9 1 | 6 8 4 
     1 6 4 | 8 7 5 | 2 9 3
```
]

---

# Le sudoku

.left-column[
### Règles du jeu
### Notations
]
.right-column[
Les Units et les Peers :
```python
    A1 A2 A3 |          |         
    B1 B2 B3 |          |         
    C1 C2 C3 | C4 C5 C6 | C7 C8 C9
    ---------+----------+---------
       D2    |          |         
       E2    |          |         
       F2    |          |         
    ---------+----------+---------
       G2    |          |         
       H2    |          |         
       I2    |          |         
```
]

---

# Le sudoku

.left-column[
### Règles du jeu
### Notations
### Algorithme
]
.right-column[
Comment résoudre donc une grille de Sudoku ?
- Lecture de la grille
- Afficher une grille
- Appliquer les contraintes
 - assigner les valeurs de base
 - eliminer les possibilités restantes
 - Si une case ne peut plus contenir qu'une valeur, l'assigner
 - Itérer le processus jusqu'à ce qu'il n'y ait plus de possiblité
- Choisir une case et tenter les possibilités restantes
]

---

# Le sudoku -- Notes de développement

.left-column[
### Construction des squares 
]
.right-column[
- mes lignes sont A, B, C, D, ...
- mes colones sont 1, 2, 3, ...
- Comment avoir A1, A2, ..., I8, I9 ???
```python
>>> c = '1'
>>> r = 'A'
>>> [ r + c ]
[ 'A1' ]
>>> [ r+c, r+c ]
[ 'A1', 'A1' ]
```
Donc :
```python
>>> l = []
>>> for r in rows:
...     for c in cols:
...         l.append(r+c)
>>> l
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
```
]

---

# Le sudoku -- Notes de développement

.left-column[
### Construction des squares 
]
.right-column[
- Mais il y a mieux ?
```python
>>> rows = 'ABC'
>>> cols = '123'
>>> [ r+c for r in rows for c in cols ]
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
```
]

---

count: false

# Le sudoku -- Notes de développement

.left-column[
### Construction des squares 
]
.right-column[
- Mais il y a mieux ?
```python
>>> rows = 'ABC'
>>> cols = '123'
>>> [ r+c for r in rows for c in cols ]
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
```
- Inlining : Technique visant à écrire le maximum de code sur la même ligne
```python
>>> l = '123456789'
>>> [ v for v in l ]
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> r = []
>>> for v in l:
...     r.append(v)
>>> r
```
]

---

# Le sudoku -- Notes de développement

.left-column[
### Construction des squares 
]
.right-column[
- Et on peut aller plus loin avec des tests :
```python
>>> l = '123456789'
>>> [ ( int(v) if int(v)%2==0 else O ) for v in l ]
[0, 2, 0, 4, 0, 6, 0, 8, 0]
```
]

---

# Le sudoku -- Notes de développement

.left-column[
### Construction des squares 
### Les dictionnaires et les values
]
.right-column[
- les dictionnaires sont les tableaux associatifs de python
```python
>>> d = dict()
>>> d['A'] = 1
>>> d[5] = 2
>>> d
{5:2, 'A':1}
>>> d['A']
1
```
- ils permettent de stocker des valeurs associées à des clées. Plus simple à
  retrouver.
```python
>>> d = dict( (s, c) for s in ['A1', 'B1' ] )
>>> d
{'B1': '123456789', 'A1': '123456789'}
```
]

---

# Le sudoku -- Notes de développement

.left-column[
### Construction des squares 
### Les dictionnaires et les values
]
.right-column[
- Astuce pour construire un dictionnaire à partir de deux listes de même taille
```python
>>> l = '123456789'
>>> c = 'ABCDEFGHI'
>>> dict(zip(l,c))
{'8': 'H', '6': 'F', '3': 'C', '5': 'E', '9': 'I', 
'7': 'G', '1': 'A', '4': 'D', '2': 'B'}
>>> dict(zip(c,l))
{'G': '7', 'F': '6', 'C': '3', 'I': '9', 'E': '5', 
'A': '1', 'H': '8', 'B': '2', 'D': '4'}
```
]

---

# Le sudoku -- Notes de développement

.left-column[
### Construction des squares 
### Les dictionnaires et les values
### Les retours multiples et dict.items()
]
.right-column[
- Comment parcourir l'ensemble d'un dictionnaire ???
```python
>>> d = dict(zip(l, chars))
>>> d[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> d['A1']
'1'
>>> for s,d in d.items():
...     print('%s => %s' % (s,d))
C3 => 9
...
A2 => 2
```
]

---

# Le sudoku -- Notes de développement

.left-column[
### La fonction all()
]
.right-column[
- Soit l un tableau, renvoyer vrai si tous les éléments de l sont divisibles
  par 2 :
```python
>>> l = [ v for v in range(0,20,2) ]
>>> ret = True
>>> for v in l:
...     if v % 2 != 0:
...         ret = False
...         break
>>> ret
True
```
- c'est un peu long non ?
]

---

# Le sudoku -- Notes de développement

.left-column[
### La fonction all()
]
.right-column[
- Examinons all()
```python
>>> all([True])
True
>>> all([True, False])
False
>>> all([True, True])
True
```
- Comment générer le tableau des tests à vérifier ?
```python
>>> [ v % 2 == 0 for v in l ]
[True, True, True, True, True, True, True, True, True]
>>> all( [ v%2 == 0 for v in l ])
True
```
]

---

# Le sudoku -- Notes de développement

.left-column[
### La fonction all()
### Les sets
]
.right-column[
- Les set sont des ensembles non ordonnés d'éléments uniques. Ils sont très
  pratiques pour éliminer des valeurs multiples
```python
>>> l = list('12345654321')
>>> l
['1', '2', '3', '4', '5', '6', '5', '4', '3', '2', '1']
>>> l = list(set(l))
>>> l
['5', '4', '2', '6', '3', '1']
>>> l.sort()
>>> l
['1', '2', '3', '4', '5', '6']
```
]

---

# TPs

- Sujet 1 :
> Voici un algorithme simple permettant de générer des grilles de Sudoku :
> - faire un mélange aléatoire des cases de la grille
> - une par une remplir les cases avec un chiffre aléatoire en respectant les
>   possibilités pour ne pas générer une grille impossible
> - Si une contradiction aparaît, recommencer
> - Si 17 cases sont remplies, alors la grille est prête
> Implémentez cet algorithme et résolvez 1000 grilles ainsi générés. Conserver
> les 10 grilles les plus lentes à être résolues

---

# TPs

- Sujet 2 :
> Vous pouvez lire dans un fichier texte des ensembles de 5 lignes. La première
> ligne contient une question, les 4 suivantes les propositions de réponses.
> Réaliser un programme qui génère 10 versions différentes de cette liste de
> questions et de réponses. Pour chaque version différente les questions ne
> seront pas dans le même ordre. Pour chaque question, les réponses ne seront
> pas dans le même ordre non plus.

---

# TPs

- Modalités :
 - Un seul TP est à rendre.
 - Les TPs doivent être réalisés par groupes de une ou deux personnes
 - La date limite pour rendre votre TP est le vendredi 27/01 17h. L'heure du
   mail fera foi.
 - Vous rendrez vos TP par mail à jean-christophe.gay@dauphine.fr
 - Le sujet du mail sera : '[Python] ... '
 - La pièce jointe sera un fichier zip contenant le code et les traces
   d'exécutions

---

name: ToDo

# A suivre...

Si vous avez des idées... nous pourrons les réaliser.

???

# Fonctions classes et méthodes

# Automate the boring stuff with python

# A la marge :
Git
GitHub

---

# Bibliographie

- Python for Finance, Yuxin Yan, PACK, date ?
- Automate the boring stuff with Python
- Python for Finance, O'Reilly
- Mettre au moins un autre livre

