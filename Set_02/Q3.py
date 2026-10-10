import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X=np.array([1,2,3,4,5,6],dtype=float).reshape(-1,1)
y=np.array([4,5,8,9,11,14],dtype=float)
def fit_and_report(y,label):
    model=LinearRegression().fit(X,y); pred=model.predict(X)
    print(f"{label}: slope={model.coef_[0]:.4f}, intercept={model.intercept_:.4f}, prediction at 7 hours={model.predict([[7]])[0]:.4f}, R^2={r2_score(y,pred):.4f}")
    return model,pred
m1,p1=fit_and_report(y,"Original data")
y2=y.copy(); y2[-1]=18
m2,p2=fit_and_report(y2,"After changing score at 6 hours to 18")
xx=np.linspace(1,7,100).reshape(-1,1)
plt.scatter(X,y,label="Original observations"); plt.plot(xx,m1.predict(xx),label="Original fit")
plt.scatter(X,y2,marker="x",label="Modified observations"); plt.plot(xx,m2.predict(xx),label="Modified fit")
plt.xlabel("Study hours"); plt.ylabel("Score"); plt.title("Linear regression before and after target change"); plt.legend(); plt.tight_layout(); plt.show()
print("R² measures the fraction of target variance explained by the fitted linear model; an outlying change can raise or lower it.")
