def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]: 
        tab_a[i] = tab[i] 
        tab_a[i+1] = a
        i = i + 1 
    return tab_a


assert insere([1,3, 5, 7], 4) == [1,3,4,5,7]
assert insere([], 2)== [2]