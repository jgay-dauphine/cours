# code: utf-8

"""
Ceci est notre module d'affichage de suites mathématiques
Il contient :
- fib
"""

def fib(rang):
    """
    Ceci est la fonction qui affiche l'ensemble des
    éléments de la suite de Fibonacci de 1 à rang
    """
    # Initialisation
    (u, v) = (1, 1)
    # Itérations
    while u <= rang:
        print(u, end=' ')
        (u, v) = (v, u+v)
    print()

def fib2(rang):   # renvoit la suite de  Fibonacci jusqu'à n
    res = []
    u, v = 1, 1
    while u <= rang:
        res.append(u)
        u, v = v, u+v
    return res

if __name__ == '__main__':
    
    print('Tests du module suites :')
    print('affichage des éléments jusqu\'à 50 :')
    fib(50)
    print('Récupération des valeurs des éléments jusqu\'à 50')
    values = fib2(50)
    print(values)
