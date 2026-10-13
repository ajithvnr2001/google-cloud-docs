---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceSuspensionInfo
title: Database Center v1beta API - Class ResourceSuspensionInfo (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:02.747076+00:00
---

# Database Center v1beta API - Class ResourceSuspensionInfo (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceSuspensionInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class ResourceSuspensionInfo (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class ResourceSuspensionInfo : IMessage<ResourceSuspensionInfo>, IEquatable<ResourceSuspensionInfo>, IDeepCloneable<ResourceSuspensionInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class ResourceSuspensionInfo.

Resource suspension info for a database resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceSuspensionInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResourceSuspensionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceSuspensionInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceSuspensionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceSuspensionInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResourceSuspensionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceSuspensionInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### ResourceSuspensionInfo()
    
    
    public ResourceSuspensionInfo()

### ResourceSuspensionInfo(ResourceSuspensionInfo)
    
    
    public ResourceSuspensionInfo(ResourceSuspensionInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceSuspensionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceSuspensionInfo)`  
  
  
## Properties 

### ResourceSuspended
    
    
    public bool ResourceSuspended { get; set; }

Is resource suspended.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SuspensionReason
    
    
    public SuspensionReason SuspensionReason { get; set; }

Suspension reason for the resource.

**Property Value**  
---  
**Type** | **Description**  
`[SuspensionReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SuspensionReason)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
