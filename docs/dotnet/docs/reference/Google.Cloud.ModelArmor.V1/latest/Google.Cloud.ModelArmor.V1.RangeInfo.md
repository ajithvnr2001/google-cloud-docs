---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RangeInfo
title: Model Armor v1 API - Class RangeInfo (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:33.190166+00:00
---

# Model Armor v1 API - Class RangeInfo (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RangeInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1 API - Class RangeInfo (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta07 
    
    
    public sealed class RangeInfo : IMessage<RangeInfo>, IEquatable<RangeInfo>, IDeepCloneable<RangeInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1 API class RangeInfo.

Half-open range interval [start, end)

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RangeInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RangeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RangeInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RangeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RangeInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RangeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RangeInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1)

## Assembly

Google.Cloud.ModelArmor.V1.dll

## Constructors 

### RangeInfo()
    
    
    public RangeInfo()

### RangeInfo(RangeInfo)
    
    
    public RangeInfo(RangeInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RangeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RangeInfo)`  
  
  
## Properties 

### End
    
    
    public long End { get; set; }

Index of last character (exclusive).

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### HasEnd
    
    
    public bool HasEnd { get; }

Gets whether the "end" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStart
    
    
    public bool HasStart { get; }

Gets whether the "start" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Start
    
    
    public long Start { get; set; }

For proto3, value cannot be set to 0 unless the field is optional. Ref: <https://protobuf.dev/programming-guides/proto3/#default> Index of first character (inclusive).

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
