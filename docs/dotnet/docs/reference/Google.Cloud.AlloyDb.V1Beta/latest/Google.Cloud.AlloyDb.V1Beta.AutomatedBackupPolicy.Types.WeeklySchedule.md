---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.WeeklySchedule
title: AlloyDB v1beta API - Class AutomatedBackupPolicy.Types.WeeklySchedule (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:08.617979+00:00
---

# AlloyDB v1beta API - Class AutomatedBackupPolicy.Types.WeeklySchedule (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.WeeklySchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class AutomatedBackupPolicy.Types.WeeklySchedule (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class AutomatedBackupPolicy.Types.WeeklySchedule : IMessage<AutomatedBackupPolicy.Types.WeeklySchedule>, IEquatable<AutomatedBackupPolicy.Types.WeeklySchedule>, IDeepCloneable<AutomatedBackupPolicy.Types.WeeklySchedule>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class AutomatedBackupPolicy.Types.WeeklySchedule.

A weekly schedule starts a backup at prescribed start times within a day, for the specified days of the week.

The weekly schedule message is flexible and can be used to create many types of schedules. For example, to have a daily backup that starts at 22:00, configure the `start_times` field to have one element "22:00" and the `days_of_week` field to have all seven days of the week.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutomatedBackupPolicy.Types.WeeklySchedule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.WeeklySchedule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.WeeklySchedule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.WeeklySchedule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### WeeklySchedule()
    
    
    public WeeklySchedule()

### WeeklySchedule(WeeklySchedule)
    
    
    public WeeklySchedule(AutomatedBackupPolicy.Types.WeeklySchedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.WeeklySchedule)`  
  
  
## Properties 

### DaysOfWeek
    
    
    public RepeatedField<DayOfWeek> DaysOfWeek { get; }

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DayOfWeek](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DayOfWeek.html)` |   
  
### StartTimes
    
    
    public RepeatedField<TimeOfDay> StartTimes { get; }

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[TimeOfDay](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeOfDay.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
