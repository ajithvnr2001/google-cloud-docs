---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus
title: Batch v1 API - Class TaskStatus (2.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:45.842396+00:00
---

# Batch v1 API - Class TaskStatus (2.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Batch v1 API - Class TaskStatus (2.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.16.0 (latest)  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class TaskStatus : IMessage<TaskStatus>, IEquatable<TaskStatus>, IDeepCloneable<TaskStatus>, IBufferMessage, IMessage

Reference documentation and code samples for the Batch v1 API class TaskStatus.

Status of a task.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TaskStatus

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TaskStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TaskStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TaskStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Batch.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1)

## Assembly

Google.Cloud.Batch.V1.dll

## Constructors 

### TaskStatus()
    
    
    public TaskStatus()

### TaskStatus(TaskStatus)
    
    
    public TaskStatus(TaskStatus other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TaskStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus)`  
  
  
## Properties 

### State
    
    
    public TaskStatus.Types.State State { get; set; }

Task state.

**Property Value**  
---  
**Type** | **Description**  
`[TaskStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus.Types.State)` |   
  
### StatusEvents
    
    
    public RepeatedField<StatusEvent> StatusEvents { get; }

Detailed info about why the state is reached.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[StatusEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.StatusEvent)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
