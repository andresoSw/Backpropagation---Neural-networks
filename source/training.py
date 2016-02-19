from os import listdir
from os.path import isfile,join
from neuralnetwork import NeuralNetwork,EstimationError
import numpy as numpy

datasets_dir = 'testfile'
for index,file_name in enumerate(listdir(datasets_dir)):
	print "%s)=============================================================" %(index+1)
	print "Training network from dataset: %s" %(file_name)
	data_file = join(datasets_dir,file_name)
	if not isfile(data_file): continue

	x_input = []
	target = []
	with open(data_file,'r+') as dataset:
		data = dataset.readlines()
		for entry in data:
			(x,y,area) = entry.split()
			x = float(x)
			y = float(y)
			area = int(area)
			if area==-1: area = 0
			x_input.append([x,y])
			target.append([area])

	x_input = numpy.array(x_input)
	target = numpy.array(target)

	numpy.random.seed(seed=1) #using fixed seed for testing purposes
	_ , xColumns = x_input.shape
	_ , targetColumns = target.shape
	n_hidden = 10
	momentum = 0
	neuralNetwork = NeuralNetwork(learning_rate=0.01,n_in=xColumns,n_hidden=n_hidden,n_out=targetColumns, momentum = momentum)

	neuralNetwork.initialize_weights()
	results_file = ''.join(['results_lr',str(neuralNetwork.learning_rate),'_m',str(momentum),'_',str(n_hidden),"hidden",file_name.rsplit('.', 1)[0]]+['.out'])

	neuralNetwork.backpropagation(x_input,target,maxIterations=10000, batch= False,file_name=results_file)