---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs
title: Vertex AI v1beta1 API - Class AutoMlImageObjectDetectionInputs (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:37.774048+00:00
---

# Vertex AI v1beta1 API - Class AutoMlImageObjectDetectionInputs (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AutoMlImageObjectDetectionInputs (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AutoMlImageObjectDetectionInputs : IMessage<AutoMlImageObjectDetectionInputs>, IEquatable<AutoMlImageObjectDetectionInputs>, IDeepCloneable<AutoMlImageObjectDetectionInputs>, IBufferMessage, IMessage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutoMlImageObjectDetectionInputs

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AutoMlImageObjectDetectionInputs()
    
    
    public AutoMlImageObjectDetectionInputs()

### AutoMlImageObjectDetectionInputs(AutoMlImageObjectDetectionInputs)
    
    
    public AutoMlImageObjectDetectionInputs(AutoMlImageObjectDetectionInputs other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs)`  
  
  
## Properties 

### BudgetMilliNodeHours
    
    
    public long BudgetMilliNodeHours { get; set; }

The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. For modelType `cloud`(default), the budget must be between 20,000 and 900,000 milli node hours, inclusive. The default value is 216,000 which represents one day in wall time, considering 9 nodes are used. For model types `mobile-tf-low-latency-1`, `mobile-tf-versatile-1`, `mobile-tf-high-accuracy-1` the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### DisableEarlyStopping
    
    
    public bool DisableEarlyStopping { get; set; }

Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Object Detection might stop training before the entire training budget has been used.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ModelType
    
    
    public AutoMlImageObjectDetectionInputs.Types.ModelType ModelType { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs.Types)[ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs.Types.ModelType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
