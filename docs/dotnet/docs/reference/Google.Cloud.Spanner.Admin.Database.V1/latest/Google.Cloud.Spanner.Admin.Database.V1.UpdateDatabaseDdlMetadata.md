---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseDdlMetadata
title: Google Cloud Spanner Database Administration v1 API - Class UpdateDatabaseDdlMetadata (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:40.167957+00:00
---

# Google Cloud Spanner Database Administration v1 API - Class UpdateDatabaseDdlMetadata (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseDdlMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Database Administration v1 API - Class UpdateDatabaseDdlMetadata (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class UpdateDatabaseDdlMetadata : IMessage<UpdateDatabaseDdlMetadata>, IEquatable<UpdateDatabaseDdlMetadata>, IDeepCloneable<UpdateDatabaseDdlMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner Database Administration v1 API class UpdateDatabaseDdlMetadata.

Metadata type for the operation returned by [UpdateDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateDatabaseDdlMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseDdlMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseDdlMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseDdlMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1)

## Assembly

Google.Cloud.Spanner.Admin.Database.V1.dll

## Constructors 

### UpdateDatabaseDdlMetadata()
    
    
    public UpdateDatabaseDdlMetadata()

### UpdateDatabaseDdlMetadata(UpdateDatabaseDdlMetadata)
    
    
    public UpdateDatabaseDdlMetadata(UpdateDatabaseDdlMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseDdlMetadata)`  
  
  
## Properties 

### Actions
    
    
    public RepeatedField<DdlStatementActionInfo> Actions { get; }

The brief action info for the DDL statements. `actions[i]` is the brief info for `statements[i]`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DdlStatementActionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DdlStatementActionInfo)` |   
  
### CommitTimestamps
    
    
    public RepeatedField<Timestamp> CommitTimestamps { get; }

Reports the commit timestamps of all statements that have succeeded so far, where `commit_timestamps[i]` is the commit timestamp for the statement `statements[i]`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Database
    
    
    public string Database { get; set; }

The database being modified.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DatabaseAsDatabaseName
    
    
    public DatabaseName DatabaseAsDatabaseName { get; set; }

Google.Cloud.Spanner.Common.V1.DatabaseName-typed view over the [Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.UpdateDatabaseDdlMetadata#Google_Cloud_Spanner_Admin_Database_V1_UpdateDatabaseDdlMetadata_Database) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`Google.Cloud.Spanner.Common.V1.DatabaseName` |   
  
### Progress
    
    
    public RepeatedField<OperationProgress> Progress { get; }

The progress of the [UpdateDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl] operations. All DDL statements will have continuously updating progress, and `progress[i]` is the operation progress for `statements[i]`. Also, `progress[i]` will have start time and end time populated with commit timestamp of operation, as well as a progress of 100% once the operation has completed.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[OperationProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.OperationProgress)` |   
  
### Statements
    
    
    public RepeatedField<string> Statements { get; }

For an update this list contains all the statements. For an individual statement, this list contains only that statement.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Throttled
    
    
    public bool Throttled { get; set; }

Output only. When true, indicates that the operation is throttled e.g. due to resource constraints. When resources become available the operation will resume and this field will be false again.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
