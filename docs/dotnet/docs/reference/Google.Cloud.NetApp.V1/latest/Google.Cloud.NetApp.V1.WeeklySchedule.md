---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.WeeklySchedule
title: NetApp v1 API - Class WeeklySchedule (1.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:02.854537+00:00
---

# NetApp v1 API - Class WeeklySchedule (1.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.WeeklySchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  NetApp v1 API - Class WeeklySchedule (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class WeeklySchedule : IMessage<WeeklySchedule>, IEquatable<WeeklySchedule>, IDeepCloneable<WeeklySchedule>, IBufferMessage, IMessage

Reference documentation and code samples for the NetApp v1 API class WeeklySchedule.

Make a snapshot every week e.g. at Monday 04:00, Wednesday 05:20, Sunday 23:50

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WeeklySchedule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.WeeklySchedule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.WeeklySchedule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.WeeklySchedule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetApp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1)

## Assembly

Google.Cloud.NetApp.V1.dll

## Constructors 

### WeeklySchedule()
    
    
    public WeeklySchedule()

### WeeklySchedule(WeeklySchedule)
    
    
    public WeeklySchedule(WeeklySchedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.WeeklySchedule)`  
  
  
## Properties 

### Day
    
    
    public string Day { get; set; }

Set the day or days of the week to make a snapshot. Accepts a comma separated days of the week. Defaults to 'Sunday'.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasDay
    
    
    public bool HasDay { get; }

Gets whether the "day" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasHour
    
    
    public bool HasHour { get; }

Gets whether the "hour" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMinute
    
    
    public bool HasMinute { get; }

Gets whether the "minute" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSnapshotsToKeep
    
    
    public bool HasSnapshotsToKeep { get; }

Gets whether the "snapshots_to_keep" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Hour
    
    
    public double Hour { get; set; }

Set the hour to start the snapshot (0-23), defaults to midnight (0).

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### Minute
    
    
    public double Minute { get; set; }

Set the minute of the hour to start the snapshot (0-59), defaults to the top of the hour (0).

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### SnapshotsToKeep
    
    
    public double SnapshotsToKeep { get; set; }

The maximum number of Snapshots to keep for the hourly schedule

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
