---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse
title: Vertex AI v1beta1 API - Class AssessDataResponse (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:21.941147+00:00
---

# Vertex AI v1beta1 API - Class AssessDataResponse (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AssessDataResponse (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AssessDataResponse : IMessage<AssessDataResponse>, IEquatable<AssessDataResponse>, IDeepCloneable<AssessDataResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AssessDataResponse.

Response message for [DatasetService.AssessData][google.cloud.aiplatform.v1beta1.DatasetService.AssessData].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AssessDataResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AssessDataResponse()
    
    
    public AssessDataResponse()

### AssessDataResponse(AssessDataResponse)
    
    
    public AssessDataResponse(AssessDataResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse)`  
  
  
## Properties 

### AssessmentResultCase
    
    
    public AssessDataResponse.AssessmentResultOneofCase AssessmentResultCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse)[AssessmentResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.AssessmentResultOneofCase)` |   
  
### BatchPredictionResourceUsageAssessmentResult
    
    
    public AssessDataResponse.Types.BatchPredictionResourceUsageAssessmentResult BatchPredictionResourceUsageAssessmentResult { get; set; }

Optional. The result of the batch prediction resource usage assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types)[BatchPredictionResourceUsageAssessmentResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types.BatchPredictionResourceUsageAssessmentResult)` |   
  
### BatchPredictionValidationAssessmentResult
    
    
    public AssessDataResponse.Types.BatchPredictionValidationAssessmentResult BatchPredictionValidationAssessmentResult { get; set; }

Optional. The result of the batch prediction validation assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types)[BatchPredictionValidationAssessmentResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types.BatchPredictionValidationAssessmentResult)` |   
  
### TuningResourceUsageAssessmentResult
    
    
    public AssessDataResponse.Types.TuningResourceUsageAssessmentResult TuningResourceUsageAssessmentResult { get; set; }

Optional. The result of the tuning resource usage assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types)[TuningResourceUsageAssessmentResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types.TuningResourceUsageAssessmentResult)` |   
  
### TuningValidationAssessmentResult
    
    
    public AssessDataResponse.Types.TuningValidationAssessmentResult TuningValidationAssessmentResult { get; set; }

Optional. The result of the tuning validation assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types)[TuningValidationAssessmentResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataResponse.Types.TuningValidationAssessmentResult)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
