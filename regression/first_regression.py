from sklearn.linear_model import LinearRegression
import os

# Linear regression tries to create a linear equation: y = k * x + b, where x is a parameter
reg = LinearRegression(n_jobs=os.cpu_count())

reg.fit([[20, 80], [20, 100], [20, 120], [40, 80], [40, 100], [40, 120], [60, 80], [60, 100],
         [60, 120]], [100, 150, 200, 200, 250, 300, 300, 350, 400])

print(reg.coef_)  # k =
print(reg.intercept_)  # b =
