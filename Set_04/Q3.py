import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X=np.array([2,4,6,8,10,12],float).reshape(-1,1)
y=np.array([5,9,13,17,21,25],float)
def report(target,label):
    m=LinearRegression().fit(X,target); p=m.predict(X)
    print(f"{label}: slope={m.coef_[0]:.4f}, intercept={m.intercept_:.4f}, prediction at 15={m.predict([[15]])[0]:.4f}, R^2={r2_score(target,p):.4f}")
    return m
m=report(y,"Original")
y2=y.copy(); y2[2]+=5 # transparent modification: change the observation at X=6 from 13 to 18
m2=report(y2,"Modified (Y at X=6 changed from 13 to 18)")
xx=np.linspace(0,16,100).reshape(-1,1)
plt.scatter(X,y,label="Original"); plt.plot(xx,m.predict(xx),label="Original fit")
plt.scatter(X,y2,marker="x",label="Modified"); plt.plot(xx,m2.predict(xx),label="Modified fit")
plt.xlabel("X"); plt.ylabel("Y"); plt.legend(); plt.tight_layout(); plt.show()
