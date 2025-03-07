#-------------------------------------------------------------------------
# AUTHOR: Jimmy Nguyen
# FILENAME: decision_tree.py
# SPECIFICATION: This program reads a csv file and outputs a decision tree.
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
# Table of Data --> Numerics
#---------------------------#
# Age:                        Young (1), Prepresbyopic (2), Presbyopic (3)
# Spectacle Prescription:     Myope (1), Hypermetrope (2)
# Astigmatism:                Yes (1), No (2)
# Tear Production Rate:       Reduced (1), Normal (2)
feature_conversions = {
   "Young": 1, "Prepresbyopic": 2, "Presbyopic": 3,
   "Myope": 1, "Hypermetrope": 2,
   "Yes": 1, "No": 2,         # 
   "Reduced": 1, "Normal": 2
}

for row in db:
   X.append([feature_conversions[row[0]], feature_conversions[row[1]], feature_conversions[row[2]], feature_conversions[row[3]]])
   Y.append(1 if row[4] == "Yes" else 2)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> addd your Python code here


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()