import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.patches as mpatches

X = np.array([[6,4],[12,17],[16,14],[22,12],[31,41],[60,72],[69,81],[63,74],[52,53],[82,89]])
plt.scatter(X[:,0],X[:,1])

kmeans = KMeans(n_clusters=2,max_iter=3)
kmeans.fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
print(kmeans.n_iter_)


plt.scatter(X[:,0],X[:,1],c=kmeans.labels_,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="green", label="Clusters' center points",marker="*")





red_patch = mpatches.Patch(color='red', label='Cluster points')
purple_patch = mpatches.Patch(color='purple',label='Another cluster points')
green_patch = mpatches.Patch(color='green',label="Clusters' centers")
plt.legend(handles=[red_patch,purple_patch,green_patch])
plt.title('Visualization of clusters & centroids')
plt.show()