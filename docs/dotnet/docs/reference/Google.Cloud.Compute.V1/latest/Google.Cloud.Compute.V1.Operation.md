---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation
title: Compute Engine v1 API - Class Operation (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:10.645374+00:00
---

# Compute Engine v1 API - Class Operation (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class Operation (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Operation : IMessage<Operation>, IEquatable<Operation>, IDeepCloneable<Operation>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class Operation.

Represents an Operation resource.

Google Compute Engine has three Operation resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations)



You can use an operation resource to manage asynchronous API requests. For more information, readHandling API responses.

Operations can be global, regional or zonal.

  * For global operations, use the `globalOperations` resource.
  * For regional operations, use the `regionOperations` resource.
  * For zonal operations, use the `zoneOperations` resource.



For more information, read Global, Regional, and Zonal Resources.

Note that completed Operation resources have a limited retention period.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Operation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### Operation()
    
    
    public Operation()

### Operation(Operation)
    
    
    public Operation(Operation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)`  
  
  
## Properties 

### ClientOperationId
    
    
    public string ClientOperationId { get; set; }

[Output Only] The value of `requestId` if you provided it in the request. Not present otherwise.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreationTimestamp
    
    
    public string CreationTimestamp { get; set; }

[Deprecated] This field is deprecated.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

[Output Only] A textual description of the operation, which is set when the operation is created.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EndTime
    
    
    public string EndTime { get; set; }

[Output Only] The time that this operation was completed. This value is inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Error
    
    
    public Error Error { get; set; }

[Output Only] If errors are generated during processing of the operation, this field will be populated.

**Property Value**  
---  
**Type** | **Description**  
`[Error](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Error)` |   
  
### GetHealthOperationMetadata
    
    
    public GetHealthOperationMetadata GetHealthOperationMetadata { get; set; }

Output only. Metadata for GetHealth operations.

**Property Value**  
---  
**Type** | **Description**  
`[GetHealthOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetHealthOperationMetadata)` |   
  
### GetVersionOperationMetadata
    
    
    public GetVersionOperationMetadata GetVersionOperationMetadata { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[GetVersionOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetVersionOperationMetadata)` |   
  
### HasClientOperationId
    
    
    public bool HasClientOperationId { get; }

Gets whether the "client_operation_id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCreationTimestamp
    
    
    public bool HasCreationTimestamp { get; }

Gets whether the "creation_timestamp" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDescription
    
    
    public bool HasDescription { get; }

Gets whether the "description" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEndTime
    
    
    public bool HasEndTime { get; }

Gets whether the "end_time" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasHttpErrorMessage
    
    
    public bool HasHttpErrorMessage { get; }

Gets whether the "http_error_message" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasHttpErrorStatusCode
    
    
    public bool HasHttpErrorStatusCode { get; }

Gets whether the "http_error_status_code" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasId
    
    
    public bool HasId { get; }

Gets whether the "id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInsertTime
    
    
    public bool HasInsertTime { get; }

Gets whether the "insert_time" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasKind
    
    
    public bool HasKind { get; }

Gets whether the "kind" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasName
    
    
    public bool HasName { get; }

Gets whether the "name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasOperationGroupId
    
    
    public bool HasOperationGroupId { get; }

Gets whether the "operation_group_id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasOperationType
    
    
    public bool HasOperationType { get; }

Gets whether the "operation_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasProgress
    
    
    public bool HasProgress { get; }

Gets whether the "progress" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRegion
    
    
    public bool HasRegion { get; }

Gets whether the "region" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSelfLink
    
    
    public bool HasSelfLink { get; }

Gets whether the "self_link" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStartTime
    
    
    public bool HasStartTime { get; }

Gets whether the "start_time" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStatus
    
    
    public bool HasStatus { get; }

Gets whether the "status" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStatusMessage
    
    
    public bool HasStatusMessage { get; }

Gets whether the "status_message" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTargetId
    
    
    public bool HasTargetId { get; }

Gets whether the "target_id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTargetLink
    
    
    public bool HasTargetLink { get; }

Gets whether the "target_link" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasUser
    
    
    public bool HasUser { get; }

Gets whether the "user" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasZone
    
    
    public bool HasZone { get; }

Gets whether the "zone" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HttpErrorMessage
    
    
    public string HttpErrorMessage { get; set; }

[Output Only] If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HttpErrorStatusCode
    
    
    public int HttpErrorStatusCode { get; set; }

[Output Only] If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Id
    
    
    public ulong Id { get; set; }

[Output Only] The unique identifier for the operation. This identifier is defined by the server.

**Property Value**  
---  
**Type** | **Description**  
`[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)` |   
  
### InsertTime
    
    
    public string InsertTime { get; set; }

[Output Only] The time that this operation was requested. This value is inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstancesBulkInsertOperationMetadata
    
    
    public InstancesBulkInsertOperationMetadata InstancesBulkInsertOperationMetadata { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[InstancesBulkInsertOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesBulkInsertOperationMetadata)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] Type of the resource. Always `compute#operation` for Operation resources.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

[Output Only] Name of the operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OperationGroupId
    
    
    public string OperationGroupId { get; set; }

Output only. [Output Only] An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OperationType
    
    
    public string OperationType { get; set; }

[Output Only] The type of operation, such as `insert`, `update`, or `delete`, and so on.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Progress
    
    
    public int Progress { get; set; }

[Output Only] An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Region
    
    
    public string Region { get; set; }

[Output Only] The URL of the region where the operation resides. Only applicable when performing regional operations.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SelfLink
    
    
    public string SelfLink { get; set; }

[Output Only] Server-defined URL for the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SetCommonInstanceMetadataOperationMetadata
    
    
    public SetCommonInstanceMetadataOperationMetadata SetCommonInstanceMetadataOperationMetadata { get; set; }

Output only. [Output Only] If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state.

**Property Value**  
---  
**Type** | **Description**  
`[SetCommonInstanceMetadataOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetCommonInstanceMetadataOperationMetadata)` |   
  
### StartTime
    
    
    public string StartTime { get; set; }

[Output Only] The time that this operation was started by the server. This value is inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Status
    
    
    public Operation.Types.Status Status { get; set; }

[Output Only] The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`.

**Property Value**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation.Types)[Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation.Types.Status)` |   
  
### StatusMessage
    
    
    public string StatusMessage { get; set; }

[Output Only] An optional textual description of the current status of the operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TargetId
    
    
    public ulong TargetId { get; set; }

[Output Only] The unique target ID, which identifies a specific incarnation of the target resource.

**Property Value**  
---  
**Type** | **Description**  
`[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)` |   
  
### TargetLink
    
    
    public string TargetLink { get; set; }

[Output Only] The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### User
    
    
    public string User { get; set; }

[Output Only] User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Warnings
    
    
    public RepeatedField<Warnings> Warnings { get; }

[Output Only] If warning messages are generated during processing of the operation, this field will be populated.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Warnings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Warnings)` |   
  
### Zone
    
    
    public string Zone { get; set; }

[Output Only] The URL of the zone where the operation resides. Only applicable when performing per-zone operations.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
