---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteMulticloudDataTransferConfigRequest
title: Network Connectivity v1beta API - Class DeleteMulticloudDataTransferConfigRequest (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:13.389554+00:00
---

# Network Connectivity v1beta API - Class DeleteMulticloudDataTransferConfigRequest (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteMulticloudDataTransferConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Class DeleteMulticloudDataTransferConfigRequest (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public sealed class DeleteMulticloudDataTransferConfigRequest : IMessage<DeleteMulticloudDataTransferConfigRequest>, IEquatable<DeleteMulticloudDataTransferConfigRequest>, IDeepCloneable<DeleteMulticloudDataTransferConfigRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Connectivity v1beta API class DeleteMulticloudDataTransferConfigRequest.

Request message to delete a `MulticloudDataTransferConfig` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteMulticloudDataTransferConfigRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteMulticloudDataTransferConfigRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteMulticloudDataTransferConfigRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteMulticloudDataTransferConfigRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Constructors 

### DeleteMulticloudDataTransferConfigRequest()
    
    
    public DeleteMulticloudDataTransferConfigRequest()

### DeleteMulticloudDataTransferConfigRequest(DeleteMulticloudDataTransferConfigRequest)
    
    
    public DeleteMulticloudDataTransferConfigRequest(DeleteMulticloudDataTransferConfigRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteMulticloudDataTransferConfigRequest)`  
  
  
## Properties 

### Etag
    
    
    public string Etag { get; set; }

Optional. The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MulticloudDataTransferConfigName
    
    
    public MulticloudDataTransferConfigName MulticloudDataTransferConfigName { get; set; }

[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.MulticloudDataTransferConfigName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DeleteMulticloudDataTransferConfigRequest#Google_Cloud_NetworkConnectivity_V1Beta_DeleteMulticloudDataTransferConfigRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.MulticloudDataTransferConfigName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the `MulticloudDataTransferConfig` resource to delete.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server waits for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, can ignore the second request. This prevents clients from accidentally creating duplicate `MulticloudDataTransferConfig` resources.

The request ID must be a valid UUID with the exception that zero UUID (00000000-0000-0000-0000-000000000000) isn't supported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
