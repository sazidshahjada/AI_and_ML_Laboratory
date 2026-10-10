import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# Example problem: predict a small machine's output from operating hours.
X=np.array([1,2,3,4,5,6,7,8,9,10,11,12],float).reshape(-1,1)
y=np.array([3.2,4.1,5.9,7.8,9.1,11.2,12.8,15.1,16.4,18.9,20.2,22.1])
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42)
m=LinearRegression().fit(Xtr,ytr)
print(f"Slope={m.coef_[0]:.4f}, intercept={m.intercept_:.4f}")
print(f"Train R^2={r2_score(ytr,m.predict(Xtr)):.4f}")
print(f"Test R^2={r2_score(yte,m.predict(Xte)):.4f}")
print("Predictions at 13 and 15 hours:",m.predict([[13],[15]]))
xx=np.linspace(0,16,100).reshape(-1,1)
plt.scatter(Xtr,ytr,label="Train");plt.scatter(Xte,yte,label="Test",marker="x")
plt.plot(xx,m.predict(xx),label="Fitted line");plt.xlabel("Operating hours");plt.ylabel("Output");plt.legend();plt.tight_layout();plt.show()
print("Interpretation: the fitted slope estimates average output increase per operating hour. Limitation: a linear trend may fail outside the observed range or when other factors change.")
