from sklearn.tree import DecisionTreeClassifier
import pandas as pd
clf = DecisionTreeClassifier()
data = pd.read_csv("music.csv")
X = data.drop(columns="genre")
y = data["genre"]
clf.fit(X, y)
predictions = clf.predict([[60, 1]])
print(predictions)