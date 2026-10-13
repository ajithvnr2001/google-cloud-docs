---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry
title: Database Migration v1 API - Class BackgroundJobLogEntry (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:01.973179+00:00
---

# Database Migration v1 API - Class BackgroundJobLogEntry (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Migration v1 API - Class BackgroundJobLogEntry (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.5.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.4.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.3.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.2.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.1.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.0.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.2.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.1.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.0.0/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)


    
    
    public sealed class BackgroundJobLogEntry : IMessage<BackgroundJobLogEntry>, IEquatable<BackgroundJobLogEntry>, IDeepCloneable<BackgroundJobLogEntry>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Migration v1 API class BackgroundJobLogEntry.

Execution log of a background job.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackgroundJobLogEntry

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudDms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1)

## Assembly

Google.Cloud.CloudDms.V1.dll

## Constructors 

### BackgroundJobLogEntry()
    
    
    public BackgroundJobLogEntry()

### BackgroundJobLogEntry(BackgroundJobLogEntry)
    
    
    public BackgroundJobLogEntry(BackgroundJobLogEntry other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)`  
  
  
## Properties 

### ApplyJobDetails
    
    
    public BackgroundJobLogEntry.Types.ApplyJobDetails ApplyJobDetails { get; set; }

Output only. Apply job details.

**Property Value**  
---  
**Type** | **Description**  
`[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types)[ApplyJobDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types.ApplyJobDetails)` |   
  
### CompletionComment
    
    
    public string CompletionComment { get; set; }

Output only. Job completion comment, such as how many entities were seeded, how many warnings were found during conversion, and similar information.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CompletionState
    
    
    public BackgroundJobLogEntry.Types.JobCompletionState CompletionState { get; set; }

Output only. Job completion state, i.e. the final state after the job completed.

**Property Value**  
---  
**Type** | **Description**  
`[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types)[JobCompletionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types.JobCompletionState)` |   
  
### ConvertJobDetails
    
    
    public BackgroundJobLogEntry.Types.ConvertJobDetails ConvertJobDetails { get; set; }

Output only. Convert job details.

**Property Value**  
---  
**Type** | **Description**  
`[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types)[ConvertJobDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types.ConvertJobDetails)` |   
  
### FinishTime
    
    
    public Timestamp FinishTime { get; set; }

The timestamp when the background job was finished.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Id
    
    
    public string Id { get; set; }

The background job log entry ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ImportRulesJobDetails
    
    
    public BackgroundJobLogEntry.Types.ImportRulesJobDetails ImportRulesJobDetails { get; set; }

Output only. Import rules job details.

**Property Value**  
---  
**Type** | **Description**  
`[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types)[ImportRulesJobDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types.ImportRulesJobDetails)` |   
  
### JobDetailsCase
    
    
    public BackgroundJobLogEntry.JobDetailsOneofCase JobDetailsCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)[JobDetailsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.JobDetailsOneofCase)` |   
  
### JobType
    
    
    public BackgroundJobType JobType { get; set; }

The type of job that was executed.

**Property Value**  
---  
**Type** | **Description**  
`[BackgroundJobType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobType)` |   
  
### RequestAutocommit
    
    
    public bool RequestAutocommit { get; set; }

Output only. Whether the client requested the conversion workspace to be committed after a successful completion of the job.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SeedJobDetails
    
    
    public BackgroundJobLogEntry.Types.SeedJobDetails SeedJobDetails { get; set; }

Output only. Seed job details.

**Property Value**  
---  
**Type** | **Description**  
`[BackgroundJobLogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types)[SeedJobDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.BackgroundJobLogEntry.Types.SeedJobDetails)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

The timestamp when the background job was started.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
