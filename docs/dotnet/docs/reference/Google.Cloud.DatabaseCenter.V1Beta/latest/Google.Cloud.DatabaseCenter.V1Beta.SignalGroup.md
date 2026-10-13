---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalGroup
title: Database Center v1beta API - Class SignalGroup (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:03.712457+00:00
---

# Database Center v1beta API - Class SignalGroup (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class SignalGroup (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class SignalGroup : IMessage<SignalGroup>, IEquatable<SignalGroup>, IDeepCloneable<SignalGroup>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class SignalGroup.

A group of signals and their counts.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SignalGroup

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SignalGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalGroup), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SignalGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalGroup), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SignalGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalGroup), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### SignalGroup()
    
    
    public SignalGroup()

### SignalGroup(SignalGroup)
    
    
    public SignalGroup(SignalGroup other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SignalGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalGroup)`  
  
  
## Properties 

### DisplayName
    
    
    public string DisplayName { get; set; }

Title of a signal group corresponding to the request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IssueCount
    
    
    public int IssueCount { get; set; }

When applied to a DatabaseResource represents count of issues associated with the resource. A signal is an issue when its SignalStatus field is set to SIGNAL_STATUS_ISSUE.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Signals
    
    
    public RepeatedField<Signal> Signals { get; }

List of signals present in the group and associated with the resource.

Only applies to a DatabaseResource.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Signal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Signal)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
