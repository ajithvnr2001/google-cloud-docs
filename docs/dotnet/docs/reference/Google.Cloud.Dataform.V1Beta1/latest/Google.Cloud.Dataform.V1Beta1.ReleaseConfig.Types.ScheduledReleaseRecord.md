---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord
title: Dataform v1beta1 API - Class ReleaseConfig.Types.ScheduledReleaseRecord (1.0.0-beta15) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:30.825525+00:00
---

# Dataform v1beta1 API - Class ReleaseConfig.Types.ScheduledReleaseRecord (1.0.0-beta15)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1beta1 API - Class ReleaseConfig.Types.ScheduledReleaseRecord (1.0.0-beta15) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta15 (latest)  1.0.0-beta14 
    
    
    public sealed class ReleaseConfig.Types.ScheduledReleaseRecord : IMessage<ReleaseConfig.Types.ScheduledReleaseRecord>, IEquatable<ReleaseConfig.Types.ScheduledReleaseRecord>, IDeepCloneable<ReleaseConfig.Types.ScheduledReleaseRecord>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataform v1beta1 API class ReleaseConfig.Types.ScheduledReleaseRecord.

A record of an attempt to create a compilation result for this release config.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReleaseConfig.Types.ScheduledReleaseRecord

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types)[ScheduledReleaseRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types)[ScheduledReleaseRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types)[ScheduledReleaseRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1)

## Assembly

Google.Cloud.Dataform.V1Beta1.dll

## Constructors 

### ScheduledReleaseRecord()
    
    
    public ScheduledReleaseRecord()

### ScheduledReleaseRecord(ScheduledReleaseRecord)
    
    
    public ScheduledReleaseRecord(ReleaseConfig.Types.ScheduledReleaseRecord other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types)[ScheduledReleaseRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord)`  
  
  
## Properties 

### CompilationResult
    
    
    public string CompilationResult { get; set; }

The name of the created compilation result, if one was successfully created. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CompilationResultAsCompilationResultName
    
    
    public CompilationResultName CompilationResultAsCompilationResultName { get; set; }

[CompilationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultName)-typed view over the [CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord#Google_Cloud_Dataform_V1Beta1_ReleaseConfig_Types_ScheduledReleaseRecord_CompilationResult) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CompilationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResultName)` |   
  
### ErrorStatus
    
    
    public Status ErrorStatus { get; set; }

The error status encountered upon this attempt to create the compilation result, if the attempt was unsuccessful.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### HasCompilationResult
    
    
    public bool HasCompilationResult { get; }

Gets whether the "compilation_result" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ReleaseTime
    
    
    public Timestamp ReleaseTime { get; set; }

Output only. The timestamp of this release attempt.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ResultCase
    
    
    public ReleaseConfig.Types.ScheduledReleaseRecord.ResultOneofCase ResultCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types)[ScheduledReleaseRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord)[ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig.Types.ScheduledReleaseRecord.ResultOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
