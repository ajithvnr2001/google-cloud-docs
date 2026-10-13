---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest
title: Distributed Cloud Edge Network v1 API - Class DeleteSubnetRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:35.047744+00:00
---

# Distributed Cloud Edge Network v1 API - Class DeleteSubnetRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network v1 API - Class DeleteSubnetRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.5.0/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.4.0/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.3.0/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.2.0/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.1.0/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.0.0/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)


    
    
    public sealed class DeleteSubnetRequest : IMessage<DeleteSubnetRequest>, IEquatable<DeleteSubnetRequest>, IDeepCloneable<DeleteSubnetRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Distributed Cloud Edge Network v1 API class DeleteSubnetRequest.

Message for deleting a Subnet

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteSubnetRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.EdgeNetwork.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1)

## Assembly

Google.Cloud.EdgeNetwork.V1.dll

## Constructors 

### DeleteSubnetRequest()
    
    
    public DeleteSubnetRequest()

### DeleteSubnetRequest(DeleteSubnetRequest)
    
    
    public DeleteSubnetRequest(DeleteSubnetRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the resource

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubnetName
    
    
    public SubnetName SubnetName { get; set; }

[SubnetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.SubnetName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.DeleteSubnetRequest#Google_Cloud_EdgeNetwork_V1_DeleteSubnetRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SubnetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.SubnetName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
