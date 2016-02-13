import unittest
import numpy as numpy
from neuralnetwork import NeuralNetwork,EstimationError

class NeuralNetworkTest(unittest.TestCase):

	def setUp(self):
		self.neuralNetwork = NeuralNetwork(eta=0.7,n_in=2,n_hidden=14,n_out=1)
		self.acceptanceEpsilon = 0.07
		self.seed = 1
		self.maxIterations = 10000

	def tearDown(self):
		del self.neuralNetwork
		del self.acceptanceEpsilon
		del self.seed

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

		self.neuralNetwork.backpropagation(x,target,maxIterations=self.maxIterations)

		# Network result after training
		estimation = self.neuralNetwork.feed_forward(x)

		estimationError = EstimationError(estimatedValues=estimation,targetValues=target)
		estimationError.computeErrors()
		totalError = estimationError.getTotalError()
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

		self.neuralNetwork.backpropagation(x,target,maxIterations=self.maxIterations)

		# Network result after training
		estimation = self.neuralNetwork.feed_forward(x)

		estimationError = EstimationError(estimatedValues=estimation,targetValues=target)
		estimationError.computeErrors()
		totalError = estimationError.getTotalError()

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

		self.neuralNetwork.backpropagation(x,target,maxIterations=self.maxIterations)

		# Network result after training
		estimation = self.neuralNetwork.feed_forward(x)

		estimationError = EstimationError(estimatedValues=estimation,targetValues=target)
		estimationError.computeErrors()
		totalError = estimationError.getTotalError()

		self.assertTrue(totalError<=self.acceptanceEpsilon)

def main():
	unittest.main()

if __name__ == '__main__':
    main()