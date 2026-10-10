# Python/scikit-learn equivalent of the WEKA Explorer exercise.
# For the exact submission, also run J48 and IBk in WEKA Explorer and save its result buffer.
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

iris = load_iris()
X, y = iris.data, iris.target
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
models = [
    ("J48-like Decision Tree", DecisionTreeClassifier(random_state=42)),
    ("IBk k=1", KNeighborsClassifier(n_neighbors=1)),
    ("IBk k=3", KNeighborsClassifier(n_neighbors=3)),
    ("IBk k=5", KNeighborsClassifier(n_neighbors=5)),
]

fig, axes = plt.subplots(2, 2, figsize=(11, 9))
for (name, model), ax in zip(models, axes.flat):
    predictions = cross_val_predict(model, X, y, cv=cv)
    print(f"\\n{name}: accuracy={accuracy_score(y, predictions):.4f}")
    print("Confusion matrix:\\n", confusion_matrix(y, predictions))
    print(classification_report(y, predictions, target_names=iris.target_names))
    ConfusionMatrixDisplay.from_predictions(
        y, predictions, display_labels=iris.target_names,
        cmap="Blues", values_format="d", colorbar=False, ax=ax,
    )
    ax.set_title(name)
fig.suptitle("Iris 10-fold cross-validation confusion matrices")
fig.tight_layout()
plt.show()
print("WEKA note: sklearn DecisionTree is conceptually similar to J48, but is not an identical implementation.")
