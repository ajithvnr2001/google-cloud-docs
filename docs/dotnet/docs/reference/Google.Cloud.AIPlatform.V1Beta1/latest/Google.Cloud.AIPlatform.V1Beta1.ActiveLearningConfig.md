---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig
title: Vertex AI v1beta1 API - Class ActiveLearningConfig (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:01.014598+00:00
---

# Vertex AI v1beta1 API - Class ActiveLearningConfig (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ActiveLearningConfig (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ActiveLearningConfig : IMessage<ActiveLearningConfig>, IEquatable<ActiveLearningConfig>, IDeepCloneable<ActiveLearningConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class ActiveLearningConfig.

Parameters that configure the active learning pipeline. Active learning will label the data incrementally by several iterations. For every iteration, it will select a batch of data based on the sampling strategy.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ActiveLearningConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ActiveLearningConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ActiveLearningConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ActiveLearningConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ActiveLearningConfig()
    
    
    public ActiveLearningConfig()

### ActiveLearningConfig(ActiveLearningConfig)
    
    
    public ActiveLearningConfig(ActiveLearningConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ActiveLearningConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig)`  
  
  
## Properties 

### HasMaxDataItemCount
    
    
    public bool HasMaxDataItemCount { get; }

Gets whether the "max_data_item_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxDataItemPercentage
    
    
    public bool HasMaxDataItemPercentage { get; }

Gets whether the "max_data_item_percentage" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HumanLabelingBudgetCase
    
    
    public ActiveLearningConfig.HumanLabelingBudgetOneofCase HumanLabelingBudgetCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ActiveLearningConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig)[HumanLabelingBudgetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ActiveLearningConfig.HumanLabelingBudgetOneofCase)` |   
  
### MaxDataItemCount
    
    
    public long MaxDataItemCount { get; set; }

Max number of human labeled DataItems.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### MaxDataItemPercentage
    
    
    public int MaxDataItemPercentage { get; set; }

Max percent of total DataItems for human labeling.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SampleConfig
    
    
    public SampleConfig SampleConfig { get; set; }

Active learning data sampling config. For every active learning labeling iteration, it will select a batch of data based on the sampling strategy.

**Property Value**  
---  
**Type** | **Description**  
`[SampleConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SampleConfig)` |   
  
### TrainingConfig
    
    
    public TrainingConfig TrainingConfig { get; set; }

CMLE training config. For every active learning labeling iteration, system will train a machine learning model on CMLE. The trained model will be used by data sampling algorithm to select DataItems.

**Property Value**  
---  
**Type** | **Description**  
`[TrainingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.TrainingConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
