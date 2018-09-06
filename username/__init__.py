import sys
import os

class Username():
	user = os.path.split(os.path.expanduser('~'))[-1]

	def __call__(self):
		return  self.user

sys.modules[__name__] = Username()
