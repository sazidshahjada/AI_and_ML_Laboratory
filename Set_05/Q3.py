import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)
models = {}
depths = [1, 2, 3, 4, None]
train_scores, test_scores = [], []
for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X_train, y_train)
    train_score = accuracy_score(y_train, model.predict(X_train))
    test_score = accuracy_score(y_test, model.predict(X_test))
    models[depth] = model
    train_scores.append(train_score)
    test_scores.append(test_score)
    print(f"max_depth={depth}: train accuracy={train_score:.4f}, test accuracy={test_score:.4f}")

best_depth = max(models, key=lambda depth: accuracy_score(y_test, models[depth].predict(X_test)))
best = models[best_depth]
predictions = best.predict(X_test)
print("Best depth by test accuracy:", best_depth)
print("Confusion matrix:\\n", confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions, target_names=iris.target_names))

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].plot(range(len(depths)), train_scores, marker="o", label="Train")
axes[0].plot(range(len(depths)), test_scores, marker="s", label="Test")
axes[0].set_xticks(range(len(depths)), [str(depth) for depth in depths])
axes[0].set(xlabel="Maximum tree depth", ylabel="Accuracy", title="Accuracy by tree depth")
axes[0].set_ylim(0, 1.05)
axes[0].grid(alpha=0.25)
axes[0].legend()
ConfusionMatrixDisplay.from_predictions(
    y_test, predictions, display_labels=iris.target_names,
    cmap="Blues", values_format="d", colorbar=False, ax=axes[1],
)
axes[1].set_title(f"Best tree (max_depth={best_depth})")
fig.tight_layout()
plt.show()
print("Shallow trees may underfit; very deep trees may overfit. Test performance, not training accuracy alone, guides selection.")
