from operator import truediv
from os import abort


def grille(taille):
    g=[]
    for i in range(taille):
        l=[]
        for j in range(taille):
            l=l+[False]
        g=g+[l]
    return g

def affichegrille(g):
    for l in g:
        x=""
        for c in l:
            if c==False:
                x=x+" x "
            else:
                x=x+" o "
        print(x)
BateauJ1=grille(10)
BateauJ2=grille(10)
CoupsJ1=grille(10)
CoupsJ2=grille(10)


def ajoutebateau(grille,x,y,taille,direction):
    if direction==True:
        if taille+x>len(grille):
            return False
        for i in range(taille):
            grille[y][x] = True
            x=x+1
    if direction==False:
        if taille + y > len(grille):
            return False
        for i in range(taille):
            grille[y][x] = True
            y=y+1




if __name__ == '__main__':
    test=grille(10)
    ajoutebateau(test,0,10,8,False)
    affichegrille(test)

