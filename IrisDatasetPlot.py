import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Create a postition for the plot, first digit is rows, secnd is columns and the third digit is position
fig = plt.figure()
ax1 = plt.subplot(431)
ax2 = plt.subplot(432)
ax3 = plt.subplot(433)
ax4 = plt.subplot(434)
ax5 = plt.subplot(435)
ax6 = plt.subplot(436)
ax7 = plt.subplot(437)
ax8 = plt.subplot(438)
ax9 = plt.subplot(439)
ax10 = plt.subplot(4,3,10)
ax11 = plt.subplot(4,3,11)
ax12 = plt.subplot(4,3,12)

# Load the dataset.
iris = load_iris()

#Extract the data into an array
data = np.array(iris['data'])

#Extract Target data into array
targets = np.array(iris['target'])

# Create a color selector for the different flowers
cd = {0:'r',1:'b',2:"g"}

# Loop over the color selector to assign the flowers their colors
cols = np.array([cd[target] for target in targets])

# Create a scatter plot using the indexes of the array
ax1.scatter(data[:,0], data[:,1], c=cols)
ax2.scatter(data[:,0], data[:,2], c=cols)
ax3.scatter(data[:,0], data[:,3], c=cols)
ax4.scatter(data[:,1], data[:,0], c=cols)
ax5.scatter(data[:,1], data[:,2], c=cols)
ax6.scatter(data[:,1], data[:,3], c=cols)
ax7.scatter(data[:,2], data[:,0], c=cols)
ax8.scatter(data[:,2], data[:,1], c=cols)
ax9.scatter(data[:,2], data[:,3], c=cols)
ax10.scatter(data[:,3], data[:,0], c=cols)
ax11.scatter(data[:,3], data[:,1], c=cols)
ax12.scatter(data[:,3], data[:,2], c=cols)

# Show the graph
plt.show()