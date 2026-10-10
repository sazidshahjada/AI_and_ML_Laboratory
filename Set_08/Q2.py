from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_predict,StratifiedKFold
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
X,y=load_iris(return_X_y=True); cv=StratifiedKFold(n_splits=10,shuffle=True,random_state=42)
models=[
 ("IBk/k-NN k=5 raw",KNeighborsClassifier(5)),
 ("IBk/k-NN k=5 standardized",make_pipeline(StandardScaler(),KNeighborsClassifier(5))),
 ("IBk/k-NN k=5 normalized",make_pipeline(MinMaxScaler(),KNeighborsClassifier(5))),
 ("J48-like Decision Tree",DecisionTreeClassifier(random_state=42))]
fig, axes = plt.subplots(2, 2, figsize=(11, 9))
for (name,m), ax in zip(models, axes.flat):
    pred=cross_val_predict(m,X,y,cv=cv)
    print(f"\\n{name}: accuracy={accuracy_score(y,pred):.4f}")
    print("Confusion matrix:\\n",confusion_matrix(y,pred))
    ConfusionMatrixDisplay.from_predictions(
        y, pred, display_labels=load_iris().target_names,
        cmap="Blues", values_format="d", colorbar=False, ax=ax,
    )
    ax.set_title(name)
fig.suptitle("Iris 10-fold cross-validation confusion matrices")
fig.tight_layout()
plt.show()
print("Exact WEKA Explorer screenshots/result-buffer output must be captured in WEKA separately; sklearn's tree is not byte-for-byte J48.")
import matplotlib.pyplot as plt
