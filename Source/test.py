import numpy as np
from neuralnetwork import NeuralNetwork

if __name__ == '__main__':
	x = np.array([[0,0],[0,1],[1,0],[1,1]])
	y = np.array([[0],[1],[1],[0]])

	nn = NeuralNetwork(0.7,2,8,1)
	# Train network with a given number of iterations
	nn.backpropagation(x,y,10000)

	# Network result after training
	print nn.feed_forward(x)