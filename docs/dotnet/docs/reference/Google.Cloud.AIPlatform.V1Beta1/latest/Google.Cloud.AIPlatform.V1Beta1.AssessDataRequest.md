---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest
title: Vertex AI v1beta1 API - Class AssessDataRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:18.068375+00:00
---

# Vertex AI v1beta1 API - Class AssessDataRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AssessDataRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AssessDataRequest : IMessage<AssessDataRequest>, IEquatable<AssessDataRequest>, IDeepCloneable<AssessDataRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AssessDataRequest.

Request message for [DatasetService.AssessData][google.cloud.aiplatform.v1beta1.DatasetService.AssessData]. Used only for MULTIMODAL datasets.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AssessDataRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AssessDataRequest()
    
    
    public AssessDataRequest()

### AssessDataRequest(AssessDataRequest)
    
    
    public AssessDataRequest(AssessDataRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest)`  
  
  
## Properties 

### AssessmentConfigCase
    
    
    public AssessDataRequest.AssessmentConfigOneofCase AssessmentConfigCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest)[AssessmentConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.AssessmentConfigOneofCase)` |   
  
### BatchPredictionResourceUsageAssessmentConfig
    
    
    public AssessDataRequest.Types.BatchPredictionResourceUsageAssessmentConfig BatchPredictionResourceUsageAssessmentConfig { get; set; }

Optional. Configuration for the batch prediction resource usage assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types)[BatchPredictionResourceUsageAssessmentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types.BatchPredictionResourceUsageAssessmentConfig)` |   
  
### BatchPredictionValidationAssessmentConfig
    
    
    public AssessDataRequest.Types.BatchPredictionValidationAssessmentConfig BatchPredictionValidationAssessmentConfig { get; set; }

Optional. Configuration for the batch prediction validation assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types)[BatchPredictionValidationAssessmentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types.BatchPredictionValidationAssessmentConfig)` |   
  
### DatasetName
    
    
    public DatasetName DatasetName { get; set; }

[DatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DatasetName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest#Google_Cloud_AIPlatform_V1Beta1_AssessDataRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DatasetName)` |   
  
### GeminiRequestReadConfig
    
    
    public GeminiRequestReadConfig GeminiRequestReadConfig { get; set; }

Optional. The Gemini request read config for the dataset.

**Property Value**  
---  
**Type** | **Description**  
`[GeminiRequestReadConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GeminiRequestReadConfig)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the Dataset resource. Used only for MULTIMODAL datasets. Format: `projects/{project}/locations/{location}/datasets/{dataset}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TuningResourceUsageAssessmentConfig
    
    
    public AssessDataRequest.Types.TuningResourceUsageAssessmentConfig TuningResourceUsageAssessmentConfig { get; set; }

Optional. Configuration for the tuning resource usage assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types)[TuningResourceUsageAssessmentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types.TuningResourceUsageAssessmentConfig)` |   
  
### TuningValidationAssessmentConfig
    
    
    public AssessDataRequest.Types.TuningValidationAssessmentConfig TuningValidationAssessmentConfig { get; set; }

Optional. Configuration for the tuning validation assessment.

**Property Value**  
---  
**Type** | **Description**  
`[AssessDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types)[TuningValidationAssessmentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssessDataRequest.Types.TuningValidationAssessmentConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
