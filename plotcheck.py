import getplots

def plotCheck(img, corners):

    plots = getplots.getPlotsDict(img,corners)
    
    if len(plots.keys()) == 1:
        return False

    if len(plots.keys()) < 3:
        return False

    return True
