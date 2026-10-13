---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult
title: Vertex AI v1beta1 API - Class AggregationResult (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:05.707060+00:00
---

# Vertex AI v1beta1 API - Class AggregationResult (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AggregationResult (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AggregationResult : IMessage<AggregationResult>, IEquatable<AggregationResult>, IDeepCloneable<AggregationResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AggregationResult.

The aggregation result for a single metric.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AggregationResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AggregationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AggregationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AggregationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AggregationResult()
    
    
    public AggregationResult()

### AggregationResult(AggregationResult)
    
    
    public AggregationResult(AggregationResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AggregationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult)`  
  
  
## Properties 

### AggregationMetric
    
    
    public Metric.Types.AggregationMetric AggregationMetric { get; set; }

Aggregation metric.

**Property Value**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Metric)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Metric.Types)[AggregationMetric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Metric.Types.AggregationMetric)` |   
  
### AggregationResultCase
    
    
    public AggregationResult.AggregationResultOneofCase AggregationResultCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AggregationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult)[AggregationResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AggregationResult.AggregationResultOneofCase)` |   
  
### BleuMetricValue
    
    
    public BleuMetricValue BleuMetricValue { get; set; }

Results for bleu metric.

**Property Value**  
---  
**Type** | **Description**  
`[BleuMetricValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BleuMetricValue)` |   
  
### CustomCodeExecutionResult
    
    
    public CustomCodeExecutionResult CustomCodeExecutionResult { get; set; }

Result for code execution metric.

**Property Value**  
---  
**Type** | **Description**  
`[CustomCodeExecutionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CustomCodeExecutionResult)` |   
  
### ExactMatchMetricValue
    
    
    public ExactMatchMetricValue ExactMatchMetricValue { get; set; }

Results for exact match metric.

**Property Value**  
---  
**Type** | **Description**  
`[ExactMatchMetricValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExactMatchMetricValue)` |   
  
### PairwiseMetricResult
    
    
    public PairwiseMetricResult PairwiseMetricResult { get; set; }

Result for pairwise metric.

**Property Value**  
---  
**Type** | **Description**  
`[PairwiseMetricResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PairwiseMetricResult)` |   
  
### PointwiseMetricResult
    
    
    public PointwiseMetricResult PointwiseMetricResult { get; set; }

Result for pointwise metric.

**Property Value**  
---  
**Type** | **Description**  
`[PointwiseMetricResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PointwiseMetricResult)` |   
  
### RougeMetricValue
    
    
    public RougeMetricValue RougeMetricValue { get; set; }

Results for rouge metric.

**Property Value**  
---  
**Type** | **Description**  
`[RougeMetricValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RougeMetricValue)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
