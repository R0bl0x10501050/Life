class Energy:
	def __init__(self):
		self.type = "potential"
		self.__useable = False
		self.value = 1

	def makeUseable(self):
		self.__useable = True
	
	def use(self):
		return self.value

	def _toPotential(self):
		self.type = "potential"

	def _toKinetic(self):
		self.type = "kinetic"

	def _toThermal(self):
		self.type = "thermal"

	def _toChemical(self):
		self.type = "chemical"

	def _toGravitational(self):
		self.type = "gravitational"

	def _toRadiant(self):
		self.type = "radiant"

	def _toMechanical(self):
		self.type = "mechanical"

	def _toSound(self):
		self.type = "sound"

	def _toElasticPotential(self):
		self.type = "elastic_potential"

	def _toLight(self):
		self.type = "light"

	def _toRotational(self):
		self.type = "rotational"

	def _toMagnetic(self):
		self.type = "magnetic"

	def _toElectricPotential(self):
		self.type = "electric_potential"

	def _toSurface(self):
		self.type = "surface"

	def _toBinding(self):
		self.type = "binding"