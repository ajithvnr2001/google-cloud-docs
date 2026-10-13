---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Resource
title: Workload Manager v1 API - Class Resource (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:22.419838+00:00
---

# Workload Manager v1 API - Class Resource (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Resource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Workload Manager v1 API - Class Resource (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class Resource : IMessage<Resource>, IEquatable<Resource>, IDeepCloneable<Resource>, IBufferMessage, IMessage

Reference documentation and code samples for the Workload Manager v1 API class Resource.

Resource in execution result.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Resource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Resource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Resource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Resource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.WorkloadManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1)

## Assembly

Google.Cloud.WorkloadManager.V1.dll

## Constructors 

### Resource()
    
    
    public Resource()

### Resource(Resource)
    
    
    public Resource(Resource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Resource)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

The name of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

The service account associated with the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public string Type { get; set; }

The type of resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-22 UTC."],[],[]] 
