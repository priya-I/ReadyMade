from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def scatter(x,y,count,xlabel,ylabel):
	fig="./static/images/plots/scatter"+str(count)+".png"
	x=x.replace('NaN',0)
	y=y.replace('NaN',0)
	figure=plt.figure()
	ax=figure.add_subplot(111)
	ax.scatter(x,y)
	#title=xlabel+" against "+ylabel
	title="Plot #"+str(count)
	ax.set_title(title)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	figure.savefig(fig)
	return fig