from os import listdir
from os.path import isfile,join
from neuralnetwork import NeuralNetwork,EstimationError
import numpy as numpy

datasets_dir = 'datasets'
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
			x_input.append([x,y])
			target.append([area])

	x_input = numpy.array(x_input)
	target = numpy.array(target)

	numpy.random.seed(seed=1) #using fixed seed for testing purposes
	_ , xColumns = x_input.shape
	_ , targetColumns = target.shape
	neuralNetwork = NeuralNetwork(learning_rate=0.7,n_in=xColumns,n_hidden=14,n_out=targetColumns)

	neuralNetwork.initialize_weights()
	neuralNetwork.backpropagation(x_input,target,maxIterations=10000)

	# Network result after training
	estimation = neuralNetwork .feed_forward(x_input)


	estimationError = EstimationError(estimatedValues=estimation,targetValues=target)
	estimationError.computeErrors()
	totalError = estimationError.getTotalError()
	results_file = ''.join(['results_',file_name])
	print "Writing results in file: %s" %(results_file)
	with open(results_file,'w+') as results_data:
		results_data.write("Estimated values:")
		results_data.write(str(estimation))
		results_data.write("----------------")
		results_data.write("Target values:")
		results_data.write(str(target))
		results_data.write("----------------")
		results_data.write("Total Error: %s" %(totalError))