---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata
title: AlloyDB v1 API - Class OperationMetadata (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:03.373721+00:00
---

# AlloyDB v1 API - Class OperationMetadata (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1 API - Class OperationMetadata (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class OperationMetadata : IMessage<OperationMetadata>, IEquatable<OperationMetadata>, IDeepCloneable<OperationMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1 API class OperationMetadata.

Represents the metadata of the long-running operation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OperationMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1)

## Assembly

Google.Cloud.AlloyDb.V1.dll

## Constructors 

### OperationMetadata()
    
    
    public OperationMetadata()

### OperationMetadata(OperationMetadata)
    
    
    public OperationMetadata(OperationMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata)`  
  
  
## Properties 

### ApiVersion
    
    
    public string ApiVersion { get; set; }

Output only. API version used to start the operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BatchCreateInstancesMetadata
    
    
    public BatchCreateInstancesMetadata BatchCreateInstancesMetadata { get; set; }

Output only. BatchCreateInstances related metadata.

**Property Value**  
---  
**Type** | **Description**  
`[BatchCreateInstancesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.BatchCreateInstancesMetadata)` |   
  
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
  
### RequestSpecificCase
    
    
    public OperationMetadata.RequestSpecificOneofCase RequestSpecificCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata)[RequestSpecificOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.OperationMetadata.RequestSpecificOneofCase)` |   
  
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
  
### UpgradeClusterStatus
    
    
    public UpgradeClusterStatus UpgradeClusterStatus { get; set; }

Output only. UpgradeClusterStatus related metadata.

**Property Value**  
---  
**Type** | **Description**  
`[UpgradeClusterStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.UpgradeClusterStatus)` |   
  
### Verb
    
    
    public string Verb { get; set; }

Output only. Name of the verb executed by the operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
