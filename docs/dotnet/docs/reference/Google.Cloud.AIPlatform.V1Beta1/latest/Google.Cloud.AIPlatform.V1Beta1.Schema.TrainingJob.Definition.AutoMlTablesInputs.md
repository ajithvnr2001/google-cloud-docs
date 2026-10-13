---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs
title: Vertex AI v1beta1 API - Class AutoMlTablesInputs (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:43.501919+00:00
---

# Vertex AI v1beta1 API - Class AutoMlTablesInputs (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AutoMlTablesInputs (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AutoMlTablesInputs : IMessage<AutoMlTablesInputs>, IEquatable<AutoMlTablesInputs>, IDeepCloneable<AutoMlTablesInputs>, IBufferMessage, IMessage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutoMlTablesInputs

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AutoMlTablesInputs()
    
    
    public AutoMlTablesInputs()

### AutoMlTablesInputs(AutoMlTablesInputs)
    
    
    public AutoMlTablesInputs(AutoMlTablesInputs other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)`  
  
  
## Properties 

### AdditionalExperiments
    
    
    public RepeatedField<string> AdditionalExperiments { get; }

Additional experiment flags for the Tables training pipeline.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AdditionalOptimizationObjectiveConfigCase
    
    
    public AutoMlTablesInputs.AdditionalOptimizationObjectiveConfigOneofCase AdditionalOptimizationObjectiveConfigCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)[AdditionalOptimizationObjectiveConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.AdditionalOptimizationObjectiveConfigOneofCase)` |   
  
### DisableEarlyStopping
    
    
    public bool DisableEarlyStopping { get; set; }

Use the entire training budget. This disables the early stopping feature. By default, the early stopping feature is enabled, which means that AutoML Tables might stop training before the entire training budget has been used.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ExportEvaluatedDataItemsConfig
    
    
    public ExportEvaluatedDataItemsConfig ExportEvaluatedDataItemsConfig { get; set; }

Configuration for exporting test set predictions to a BigQuery table. If this configuration is absent, then the export is not performed.

**Property Value**  
---  
**Type** | **Description**  
`[ExportEvaluatedDataItemsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.ExportEvaluatedDataItemsConfig)` |   
  
### HasOptimizationObjectivePrecisionValue
    
    
    public bool HasOptimizationObjectivePrecisionValue { get; }

Gets whether the "optimization_objective_precision_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasOptimizationObjectiveRecallValue
    
    
    public bool HasOptimizationObjectiveRecallValue { get; }

Gets whether the "optimization_objective_recall_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### OptimizationObjective
    
    
    public string OptimizationObjective { get; set; }

Objective function the model is optimizing towards. The training process creates a model that maximizes/minimizes the value of the objective function over the validation set.

The supported optimization objectives depend on the prediction type. If the field is not set, a default objective function is used.

classification (binary): "maximize-au-roc" (default) - Maximize the area under the receiver operating characteristic (ROC) curve. "minimize-log-loss" - Minimize log loss. "maximize-au-prc" - Maximize the area under the precision-recall curve. "maximize-precision-at-recall" - Maximize precision for a specified recall value. "maximize-recall-at-precision" - Maximize recall for a specified precision value.

classification (multi-class): "minimize-log-loss" (default) - Minimize log loss.

regression: "minimize-rmse" (default) - Minimize root-mean-squared error (RMSE). "minimize-mae" - Minimize mean-absolute error (MAE). "minimize-rmsle" - Minimize root-mean-squared log error (RMSLE).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OptimizationObjectivePrecisionValue
    
    
    public float OptimizationObjectivePrecisionValue { get; set; }

Required when optimization_objective is "maximize-recall-at-precision". Must be between 0 and 1, inclusive.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### OptimizationObjectiveRecallValue
    
    
    public float OptimizationObjectiveRecallValue { get; set; }

Required when optimization_objective is "maximize-precision-at-recall". Must be between 0 and 1, inclusive.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### PredictionType
    
    
    public string PredictionType { get; set; }

The type of prediction the Model is to produce. "classification" - Predict one out of multiple target values is picked for each row. "regression" - Predict a value based on its relation to other values. This type is available only to columns that contain semantically numeric values, i.e. integers or floating point number, even if stored as e.g. strings.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TargetColumn
    
    
    public string TargetColumn { get; set; }

The column name of the target column that the model is to predict.

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
    
    
    public RepeatedField<AutoMlTablesInputs.Types.Transformation> Transformations { get; }

Each transformation will apply transform function to given input column. And the result will be used for training. When creating transformation for BigQuery Struct column, the column should be flattened using "." as the delimiter.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types)[Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation)` |   
  
### WeightColumnName
    
    
    public string WeightColumnName { get; set; }

Column name that should be used as the weight column. Higher values in this column give more importance to the row during model training. The column must have numeric values between 0 and 10000 inclusively; 0 means the row is ignored for training. If weight column field is not set, then all rows are assumed to have equal weight of 1.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
