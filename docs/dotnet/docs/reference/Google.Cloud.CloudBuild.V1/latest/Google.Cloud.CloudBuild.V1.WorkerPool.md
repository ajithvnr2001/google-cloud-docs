---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool
title: Cloud Build v1 API - Class WorkerPool (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:19.443296+00:00
---

# Cloud Build v1 API - Class WorkerPool (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v1 API - Class WorkerPool (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class WorkerPool : IMessage<WorkerPool>, IEquatable<WorkerPool>, IDeepCloneable<WorkerPool>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Build v1 API class WorkerPool.

Configuration for a `WorkerPool`.

Cloud Build owns and maintains a pool of workers for general use and have no access to a project's private network. By default, builds submitted to Cloud Build will use a worker from this pool.

If your build needs access to resources on a private network, create and use a `WorkerPool` to run your builds. Private `WorkerPool`s give your builds access to any single VPC network that you administer, including any on-prem resources connected to that VPC network. For an overview of private pools, see [Private pools overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WorkerPool

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudBuild.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1)

## Assembly

Google.Cloud.CloudBuild.V1.dll

## Constructors 

### WorkerPool()
    
    
    public WorkerPool()

### WorkerPool(WorkerPool)
    
    
    public WorkerPool(WorkerPool other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool)`  
  
  
## Properties 

### Annotations
    
    
    public MapField<string, string> Annotations { get; }

User specified annotations. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ConfigCase
    
    
    public WorkerPool.ConfigOneofCase ConfigCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool)[ConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool.ConfigOneofCase)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Time at which the request to create the `WorkerPool` was received.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DeleteTime
    
    
    public Timestamp DeleteTime { get; set; }

Output only. Time at which the request to delete the `WorkerPool` was received.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

A user-specified, human-readable name for the `WorkerPool`. If provided, this value must be 1-63 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Output only. Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name of the `WorkerPool`, with format `projects/{project}/locations/{location}/workerPools/{worker_pool}`. The value of `{worker_pool}` is provided by `worker_pool_id` in `CreateWorkerPool` request and the value of `{location}` is determined by the endpoint accessed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrivatePoolV1Config
    
    
    public PrivatePoolV1Config PrivatePoolV1Config { get; set; }

Private Pool configuration.

**Property Value**  
---  
**Type** | **Description**  
`[PrivatePoolV1Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.PrivatePoolV1Config)` |   
  
### State
    
    
    public WorkerPool.Types.State State { get; set; }

Output only. `WorkerPool` state.

**Property Value**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool.Types.State)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. A unique identifier for the `WorkerPool`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Time at which the request to update the `WorkerPool` was received.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### WorkerPoolName
    
    
    public WorkerPoolName WorkerPoolName { get; set; }

[WorkerPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPoolName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPool#Google_Cloud_CloudBuild_V1_WorkerPool_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[WorkerPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.WorkerPoolName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
