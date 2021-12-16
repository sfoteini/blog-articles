# Predict CO2 emissions from cars with Azure Machine Learning

<p>
  <a href="https://foteinisavvidou.azurewebsites.net/predict-co2-emissions-from-cars-with-azure-machine-learning" target="_blank"><img src="https://img.shields.io/badge/Instructions-informational?style=for-the-badge" alt="Instructions"></a>
  <a href="fuel_consumption.csv" target="_blank"><img src="https://img.shields.io/badge/Dataset-red?style=for-the-badge" alt="Data"></a>
</p>

In this tutorial, you will learn how to train a machine learning model in Azure Machine Learning Designer without writing a single line of code. You will create a simple linear regression model to predict carbon dioxide emissions from cars.

You will learn how to:
* Create an Azure Machine Learning workspace.
* Create and run a pipeline.
* Import data.
* Train and evaluate a linear regression model.

To complete the exercise, you will need:
* An Azure subscription.
* The [fuel_consumption.csv](fuel_consumption.csv) file. The data has been taken from the [Government of Canada](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64) website.

<br>

## Understanding the dataset
### Model
* 4WD/4X4 = Four-wheel drive
* AWD = All-wheel drive
* FFV = Flexible-fuel vehicle
* SWB = Short wheelbase
* LWB = Long wheelbase
* EWB = Extended wheelbase

### Transmission
* A = automatic
* AM = automated manual
* AS = automatic with select shift
* AV = continuously variable
* M = manual
* 3 – 10 = Number of gears

### Fuel type
* X = regular gasoline
* Z = premium gasoline
* D = diesel
* E = ethanol (E85)
* N = natural gas

### Fuel consumption
City and highway fuel consumption ratings are shown in liters per 100 kilometers (L/100 km), the combined rating (55% city, 45% highways) is shown in L/100 km and in miles per imperial gallon (mpg)

### CO2 emissions
The tailpipe emissions of carbon dioxide (in grams per kilometer) for combined city and highway driving
