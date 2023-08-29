import numpy as np

# DISTANCE ROLL
d_dict = {
    "mario": [1, 3, 3, 3, 5, 6],
    "luigi": [1, 1, 1, 5, 6, 7],
    "peach": [0, 2, 4, 4, 4, 6],
    "daisy": [3, 3, 3, 3, 4, 4],
    "wario": [0, 0, 6, 6, 6, 6 ],
    "waluigi": [0, 1, 3, 5, 5, 7],
    "yoshi": [0, 1, 3, 5, 5, 7],
    "rosalina": [0, 0, 2, 3, 4, 8],
    "dk": [0, 0, 0, 0, 10, 10],
    "ddk": [0, 0, 0, 7, 7, 7],
    "goomba": [0, 0, 3, 4, 5, 6],
    "sg": [0, 4, 4, 4, 4, 4],
    "kt": [1, 1, 2, 3, 3, 10],
    "mm": [0, 2, 3, 4, 5, 6 ],
    "bowser": [0, 0, 1, 8, 9, 10],
    "bowser_jr": [1, 1, 1, 4, 4, 9],
    "boo": [0, 0, 5, 5, 7, 7],
    "hammber": [0, 1, 1, 1, 5, 5],
    "bones": [1, 1, 1, 6, 6, 6],
    "pom": [0, 3, 3, 3, 3, 8]
}

# COINS ROLL
c_dict = {
    "wario": [-2, -2, 0, 0, 0, 0],
    "waluigi": [-3, 0, 0, 0, 0, 0],
    "rosalina": [+2, +2, 0, 0, 0, 0],
    "goomba": [+2, +2, 0, 0, 0, 0],
    "bowser": [-3, -3, 0, 0, 0, 0],
    "boo": [-2, -2, 0, 0, 0, 0],
    "hammber": [+3, 0, 0, 0, 0, 0]
}

def party(x):
    # TOTAL COINS
    marioC = 5
    luigiC = 5
    peachC = 5
    daisyC = 5
    warioC = 5
    waluigiC = 5
    yoshiC = 5
    rosalinaC = 5
    dkC = 5
    ddkC = 5
    goombaC = 5
    sgC = 5
    ktC = 5
    mmC = 5
    bowserC = 5
    bowser_jrC = 5
    booC = 5
    hammberC = 5
    bonesC = 5
    pomC = 5

    # TOTAL DISTANCE
    marioD = 0
    luigiD = 0
    peachD = 0
    daisyD = 0
    warioD = 0
    waluigiD = 0
    yoshiD = 0
    rosalinaD = 0
    dkD = 0
    ddkD = 0
    goombaD = 0
    sgD = 0
    ktD = 0
    mmD = 0
    bowserD = 0
    bowser_jrD = 0
    booD = 0
    hammberD = 0
    bonesD = 0
    pomD = 0

    all = ["mario", "luigi", "peach", "daisy", "wario", "waluigi", "yoshi",
        "rosalina", "dk", "ddk", "goomba", "sg", "kt", "mm", "bowser", "bowser_jr",
        "boo", "hammber", "bones", "pom"]

    totalD = [marioD, luigiD, peachD, daisyD, warioD, waluigiD, yoshiD,
            rosalinaD, dkD, ddkD, goombaD, sgD, ktD, mmD, bowserD, bowser_jrD,
            booD, hammberD, bonesD, pomD]

    totalC = [marioC, luigiC, peachC, daisyC, warioC, waluigiC, yoshiC,
            rosalinaC, dkC, ddkC, goombaC, sgC, ktC, mmC, bowserC, bowser_jrC,
            booC, hammberC, bonesC, pomC]

    for i in range(int(x)):
        for j in all:
            # distance
            yee = d_dict.get(j)             # find in dict
            haw = np.random.choice(yee)
            totalD[all.index(j)] += haw     # add to total

            # check for dk
            if yee == 0 and j == "dk":
                heck = np.random.choice(4,1)
                if heck == 1:
                    totalC[all.index(j)] += 5   # convert coins
                    
            # check for ddk
            elif yee == 0 and j == "ddk":
                heck = np.random.choice(3,1)
                if heck == 1:
                    totalC[all.index(j)] += 2   # convert coins
            
            # check if choice is coin-related
            if j in c_dict:
                yee = c_dict.get(j)
                haw = list(yee)
                yeehaw = np.random.choice(haw)
                totalC[all.index(j)] += yeehaw  # add to total

    bigD = max(totalD)
    bigC = max(totalC)
    sadD = min(totalD)
    sadC = min(totalC)

    print("-----")
    print(all[totalD.index(bigD)], "be zoomin at", bigD, "steps")
    print(all[totalC.index(bigC)], "be ballin at", bigC, "coins")
    print("-----")
    print(all[totalD.index(sadD)], "be still at", sadD, "steps")
    print(all[totalC.index(sadC)], "be broke at", sadC, "coins")

x = input("party how many rounds? ")
party(x)