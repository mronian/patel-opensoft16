from imports import *
from helpers import *
from getPlotContours import *


minPatchSize = 1
hdelta = 5
radius = 10
seriesLenThresh = 150

def getClrs(col):

    hvals = col[:,0]

    out = []

    hpatch = 0
    numPts = 0
    i = 0

    # print "************************************"

    while i < len(hvals):
        h = hvals[i]
        if h == 190:
            i += 1
            continue

        if numPts == 0:
            patch = []
            hpatch = hvals[i]
            while i < len(hvals) and abs(hvals[i] - hpatch) < hdelta:
                patch.append(i)
                numPts += 1
                i+= 1 

        if numPts >= minPatchSize:
            # print hpatch
            # if hpatch == 177:
            #     print hpatch, int(np.array(patch).mean())
            out.append((hpatch, int(np.array(patch).mean())  ))
            # out.append((hpatch, int(np.array(patch).mean())  ))

        numPts = 0
        
    return out


def getPlotsDict(image, corners):

    img = getSubImage(image.hsv, corners)

    def m(idx, yval=None):
        # idx -= corners[0][0]
        ar = img[:,idx]
        ar[(ar[:,2] > 254) * (ar[:,1] < 50) , 0] = 190
        ar[(ar[:,2] > 254) * (ar[:,1] < 50) , 1] = 0

        ar[(ar[:,2] < 50) , 0] = 190
        # print ar[:,0]
        # print ar[:,1]
        # print ar[:,2]

        return getClrs(np.array(ar, dtype=int))

    plots = {}


    def getKey(clr):
        for k in plots.keys():
            if abs(k - clr) < hdelta:
                return k
        return clr

    for x in range(img.shape[1]):

        clrs = m(x)

        for (clr, ypos) in clrs:

            # if 165 in plots.keys() and clr == 167:
            #     import pdb; pdb.set_trace()

            k = getKey(clr)

            if k not in plots.keys():
                plt = []
                plt.append([x,ypos])
                plots[clr] = [plt]
                continue
            
            done = False

            for i,plt in enumerate(plots[k]):
                if getDistance([x,ypos] , plt[-1]) < radius:
                    plots[k][i].append([x,ypos])
                    done = True
                    break

            if done == False:
                plt = []
                plt.append([x,ypos])
                plots[k].append(plt)


    return plots 

    # PLOTS CALCULATED TILL HERE *******************************

    def plt(k):
        
        pts = []
        for p in plots[k]:
            if len(p) < 5:
                continue
            pts += p

        plotPoints(img, pts)

    for k in plots.keys():
        plotMulti(img, plots[k])
        print k


    allPts = []

    for k in plots.keys():
        sPlots = sorted(plots[k], key = lambda x: len(x))
        allPts.append(sPlots[-1])


    allPts = sorted(allPts, key = lambda x: len(x))

    showimg(image.img, m)

    return plots


def checkSeriesinCnt(series, cnt):

    numOut = 0
    numTsh = 0

    for p in series:
        if cv2.pointPolygonTest(cnt , tuple(p) , False) == -1:
            numOut += 1

        if numOut > numTsh:
            return False

    return True

def getInterpolateImage(image, corners, series):

    out = np.ones((image.img.shape[0], image.img.shape[1]), dtype=np.uint8) * 255
    ser = np.array(series)
    ser += corners[0]
    for p in ser:
        out[p[1], p[0]] = 0
    # out[ser] = 255
    # showimg(out)

    return out

def getPlots(image, corners):

    plotsDict = getPlotsDict(image, corners)

    img = getSubImage(image.hsv, corners)

    conts = getPlotConts(img, corners)

    def extractOneHPlot(h):

        candis = []

        allSeries = plotsDict[h]

        for cnt in conts:
            serOut = []
            for series in allSeries:
                if checkSeriesinCnt(series, cnt):
                    serOut += series

            candis.append( (serOut, cnt) )

        candis = sorted(candis, key=lambda x: len(x[0]))

        cnt = candis[-1][1]
        cnt = cnt.reshape((cnt.shape[0], cnt.shape[2]))
        series = candis[-1][0]

        # print h, len(series)
        return series, cnt


    outs = []
    outDict = {}


    prevCnt = 0

    for i,k in enumerate(sorted(plotsDict.keys())):
        if k == 0:
            continue
        ser, cnt = extractOneHPlot(k)

        if len(ser) > seriesLenThresh:
            if len(outs) > 0:
                if k - outs[-1][2] < 10:
                    continue

                if len(ser) < prevCnt:
                    prevCnt = len(ser)
                    continue

            intpImage = getInterpolateImage(image, corners, ser)
            outs.append((ser, cnt, k, intpImage))

            outDict[k] = (ser, cnt, intpImage)

            # plotPoints(img, ser)
            print k

        prevCnt = len(ser)


    return outDict

