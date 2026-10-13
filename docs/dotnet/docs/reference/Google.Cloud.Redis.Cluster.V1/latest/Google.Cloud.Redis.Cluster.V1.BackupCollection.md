---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection
title: Google Cloud Memorystore for Redis (cluster management) v1 API - Class BackupCollection (1.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:38.625631+00:00
---

# Google Cloud Memorystore for Redis (cluster management) v1 API - Class BackupCollection (1.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis (cluster management) v1 API - Class BackupCollection (1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BackupCollection : IMessage<BackupCollection>, IEquatable<BackupCollection>, IDeepCloneable<BackupCollection>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Memorystore for Redis (cluster management) v1 API class BackupCollection.

BackupCollection of a cluster.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackupCollection

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.Cluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1)

## Assembly

Google.Cloud.Redis.Cluster.V1.dll

## Constructors 

### BackupCollection()
    
    
    public BackupCollection()

### BackupCollection(BackupCollection)
    
    
    public BackupCollection(BackupCollection other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection)`  
  
  
## Properties 

### BackupCollectionName
    
    
    public BackupCollectionName BackupCollectionName { get; set; }

[BackupCollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollectionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection#Google_Cloud_Redis_Cluster_V1_BackupCollection_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BackupCollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollectionName)` |   
  
### Cluster
    
    
    public string Cluster { get; set; }

Output only. The full resource path of the cluster the backup collection belongs to. Example: projects/{project}/locations/{location}/clusters/{cluster}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ClusterAsClusterName
    
    
    public ClusterName ClusterAsClusterName { get; set; }

[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ClusterName)-typed view over the [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection#Google_Cloud_Redis_Cluster_V1_BackupCollection_Cluster) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ClusterName)` |   
  
### ClusterUid
    
    
    public string ClusterUid { get; set; }

Output only. The cluster uid of the backup collection.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KmsKey
    
    
    public string KmsKey { get; set; }

Output only. The KMS key used to encrypt the backups under this backup collection.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KmsKeyAsCryptoKeyName
    
    
    public CryptoKeyName KmsKeyAsCryptoKeyName { get; set; }

[CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CryptoKeyName)-typed view over the [KmsKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection#Google_Cloud_Redis_Cluster_V1_BackupCollection_KmsKey) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CryptoKeyName)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Full resource path of the backup collection.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. System assigned unique identifier of the backup collection.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
