def recherche(elt,tab):
    resultat=None
    for indice in range(len(tab)):
        if tab[indice]==elt:
            resultat=indice
            break
    return resultat