import numpy as np

def sigmoid(x):
	return 1.0/(1.0 + np.exp(-x))

def sigmoid_derivate(x):
	return x*(1.0-x)

class NeuralNetwork:

	def __init__(self,eta,n_in,n_hidden,n_out):
		# learning factor
		self.eta = eta
		self.n_in = n_in
		self.n_hidden = n_hidden
		self.n_out = n_out

		self.initialize_weights()

	def initialize_weights(self):
		# Weights from input unit to hidden unit
		self.W1 = (0.1)*np.random.random((self.n_in,self.n_hidden))-0.5
		# Activation threshold on hidden layer
		# To be used
		self.hidden_threshold = (0.1)*np.random.random((1,self.n_hidden))-0.5

		# Weights from hidden unit to output unit
		self.W2 = (0.1)*np.random.random((self.n_hidden,self.n_out))-0.5
		# Activation threshold on output layer 
		# To be used
		self.output_threshold = (0.1)*np.random.random((1,self.n_out))-0.5


	def feed_forward(self,X):
		# output of input layer fed with input values
		self.a1 = sigmoid(np.dot(X,self.W1))
		# output of hidden layer fed with output of input layer
		self.y = sigmoid(np.dot(self.a1,self.W2))		
		return self.y	

	# backpropagation updating weights with a single example
	def backpropagate(self,X,T):
		for i in range(0,len(X)):
			x = np.atleast_2d(X[i])
			t = np.atleast_2d(T[i])
			self.feed_forward(x)

			output_error = t - self.y
			output_delta = output_error*sigmoid_derivate(self.y)

			hidden_error = output_delta.dot(self.W2.T)
			hidden_delta = hidden_error*sigmoid_derivate(self.a1)

			self.W2 += self.eta*self.a1.T.dot(output_delta)
			self.W1 += self.eta*x.T.dot(hidden_delta)

	# backpropagation updating weights with all examples
	def backpropagate_batch(self,X,T):
		self.feed_forward(X)
		# error in output layer
		output_error = T - self.y
		output_delta = output_error*sigmoid_derivate(self.y)

		# error in hidden layer
		hidden_error = output_delta.dot(self.W2.T)
		hidden_delta = hidden_error*sigmoid_derivate(self.a1)

		# updating weigths
		self.W2 += self.eta*self.a1.T.dot(output_delta)
		self.W1 += self.eta*X.T.dot(hidden_delta)

	# backpropagation for a number of N iteration
	def backpropagation(self,X,T,N, batch = True):
		if batch: 
			for i in range(0,N):
				self.backpropagate_batch(X,T)
		else:
			for i in range(0,N):
				self.backpropagate(X,T)


if __name__ == '__main__':
	
	np.random.seed(1)

	x = np.array([[0,0],[0,1],[1,0],[1,1]])
	y = np.array([[0],[1],[1],[0]])

	nn = NeuralNetwork(0.7,2,8,1)
	# Train network with a given number of iterations
	nn.backpropagation(x,y,10000)

	# Network result after training
	print nn.feed_forward(x)
