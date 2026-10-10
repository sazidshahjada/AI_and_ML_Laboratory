import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support, classification_report, ConfusionMatrixDisplay
iris = load_iris()
X, y, names = iris.data, iris.target, iris.target_names
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)
models = [
    ("k-NN k=3", KNeighborsClassifier(n_neighbors=3)),
    ("Decision Tree max_depth=3", DecisionTreeClassifier(max_depth=3, random_state=42)),
]
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
for (name, model), ax in zip(models, axes):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"\n{name}: accuracy={accuracy_score(y_test, predictions):.4f}")
    print("Confusion matrix:\n", confusion_matrix(y_test, predictions))
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, predictions, average="macro", zero_division=0
    )
    print(f"Macro precision={precision:.4f}, recall={recall:.4f}, F1={f1:.4f}")
    print(classification_report(y_test, predictions, target_names=names))
    wrong = np.where(predictions != y_test)[0]
    errors = [
        (int(index), names[y_test[index]], names[predictions[index]])
        for index in wrong
    ]
    print("Misclassified test rows (test-row-index, true, predicted):", errors)
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        predictions,
        display_labels=names,
        cmap="Blues",
        values_format="d",
        colorbar=False,
        ax=ax,
    )
    ax.set_title(name)
fig.suptitle("Iris test-set confusion matrices")
fig.tight_layout()
plt.show()
print("Choose based on this split's test metrics and practical needs; this is one run, not proof that one model is universally better.")
import matplotlib.pyplot as plt
