---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAwsNodePoolRequest
title: Anthos Multi-Cloud v1 API - Class DeleteAwsNodePoolRequest (2.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:51.046869+00:00
---

# Anthos Multi-Cloud v1 API - Class DeleteAwsNodePoolRequest (2.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAwsNodePoolRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Anthos Multi-Cloud v1 API - Class DeleteAwsNodePoolRequest (2.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.0 (latest)  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0-beta01 
    
    
    [Obsolete]
    public sealed class DeleteAwsNodePoolRequest : IMessage<DeleteAwsNodePoolRequest>, IEquatable<DeleteAwsNodePoolRequest>, IDeepCloneable<DeleteAwsNodePoolRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Anthos Multi-Cloud v1 API class DeleteAwsNodePoolRequest.

Request message for `AwsClusters.DeleteAwsNodePool` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteAwsNodePoolRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteAwsNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAwsNodePoolRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteAwsNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAwsNodePoolRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteAwsNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAwsNodePoolRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeMultiCloud.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1)

## Assembly

Google.Cloud.GkeMultiCloud.V1.dll

## Constructors 

### DeleteAwsNodePoolRequest()
    
    
    public DeleteAwsNodePoolRequest()

### DeleteAwsNodePoolRequest(DeleteAwsNodePoolRequest)
    
    
    public DeleteAwsNodePoolRequest(DeleteAwsNodePoolRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteAwsNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAwsNodePoolRequest)`  
  
  
## Properties 

### AllowMissing
    
    
    public bool AllowMissing { get; set; }

If set to true, and the [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool] resource is not found, the request will succeed but no action will be taken on the server and a completed [Operation][google.longrunning.Operation] will be returned.

Useful for idempotent deletion.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### AwsNodePoolName
    
    
    [Obsolete]
    public AwsNodePoolName AwsNodePoolName { get; set; }

[AwsNodePoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AwsNodePoolName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.DeleteAwsNodePoolRequest#Google_Cloud_GkeMultiCloud_V1_DeleteAwsNodePoolRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AwsNodePoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AwsNodePoolName)` |   
  
### Etag
    
    
    public string Etag { get; set; }

The current ETag of the [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool].

Allows clients to perform deletions through optimistic concurrency control.

If the provided ETag does not match the current etag of the node pool, the request will fail and an ABORTED error will be returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IgnoreErrors
    
    
    public bool IgnoreErrors { get; set; }

Optional. If set to true, the deletion of [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool] resource will succeed even if errors occur during deleting in node pool resources. Using this parameter may result in orphaned resources in the node pool.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name the [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool] to delete.

`AwsNodePool` names are formatted as `projects/<project-id>/locations/<region>/awsClusters/<cluster-id>/awsNodePools/<node-pool-id>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

If set, only validate the request, but do not actually delete the node pool.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-26 UTC."],[],[]] 
