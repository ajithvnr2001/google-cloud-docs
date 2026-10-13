---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep
title: VM Migration v1 API - Class DiskMigrationStep (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:45.562409+00:00
---

# VM Migration v1 API - Class DiskMigrationStep (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VM Migration v1 API - Class DiskMigrationStep (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.8.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.7.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.6.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.5.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.4.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.3.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.2.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.1.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.0.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/1.0.0/Google.Cloud.VMMigration.V1.DiskMigrationStep)


    
    
    public sealed class DiskMigrationStep : IMessage<DiskMigrationStep>, IEquatable<DiskMigrationStep>, IDeepCloneable<DiskMigrationStep>, IBufferMessage, IMessage

Reference documentation and code samples for the VM Migration v1 API class DiskMigrationStep.

DiskMigrationStep holds information about the disk migration step progress.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DiskMigrationStep

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DiskMigrationStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DiskMigrationStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DiskMigrationStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VMMigration.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1)

## Assembly

Google.Cloud.VMMigration.V1.dll

## Constructors 

### DiskMigrationStep()
    
    
    public DiskMigrationStep()

### DiskMigrationStep(DiskMigrationStep)
    
    
    public DiskMigrationStep(DiskMigrationStep other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DiskMigrationStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep)`  
  
  
## Properties 

### CopyingSourceDiskSnapshot
    
    
    public CopyingSourceDiskSnapshotStep CopyingSourceDiskSnapshot { get; set; }

Copying source disk snapshot step.

**Property Value**  
---  
**Type** | **Description**  
`[CopyingSourceDiskSnapshotStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.CopyingSourceDiskSnapshotStep)` |   
  
### CreatingSourceDiskSnapshot
    
    
    public CreatingSourceDiskSnapshotStep CreatingSourceDiskSnapshot { get; set; }

Creating source disk snapshot step.

**Property Value**  
---  
**Type** | **Description**  
`[CreatingSourceDiskSnapshotStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.CreatingSourceDiskSnapshotStep)` |   
  
### EndTime
    
    
    public Timestamp EndTime { get; set; }

Output only. The time the step has ended.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ProvisioningTargetDisk
    
    
    public ProvisioningTargetDiskStep ProvisioningTargetDisk { get; set; }

Creating target disk step.

**Property Value**  
---  
**Type** | **Description**  
`[ProvisioningTargetDiskStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ProvisioningTargetDiskStep)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Output only. The time the step has started.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### StepCase
    
    
    public DiskMigrationStep.StepOneofCase StepCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DiskMigrationStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep)[StepOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.DiskMigrationStep.StepOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
