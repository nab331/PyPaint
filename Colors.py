

class Colors:
    coolgrey = (52, 73, 94)
    pick = (103, 128, 159)
    silver = (189, 195, 199)
    spacecol = (70, 70, 70)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    coolred = (231, 76, 60)
    darkred = (201, 46, 30)

    coolpurple = (142, 68, 173)

    coolblue = (52, 152, 219)
    darkblue = (22, 122, 189)

    coolyellow = (244, 208, 63)
    darkyellow = (214, 178, 33)

    hyperlapse = (103, 128, 159)
    coolgreen = (27, 188, 155)
    darkgreen = (16, 68, 40)
    carrot = (230, 126, 34)
    cloud = (236, 240, 241)
    brown = (139, 69, 19)
    yellow = (255, 255, 0)

    def __init__(self):
        return


def tupadd(tup, howmuch):
    listify = list(tup)

    for i in range(len(listify)):
        if 0 < (listify[i] + howmuch) < 255:
            listify[i] += howmuch

    return listify
