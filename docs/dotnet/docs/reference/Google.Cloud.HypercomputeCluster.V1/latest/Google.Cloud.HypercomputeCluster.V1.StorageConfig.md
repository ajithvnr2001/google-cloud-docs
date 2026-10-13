---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.StorageConfig
title: Cluster Director v1 API - Class StorageConfig (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:47.482569+00:00
---

# Cluster Director v1 API - Class StorageConfig (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.StorageConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cluster Director v1 API - Class StorageConfig (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class StorageConfig : IMessage<StorageConfig>, IEquatable<StorageConfig>, IDeepCloneable<StorageConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Cluster Director v1 API class StorageConfig.

Description of how a [storage resource][google.cloud.hypercomputecluster.v1.StorageResource] should be mounted on a VM instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StorageConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.StorageConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.StorageConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.StorageConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.HypercomputeCluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1)

## Assembly

Google.Cloud.HypercomputeCluster.V1.dll

## Constructors 

### StorageConfig()
    
    
    public StorageConfig()

### StorageConfig(StorageConfig)
    
    
    public StorageConfig(StorageConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.StorageConfig)`  
  
  
## Properties 

### Id
    
    
    public string Id { get; set; }

Required. ID of the storage resource to mount, which must match a key in the cluster's [storage_resources][google.cloud.hypercomputecluster.v1.Cluster.storage_resources].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LocalMount
    
    
    public string LocalMount { get; set; }

Required. A directory inside the VM instance's file system where the storage resource should be mounted (e.g., `/mnt/share`).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
