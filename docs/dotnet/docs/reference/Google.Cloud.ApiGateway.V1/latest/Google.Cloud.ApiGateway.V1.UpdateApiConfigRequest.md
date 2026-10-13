---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.UpdateApiConfigRequest
title: API Gateway v1 API - Class UpdateApiConfigRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:54.936125+00:00
---

# API Gateway v1 API - Class UpdateApiConfigRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.UpdateApiConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API Gateway v1 API - Class UpdateApiConfigRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.1.0  1.0.0 
    
    
    public sealed class UpdateApiConfigRequest : IMessage<UpdateApiConfigRequest>, IEquatable<UpdateApiConfigRequest>, IDeepCloneable<UpdateApiConfigRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the API Gateway v1 API class UpdateApiConfigRequest.

Request message for ApiGatewayService.UpdateApiConfig

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateApiConfigRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateApiConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.UpdateApiConfigRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateApiConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.UpdateApiConfigRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateApiConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.UpdateApiConfigRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiGateway.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1)

## Assembly

Google.Cloud.ApiGateway.V1.dll

## Constructors 

### UpdateApiConfigRequest()
    
    
    public UpdateApiConfigRequest()

### UpdateApiConfigRequest(UpdateApiConfigRequest)
    
    
    public UpdateApiConfigRequest(UpdateApiConfigRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateApiConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.UpdateApiConfigRequest)`  
  
  
## Properties 

### ApiConfig
    
    
    public ApiConfig ApiConfig { get; set; }

Required. API Config resource.

**Property Value**  
---  
**Type** | **Description**  
`[ApiConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiConfig)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Field mask is used to specify the fields to be overwritten in the ApiConfig resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
