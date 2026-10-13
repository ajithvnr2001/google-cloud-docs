---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs
title: Class AutoMlForecastingInputs (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:28:22.603163+00:00
---

# Class AutoMlForecastingInputs (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutoMlForecastingInputs (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    AutoMlForecastingInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

## Attributes  
  
---  
**Name** | **Description**  
`target_column` |  `str`   
The name of the column that the model is to predict.   
`time_series_identifier_column` |  `str`   
The name of the column that identifies the time series.   
`time_column` |  `str`   
The name of the column that identifies time order in the time series.   
`transformations` |  `MutableSequence[[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation)]`   
Each transformation will apply transform function to given input column. And the result will be used for training. When creating transformation for BigQuery Struct column, the column should be flattened using "." as the delimiter.   
`optimization_objective` |  `str`   
Objective function the model is optimizing towards. The training process creates a model that optimizes the value of the objective function over the validation set. The supported optimization objectives: \- "minimize-rmse" (default) - Minimize root-mean-squared error (RMSE). \- "minimize-mae" - Minimize mean-absolute error (MAE). \- "minimize-rmsle" - Minimize root-mean-squared log error (RMSLE). \- "minimize-rmspe" - Minimize root-mean-squared percentage error (RMSPE). \- "minimize-wape-mae" - Minimize the combination of weighted absolute percentage error (WAPE) and mean-absolute-error (MAE). \- "minimize-quantile-loss" - Minimize the quantile loss at the quantiles defined in `quantiles`.   
`train_budget_milli_node_hours` |  `int`   
Required. The train budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The training cost of the model will not exceed this budget. The final cost will be attempted to be close to the budget, though may end up being (even) noticeably smaller - at the backend's discretion. This especially may happen when further model training ceases to provide any improvements. If the budget is set to a value known to be insufficient to train a model for the given dataset, the training won't be attempted and will error. The train budget must be between 1,000 and 72,000 milli node hours, inclusive.   
`weight_column` |  `str`   
Column name that should be used as the weight column. Higher values in this column give more importance to the row during model training. The column must have numeric values between 0 and 10000 inclusively; 0 means the row is ignored for training. If weight column field is not set, then all rows are assumed to have equal weight of 1.   
`time_series_attribute_columns` |  `MutableSequence[str]`   
Column names that should be used as attribute columns. The value of these columns does not vary as a function of time. For example, store ID or item color.   
`unavailable_at_forecast_columns` |  `MutableSequence[str]`   
Names of columns that are unavailable when a forecast is requested. This column contains information for the given entity (identified by the time_series_identifier_column) that is unknown before the forecast For example, actual weather on a given day.   
`available_at_forecast_columns` |  `MutableSequence[str]`   
Names of columns that are available and provided when a forecast is requested. These columns contain information for the given entity (identified by the time_series_identifier_column column) that is known at forecast. For example, predicted weather for a specific day.   
`data_granularity` |  `[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Granularity](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Granularity)`   
Expected difference in time granularity between rows in the data.   
`forecast_horizon` |  `int`   
The amount of time into the future for which forecasted values for the target are returned. Expressed in number of units defined by the `data_granularity` field.   
`context_window` |  `int`   
The amount of time into the past training and prediction data is used for model training and prediction respectively. Expressed in number of units defined by the `data_granularity` field.   
`export_evaluated_data_items_config` |  `[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.ExportEvaluatedDataItemsConfig](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.ExportEvaluatedDataItemsConfig)`   
Configuration for exporting test set predictions to a BigQuery table. If this configuration is absent, then the export is not performed.   
`quantiles` |  `MutableSequence[float]`   
Quantiles to use for minimize-quantile-loss `optimization_objective`. Up to 5 quantiles are allowed of values between 0 and 1, exclusive. Required if the value of optimization_objective is minimize-quantile-loss. Represents the percent quantiles to use for that objective. Quantiles must be unique.   
`validation_options` |  `str`   
Validation options for the data validation component. The available options are: \- "fail-pipeline" - default, will validate against the validation and fail the pipeline if it fails. \- "ignore-validation" - ignore the results of the validation and continue   
`additional_experiments` |  `MutableSequence[str]`   
Additional experiment flags for the time series forcasting training.   
  
## Classes 

### Granularity
    
    
    Granularity(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A duration of time expressed in time granularity units.

### Transformation
    
    
    Transformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Methods 

### AutoMlForecastingInputs
    
    
    AutoMlForecastingInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

### AutoMlForecastingInputs
    
    
    AutoMlForecastingInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
