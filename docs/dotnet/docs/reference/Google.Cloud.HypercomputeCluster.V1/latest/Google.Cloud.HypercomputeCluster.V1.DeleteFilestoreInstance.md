---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.DeleteFilestoreInstance
title: Cluster Director v1 API - Class DeleteFilestoreInstance (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:15.877542+00:00
---

# Cluster Director v1 API - Class DeleteFilestoreInstance (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.DeleteFilestoreInstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cluster Director v1 API - Class DeleteFilestoreInstance (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class DeleteFilestoreInstance : IMessage<DeleteFilestoreInstance>, IEquatable<DeleteFilestoreInstance>, IDeepCloneable<DeleteFilestoreInstance>, IBufferMessage, IMessage

Reference documentation and code samples for the Cluster Director v1 API class DeleteFilestoreInstance.

When set in OperationStep, indicates that a Filestore instance should be deleted.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteFilestoreInstance

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteFilestoreInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.DeleteFilestoreInstance), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteFilestoreInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.DeleteFilestoreInstance), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteFilestoreInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.DeleteFilestoreInstance), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.HypercomputeCluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1)

## Assembly

Google.Cloud.HypercomputeCluster.V1.dll

## Constructors 

### DeleteFilestoreInstance()
    
    
    public DeleteFilestoreInstance()

### DeleteFilestoreInstance(DeleteFilestoreInstance)
    
    
    public DeleteFilestoreInstance(DeleteFilestoreInstance other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteFilestoreInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.DeleteFilestoreInstance)`  
  
  
## Properties 

### Filestore
    
    
    public string Filestore { get; set; }

Output only. Name of the Filestore instance, in the format `projects/{project}/locations/{location}/instances/{instance}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FilestoreAsFileInstanceName
    
    
    public FileInstanceName FilestoreAsFileInstanceName { get; set; }

[FileInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.FileInstanceName)-typed view over the [Filestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.DeleteFilestoreInstance#Google_Cloud_HypercomputeCluster_V1_DeleteFilestoreInstance_Filestore) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FileInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.FileInstanceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
