---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.ObjectConditions
title: Storage Transfer v1 API - Class ObjectConditions (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:26.432337+00:00
---

# Storage Transfer v1 API - Class ObjectConditions (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.ObjectConditions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Storage Transfer v1 API - Class ObjectConditions (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.9.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.8.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.7.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.6.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.5.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.4.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.3.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.2.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.1.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.0.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/1.2.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/1.1.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/1.0.0/Google.Cloud.StorageTransfer.V1.ObjectConditions)


    
    
    public sealed class ObjectConditions : IMessage<ObjectConditions>, IEquatable<ObjectConditions>, IDeepCloneable<ObjectConditions>, IBufferMessage, IMessage

Reference documentation and code samples for the Storage Transfer v1 API class ObjectConditions.

Conditions that determine which objects are transferred. Applies only to Cloud Data Sources such as S3, Azure, and Cloud Storage.

The "last modification time" refers to the time of the last change to the object's content or metadata — specifically, this is the `updated` property of Cloud Storage objects, the `LastModified` field of S3 objects, and the `Last-Modified` header of Azure blobs.

For S3 objects, the `LastModified` value is the time the object begins uploading. If the object meets your "last modification time" criteria, but has not finished uploading, the object is not transferred. See [Transfer from Amazon S3 to Cloud Storage](https://cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#transfer_options) for more information.

Transfers with a [PosixFilesystem][google.storagetransfer.v1.PosixFilesystem] source or destination don't support `ObjectConditions`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ObjectConditions

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ObjectConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.ObjectConditions), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ObjectConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.ObjectConditions), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ObjectConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.ObjectConditions), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.StorageTransfer.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1)

## Assembly

Google.Cloud.StorageTransfer.V1.dll

## Constructors 

### ObjectConditions()
    
    
    public ObjectConditions()

### ObjectConditions(ObjectConditions)
    
    
    public ObjectConditions(ObjectConditions other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ObjectConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.ObjectConditions)`  
  
  
## Properties 

### ExcludePrefixes
    
    
    public RepeatedField<string> ExcludePrefixes { get; }

If you specify `exclude_prefixes`, Storage Transfer Service uses the items in the `exclude_prefixes` array to determine which objects to exclude from a transfer. Objects must not start with one of the matching `exclude_prefixes` for inclusion in a transfer.

The following are requirements of `exclude_prefixes`:

  * Each exclude-prefix can contain any sequence of Unicode characters, to a max length of 1024 bytes when UTF8-encoded, and must not contain Carriage Return or Line Feed characters. Wildcard matching and regular expression matching are not supported.

  * Each exclude-prefix must omit the leading slash. For example, to exclude the object `s3://my-aws-bucket/logs/y=2015/requests.gz`, specify the exclude-prefix as `logs/y=2015/requests.gz`.

  * None of the exclude-prefix values can be empty, if specified.

  * Each exclude-prefix must exclude a distinct portion of the object namespace. No exclude-prefix may be a prefix of another exclude-prefix.

  * If [include_prefixes][google.storagetransfer.v1.ObjectConditions.include_prefixes] is specified, then each exclude-prefix must start with the value of a path explicitly included by `include_prefixes`.




The max size of `exclude_prefixes` is 1000.

For more information, see [Filtering objects from transfers](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IncludePrefixes
    
    
    public RepeatedField<string> IncludePrefixes { get; }

If you specify `include_prefixes`, Storage Transfer Service uses the items in the `include_prefixes` array to determine which objects to include in a transfer. Objects must start with one of the matching `include_prefixes` for inclusion in the transfer. If [exclude_prefixes][google.storagetransfer.v1.ObjectConditions.exclude_prefixes] is specified, objects must not start with any of the `exclude_prefixes` specified for inclusion in the transfer.

The following are requirements of `include_prefixes`:

  * Each include-prefix can contain any sequence of Unicode characters, to a max length of 1024 bytes when UTF8-encoded, and must not contain Carriage Return or Line Feed characters. Wildcard matching and regular expression matching are not supported.

  * Each include-prefix must omit the leading slash. For example, to include the object `s3://my-aws-bucket/logs/y=2015/requests.gz`, specify the include-prefix as `logs/y=2015/requests.gz`.

  * None of the include-prefix values can be empty, if specified.

  * Each include-prefix must include a distinct portion of the object namespace. No include-prefix may be a prefix of another include-prefix.




The max size of `include_prefixes` is 1000.

For more information, see [Filtering objects from transfers](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LastModifiedBefore
    
    
    public Timestamp LastModifiedBefore { get; set; }

If specified, only objects with a "last modification time" before this timestamp and objects that don't have a "last modification time" are transferred.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### LastModifiedSince
    
    
    public Timestamp LastModifiedSince { get; set; }

If specified, only objects with a "last modification time" on or after this timestamp and objects that don't have a "last modification time" are transferred.

The `last_modified_since` and `last_modified_before` fields can be used together for chunked data processing. For example, consider a script that processes each day's worth of data at a time. For that you'd set each of the fields as follows:

  * `last_modified_since` to the start of the day

  * `last_modified_before` to the end of the day




**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### MaxTimeElapsedSinceLastModification
    
    
    public Duration MaxTimeElapsedSinceLastModification { get; set; }

Ensures that objects are not transferred if a specific maximum time has elapsed since the "last modification time". When a [TransferOperation][google.storagetransfer.v1.TransferOperation] begins, objects with a "last modification time" are transferred only if the elapsed time between the [start_time][google.storagetransfer.v1.TransferOperation.start_time] of the `TransferOperation`and the "last modification time" of the object is less than the value of max_time_elapsed_since_last_modification`. Objects that do not have a "last modification time" are also transferred.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### MinTimeElapsedSinceLastModification
    
    
    public Duration MinTimeElapsedSinceLastModification { get; set; }

Ensures that objects are not transferred until a specific minimum time has elapsed after the "last modification time". When a [TransferOperation][google.storagetransfer.v1.TransferOperation] begins, objects with a "last modification time" are transferred only if the elapsed time between the [start_time][google.storagetransfer.v1.TransferOperation.start_time] of the `TransferOperation` and the "last modification time" of the object is equal to or greater than the value of min_time_elapsed_since_last_modification`. Objects that do not have a "last modification time" are also transferred.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
