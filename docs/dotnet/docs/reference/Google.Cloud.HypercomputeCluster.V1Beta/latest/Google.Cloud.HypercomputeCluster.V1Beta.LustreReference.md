---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreReference
title: Cluster Director v1beta API - Class LustreReference (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:53.267344+00:00
---

# Cluster Director v1beta API - Class LustreReference (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cluster Director v1beta API - Class LustreReference (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class LustreReference : IMessage<LustreReference>, IEquatable<LustreReference>, IDeepCloneable<LustreReference>, IBufferMessage, IMessage

Reference documentation and code samples for the Cluster Director v1beta API class LustreReference.

A reference to a [Managed Lustre](https://cloud.google.com/products/managed-lustre) instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LustreReference

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[LustreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreReference), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[LustreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreReference), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[LustreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreReference), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.HypercomputeCluster.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta)

## Assembly

Google.Cloud.HypercomputeCluster.V1Beta.dll

## Constructors 

### LustreReference()
    
    
    public LustreReference()

### LustreReference(LustreReference)
    
    
    public LustreReference(LustreReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[LustreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreReference)`  
  
  
## Properties 

### Lustre
    
    
    public string Lustre { get; set; }

Output only. Name of the Managed Lustre instance, in the format `projects/{project}/locations/{location}/instances/{instance}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LustreAsLustreInstanceName
    
    
    public LustreInstanceName LustreAsLustreInstanceName { get; set; }

[LustreInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreInstanceName)-typed view over the [Lustre](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreReference#Google_Cloud_HypercomputeCluster_V1Beta_LustreReference_Lustre) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LustreInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1Beta/latest/Google.Cloud.HypercomputeCluster.V1Beta.LustreInstanceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-03 UTC."],[],[]] 
