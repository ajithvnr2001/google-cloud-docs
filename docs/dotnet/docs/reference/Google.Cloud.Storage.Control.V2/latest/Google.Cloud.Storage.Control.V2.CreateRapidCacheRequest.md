---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest
title: Cloud Storage v2 API - Class CreateRapidCacheRequest (1.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:10.320758+00:00
---

# Cloud Storage v2 API - Class CreateRapidCacheRequest (1.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Storage v2 API - Class CreateRapidCacheRequest (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1 
    
    
    public sealed class CreateRapidCacheRequest : IMessage<CreateRapidCacheRequest>, IEquatable<CreateRapidCacheRequest>, IDeepCloneable<CreateRapidCacheRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Storage v2 API class CreateRapidCacheRequest.

Request message for CreateRapidCache.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateRapidCacheRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2)

## Assembly

Google.Cloud.Storage.Control.V2.dll

## Constructors 

### CreateRapidCacheRequest()
    
    
    public CreateRapidCacheRequest()

### CreateRapidCacheRequest(CreateRapidCacheRequest)
    
    
    public CreateRapidCacheRequest(CreateRapidCacheRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsBucketName
    
    
    public BucketName ParentAsBucketName { get; set; }

[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest#Google_Cloud_Storage_Control_V2_CreateRapidCacheRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)` |   
  
### RapidCache
    
    
    public RapidCache RapidCache { get; set; }

Required. The RapidCache to create. Default values for ingest_on_write, ttl and admission_policy will be applied if not specified in the request.

**Property Value**  
---  
**Type** | **Description**  
`[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A unique identifier for this request. UUID is the recommended format, but other formats are still accepted. This request is only idempotent if a `request_id` is provided.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
