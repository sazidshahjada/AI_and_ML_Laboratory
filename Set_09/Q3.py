import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
X=load_iris().data[:,:2]; iris=load_iris(); ks=[2,3,4,5]
inertias=[];silhouettes=[]
for k in ks:
    km=KMeans(n_clusters=k,random_state=42,n_init=10).fit(X)
    inertias.append(km.inertia_);silhouettes.append(silhouette_score(X,km.labels_))
    print(f"k={k}: inertia={km.inertia_:.4f}, silhouette={silhouettes[-1]:.4f}")
plt.figure();plt.plot(ks,inertias,"o-");plt.xlabel("k");plt.ylabel("Inertia");plt.title("Elbow plot");plt.tight_layout()
plt.figure();plt.plot(ks,silhouettes,"o-");plt.xlabel("k");plt.ylabel("Silhouette score");plt.title("Silhouette vs k");plt.tight_layout()
best_k=ks[max(range(len(ks)),key=lambda i:silhouettes[i])]
km=KMeans(n_clusters=best_k,random_state=42,n_init=10).fit(X)
plt.figure();plt.scatter(X[:,0],X[:,1],c=km.labels_,s=25);plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],marker="X",s=180,edgecolor="black")
plt.xlabel(iris.feature_names[0]);plt.ylabel(iris.feature_names[1]);plt.title(f"Selected k={best_k}");plt.tight_layout();plt.show()
print("Selected k by highest silhouette among tested values:",best_k)
print("Inertia generally decreases as k grows because each point can be assigned to one of more, smaller clusters.")
