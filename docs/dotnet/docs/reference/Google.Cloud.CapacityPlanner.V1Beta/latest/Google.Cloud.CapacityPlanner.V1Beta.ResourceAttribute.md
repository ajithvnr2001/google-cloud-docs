---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute
title: Capacity Planner v1beta API - Class ResourceAttribute (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:41.485735+00:00
---

# Capacity Planner v1beta API - Class ResourceAttribute (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Capacity Planner v1beta API - Class ResourceAttribute (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta02 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/1.0.0-beta01/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute)


    
    
    public sealed class ResourceAttribute : IMessage<ResourceAttribute>, IEquatable<ResourceAttribute>, IDeepCloneable<ResourceAttribute>, IBufferMessage, IMessage

Reference documentation and code samples for the Capacity Planner v1beta API class ResourceAttribute.

An attribute of a Google Cloud Platform resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceAttribute

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResourceAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResourceAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CapacityPlanner.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta)

## Assembly

Google.Cloud.CapacityPlanner.V1Beta.dll

## Constructors 

### ResourceAttribute()
    
    
    public ResourceAttribute()

### ResourceAttribute(ResourceAttribute)
    
    
    public ResourceAttribute(ResourceAttribute other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute)`  
  
  
## Properties 

### Key
    
    
    public string Key { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Value
    
    
    public ResourceValue Value { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[ResourceValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceValue)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
