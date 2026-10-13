---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitLogEntry
title: Dataform v1beta1 API - Class CommitLogEntry (1.0.0-beta15) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:25.547000+00:00
---

# Dataform v1beta1 API - Class CommitLogEntry (1.0.0-beta15)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitLogEntry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1beta1 API - Class CommitLogEntry (1.0.0-beta15) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta15 (latest)  1.0.0-beta14 
    
    
    public sealed class CommitLogEntry : IMessage<CommitLogEntry>, IEquatable<CommitLogEntry>, IDeepCloneable<CommitLogEntry>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataform v1beta1 API class CommitLogEntry.

Represents a single commit log.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CommitLogEntry

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CommitLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitLogEntry), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CommitLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitLogEntry), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CommitLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitLogEntry), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1)

## Assembly

Google.Cloud.Dataform.V1Beta1.dll

## Constructors 

### CommitLogEntry()
    
    
    public CommitLogEntry()

### CommitLogEntry(CommitLogEntry)
    
    
    public CommitLogEntry(CommitLogEntry other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CommitLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitLogEntry)`  
  
  
## Properties 

### Author
    
    
    public CommitAuthor Author { get; set; }

The commit author for this commit log entry.

**Property Value**  
---  
**Type** | **Description**  
`[CommitAuthor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitAuthor)` |   
  
### CommitMessage
    
    
    public string CommitMessage { get; set; }

The commit message for this commit log entry.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CommitSha
    
    
    public string CommitSha { get; set; }

The commit SHA for this commit log entry.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CommitTime
    
    
    public Timestamp CommitTime { get; set; }

Commit timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
