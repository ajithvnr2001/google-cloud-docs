---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs
title: Vertex AI v1beta1 API - Class AutoMlForecastingInputs (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:34.267998+00:00
---

# Vertex AI v1beta1 API - Class AutoMlForecastingInputs (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AutoMlForecastingInputs (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AutoMlForecastingInputs : IMessage<AutoMlForecastingInputs>, IEquatable<AutoMlForecastingInputs>, IDeepCloneable<AutoMlForecastingInputs>, IBufferMessage, IMessage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutoMlForecastingInputs

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutoMlForecastingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutoMlForecastingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutoMlForecastingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AutoMlForecastingInputs()
    
    
    public AutoMlForecastingInputs()

### AutoMlForecastingInputs(AutoMlForecastingInputs)
    
    
    public AutoMlForecastingInputs(AutoMlForecastingInputs other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutoMlForecastingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs)`  
  
  
## Properties 

### AdditionalExperiments
    
    
    public RepeatedField<string> AdditionalExperiments { get; }

Additional experiment flags for the time series forcasting training.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AvailableAtForecastColumns
    
    
    public RepeatedField<string> AvailableAtForecastColumns { get; }

Names of columns that are available and provided when a forecast is requested. These columns contain information for the given entity (identified by the time_series_identifier_column column) that is known at forecast. For example, predicted weather for a specific day.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ContextWindow
    
    
    public long ContextWindow { get; set; }

The amount of time into the past training and prediction data is used for model training and prediction respectively. Expressed in number of units defined by the `data_granularity` field.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### DataGranularity
    
    
    public AutoMlForecastingInputs.Types.Granularity DataGranularity { get; set; }

Expected difference in time granularity between rows in the data.

**Property Value**  
---  
**Type** | **Description**  
`[AutoMlForecastingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types)[Granularity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Granularity)` |   
  
### ExportEvaluatedDataItemsConfig
    
    
    public ExportEvaluatedDataItemsConfig ExportEvaluatedDataItemsConfig { get; set; }

Configuration for exporting test set predictions to a BigQuery table. If this configuration is absent, then the export is not performed.

**Property Value**  
---  
**Type** | **Description**  
`[ExportEvaluatedDataItemsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.ExportEvaluatedDataItemsConfig)` |   
  
### ForecastHorizon
    
    
    public long ForecastHorizon { get; set; }

The amount of time into the future for which forecasted values for the target are returned. Expressed in number of units defined by the `data_granularity` field.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### OptimizationObjective
    
    
    public string OptimizationObjective { get; set; }

Objective function the model is optimizing towards. The training process creates a model that optimizes the value of the objective function over the validation set.

The supported optimization objectives:

  * "minimize-rmse" (default) - Minimize root-mean-squared error (RMSE).

  * "minimize-mae" - Minimize mean-absolute error (MAE).

  * "minimize-rmsle" - Minimize root-mean-squared log error (RMSLE).

  * "minimize-rmspe" - Minimize root-mean-squared percentage error (RMSPE).

  * "minimize-wape-mae" - Minimize the combination of weighted absolute percentage error (WAPE) and mean-absolute-error (MAE).

  * "minimize-quantile-loss" - Minimize the quantile loss at the quantiles defined in `quantiles`.




**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Quantiles
    
    
    public RepeatedField<double> Quantiles { get; }

Quantiles to use for minimize-quantile-loss `optimization_objective`. Up to 5 quantiles are allowed of values between 0 and 1, exclusive. Required if the value of optimization_objective is minimize-quantile-loss. Represents the percent quantiles to use for that objective. Quantiles must be unique.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### TargetColumn
    
    
    public string TargetColumn { get; set; }

The name of the column that the model is to predict.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeColumn
    
    
    public string TimeColumn { get; set; }

The name of the column that identifies time order in the time series.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeSeriesAttributeColumns
    
    
    public RepeatedField<string> TimeSeriesAttributeColumns { get; }

Column names that should be used as attribute columns. The value of these columns does not vary as a function of time. For example, store ID or item color.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeSeriesIdentifierColumn
    
    
    public string TimeSeriesIdentifierColumn { get; set; }

The name of the column that identifies the time series.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TrainBudgetMilliNodeHours
    
    
    public long TrainBudgetMilliNodeHours { get; set; }

Required. The train budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour.

The training cost of the model will not exceed this budget. The final cost will be attempted to be close to the budget, though may end up being (even) noticeably smaller - at the backend's discretion. This especially may happen when further model training ceases to provide any improvements.

If the budget is set to a value known to be insufficient to train a model for the given dataset, the training won't be attempted and will error.

The train budget must be between 1,000 and 72,000 milli node hours, inclusive.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Transformations
    
    
    public RepeatedField<AutoMlForecastingInputs.Types.Transformation> Transformations { get; }

Each transformation will apply transform function to given input column. And the result will be used for training. When creating transformation for BigQuery Struct column, the column should be flattened using "." as the delimiter.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AutoMlForecastingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types)[Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation)` |   
  
### UnavailableAtForecastColumns
    
    
    public RepeatedField<string> UnavailableAtForecastColumns { get; }

Names of columns that are unavailable when a forecast is requested. This column contains information for the given entity (identified by the time_series_identifier_column) that is unknown before the forecast For example, actual weather on a given day.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValidationOptions
    
    
    public string ValidationOptions { get; set; }

Validation options for the data validation component. The available options are:

  * "fail-pipeline" - default, will validate against the validation and fail the pipeline if it fails.

  * "ignore-validation" - ignore the results of the validation and continue




**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WeightColumn
    
    
    public string WeightColumn { get; set; }

Column name that should be used as the weight column. Higher values in this column give more importance to the row during model training. The column must have numeric values between 0 and 10000 inclusively; 0 means the row is ignored for training. If weight column field is not set, then all rows are assumed to have equal weight of 1.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
