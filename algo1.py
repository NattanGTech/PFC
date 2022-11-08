#DEBUT
r = 12000
s = 1250
e = 10
rh = 230

assertion1 = ((365 * 3) / (24 - (16 - 8))) * (rh) > r == (e * s < r)
assertion1Pt1 = ((365 * 3) / (24 - (16 - 8))) * (rh) > r # True
assertion1Pt2 = (e * s < r) # False

# assertion1 === (assertion1Pt1 == assertion1Pt2)
# assertion1 === (assertion1Pt1 == False)
# assertion1 === (True == False)

print(assertion1)


assertionDeux = (365 * 3) / (4 - (12 - 8)) * (rh) > r == (e * s < r)
assertionDeuxPtUn = (365 * 3) / (4 - (12 - 8)) * (rh) > r # False
assertionDeuxPtDeux = (e * s < r) # False

# assertionDeux === (assertionDeuxPtUn == assertionDeuxPtDeux)
# assertionDeux === (assertionDeuxPtUn == False)
# assertionDeux === (False == False)

print(assertionDeux)


def calculPtDeux():
    return (e * s < r)

assertionDeux = (365 * 3) / (4 - (12 - 8)) * (rh) > r == calculPtDeux()

#FIN