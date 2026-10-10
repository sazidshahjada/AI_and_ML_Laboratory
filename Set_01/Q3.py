import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

X,y=load_iris(return_X_y=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,stratify=y,random_state=42)
scores={}
for k in [1,3,5,7]:
    model=KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)
    pred=model.predict(X_test); scores[k]=accuracy_score(y_test,pred)
    print(f"k={k}: accuracy={scores[k]:.4f}")
best_k=max(scores,key=scores.get)
print(f"Best k (ties resolved by first encountered): {best_k}")
plain=KNeighborsClassifier(n_neighbors=best_k).fit(X_train,y_train)
pred=plain.predict(X_test)
pred_unscaled = pred
print("Unscaled confusion matrix:\\n",confusion_matrix(y_test,pred_unscaled))
scaled=make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=best_k)).fit(X_train,y_train)
pred_s=scaled.predict(X_test)
print(f"Scaled accuracy={accuracy_score(y_test,pred_s):.4f}")
print("Scaled confusion matrix:\\n",confusion_matrix(y_test,pred_s))
print("Scaled classification report:\\n",classification_report(y_test,pred_s,target_names=load_iris().target_names))
print("Comment: k-NN uses distances, so feature scaling can change neighbor rankings and accuracy.")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, predictions, title in zip(
    axes,
    (pred_unscaled, pred_s),
    ("Unscaled k-NN", "Scaled k-NN"),
):
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        predictions,
        display_labels=load_iris().target_names,
        cmap="Blues",
        values_format="d",
        colorbar=False,
        ax=ax,
    )
    ax.set_title(title)
fig.suptitle(f"Iris k-NN confusion matrices (k={best_k})")
fig.tight_layout()
plt.show()
