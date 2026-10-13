---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse
title: Vertex AI v1 API - Class EvaluateInstancesResponse (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:51.260308+00:00
---

# Vertex AI v1 API - Class EvaluateInstancesResponse (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class EvaluateInstancesResponse (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class EvaluateInstancesResponse : IMessage<EvaluateInstancesResponse>, IEquatable<EvaluateInstancesResponse>, IDeepCloneable<EvaluateInstancesResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1 API class EvaluateInstancesResponse.

Response message for EvaluationService.EvaluateInstances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EvaluateInstancesResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[EvaluateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[EvaluateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[EvaluateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### EvaluateInstancesResponse()
    
    
    public EvaluateInstancesResponse()

### EvaluateInstancesResponse(EvaluateInstancesResponse)
    
    
    public EvaluateInstancesResponse(EvaluateInstancesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[EvaluateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse)`  
  
  
## Properties 

### BleuResults
    
    
    public BleuResults BleuResults { get; set; }

Results for bleu metric.

**Property Value**  
---  
**Type** | **Description**  
`[BleuResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BleuResults)` |   
  
### CoherenceResult
    
    
    public CoherenceResult CoherenceResult { get; set; }

Result for coherence metric.

**Property Value**  
---  
**Type** | **Description**  
`[CoherenceResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CoherenceResult)` |   
  
### CometResult
    
    
    public CometResult CometResult { get; set; }

Translation metrics. Result for Comet metric.

**Property Value**  
---  
**Type** | **Description**  
`[CometResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CometResult)` |   
  
### EvaluationResultsCase
    
    
    public EvaluateInstancesResponse.EvaluationResultsOneofCase EvaluationResultsCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[EvaluateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse)[EvaluationResultsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluateInstancesResponse.EvaluationResultsOneofCase)` |   
  
### ExactMatchResults
    
    
    public ExactMatchResults ExactMatchResults { get; set; }

Auto metric evaluation results. Results for exact match metric.

**Property Value**  
---  
**Type** | **Description**  
`[ExactMatchResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ExactMatchResults)` |   
  
### FluencyResult
    
    
    public FluencyResult FluencyResult { get; set; }

LLM-based metric evaluation result. General text generation metrics, applicable to other categories. Result for fluency metric.

**Property Value**  
---  
**Type** | **Description**  
`[FluencyResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FluencyResult)` |   
  
### FulfillmentResult
    
    
    public FulfillmentResult FulfillmentResult { get; set; }

Result for fulfillment metric.

**Property Value**  
---  
**Type** | **Description**  
`[FulfillmentResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FulfillmentResult)` |   
  
### GroundednessResult
    
    
    public GroundednessResult GroundednessResult { get; set; }

Result for groundedness metric.

**Property Value**  
---  
**Type** | **Description**  
`[GroundednessResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GroundednessResult)` |   
  
### MetricResults
    
    
    public RepeatedField<MetricResult> MetricResults { get; }

Metric results for each instance. The order of the metric results is guaranteed to be the same as the order of the instances in the request.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MetricResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MetricResult)` |   
  
### MetricxResult
    
    
    public MetricxResult MetricxResult { get; set; }

Result for Metricx metric.

**Property Value**  
---  
**Type** | **Description**  
`[MetricxResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MetricxResult)` |   
  
### PairwiseMetricResult
    
    
    public PairwiseMetricResult PairwiseMetricResult { get; set; }

Result for pairwise metric.

**Property Value**  
---  
**Type** | **Description**  
`[PairwiseMetricResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PairwiseMetricResult)` |   
  
### PairwiseQuestionAnsweringQualityResult
    
    
    public PairwiseQuestionAnsweringQualityResult PairwiseQuestionAnsweringQualityResult { get; set; }

Result for pairwise question answering quality metric.

**Property Value**  
---  
**Type** | **Description**  
`[PairwiseQuestionAnsweringQualityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PairwiseQuestionAnsweringQualityResult)` |   
  
### PairwiseSummarizationQualityResult
    
    
    public PairwiseSummarizationQualityResult PairwiseSummarizationQualityResult { get; set; }

Result for pairwise summarization quality metric.

**Property Value**  
---  
**Type** | **Description**  
`[PairwiseSummarizationQualityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PairwiseSummarizationQualityResult)` |   
  
### PointwiseMetricResult
    
    
    public PointwiseMetricResult PointwiseMetricResult { get; set; }

Generic metrics. Result for pointwise metric.

**Property Value**  
---  
**Type** | **Description**  
`[PointwiseMetricResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PointwiseMetricResult)` |   
  
### QuestionAnsweringCorrectnessResult
    
    
    public QuestionAnsweringCorrectnessResult QuestionAnsweringCorrectnessResult { get; set; }

Result for question answering correctness metric.

**Property Value**  
---  
**Type** | **Description**  
`[QuestionAnsweringCorrectnessResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QuestionAnsweringCorrectnessResult)` |   
  
### QuestionAnsweringHelpfulnessResult
    
    
    public QuestionAnsweringHelpfulnessResult QuestionAnsweringHelpfulnessResult { get; set; }

Result for question answering helpfulness metric.

**Property Value**  
---  
**Type** | **Description**  
`[QuestionAnsweringHelpfulnessResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QuestionAnsweringHelpfulnessResult)` |   
  
### QuestionAnsweringQualityResult
    
    
    public QuestionAnsweringQualityResult QuestionAnsweringQualityResult { get; set; }

Question answering only metrics. Result for question answering quality metric.

**Property Value**  
---  
**Type** | **Description**  
`[QuestionAnsweringQualityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QuestionAnsweringQualityResult)` |   
  
### QuestionAnsweringRelevanceResult
    
    
    public QuestionAnsweringRelevanceResult QuestionAnsweringRelevanceResult { get; set; }

Result for question answering relevance metric.

**Property Value**  
---  
**Type** | **Description**  
`[QuestionAnsweringRelevanceResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QuestionAnsweringRelevanceResult)` |   
  
### RougeResults
    
    
    public RougeResults RougeResults { get; set; }

Results for rouge metric.

**Property Value**  
---  
**Type** | **Description**  
`[RougeResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.RougeResults)` |   
  
### SafetyResult
    
    
    public SafetyResult SafetyResult { get; set; }

Result for safety metric.

**Property Value**  
---  
**Type** | **Description**  
`[SafetyResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SafetyResult)` |   
  
### SummarizationHelpfulnessResult
    
    
    public SummarizationHelpfulnessResult SummarizationHelpfulnessResult { get; set; }

Result for summarization helpfulness metric.

**Property Value**  
---  
**Type** | **Description**  
`[SummarizationHelpfulnessResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SummarizationHelpfulnessResult)` |   
  
### SummarizationQualityResult
    
    
    public SummarizationQualityResult SummarizationQualityResult { get; set; }

Summarization only metrics. Result for summarization quality metric.

**Property Value**  
---  
**Type** | **Description**  
`[SummarizationQualityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SummarizationQualityResult)` |   
  
### SummarizationVerbosityResult
    
    
    public SummarizationVerbosityResult SummarizationVerbosityResult { get; set; }

Result for summarization verbosity metric.

**Property Value**  
---  
**Type** | **Description**  
`[SummarizationVerbosityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SummarizationVerbosityResult)` |   
  
### ToolCallValidResults
    
    
    public ToolCallValidResults ToolCallValidResults { get; set; }

Tool call metrics. Results for tool call valid metric.

**Property Value**  
---  
**Type** | **Description**  
`[ToolCallValidResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ToolCallValidResults)` |   
  
### ToolNameMatchResults
    
    
    public ToolNameMatchResults ToolNameMatchResults { get; set; }

Results for tool name match metric.

**Property Value**  
---  
**Type** | **Description**  
`[ToolNameMatchResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ToolNameMatchResults)` |   
  
### ToolParameterKeyMatchResults
    
    
    public ToolParameterKeyMatchResults ToolParameterKeyMatchResults { get; set; }

Results for tool parameter key match metric.

**Property Value**  
---  
**Type** | **Description**  
`[ToolParameterKeyMatchResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ToolParameterKeyMatchResults)` |   
  
### ToolParameterKvMatchResults
    
    
    public ToolParameterKVMatchResults ToolParameterKvMatchResults { get; set; }

Results for tool parameter key value match metric.

**Property Value**  
---  
**Type** | **Description**  
`[ToolParameterKVMatchResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ToolParameterKVMatchResults)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
