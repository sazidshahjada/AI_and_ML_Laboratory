import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
X=load_iris().data[:,:2]
iris=load_iris()
for k in [2,3,4,5]:
    model=KMeans(n_clusters=k,random_state=42,n_init=10).fit(X)
    sil=silhouette_score(X,model.labels_)
    print(f"k={k}: inertia={model.inertia_:.4f}, silhouette={sil:.4f}")
    plt.figure()
    plt.scatter(X[:,0],X[:,1],c=model.labels_,s=25)
    plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],marker="X",s=180,edgecolor="black")
    plt.xlabel(iris.feature_names[0]); plt.ylabel(iris.feature_names[1]); plt.title(f"K-means on first two Iris features (k={k})")
    plt.tight_layout()
plt.show()
print("Cluster IDs are arbitrary IDs assigned by the algorithm, not Iris species labels; cluster 0 need not mean setosa.")
