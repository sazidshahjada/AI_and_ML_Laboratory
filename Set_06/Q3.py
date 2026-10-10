import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
X,y=load_iris(return_X_y=True); names=load_iris().target_names
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.30,stratify=y,random_state=42)
models={"k-NN k=5":KNeighborsClassifier(n_neighbors=5),"Decision Tree depth=3":DecisionTreeClassifier(max_depth=3,random_state=42)}
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
for (name,m), ax in zip(models.items(), axes):
    m.fit(Xtr,ytr); p=m.predict(Xte)
    print(f"\\n{name} accuracy={accuracy_score(yte,p):.4f}")
    print("Confusion matrix:\\n",confusion_matrix(yte,p))
    wrong=np.where(p!=yte)[0]
    print("Misclassified test rows (test-row-index, true, predicted):",[(int(i),names[yte[i]],names[p[i]]) for i in wrong])
    ConfusionMatrixDisplay.from_predictions(yte, p, display_labels=names, cmap="Blues", values_format="d", colorbar=False, ax=ax)
    ax.set_title(name)
scaled=make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=5)).fit(Xtr,ytr)
ps=scaled.predict(Xte)
print(f"\\nScaled k-NN accuracy={accuracy_score(yte,ps):.4f}")
print("Scaled k-NN confusion matrix:\\n",confusion_matrix(yte,ps))
ConfusionMatrixDisplay.from_predictions(yte, ps, display_labels=names, cmap="Blues", values_format="d", colorbar=False, ax=axes[2])
axes[2].set_title("Scaled k-NN k=5")
fig.suptitle("Iris test-set confusion matrices")
fig.tight_layout()
plt.show()
print("Scaling changes distance geometry for k-NN. Decision trees split one feature at a time and are largely invariant to monotonic feature scaling.")
