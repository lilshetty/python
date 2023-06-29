from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer

positive_set = ["we are lucky","we are loved","we will win","we are best","we are happy"]
#print (positive_set)

negative_set =["we are hated","we are unlucky","we are sad","we are worst","we will lose"]
#print (negative_set)

sample_set = ["we are lucky","we are unlucky","we are worst","we are happy","we are sad"]
print(sample_set)

data_set = positive_set + negative_set
#print(data_set)
data_labels = ["POSITIVE"] * len(positive_set) + ["NEGATIVE"] *len(negative_set)
#print(data_labels)

vectorizer = CountVectorizer()
vectorizer.fit(data_set)
data_vectors = vectorizer.transform(data_set)
sample_vectors = vectorizer.transform(sample_set)
#feature_name = vectorizer.get_feature_names_out ()
#print(data_vectors.toarray())
#print("    ")
#print(sample_vectors.toarray())
#print(feature_name)

classifier  = tree.DecisionTreeClassifier ()
classifier.fit(data_vectors, data_labels)
predictions = classifier.predict (sample_vectors)
print (predictions)
