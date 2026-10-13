---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.OperationMetadata
title: Backup for GKE v1 API - Class OperationMetadata (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:21.309120+00:00
---

# Backup for GKE v1 API - Class OperationMetadata (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.OperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup for GKE v1 API - Class OperationMetadata (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.8.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.7.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.6.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.5.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.4.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.3.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.2.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.1.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.0.0/Google.Cloud.GkeBackup.V1.OperationMetadata)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/1.0.0-beta01/Google.Cloud.GkeBackup.V1.OperationMetadata)


    
    
    public sealed class OperationMetadata : IMessage<OperationMetadata>, IEquatable<OperationMetadata>, IDeepCloneable<OperationMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup for GKE v1 API class OperationMetadata.

Represents the metadata of the long-running operation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OperationMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.OperationMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.OperationMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.OperationMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeBackup.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1)

## Assembly

Google.Cloud.GkeBackup.V1.dll

## Constructors 

### OperationMetadata()
    
    
    public OperationMetadata()

### OperationMetadata(OperationMetadata)
    
    
    public OperationMetadata(OperationMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.OperationMetadata)`  
  
  
## Properties 

### ApiVersion
    
    
    public string ApiVersion { get; set; }

Output only. API version used to start the operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time the operation was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### EndTime
    
    
    public Timestamp EndTime { get; set; }

Output only. The time the operation finished running.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### RequestedCancellation
    
    
    public bool RequestedCancellation { get; set; }

Output only. Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have [google.longrunning.Operation.error][google.longrunning.Operation.error] value with a [google.rpc.Status.code][google.rpc.Status.code] of 1, corresponding to `Code.CANCELLED`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### StatusMessage
    
    
    public string StatusMessage { get; set; }

Output only. Human-readable status of the operation, if any.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Target
    
    
    public string Target { get; set; }

Output only. Server-defined resource path for the target of the operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Verb
    
    
    public string Verb { get; set; }

Output only. Name of the verb executed by the operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
