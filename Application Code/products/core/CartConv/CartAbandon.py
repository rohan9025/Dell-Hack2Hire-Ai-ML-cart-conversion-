"""
@author: Rochan Avlur - github.com/Rochan-A
"""

""" Model that uses the time spent on different sections on the product page to
 predict possibility of cart abandonment """

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import pickle

from sklearn import svm

from sklearn.model_selection import train_test_split
from sklearn import metrics

# Set Global Seed for SVM Classifier
RSEED = 50

class CartAbandon():
	def __init__(self, model=None, data=None):
		self.model = model
		self.data = data

		# Create a svm Classifier with linear kernel
		self.clf = svm.SVC(kernel='linear', probability=True)

		if self.model:
			# load the model from disk
			self.clf = pickle.load(open(model, 'rb'))
		else:
			if self.data:
				# Read the dataset for training
				self.dataset = pd.read_csv('smaller.csv')

				# Extract the labels
				labels = np.array(self.dataset.pop('label'))

				# Split the data
				train, self.test, \
				train_labels, self.test_labels = \
					train_test_split(self.dataset, \
						labels, stratify = labels, \
							test_size = 0.2, \
							random_state = RSEED)

				# Imputation of missing values
				train = train.fillna(train.mean())
				self.test = self.test.fillna(self.test.mean())

				# Features for feature importances
				features = list(train.columns)

				#Train the model using the training sets
				self.clf.fit(train, train_labels)
			else:
				raise AssertionError('No dataset or pretrained model given')

	def performance(self):
		"""
		Check the performance of the model on the test data. Prints
		the percentage, accuracy, precision and recall.

		Arguments
		-----------
		None

		Returns
		-----------
		None
		"""

		assert self.data, AssertionError('Dataset was not provided')

		#Predict the response for test dataset
		y_pred = self.clf.predict(self.test)
		print("Percentage: ",self.clf.predict_proba(self.test))

		# Model Accuracy: how often is the classifier correct?
		print("Accuracy:",metrics.accuracy_score(self.test_labels, y_pred))

		# Model Precision: what percentage of positive tuples are labeled as such?
		print("Precision:",metrics.precision_score(self.test_labels, y_pred))

		# Model Recall: what percentage of positive tuples are labelled as such?
		print("Recall:",metrics.recall_score(self.test_labels, y_pred))

	def get_percentage(self, time_split : dict):
		"""
		Get the abandonment and continuation percentage from the
		trained model.

		Arguments
		-----------
		time_split: Time split in dict.
		Ex. {'screen': 0.4, 'cpu': 0.1, 'gpu': 0.1, 'price': 0.2, 'memory': 0.2}

		Returns
		-----------
		Dict with probability of both classes for the given input
		"""
		#Predict the response for input
		l = [[time_split['cpu'], time_split['gpu'], time_split['screen'], time_split['memory'], time_split['price']]]
		return {'Abandon': self.clf.predict_proba(l)[0][0], 'Checkout': self.clf.predict_proba(l)[0][0]}

	def save(self, filename='final_model.sav'):
		"""
		Save the trained model

		Arguments
		-----------
		filename: filename to save the model. default: final_model.sav

		Returns
		-----------
		None
		"""
		# save the model to disk
		pickle.dump(self.clf, open(filename, 'wb'))

'''
if __name__ == '__main__':

	sample = {'screen': 0.4, 'cpu': 0.1, 'gpu': 0.1, 'price': 0.2, 'memory': 0.2}
	model = CartAbandon(model='final_model.sav')
	print(model.get_percentage(sample))
'''