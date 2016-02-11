import numpy as np

def sigmoid(x):
	return 1.0/(1.0 + np.exp(-x))

def sigmoid_derivate(x):
	return x*(1.0-x)

def backpropagation(X,T,eta,n_in,n_hidden,n_out):
	# Create feed-forward network with n_in, n_out, n_hidden
	# Initialize weights to small value

	weights = []
	layers = [n_in,n_hidden,n_out]

	# Weights from input layer to hidden layer
	syn0= (-0.05)*np.random.random((n_in,n_hidden))+0.05
	b1 = (-0.05) *np.random.random() + 0.05

	# Weights from hidden layer to output layer
	syn1 = (-0.05)*np.random.random((n_hidden,n_out))+0.05
	b2 = (-0.05) *np.random.random() + 0.05


	# print syn1
	# print syn0

	for i in range(1):
		for k in range(0,len(X)):
			print X[k]

	for i in range(1):

		#feed forward
		l1 = sigmoid(np.dot(X,syn0))
		l2 = sigmoid(np.dot(l1,syn1))
		print "bp output"
		print l2

		l2_error =  T - l2
		l2_delta = l2_error*sigmoid_derivate(l2)

		l1_error = l2_delta.dot(syn1.T)
		l1_delta = l1_error*sigmoid_derivate(l1)

		syn1 += eta*l1.T.dot(l2_delta)
		syn0 += eta*X.T.dot(l1_delta)

class NeuralNework:

	def __init__(self,eta,n_in,n_hidden,n_out):
		self.eta = eta
		self.n_in = n_in
		self.n_hidden = n_hidden
		self.n_out = n_out
		self.initialize_weights()

	def initialize_weights(self):
		self.W1 = (-0.05)*np.random.random((self.n_in,self.n_hidden))+0.05
		self.b1 = (-0.05)*np.random.random()+0.05	
		self.W2 = (-0.05)*np.random.random((self.n_hidden,self.n_out))+0.05
		self.b2 = (-0.05)*np.random.random()+0.05

	def feed_forward(self,X):
		# output of input layer fed with input values
		self.a1 = sigmoid(np.dot(X,self.W1)+self.b1)
		print self.a1
		# output of hidden layer fed with output of input layer
		self.y = sigmoid(np.dot(self.a1,self.W2)+self.b2)	

	def backpropagate(self,X,T):
		self.feed_forward(X)

		# error in output layer
		output_error = T - self.y
		output_delta = output_error*sigmoid_derivate(y)

		hidden_error = output_delta.dot(self.W2.T)
		hidden_delta = hidden_error*sigmoid_derivate(self.a1)

		self.W1 += self.eta*self.a1.T.dot(output_delta)
		self.W2 += self.eta*X.T.dot(hidden_delta)

	# 
	def backpropagation(self,X,T,N):
		for i in range(0,N):
			self.backpropagate(X,T)

if __name__ == '__main__':
	
	x = np.array([[0,0],[0,1],[1,0],[1,1]])
	y = np.array([[0],[1],[1],[1]])
	backpropagation(x,y,0.05,2,2,1)

	nn = NeuralNework(0.05,2,2,1)

	nn.backpropagation(x,y,10000)

	print nn.feed_forward(x)

	pass