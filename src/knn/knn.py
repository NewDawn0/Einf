import pandas as pd
from sklearn import neighbors as nb

col_names = ["weight", "height", "size"]
dataset = pd.read_csv("t-shirts.csv", names=col_names)

x = dataset[["weight", "height"]]
y = dataset[["size"]]

classifier = nb.KNeighborClassifier(n_neighbors=3)
classifier.fit(x, y)
avg = x.mean()
x_star = pd.DataFrame(avg).T
p = classifier.predict(x_star)
print(p)
