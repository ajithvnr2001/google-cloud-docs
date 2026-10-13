---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics
title: Google AutoML v1 API - Class ClassificationEvaluationMetrics (3.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:20.725285+00:00
---

# Google AutoML v1 API - Class ClassificationEvaluationMetrics (3.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google AutoML v1 API - Class ClassificationEvaluationMetrics (3.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.6.0 (latest)  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ClassificationEvaluationMetrics : IMessage<ClassificationEvaluationMetrics>, IEquatable<ClassificationEvaluationMetrics>, IDeepCloneable<ClassificationEvaluationMetrics>, IBufferMessage, IMessage

Reference documentation and code samples for the Google AutoML v1 API class ClassificationEvaluationMetrics.

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of "segment_classification" type.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ClassificationEvaluationMetrics

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ClassificationEvaluationMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ClassificationEvaluationMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ClassificationEvaluationMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AutoML.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1)

## Assembly

Google.Cloud.AutoML.V1.dll

## Constructors 

### ClassificationEvaluationMetrics()
    
    
    public ClassificationEvaluationMetrics()

### ClassificationEvaluationMetrics(ClassificationEvaluationMetrics)
    
    
    public ClassificationEvaluationMetrics(ClassificationEvaluationMetrics other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClassificationEvaluationMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics)`  
  
  
## Properties 

### AnnotationSpecId
    
    
    public RepeatedField<string> AnnotationSpecId { get; }

Output only. The annotation spec ids used for this evaluation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AuPrc
    
    
    public float AuPrc { get; set; }

Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### AuRoc
    
    
    public float AuRoc { get; set; }

Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### ConfidenceMetricsEntry
    
    
    public RepeatedField<ClassificationEvaluationMetrics.Types.ConfidenceMetricsEntry> ConfidenceMetricsEntry { get; }

Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ClassificationEvaluationMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics.Types)[ConfidenceMetricsEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics.Types.ConfidenceMetricsEntry)` |   
  
### ConfusionMatrix
    
    
    public ClassificationEvaluationMetrics.Types.ConfusionMatrix ConfusionMatrix { get; set; }

Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.

**Property Value**  
---  
**Type** | **Description**  
`[ClassificationEvaluationMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics.Types)[ConfusionMatrix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ClassificationEvaluationMetrics.Types.ConfusionMatrix)` |   
  
### LogLoss
    
    
    public float LogLoss { get; set; }

Output only. The Log Loss metric.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
