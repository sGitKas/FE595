import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


#Synopsis :
#https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()

iris = load_iris()
#lets first looks at the data and understand it
print(iris)

X = pd.DataFrame(iris.data, columns=iris['feature_names'])
iris_data = X[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)']]

# Lets assume that we dont know anything about the data and try to find the best number of clusters by using the Elbow Method


#Cluster object just like the others has a fit and predict methods
cluster = KMeans(n_clusters=3,
                 #random_state='',
                 init ='k-means++', # 'random'
                 n_init=3,
                 max_iter=3
                 )

# Fit will try to find the centroid
cluster.fit(iris_data)


#


#print(X)
data = X[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)']]

# We can store the inertia values for the various values of  cluser values from 0 to 10 and see how the Standard error reduces as N increases.

# Inertia: Sum of distances of samples to their closest cluster center
sse = {}
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, max_iter=1000).fit(data)
    data["clusters"] = kmeans.labels_
    sse[k] = kmeans.inertia_

plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel("Number of cluster")
plt.ylabel("SSE")
plt.show()