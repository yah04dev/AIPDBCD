khsais=[[2,3],[1,5],[3,5],[8,6],[2,10],[5,3],[3,15],[10,6.5],[7,17],[17,25]
naw3=["cat","dog","cat","cat","dog","cat","dog","cat","dog","dog"]
from sklearn import tree
mosanif = tree.DecisionTreeClassifier()
mosanif = mosanif.fit(khsais,naw3)
age=input("entre the age:")
poids=input("entre his poids with(kg):")
print(mosanif.predict([[age,poids]]))
