---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession
title: Google BigQuery Storage v1 API - Class ReadSession (3.20.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:31.254432+00:00
---

# Google BigQuery Storage v1 API - Class ReadSession (3.20.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery Storage v1 API - Class ReadSession (3.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.20.0 (latest)  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class ReadSession : IMessage<ReadSession>, IEquatable<ReadSession>, IDeepCloneable<ReadSession>, IBufferMessage, IMessage

Reference documentation and code samples for the Google BigQuery Storage v1 API class ReadSession.

Information about the ReadSession.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReadSession

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1)

## Assembly

Google.Cloud.BigQuery.Storage.V1.dll

## Constructors 

### ReadSession()
    
    
    public ReadSession()

### ReadSession(ReadSession)
    
    
    public ReadSession(ReadSession other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession)`  
  
  
## Properties 

### ArrowSchema
    
    
    public ArrowSchema ArrowSchema { get; set; }

Output only. Arrow schema.

**Property Value**  
---  
**Type** | **Description**  
`[ArrowSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ArrowSchema)` |   
  
### AvroSchema
    
    
    public AvroSchema AvroSchema { get; set; }

Output only. Avro schema.

**Property Value**  
---  
**Type** | **Description**  
`[AvroSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.AvroSchema)` |   
  
### DataFormat
    
    
    public DataFormat DataFormat { get; set; }

Immutable. Data format of the output data. DATA_FORMAT_UNSPECIFIED not supported.

**Property Value**  
---  
**Type** | **Description**  
`[DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.DataFormat)` |   
  
### EstimatedRowCount
    
    
    public long EstimatedRowCount { get; set; }

Output only. An estimate on the number of rows present in this session's streams. This estimate is based on metadata from the table which might be incomplete or stale.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### EstimatedTotalBytesScanned
    
    
    public long EstimatedTotalBytesScanned { get; set; }

Output only. An estimate on the number of bytes this session will scan when all streams are completely consumed. This estimate is based on metadata from the table which might be incomplete or stale.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### EstimatedTotalPhysicalFileSize
    
    
    public long EstimatedTotalPhysicalFileSize { get; set; }

Output only. A pre-projected estimate of the total physical size of files (in bytes) that this session will scan when all streams are consumed. This estimate is independent of the selected columns and can be based on incomplete or stale metadata from the table. This field is only set for BigLake tables.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ExpireTime
    
    
    public Timestamp ExpireTime { get; set; }

Output only. Time at which the session becomes invalid. After this time, subsequent requests to read this Session will return errors. The expire_time is automatically assigned and currently cannot be specified or updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Unique identifier for the session, in the form `projects/{project_id}/locations/{location}/sessions/{session_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReadOptions
    
    
    public ReadSession.Types.TableReadOptions ReadOptions { get; set; }

Optional. Read options for this session (e.g. column selection, filters).

**Property Value**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.Types)[TableReadOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.Types.TableReadOptions)` |   
  
### ReadSessionName
    
    
    public ReadSessionName ReadSessionName { get; set; }

[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession#Google_Cloud_BigQuery_Storage_V1_ReadSession_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)` |   
  
### SchemaCase
    
    
    public ReadSession.SchemaOneofCase SchemaCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession)[SchemaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.SchemaOneofCase)` |   
  
### Streams
    
    
    public RepeatedField<ReadStream> Streams { get; }

Output only. A list of streams created with the session.

At least one stream is created with the session. In the future, larger request_stream_count values _may_ result in this list being unpopulated, in that case, the user will need to use a List method to get the streams instead, which is not yet available.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ReadStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadStream)` |   
  
### Table
    
    
    public string Table { get; set; }

Immutable. Table that this ReadSession is reading from, in the form `projects/{project_id}/datasets/{dataset_id}/tables/{table_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TableAsTableName
    
    
    public TableName TableAsTableName { get; set; }

[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.TableName)-typed view over the [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession#Google_Cloud_BigQuery_Storage_V1_ReadSession_Table) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.TableName)` |   
  
### TableModifiers
    
    
    public ReadSession.Types.TableModifiers TableModifiers { get; set; }

Optional. Any modifiers which are applied when reading from the specified table.

**Property Value**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.Types)[TableModifiers](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.Types.TableModifiers)` |   
  
### TraceId
    
    
    public string TraceId { get; set; }

Optional. ID set by client to annotate a session identity. This does not need to be strictly unique, but instead the same ID should be used to group logically connected sessions (e.g. All using the same ID for all sessions needed to complete a Spark SQL query is reasonable).

Maximum length is 256 bytes.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
