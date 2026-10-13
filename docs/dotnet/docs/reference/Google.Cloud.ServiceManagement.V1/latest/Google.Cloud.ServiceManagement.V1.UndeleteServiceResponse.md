---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse
title: Service Management v1 API - Class UndeleteServiceResponse (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:31.345937+00:00
---

# Service Management v1 API - Class UndeleteServiceResponse (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Management v1 API - Class UndeleteServiceResponse (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.4.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.3.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.2.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.1.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.0.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.5.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.4.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.3.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.2.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.1.0/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)


    
    
    public sealed class UndeleteServiceResponse : IMessage<UndeleteServiceResponse>, IEquatable<UndeleteServiceResponse>, IDeepCloneable<UndeleteServiceResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Management v1 API class UndeleteServiceResponse.

Response message for UndeleteService method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UndeleteServiceResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UndeleteServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UndeleteServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UndeleteServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1)

## Assembly

Google.Cloud.ServiceManagement.V1.dll

## Constructors 

### UndeleteServiceResponse()
    
    
    public UndeleteServiceResponse()

### UndeleteServiceResponse(UndeleteServiceResponse)
    
    
    public UndeleteServiceResponse(UndeleteServiceResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UndeleteServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.UndeleteServiceResponse)`  
  
  
## Properties 

### Service
    
    
    public ManagedService Service { get; set; }

Revived service resource.

**Property Value**  
---  
**Type** | **Description**  
`[ManagedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ManagedService)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
