import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
iris=load_iris(); X=iris.data
for label,data in [("Unscaled",X),("Standardized",StandardScaler().fit_transform(X))]:
    km=KMeans(n_clusters=3,random_state=42,n_init=10).fit(data)
    print(f"\\n{label}: inertia={km.inertia_:.4f}, silhouette={silhouette_score(data,km.labels_):.4f}")
    print("Centers (in current feature scale):\\n",km.cluster_centers_)
    # Show first two features in the original units, coloring by each model's labels
    plt.figure()
    plt.scatter(X[:,0],X[:,1],c=km.labels_,s=25)
    centers=km.cluster_centers_[:,:2]
    if label=="Standardized":
        centers=StandardScaler().fit(X).inverse_transform(km.cluster_centers_)[:,:2]
    plt.scatter(centers[:,0],centers[:,1],marker="X",s=180,edgecolor="black")
    plt.xlabel(iris.feature_names[0]);plt.ylabel(iris.feature_names[1]);plt.title(f"Iris K-means k=3 — {label}")
    plt.tight_layout()
plt.show()
print("Do not compare inertia across different feature scales directly: squared distances are measured in different units.")
