---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddAddressGroupItemsRequest
title: Network Security v1 API - Class AddAddressGroupItemsRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:45.812010+00:00
---

# Network Security v1 API - Class AddAddressGroupItemsRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddAddressGroupItemsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1 API - Class AddAddressGroupItemsRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class AddAddressGroupItemsRequest : IMessage<AddAddressGroupItemsRequest>, IEquatable<AddAddressGroupItemsRequest>, IDeepCloneable<AddAddressGroupItemsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Security v1 API class AddAddressGroupItemsRequest.

Request used by the AddAddressGroupItems method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AddAddressGroupItemsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AddAddressGroupItemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddAddressGroupItemsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AddAddressGroupItemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddAddressGroupItemsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AddAddressGroupItemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddAddressGroupItemsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkSecurity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1)

## Assembly

Google.Cloud.NetworkSecurity.V1.dll

## Constructors 

### AddAddressGroupItemsRequest()
    
    
    public AddAddressGroupItemsRequest()

### AddAddressGroupItemsRequest(AddAddressGroupItemsRequest)
    
    
    public AddAddressGroupItemsRequest(AddAddressGroupItemsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AddAddressGroupItemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddAddressGroupItemsRequest)`  
  
  
## Properties 

### AddressGroup
    
    
    public string AddressGroup { get; set; }

Required. A name of the AddressGroup to add items to. Must be in the format `projects|organization/*/locations/{location}/addressGroups/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AddressGroupAsAddressGroupName
    
    
    public AddressGroupName AddressGroupAsAddressGroupName { get; set; }

[AddressGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddressGroupName)-typed view over the [AddressGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddAddressGroupItemsRequest#Google_Cloud_NetworkSecurity_V1_AddAddressGroupItemsRequest_AddressGroup) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AddressGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AddressGroupName)` |   
  
### Items
    
    
    public RepeatedField<string> Items { get; }

Required. List of items to add.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-01 UTC."],[],[]] 
