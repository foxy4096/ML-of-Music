from sklearn.tree import DecisionTreeClassifier
import pandas as pd
Age = int(input("Age "))
Gender = int(input("Gender 0 for Female and 1 for Male"))
data = pd.read_csv("music.csv")
X = data.drop(columns="genre")
y = data["genre"]
clf = DecisionTreeClassifier()
clf.fit(X, y)
predictions = clf.predict([[Age, Gender]])
