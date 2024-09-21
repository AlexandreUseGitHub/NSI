def moyenne(tab):
    additionNotes=0
    for note in tab:
	    additionNotes+=note
    return additionNotes/len(tab)
assert moyenne([1.0]) == 1.0
assert abs(moyenne([1.0, 2.0, 4.0])-2.3333333333) < 10**-6