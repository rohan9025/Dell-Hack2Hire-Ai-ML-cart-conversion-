"""
@author: Rochan Avlur - github.com/Rochan-A
"""

""" Model that looks at all user history on which product they saw and what
they finally bought """

# -*- coding: utf-8 -*-
from pomegranate import *
import numpy, pickle

class SeeBoughtRecommender():
	def __init__(self, data=None, label=None):
		self.data = data
		self.label = label

		if self.data and self.label:
			# Read the dataset for training
			data = numpy.genfromtxt(self.data, delimiter=',')

			# Learn the model on the data
			self.clf = BayesianNetwork.from_samples(data, algorithm='exact')
		else:
			raise AssertionError('No dataset or pretrained model given')

	def get_percentage(self, product):
		"""
		Get the products the user might most likely buy from the model

		Arguments
		-----------
		product: product. Value in self.label

		Returns
		-----------
		2D array with probability buying each product
		"""

		assert product in self.label, AssertionError('product not in self.label')

		#Predict the response for input
		try:
			pred = self.clf.predict_proba([self.label.index(product) + 1, None])[1].items()
		except:
			return [[]]

		l = []
		for i in pred:
			l.append([self.label[int(i[0]) - 1], i[1]])
		return l
'''
if __name__ == '__main__':

	label = ['Dell Inspiron 15 5590 v2', 'Dell Inpiron 15 5590 v3', \
		'Dell Inspiron 15 5590 v1', 'Dell Inspiron 15 7591', \
		'Dell XPS 13', 'Dell XPS 13 v2', 'Dell XPS 15 v1', \
		'Dell XPS 15 v2', 'Dell Alienware 15 v1', 'Dell Alienware 15 v2', \
		'Dell Alienware 17 v1', 'Dell Alienware 17 v2', 'Dell Latitude 14 v2', \
		'Dell Latitude 14 v3', 'Dell Latitude 14 v1', 'Dell Inspiron 17']

	model = SeeBoughtRecommender(data='my_file.csv', label=label)
	print(model.get_percentage('Dell Inpiron 15 5590 v3'))
'''