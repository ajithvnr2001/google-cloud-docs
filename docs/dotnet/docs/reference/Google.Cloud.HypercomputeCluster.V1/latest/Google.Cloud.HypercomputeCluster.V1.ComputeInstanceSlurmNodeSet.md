---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ComputeInstanceSlurmNodeSet
title: Cluster Director v1 API - Class ComputeInstanceSlurmNodeSet (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:09.519566+00:00
---

# Cluster Director v1 API - Class ComputeInstanceSlurmNodeSet (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ComputeInstanceSlurmNodeSet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cluster Director v1 API - Class ComputeInstanceSlurmNodeSet (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class ComputeInstanceSlurmNodeSet : IMessage<ComputeInstanceSlurmNodeSet>, IEquatable<ComputeInstanceSlurmNodeSet>, IDeepCloneable<ComputeInstanceSlurmNodeSet>, IBufferMessage, IMessage

Reference documentation and code samples for the Cluster Director v1 API class ComputeInstanceSlurmNodeSet.

When set in a [SlurmNodeSet][google.cloud.hypercomputecluster.v1.SlurmNodeSet], indicates that the nodeset should be backed by Compute Engine VM instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ComputeInstanceSlurmNodeSet

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ComputeInstanceSlurmNodeSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ComputeInstanceSlurmNodeSet), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ComputeInstanceSlurmNodeSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ComputeInstanceSlurmNodeSet), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ComputeInstanceSlurmNodeSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ComputeInstanceSlurmNodeSet), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.HypercomputeCluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1)

## Assembly

Google.Cloud.HypercomputeCluster.V1.dll

## Constructors 

### ComputeInstanceSlurmNodeSet()
    
    
    public ComputeInstanceSlurmNodeSet()

### ComputeInstanceSlurmNodeSet(ComputeInstanceSlurmNodeSet)
    
    
    public ComputeInstanceSlurmNodeSet(ComputeInstanceSlurmNodeSet other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ComputeInstanceSlurmNodeSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ComputeInstanceSlurmNodeSet)`  
  
  
## Properties 

### BootDisk
    
    
    public BootDisk BootDisk { get; set; }

Optional. Boot disk for the compute instance

**Property Value**  
---  
**Type** | **Description**  
`[BootDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.BootDisk)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. [Labels](https://cloud.google.com/compute/docs/labeling-resources) that should be applied to each VM instance in the nodeset.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StartupScript
    
    
    public string StartupScript { get; set; }

Optional. [Startup script](https://cloud.google.com/compute/docs/instances/startup-scripts/linux) to be run on each VM instance in the nodeset. Max 256KB.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
