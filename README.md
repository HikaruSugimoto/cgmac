# CGMac (CGM Metrics Calculator)
## Overview
This code calculates key metrics from Continuous Glucose Monitoring (CGM) data for multiple individuals. It processes time series glucose data and calculates various statistical measures including mean glucose levels, standard deviation and temporal autocorrelation properties.

## Function description

The main function `cgmac` processes CGM data and returns the following measures for each individual
- Mean glucose level
- Standard deviation of the glucose levels
- Mean of autocorrelation values
- Variance of autocorrelation values

These measures are particularly useful for
- Predicting glucose control abilities including insulin sensitivity, insulin secretion, and insulin clearance
- Prediction of diabetic complications

## Prerequisites

Required Python libraries:
- pandas
- statsmodels
- numpy

## Input data format

The input DataFrame should be structured as follows
- First column: Subject IDs
- Second column onwards: Glucose readings (time series data)
- Each row represents a different individual's CGM readings.

Example input data structure:
```python
  ID  Reading1 Reading2 Reading3 ...
0 1  120 125 118 ...
1 2  115 118 121 ...

