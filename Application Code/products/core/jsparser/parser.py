"""
	This is to parse the data given by the AJAX POST from the four webpages.

	Author: IceCereal
"""

class parser:
	def __init__(self, timestamps_raw : list):
		"""
			timestamps : list of strings
			['1561234', '1561237', ...]

			returns : (int) total time spent on the website
		"""

		self.timestamps = []

		for timeVal in timestamps_raw:
			self.timestamps.append(int(timeVal))

	def parse(self):
		timeSpent = 0

		for i in range(1,len(self.timestamps),2):
			try:
				timeSpent += self.timestamps[i] - self.timestamps[i-1]
			except:
				pass

		return timeSpent

"""
	This is to get the percentage of time spent in each section.

	Author: IceCereal
"""

class calcPercentage:
	def __init__(self, data : dict):
		"""
			data : dict of section times

			returns: (dict) of section times as percentages
		"""

		self.data = data

	def calculate_percentage(self):
		percentage_data = {}
		total_time = 0

		for key in self.data:
			total_time += self.data[key]

		for key in self.data:
			percentage_data[key] = self.data[key] / total_time


		return (percentage_data)