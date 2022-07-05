import matplotlib.pyplot as plt
from scipy import stats
def corr_func_annotate(x, y, axi=None, method="pearson", color="black", fontsize=13,square=False, **kws):

    axi = axi or plt.gca()
    if (method=="pearson"):
        r, p = stats.pearsonr(x, y)
    elif(method =="spearman"):
        r, p = stats.spearmanr(x, y)

    x = 0.2
    y = 0.9
    try:
        x=kws["xy"][0]
        y=kws["xy"][1]
    except:
        pass

    try:
         color=kws["color"]
    except:
        pass

    if (square==True):
        axi.annotate(r'$r^{2} = {%.2f}$' % (pow(r,2)), xy=(x, y), xycoords=axi.transAxes, color=color,fontsize=fontsize)

    else:
        axi.annotate(r'$r = {%.2f}(%.2f)$'% (r,p),
                xy=(x, y), xycoords=axi.transAxes, color=color,fontsize=fontsize)