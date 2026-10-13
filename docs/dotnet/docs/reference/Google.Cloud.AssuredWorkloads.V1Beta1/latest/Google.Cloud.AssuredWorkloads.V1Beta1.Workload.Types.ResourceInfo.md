---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo
title: Assured Workloads v1beta1 API - Class Workload.Types.ResourceInfo (2.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:11.193957+00:00
---

# Assured Workloads v1beta1 API - Class Workload.Types.ResourceInfo (2.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Assured Workloads v1beta1 API - Class Workload.Types.ResourceInfo (2.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta09 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo)
  * [ 2.0.0-beta08 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/2.0.0-beta08/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo)
  * [ 1.0.0-beta08 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/1.0.0-beta08/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo)


    
    
    public sealed class Workload.Types.ResourceInfo : IMessage<Workload.Types.ResourceInfo>, IEquatable<Workload.Types.ResourceInfo>, IDeepCloneable<Workload.Types.ResourceInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Assured Workloads v1beta1 API class Workload.Types.ResourceInfo.

Represent the resources that are children of this Workload.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Workload.Types.ResourceInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types)[ResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types)[ResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types)[ResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AssuredWorkloads.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1)

## Assembly

Google.Cloud.AssuredWorkloads.V1Beta1.dll

## Constructors 

### ResourceInfo()
    
    
    public ResourceInfo()

### ResourceInfo(ResourceInfo)
    
    
    public ResourceInfo(Workload.Types.ResourceInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types)[ResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo)`  
  
  
## Properties 

### ResourceId
    
    
    public long ResourceId { get; set; }

Resource identifier. For a project this represents project_number.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ResourceType
    
    
    public Workload.Types.ResourceInfo.Types.ResourceType ResourceType { get; set; }

Indicates the type of resource.

**Property Value**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types)[ResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo.Types)[ResourceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.Workload.Types.ResourceInfo.Types.ResourceType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
