---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.UpdateLbTrafficExtensionRequest
title: Network Services v1 API - Class UpdateLbTrafficExtensionRequest (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:06.044997+00:00
---

# Network Services v1 API - Class UpdateLbTrafficExtensionRequest (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.UpdateLbTrafficExtensionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1 API - Class UpdateLbTrafficExtensionRequest (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class UpdateLbTrafficExtensionRequest : IMessage<UpdateLbTrafficExtensionRequest>, IEquatable<UpdateLbTrafficExtensionRequest>, IDeepCloneable<UpdateLbTrafficExtensionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Services v1 API class UpdateLbTrafficExtensionRequest.

Message for updating a `LbTrafficExtension` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateLbTrafficExtensionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.UpdateLbTrafficExtensionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.UpdateLbTrafficExtensionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.UpdateLbTrafficExtensionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1)

## Assembly

Google.Cloud.NetworkServices.V1.dll

## Constructors 

### UpdateLbTrafficExtensionRequest()
    
    
    public UpdateLbTrafficExtensionRequest()

### UpdateLbTrafficExtensionRequest(UpdateLbTrafficExtensionRequest)
    
    
    public UpdateLbTrafficExtensionRequest(UpdateLbTrafficExtensionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.UpdateLbTrafficExtensionRequest)`  
  
  
## Properties 

### LbTrafficExtension
    
    
    public LbTrafficExtension LbTrafficExtension { get; set; }

Required. `LbTrafficExtension` resource being updated.

**Property Value**  
---  
**Type** | **Description**  
`[LbTrafficExtension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.LbTrafficExtension)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server guarantees that for 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server ignores the second request This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Optional. Used to specify the fields to be overwritten in the `LbTrafficExtension` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
