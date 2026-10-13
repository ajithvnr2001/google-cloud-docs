---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership
title: Security Command Center v2 API - Class GroupMembership (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:33.859325+00:00
---

# Security Command Center v2 API - Class GroupMembership (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class GroupMembership (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GroupMembership : IMessage<GroupMembership>, IEquatable<GroupMembership>, IDeepCloneable<GroupMembership>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Command Center v2 API class GroupMembership.

Contains details about groups of which this finding is a member. A group is a collection of findings that are related in some way.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GroupMembership

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GroupMembership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GroupMembership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GroupMembership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### GroupMembership()
    
    
    public GroupMembership()

### GroupMembership(GroupMembership)
    
    
    public GroupMembership(GroupMembership other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GroupMembership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership)`  
  
  
## Properties 

### GroupId
    
    
    public string GroupId { get; set; }

ID of the group.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GroupType
    
    
    public GroupMembership.Types.GroupType GroupType { get; set; }

Type of group.

**Property Value**  
---  
**Type** | **Description**  
`[GroupMembership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership.Types)[GroupType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.GroupMembership.Types.GroupType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
