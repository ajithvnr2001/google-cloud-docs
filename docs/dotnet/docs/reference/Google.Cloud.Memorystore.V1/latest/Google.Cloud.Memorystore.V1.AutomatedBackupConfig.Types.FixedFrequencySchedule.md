---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types.FixedFrequencySchedule
title: Memorystore v1 API - Class AutomatedBackupConfig.Types.FixedFrequencySchedule (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:46.618295+00:00
---

# Memorystore v1 API - Class AutomatedBackupConfig.Types.FixedFrequencySchedule (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types.FixedFrequencySchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1 API - Class AutomatedBackupConfig.Types.FixedFrequencySchedule (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta09 
    
    
    public sealed class AutomatedBackupConfig.Types.FixedFrequencySchedule : IMessage<AutomatedBackupConfig.Types.FixedFrequencySchedule>, IEquatable<AutomatedBackupConfig.Types.FixedFrequencySchedule>, IDeepCloneable<AutomatedBackupConfig.Types.FixedFrequencySchedule>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1 API class AutomatedBackupConfig.Types.FixedFrequencySchedule.

This schedule allows the backup to be triggered at a fixed frequency (currently only daily is supported).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutomatedBackupConfig.Types.FixedFrequencySchedule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutomatedBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types)[FixedFrequencySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types.FixedFrequencySchedule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutomatedBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types)[FixedFrequencySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types.FixedFrequencySchedule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutomatedBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types)[FixedFrequencySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types.FixedFrequencySchedule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1)

## Assembly

Google.Cloud.Memorystore.V1.dll

## Constructors 

### FixedFrequencySchedule()
    
    
    public FixedFrequencySchedule()

### FixedFrequencySchedule(FixedFrequencySchedule)
    
    
    public FixedFrequencySchedule(AutomatedBackupConfig.Types.FixedFrequencySchedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutomatedBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types)[FixedFrequencySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AutomatedBackupConfig.Types.FixedFrequencySchedule)`  
  
  
## Properties 

### StartTime
    
    
    public TimeOfDay StartTime { get; set; }

Required. The start time of every automated backup in UTC. It must be set to the start of an hour. This field is required.

**Property Value**  
---  
**Type** | **Description**  
`[TimeOfDay](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeOfDay.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
