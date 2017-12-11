from sklearn.metrics.classification import accuracy_score
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split

dataset = load_iris()

X = dataset.data
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

model = SVC()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

acc_score = accuracy_score(y_test, predictions)

print (acc_score)

