# Predict the risk of chronic kidney disease with Azure Machine Learning

<p>
  <a href="https://foteinisavvidou.azurewebsites.net/predict-the-risk-of-chronic-kidney-disease-with-azure-machine-learning" target="_blank"><img src="https://img.shields.io/badge/Instructions-informational?style=for-the-badge" alt="Instructions"></a>
  <a href="chronic_kidney_disease.csv" target="_blank"><img src="https://img.shields.io/badge/Dataset-red?style=for-the-badge" alt="Data"></a>
</p>

In this tutorial, you will learn how to train a machine learning model in Azure Machine Learning Designer without writing a single line of code. You will create a simple classification model for chronic kidney disease prediction.

You will learn how to:
* Create an Azure Machine Learning workspace.
* Create and run a pipeline.
* Import data.
* Execute a Python script in Azure Machine Learning Designer.
* Train and evaluate a classification model.

To complete the exercise, you will need:
* An Azure subscription. If you don't already have one, you can sign up for an [Azure free account](https://azure.microsoft.com).
* The [chronic_kidney_disease.csv](chronic_kidney_disease.csv) dataset. The data has been taken from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease).

<br>

## Understanding the dataset

We use the following representation to collect the dataset:

age - age

bp - blood pressure

sg - specific gravity

al - albumin

su - sugar

rbc - red blood cells

pc - pus cell

pcc - pus cell clumps

ba - bacteria

bgr - blood glucose random

bu - blood urea

sc - serum creatinine

sod - sodium

pot - potassium

hemo - hemoglobin

pcv - packed cell volume

wc - white blood cell count

rc - red blood cell count

htn - hypertension

dm - diabetes mellitus

cad - coronary artery disease

appet - appetite

pe - pedal edema

ane - anemia

class - class

Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease)
