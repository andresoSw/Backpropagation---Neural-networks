import numpy as numpy
from neuralnetwork import NeuralNetwork,EstimationError

if __name__ == '__main__':

	numpy.random.seed(seed=1) #using fixed seed for testing purposes

	#test (x1 or x2) and x3
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

	#setting number of inputs and number of outputs in the neural network
	_ , xColumns = x.shape
	_ , targetColumns = target.shape
	neuralNetwork = NeuralNetwork(learning_rate=0.7,n_in=xColumns,n_hidden=4,n_out=targetColumns)

	neuralNetwork.initialize_weights()
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
	
