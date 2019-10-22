import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split

data = pd.read_csv('ConversionDataset.csv')

y = data['Bought'].values
X = data.iloc[:,[2,3]].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=27)

SVC_model = svm.SVC(gamma='auto')

clf=RandomForestClassifier(n_estimators=100)


clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
h = clf.predict_proba([[2, 0]])
print("probability:", h)

from sklearn import metrics

KNN_model = KNeighborsClassifier(n_neighbors=5)

SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)

SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)

print("\n")

print("\n")

print("\n")




