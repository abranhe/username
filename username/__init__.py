import sys
import os

class u():
	def __call__(self):
		return os.path.split(os.path.expanduser('~'))[-1]

sys.modules[__name__] = u()
