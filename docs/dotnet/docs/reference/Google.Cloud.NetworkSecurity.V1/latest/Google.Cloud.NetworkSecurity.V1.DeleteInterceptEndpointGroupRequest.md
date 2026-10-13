---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteInterceptEndpointGroupRequest
title: Network Security v1 API - Class DeleteInterceptEndpointGroupRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:07.008499+00:00
---

# Network Security v1 API - Class DeleteInterceptEndpointGroupRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteInterceptEndpointGroupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1 API - Class DeleteInterceptEndpointGroupRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class DeleteInterceptEndpointGroupRequest : IMessage<DeleteInterceptEndpointGroupRequest>, IEquatable<DeleteInterceptEndpointGroupRequest>, IDeepCloneable<DeleteInterceptEndpointGroupRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Security v1 API class DeleteInterceptEndpointGroupRequest.

Request message for DeleteInterceptEndpointGroup.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteInterceptEndpointGroupRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteInterceptEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteInterceptEndpointGroupRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteInterceptEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteInterceptEndpointGroupRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteInterceptEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteInterceptEndpointGroupRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkSecurity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1)

## Assembly

Google.Cloud.NetworkSecurity.V1.dll

## Constructors 

### DeleteInterceptEndpointGroupRequest()
    
    
    public DeleteInterceptEndpointGroupRequest()

### DeleteInterceptEndpointGroupRequest(DeleteInterceptEndpointGroupRequest)
    
    
    public DeleteInterceptEndpointGroupRequest(DeleteInterceptEndpointGroupRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteInterceptEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteInterceptEndpointGroupRequest)`  
  
  
## Properties 

### InterceptEndpointGroupName
    
    
    public InterceptEndpointGroupName InterceptEndpointGroupName { get; set; }

[InterceptEndpointGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.InterceptEndpointGroupName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteInterceptEndpointGroupRequest#Google_Cloud_NetworkSecurity_V1_DeleteInterceptEndpointGroupRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InterceptEndpointGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.InterceptEndpointGroupName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The endpoint group to delete.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A unique identifier for this request. Must be a UUID4. This request is only idempotent if a `request_id` is provided. See <https://google.aip.dev/155> for more details.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-01 UTC."],[],[]] 
