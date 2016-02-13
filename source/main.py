import numpy as np
from neuralnetwork import NeuralNetwork,EstimationError

if __name__ == '__main__':

	np.random.seed(seed=1) #using fixed seed for testing purposes

	x = np.array([[0,0],
		      [0,1],
		      [1,0],
		      [1,1]])

	target = np.array([[0]
			  ,[1]
			  ,[1]
			  ,[0]])

	neuralNetwork = NeuralNetwork(0.7,2,14,1)

	neuralNetwork.backpropagation(x,target,maxIterations=10000)

	# Network result after training
	estimation = neuralNetwork .feed_forward(x)

	printSeparator = "----------------"
	
	print "Estimated values:"
	print estimation
	print printSeparator
	print "Target values:"
	print target
	print printSeparator

	estimationError = EstimationError(estimatedValues=estimation,targetValues=target)
	estimationError.computeErrors()
	totalError = estimationError.getTotalError()
	print "Total Error: %s" %(totalError)
	
