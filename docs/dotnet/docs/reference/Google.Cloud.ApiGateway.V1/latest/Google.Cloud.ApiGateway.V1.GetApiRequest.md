---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.GetApiRequest
title: API Gateway v1 API - Class GetApiRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:15.825624+00:00
---

# API Gateway v1 API - Class GetApiRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.GetApiRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API Gateway v1 API - Class GetApiRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.1.0  1.0.0 
    
    
    public sealed class GetApiRequest : IMessage<GetApiRequest>, IEquatable<GetApiRequest>, IDeepCloneable<GetApiRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the API Gateway v1 API class GetApiRequest.

Request message for ApiGatewayService.GetApi

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetApiRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetApiRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.GetApiRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetApiRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.GetApiRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetApiRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.GetApiRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiGateway.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1)

## Assembly

Google.Cloud.ApiGateway.V1.dll

## Constructors 

### GetApiRequest()
    
    
    public GetApiRequest()

### GetApiRequest(GetApiRequest)
    
    
    public GetApiRequest(GetApiRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetApiRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.GetApiRequest)`  
  
  
## Properties 

### ApiName
    
    
    public ApiName ApiName { get; set; }

[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.GetApiRequest#Google_Cloud_ApiGateway_V1_GetApiRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Resource name of the form: `projects/*/locations/global/apis/*`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
