from .energy import Energy
from time import sleep

class Mitochondria:
	def __init__(self):
		self.CurrentEnergy = None
	
	def produce(self):
		self.CurrentEnergy = Energy()
		sleep(0.01)
		self.CurrentEnergy.makeUseable()