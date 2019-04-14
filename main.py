import ctypes

_MNISTDemoBits = ctypes.CDLL('MNISTDemoBitsDynamicallyLoadable.so')

"""
	# Tsetlin Machine Bits
"""
class TsetlinMachineBits(object):
	
	# Initializations
	def __init__(self):
		self.TsetlinMachine = None
		self.CreateTsetlinMachine()

	# Set up the Tsetlin Machine structure
	def CreateTsetlinMachine(self):
		self.TsetlinMachine = _MNISTDemoBits.CreateTsetlinMachine()

	# Set up the Tsetlin Machine structure
	## tm: Pointer to Tsetlin Machine
	def tm_initialize(self, tm):
		_MNISTDemoBits.tm_initialize(tm)

	## tm: Pointer to Tsetlin Machine
	## s: float
	def tm_initialize_random_streams(self, tm, s):
		_MNISTDemoBits.tm_initialize_random_streams(tm, s)


	# Increment the states of each of those 32 Tsetlin Automata flagged in the active bit vector.
	## tm: Pointer to Tsetlin Machine
	## clause: int
	## chunk: int
	## active: unsigned int
	def tm_inc(self, tm, clause, chunk, active):
		_MNISTDemoBits.tm_inc(tm, clause, chunk, active)

	# Decrement the states of each of those 32 Tsetlin Automata flagged in the active bit vector.
	## tm: Pointer to Tsetlin Machine
	## clause: int
	## chunk: int
	## active: unsigned int
	def tm_dec(self, tm, clause, chunk, active):
		_MNISTDemoBits.tm_dec(tm, clause, chunk, active)

	# Sum up the votes for each class
	## tm: Pointer to Tsetlin Machine
	def sum_up_class_votes(self, tm):
		_MNISTDemoBits.sum_up_class_votes(tm)

	# Calculate the output of each clause using the actions of each Tsetline Automaton.
	## tm: Pointer to Tsetlin Machine
	## Xi: int array
	## predict: int
	def tm_calculate_clause_output(self, tm, Xi, predict):
		_MNISTDemoBits.tm_calculate_clause_output(tm, Xi, predict)

	# The Tsetlin Machine can be trained incrementally, one training example at a time.
	# Use this method directly for online and incremental training.
	## tm: Pointer to Tsetlin Machine
	## Xi: int array
	## target: int
	## s: float
	def tm_update(self, tm, Xi, target, s):
		_MNISTDemoBits.tm_update(tm, Xi, target, s)

	# Calculate Clause Output, Sum up Clause Votes
	## tm: Pointer to Tsetlin Machine
	## Xi: int array
	def tm_score(self, tm, Xi):
		return _MNISTDemoBits.tm_score(tm, Xi)

	# Get State of Tsetlin Machine
	## tm: Pointer to Tsetlin Machine
	## clause: int
	## la: int
	def tm_get_state(self, tm, clause, la):
		return _MNISTDemoBits.tm_get_state(tm, clause, la)

	## tm: Pointer to Tsetlin Machine
	## clause: int
	## la: int
	def tm_action(self, tm, clause, la):
		return _MNISTDemoBits.tm_action(tm, clause, la)

"""
	# Multiclass Tsetlin Machine Bits
"""

class MultiClassTsetlinMachineBits(object):

	# Initializations
	def __init__(self):
		self.MultiClassTsetlinMachine = None
		self.CreateMultiClassTsetlinMachine()

	# Initialize the Multiclass Tsetlin Machine structure
	## mc_tm: Pointer to Multiclass Tsetlin Machine
	def mc_tm_initialize(self, mc_tm):
		_MNISTDemoBits.mc_tm_initialize(mc_tm)

	# Evaluate the Trained Tsetlin Machine
	## mc_tm: Pointer to Multiclass Tsetlin Machine
	## X: 2D-int array
	## y: int array
	## number_of_examples: int
	def mc_tm_evaluate(self, mc_tm, X, y, number_of_examples):
		return _MNISTDemoBits.mc_tm_evaluate(mc_tm, X, y, number_of_examples)

	# Online Training of Tsetlin Machine
	## mc_tm: Pointer to Multiclass Tsetlin Machine
	## Xi: int array
	## target_class: int
	## s: float
	def mc_tm_update(self, mc_tm, Xi, target_class, s):
		_MNISTDemoBits.mc_tm_update(mc_tm, Xi, target_class, s)

	# Batch Mode Training of Tsetlin Machine
	## mc_tm: Pointer to Multiclass Tsetlin Machine
	## X: 2D-int array
	## y: int array
	## number_of_examples: int
	## epochs: int
	## s: float
	def mc_tm_fit(self, mc_tm, X, y, number_of_examples, epochs, s):
		_MNISTDemoBits.mc_tm_fit(mc_tm, X, y, number_of_examples, epochs, s)

# MNIST DEMO
def MNISTDemoBits():
	global _MNISTDemoBits
	_MNISTDemoBits.main()

"""
Main program
"""
if __name__ == '__main__':
	MNISTDemoBits();