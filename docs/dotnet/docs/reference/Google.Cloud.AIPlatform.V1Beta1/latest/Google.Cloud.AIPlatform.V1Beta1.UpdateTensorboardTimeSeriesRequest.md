---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateTensorboardTimeSeriesRequest
title: Vertex AI v1beta1 API - Class UpdateTensorboardTimeSeriesRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:43.407214+00:00
---

# Vertex AI v1beta1 API - Class UpdateTensorboardTimeSeriesRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateTensorboardTimeSeriesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class UpdateTensorboardTimeSeriesRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class UpdateTensorboardTimeSeriesRequest : IMessage<UpdateTensorboardTimeSeriesRequest>, IEquatable<UpdateTensorboardTimeSeriesRequest>, IDeepCloneable<UpdateTensorboardTimeSeriesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class UpdateTensorboardTimeSeriesRequest.

Request message for [TensorboardService.UpdateTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.UpdateTensorboardTimeSeries].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateTensorboardTimeSeriesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateTensorboardTimeSeriesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateTensorboardTimeSeriesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateTensorboardTimeSeriesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### UpdateTensorboardTimeSeriesRequest()
    
    
    public UpdateTensorboardTimeSeriesRequest()

### UpdateTensorboardTimeSeriesRequest(UpdateTensorboardTimeSeriesRequest)
    
    
    public UpdateTensorboardTimeSeriesRequest(UpdateTensorboardTimeSeriesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateTensorboardTimeSeriesRequest)`  
  
  
## Properties 

### TensorboardTimeSeries
    
    
    public TensorboardTimeSeries TensorboardTimeSeries { get; set; }

Required. The TensorboardTimeSeries' `name` field is used to identify the TensorboardTimeSeries to be updated. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`

**Property Value**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.TensorboardTimeSeries)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. Field mask is used to specify the fields to be overwritten in the TensorboardTimeSeries resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it's in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
