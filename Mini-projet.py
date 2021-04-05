# Mini-projet
from math import *
import numpy as np
from random import *


def CreationMatrice(n):
    '''on crée une matrice symétrique aléatoire de 0 et de 1
    n représente le nb de points
    0 l'absence de liaison entre les 2 points, 1 : l'arête entre 2 points'''
    tableau = np.random.rand(n,n)
    i = 0
    j = 0

    #on crée la matrice symétrique
    for i in range (n):
        for j in range (i,n):
            if(tableau[i][j]>=0.5) :
                tableau[i][j] = 1
                tableau[j][i] = 1
            else :
                tableau[i][j] = 0
                tableau[j][i] = 0


    #diagonale de 0
    k=0
    for k in range (n):
        tableau[k][k] = 0

    return tableau


def CreationMatrice2(n):
    matrice = np.zeros((n,n),dtype='i')
    coef = 0

    for i in range (n):
        for j in range (i,n):
            coef = randint(0,1)
            matrice[i][j]=coef
            matrice[j][i]=coef

    for k in range (n):
        matrice[k][k]=0

    print (matrice)
    return matrice


def CirculaireImpaire(tab_aretes):
    circulaire = false
    impair = false

    if(len(tab_aretes)%2==1):
        impair = true

    compteur=0
    for i in range (len(tab_aretes)):
        if(len(tab_aretes[i]==2)) :
            compteur += 1

    if(compteur==len(tab_aretes)):
        circulaire = true



def Coloration2(M):
    n=len(M[0])
    for i in range(n):
        for j in range (n):
            if(M[i][j]==1 and M[i][i]==0):
                if(M[j][j]==2):
                    M[i][i]=3
                else :
                    M[i][i]=2
            if(M[i][j]==1 and M[i][i]!=0 and M[j][j]!=0):
                if(M[i][i]==M[j][j]):
                    return False
    return M






#EXERCICE 2


def Coloration(n):
    listePoints = [i for i in range (0,n+1)]
    listeAretes = []
    listeCouleurs = np.zeros(n)
    couleur = 1

    matrice = CreationMatrice2(n)
    print(matrice)

    i=0
    j=0
    for i in range (n):
        tableau=[]
        for j in range (n):
            if (matrice[i][j]==1):
                tableau.append(j)
            #s'il n'y a pas d'arête entre les deux points, on ne fait rien
        listeAretes.append(tableau)
    print(listeAretes)

    longueurs = [0 for i in range (n)]
    for i in range (n):
        longueurs[i]=len(listeAretes[i])

    #on trie la liste par degré décroissants
    for i in range (n-1,1,-1):
        for j in range (i-1):
            if(longueurs[j]<longueurs[j+1]):
                longueurs[j],longueurs[j+1] = longueurs[j+1], longueurs[j]
                listeAretes[j],listeAretes[j+1] = listeAretes[j+1], listeAretes[j]
                listePoints[j],listePoints[j+1] = listePoints[j+1], listePoints[j]

    # on commence la coloration
    while(0 in listeCouleurs):
        for j in range (n):
            for i in range (0,n):
                if(listeCouleurs[i]==0 and listePoints[j] not in listeAretes[i]):
                    listeCouleurs[i] = couleur
            couleur = couleur +1

    print(listeCouleurs)

    return max(listeCouleurs)





