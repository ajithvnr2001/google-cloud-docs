---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteLbRouteExtensionRequest
title: Network Services v1beta1 API - Class DeleteLbRouteExtensionRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:28.957410+00:00
---

# Network Services v1beta1 API - Class DeleteLbRouteExtensionRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteLbRouteExtensionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1beta1 API - Class DeleteLbRouteExtensionRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class DeleteLbRouteExtensionRequest : IMessage<DeleteLbRouteExtensionRequest>, IEquatable<DeleteLbRouteExtensionRequest>, IDeepCloneable<DeleteLbRouteExtensionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Services v1beta1 API class DeleteLbRouteExtensionRequest.

Message for deleting a `LbRouteExtension` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteLbRouteExtensionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteLbRouteExtensionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteLbRouteExtensionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteLbRouteExtensionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1)

## Assembly

Google.Cloud.NetworkServices.V1Beta1.dll

## Constructors 

### DeleteLbRouteExtensionRequest()
    
    
    public DeleteLbRouteExtensionRequest()

### DeleteLbRouteExtensionRequest(DeleteLbRouteExtensionRequest)
    
    
    public DeleteLbRouteExtensionRequest(DeleteLbRouteExtensionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteLbRouteExtensionRequest)`  
  
  
## Properties 

### LbRouteExtensionName
    
    
    public LbRouteExtensionName LbRouteExtensionName { get; set; }

[LbRouteExtensionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.LbRouteExtensionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteLbRouteExtensionRequest#Google_Cloud_NetworkServices_V1Beta1_DeleteLbRouteExtensionRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LbRouteExtensionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.LbRouteExtensionName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the `LbRouteExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server guarantees that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
