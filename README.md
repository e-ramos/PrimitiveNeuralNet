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

## Results

### Training Error

| Low |High|
|--|--|
| ![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TrainingPartitionLow.png)|![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TrainingPartitionHigh.png)|



|  | Low |High|
|--|--|--|
|  MSE|64.9012 |62.9408|

### Prediction Results

| Low |High|
|--|--|
| ![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TestPartitionLow.png)|![](https://github.com/e-ramos/PrimitiveNeuralNet/blob/master/Output/TestPartitionHigh.png)|




