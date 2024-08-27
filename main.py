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


if __name__ == '__main__':
    g = grille(10)
    affichegrille(g)
