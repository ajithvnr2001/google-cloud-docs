---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus
title: AlloyDB v1beta API - Class BatchCreateInstanceStatus (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:09.415404+00:00
---

# AlloyDB v1beta API - Class BatchCreateInstanceStatus (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class BatchCreateInstanceStatus (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class BatchCreateInstanceStatus : IMessage<BatchCreateInstanceStatus>, IEquatable<BatchCreateInstanceStatus>, IDeepCloneable<BatchCreateInstanceStatus>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class BatchCreateInstanceStatus.

Message for current status of an instance in the BatchCreateInstances operation. For example, lets say a BatchCreateInstances workflow has 4 instances, Instance1 through Instance4. Lets also assume that 2 instances succeeded but the third failed to create and the 4th was never picked up for creation because of failure of the previous one. Then, resulting states would look something like:

  1. Instance1 = ROLLED_BACK
  2. Instance2 = ROLLED_BACK
  3. Instance3 = FAILED
  4. Instance4 = FAILED



However, while the operation is running, the instance might be in other states including PENDING_CREATE, ACTIVE, DELETING and CREATING. The states / do not get further updated once the operation is done.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchCreateInstanceStatus

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchCreateInstanceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchCreateInstanceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchCreateInstanceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### BatchCreateInstanceStatus()
    
    
    public BatchCreateInstanceStatus()

### BatchCreateInstanceStatus(BatchCreateInstanceStatus)
    
    
    public BatchCreateInstanceStatus(BatchCreateInstanceStatus other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchCreateInstanceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus)`  
  
  
## Properties 

### Error
    
    
    public Status Error { get; set; }

The RPC status of the instance creation operation. This field will be present if an error happened during the instance creation.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### ErrorMsg
    
    
    public string ErrorMsg { get; set; }

DEPRECATED - Use the error field instead. Error, if any error occurred and is available, during instance creation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public BatchCreateInstanceStatus.Types.State State { get; set; }

The current state of an instance involved in the batch create operation. Once the operation is complete, the final state of the instances in the LRO can be one of:

  1. ACTIVE, indicating that instances were created successfully
  2. FAILED, indicating that a particular instance failed creation
  3. ROLLED_BACK indicating that although the instance was created successfully, it had to be rolled back and deleted due to failure in other steps of the workflow.



**Property Value**  
---  
**Type** | **Description**  
`[BatchCreateInstanceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstanceStatus.Types.State)` |   
  
### Type
    
    
    public Instance.Types.InstanceType Type { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types)[InstanceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
