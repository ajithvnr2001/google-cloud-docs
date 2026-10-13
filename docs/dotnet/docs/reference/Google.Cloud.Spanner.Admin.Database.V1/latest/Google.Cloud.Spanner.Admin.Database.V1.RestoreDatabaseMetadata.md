---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata
title: Google Cloud Spanner Database Administration v1 API - Class RestoreDatabaseMetadata (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:04.602477+00:00
---

# Google Cloud Spanner Database Administration v1 API - Class RestoreDatabaseMetadata (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Database Administration v1 API - Class RestoreDatabaseMetadata (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class RestoreDatabaseMetadata : IMessage<RestoreDatabaseMetadata>, IEquatable<RestoreDatabaseMetadata>, IDeepCloneable<RestoreDatabaseMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner Database Administration v1 API class RestoreDatabaseMetadata.

Metadata type for the long-running operation returned by [RestoreDatabase][google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RestoreDatabaseMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RestoreDatabaseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RestoreDatabaseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RestoreDatabaseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1)

## Assembly

Google.Cloud.Spanner.Admin.Database.V1.dll

## Constructors 

### RestoreDatabaseMetadata()
    
    
    public RestoreDatabaseMetadata()

### RestoreDatabaseMetadata(RestoreDatabaseMetadata)
    
    
    public RestoreDatabaseMetadata(RestoreDatabaseMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RestoreDatabaseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata)`  
  
  
## Properties 

### BackupInfo
    
    
    public BackupInfo BackupInfo { get; set; }

Information about the backup used to restore the database.

**Property Value**  
---  
**Type** | **Description**  
`[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo)` |   
  
### CancelTime
    
    
    public Timestamp CancelTime { get; set; }

The time at which cancellation of this operation was received. [Operations.CancelOperation][google.longrunning.Operations.CancelOperation] starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use [Operations.GetOperation][google.longrunning.Operations.GetOperation] or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error][google.longrunning.Operation.error] value with a [google.rpc.Status.code][google.rpc.Status.code] of 1, corresponding to `Code.CANCELLED`.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DatabaseName
    
    
    public DatabaseName DatabaseName { get; set; }

Google.Cloud.Spanner.Common.V1.DatabaseName-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata#Google_Cloud_Spanner_Admin_Database_V1_RestoreDatabaseMetadata_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`Google.Cloud.Spanner.Common.V1.DatabaseName` |   
  
### Name
    
    
    public string Name { get; set; }

Name of the database being created and restored to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OptimizeDatabaseOperationName
    
    
    public string OptimizeDatabaseOperationName { get; set; }

If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored database, and remove the dependency on the restore source. The name is of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>` where the <database> is the name of database being created and restored to. The metadata type of the long-running operation is [OptimizeRestoredDatabaseMetadata][google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata]. This long-running operation will be automatically created by the system after the RestoreDatabase long-running operation completes successfully. This operation will not be created if the restore was not successful.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Progress
    
    
    public OperationProgress Progress { get; set; }

The progress of the [RestoreDatabase][google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase] operation.

**Property Value**  
---  
**Type** | **Description**  
`[OperationProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OperationProgress)` |   
  
### SourceInfoCase
    
    
    public RestoreDatabaseMetadata.SourceInfoOneofCase SourceInfoCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RestoreDatabaseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata)[SourceInfoOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseMetadata.SourceInfoOneofCase)` |   
  
### SourceType
    
    
    public RestoreSourceType SourceType { get; set; }

The type of the restore source.

**Property Value**  
---  
**Type** | **Description**  
`[RestoreSourceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreSourceType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
