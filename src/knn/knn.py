import pandas as pd
from sklearn import neighbors as nb

col_names = ["weight", "height", "size"]
dataset = pd.read_csv("t-shirts.csv", names=col_names)
X = dataset[["weight", "height"]]
y = dataset[["size"]]

clasifier = nb.KNeighborsClassifier(n_neighbors=3).fit(X, y)
avg = X.mean()
x_star = pd.DataFrame(avg).T
p = clasifier.predict(x_star)
print(p)
