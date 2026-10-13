---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.GetWorkstationRequest
title: Cloud Workstations v1 API - Class GetWorkstationRequest (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:24.819343+00:00
---

# Cloud Workstations v1 API - Class GetWorkstationRequest (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.GetWorkstationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Workstations v1 API - Class GetWorkstationRequest (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.0 (latest)  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GetWorkstationRequest : IMessage<GetWorkstationRequest>, IEquatable<GetWorkstationRequest>, IDeepCloneable<GetWorkstationRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Workstations v1 API class GetWorkstationRequest.

Request message for GetWorkstation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetWorkstationRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.GetWorkstationRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.GetWorkstationRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.GetWorkstationRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Workstations.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1)

## Assembly

Google.Cloud.Workstations.V1.dll

## Constructors 

### GetWorkstationRequest()
    
    
    public GetWorkstationRequest()

### GetWorkstationRequest(GetWorkstationRequest)
    
    
    public GetWorkstationRequest(GetWorkstationRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.GetWorkstationRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the requested resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WorkstationName
    
    
    public WorkstationName WorkstationName { get; set; }

[WorkstationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.GetWorkstationRequest#Google_Cloud_Workstations_V1_GetWorkstationRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[WorkstationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-08 UTC."],[],[]] 
