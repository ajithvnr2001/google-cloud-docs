---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.SparseVector
title: Vector Search v1 API - Class SparseVector (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:26.655892+00:00
---

# Vector Search v1 API - Class SparseVector (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.SparseVector

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vector Search v1 API - Class SparseVector (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class SparseVector : IMessage<SparseVector>, IEquatable<SparseVector>, IDeepCloneable<SparseVector>, IBufferMessage, IMessage

Reference documentation and code samples for the Vector Search v1 API class SparseVector.

A sparse vector.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SparseVector

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SparseVector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.SparseVector), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SparseVector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.SparseVector), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SparseVector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.SparseVector), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VectorSearch.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1)

## Assembly

Google.Cloud.VectorSearch.V1.dll

## Constructors 

### SparseVector()
    
    
    public SparseVector()

### SparseVector(SparseVector)
    
    
    public SparseVector(SparseVector other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SparseVector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.SparseVector)`  
  
  
## Properties 

### Indices
    
    
    public RepeatedField<int> Indices { get; }

Required. The corresponding indices for the values.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Values
    
    
    public RepeatedField<float> Values { get; }

Required. The values of the vector.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)System.Single` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
