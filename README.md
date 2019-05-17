# Primitive Neural Net

The world's most complicated way to calculate a mean


## Files

 - **`NNMainHigh.ipynb`** : A Jupyter Notebook that generates a NN with 100 Hidden Neurons
 - **`NNMainLow.ipynb`** : A Jupyter Notebook that generates a NN with only 3 Hidden Neurons
 - **/Data**: contains the Boston Housing Dataset
 - **/Output**: contains images that my algorithm generates for each dataset

## Note
The code and subsequent operations can be viewed in the web browser:

https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/NNMainLow.ipynb

https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/NNMainHigh.ipynb

## The task

I attempted to find a non-linear regression relation between two known values: crime rate in a Boston neighborhood 
and average tax rate in said neighborhood and predict the median home value in this neighborhood

I made 2 neural networks, a Low Density network, that only has 3 hidden neurons and a High Density that has 100 Hidden Neurons.
Both used a sigmoid activation function and standard backpropagation partial gradient calculation

The Dataset was, of course, partitioned into a large training set, and a test set consisting of 1/3rd the samples.
The Results are shown below

## Results

### Training Error

The plots below have the same set trained on using different networks. It is interesting to me that what a neural net essentially finds is a "fuzzy" mean. The green lines in both cases are the true arithmetic means of the training data.

| Low |High|
|--|--|
| ![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TrainingPartitionLow.png)|![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TrainingPartitionHigh.png)|



|  | Low |High|
|--|--|--|
|  MSE|64.9012 |62.9408|

### Prediction Results

As we can see from the above table, the Mean Square Error only marginally improved when the model complexity was increased by two orders of magnitude. However, the MSE does not tell the true story.
It it is clear that the higher complexity model, does a MUCH better job accounting for minute variations in the data parameters; recall that we are only using 2 (crime and tax rate) to predict value (shown here in the $10,000s) and the x axis is purely an index value. 
The point here is that unlike standard regression, the NN can find highly non-linear relations between inputs and outputs at the cost of complexity. 

Clearly, this is not an overfitting issue, since none of the samples shown in the plots below were used in the training. The non-linear variations in the high complexity model, in some sense, are "true". That is, the NN has picked out features in the training set that represent reality.

| Low |High|
|--|--|
| ![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TestPartitionLow.png)|![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TestPartitionHigh.png)|




