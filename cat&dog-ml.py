khsais=[[2,3],[1,5],[3,5],[8,6],[2,10],[5,3],[3,15],[10,6.5],[7,17],[17,25]
#ksais are a variable or groupe of lists countain a groupe of exampels of cat & dog [age,weight]
naw3=["cat","dog","cat","cat","dog","cat","dog","cat","dog","dog"]
#ksais are a variable or groupe of lists Shows each characteristic and who owns it
from sklearn import tree
mosanif = tree.DecisionTreeClassifier()
mosanif = mosanif.fit(khsais,naw3)
age=input("entre the age:")
poids=input("entre his poids with(kg):")
print(mosanif.predict([[age,poids]]))
#This program is programmed thanks yah04 You can change the names of variables and examples according to your needs
