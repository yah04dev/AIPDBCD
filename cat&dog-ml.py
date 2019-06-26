khsais=[[2,3],[1,5],[3,5],[8,6],[2,10],[5,3],[3,15],[10,6.5],[7,17],[17,25]
#ksais are a variable or groupe of lists countain a groupe of exampels of cat & dog [age,weight]
naw3=["cat","dog","cat","cat","dog","cat","dog","cat","dog","dog"]
#ksais are a variable or groupe of lists Shows each characteristic and who owns it
from sklearn import tree
#sklearn (skitlearn) are the The best library of machine learning in python & tree Is the decision tree, the tools we relied on to train the machine in this example
mosanif = tree.DecisionTreeClassifier()
mosanif = mosanif.fit(khsais,naw3)
#Within the FET function, we set properties and their owners to start the decision tree by thinking and defining rules
age=input("entre the age:")
poids=input("entre his poids with(kg):")
print(mosanif.predict([[age,poids]]))
#This program is programmed thanks yah04 
