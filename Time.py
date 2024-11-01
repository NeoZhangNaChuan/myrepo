class Time:
	def __init__(self, hour, minute):
		self.hour = hour
		self.minute = minute

	def __lt__(self, other):
		return (self.hour, self.minute) < (other.hour, other.minute)

	def __len__(self):
		return self.hour * 60 + self.minute

	def tick(self):
		self.minute = self.minute + 1
		if self.minute >= 60:
			self.minute = 0
			self.hour = (self.hour + 1) % 24

	def __str__(self):
		return str(self.hour) + ':' + str(self.minute)

	def getTime(self):
		return self.hour, self.minute

	def __sub__(self, other):
		total_minute_self = self.hour * 60 + self.minute
		total_minute_other = other.hour * 60 + other.minute
		diff_minutes = abs(total_minute_self - total_minute_other)
		hours = diff_minute // 60
		minutes = diff_minutes % 60
		return str(hours) + " hours and " + str(minutes) + " minutes"

	def setTime(self, hour, minute):
		self.hour = hour % 24
		self.minute = minute % 60


