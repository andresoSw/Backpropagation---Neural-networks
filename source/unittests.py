import unittest
import numpy as numpy
from neuralnetwork import NeuralNetwork,EstimationError

class NeuralNetworkTest(unittest.TestCase):

	def setUp(self):
		self.neuralNetwork = NeuralNetwork(learning_rate=0.7,n_hidden=4)
		self.acceptanceEpsilon = 0.063
		self.seed = 1
		self.maxIterations = 11000

	def tearDown(self):
		del self.neuralNetwork
		del self.acceptanceEpsilon
		del self.seed
		del self.maxIterations

	def retrieveEstimationError(self,x,target):

		#setting number of inputs and number of outputs in the neural network
		_ , xColumns = x.shape
		_ , targetColumns = target.shape
		self.neuralNetwork.n_in = xColumns
		self.neuralNetwork.n_out = targetColumns

		self.neuralNetwork.initialize_weights()

		self.neuralNetwork.backpropagation(x,target,maxIterations=self.maxIterations)

		# Network result after training
		estimation = self.neuralNetwork.feed_forward(x)

		estimationError = EstimationError(estimatedValues=estimation,targetValues=target)
		estimationError.computeErrors()
		totalError = estimationError.getTotalError()
		return totalError

	def testXOR(self):
		numpy.random.seed(seed=self.seed)
		x = numpy.array([[0,0],
		      [0,1],
		      [1,0],
		      [1,1]])
		target = numpy.array([[0]
			  ,[1]
			  ,[1]
			  ,[0]])

		totalError = self.retrieveEstimationError(x,target)
		self.assertTrue(totalError<=self.acceptanceEpsilon)

	def testOR(self):
		numpy.random.seed(seed=self.seed)
		x = numpy.array([[0,0],
		      [0,1],
		      [1,0],
		      [1,1]])
		target = numpy.array([[0]
			  ,[1]
			  ,[1]
			  ,[1]])

		totalError = self.retrieveEstimationError(x,target)
		self.assertTrue(totalError<=self.acceptanceEpsilon)

	def testAND(self):
		numpy.random.seed(seed=self.seed)
		x = numpy.array([[0,0],
		      [0,1],
		      [1,0],
		      [1,1]])
		target = numpy.array([[0]
			  ,[0]
			  ,[0]
			  ,[1]])

		totalError = self.retrieveEstimationError(x,target)
		self.assertTrue(totalError<=self.acceptanceEpsilon)

	#test (x1 or x2) and x3
	def testORAND(self):
		numpy.random.seed(seed=self.seed)
		x = numpy.array([[0,0,0],
		      [0,0,1],
		      [0,1,0],
		      [1,0,0],
		      [0,1,1],
		      [1,1,0],
		      [1,0,1],
		      [1,1,1]])
		target = numpy.array([[0]
			  ,[0]
			  ,[0]
			  ,[0]
			  ,[1]
			  ,[0]
			  ,[1]
			  ,[1]])

		totalError = self.retrieveEstimationError(x,target)
		self.assertTrue(totalError<=self.acceptanceEpsilon)

		#test (x1 and x2) or x3
	def testANDOR(self):
		numpy.random.seed(seed=self.seed)
		x = numpy.array([[0,0,0],
		      [0,0,1],
		      [0,1,0],
		      [1,0,0],
		      [0,1,1],
		      [1,1,0],
		      [1,0,1],
		      [1,1,1]])
		target = numpy.array([[0]
			  ,[1]
			  ,[0]
			  ,[0]
			  ,[1]
			  ,[1]
			  ,[1]
			  ,[1]])

		totalError = self.retrieveEstimationError(x,target)
		self.assertTrue(totalError<=self.acceptanceEpsilon)

def main():
	unittest.main()

if __name__ == '__main__':
    main()