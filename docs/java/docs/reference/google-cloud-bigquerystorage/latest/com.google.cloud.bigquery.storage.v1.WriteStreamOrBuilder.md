---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStreamOrBuilder
title: Interface WriteStreamOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:06.558174+00:00
---

# Interface WriteStreamOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStreamOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WriteStreamOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface WriteStreamOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCommitTime()
    
    
    public abstract Timestamp getCommitTime()

Output only. Commit time of the stream. If a stream is of `COMMITTED` type, then it will have a commit_time same as `create_time`. If the stream is of `PENDING` type, empty commit_time means it is not committed.

`.google.protobuf.Timestamp commit_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The commitTime.  
  
### getCommitTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCommitTimeOrBuilder()

Output only. Commit time of the stream. If a stream is of `COMMITTED` type, then it will have a commit_time same as `create_time`. If the stream is of `PENDING` type, empty commit_time means it is not committed.

`.google.protobuf.Timestamp commit_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Create time of the stream. For the _default stream, this is the creation_time of the table.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Create time of the stream. For the _default stream, this is the creation_time of the table.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLocation()
    
    
    public abstract String getLocation()

Output only. The geographic location where the stream's dataset resides. See <https://cloud.google.com/bigquery/docs/locations> for supported locations.

`string location = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The location.  
  
### getLocationBytes()
    
    
    public abstract ByteString getLocationBytes()

Output only. The geographic location where the stream's dataset resides. See <https://cloud.google.com/bigquery/docs/locations> for supported locations.

`string location = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for location.  
  
### getName()
    
    
    public abstract String getName()

Output only. Name of the stream, in the form `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Name of the stream, in the form `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getTableSchema()
    
    
    public abstract TableSchema getTableSchema()

Output only. The schema of the destination table. It is only returned in `CreateWriteStream` response. Caller should generate data that's compatible with this schema to send in initial `AppendRowsRequest`. The table schema could go out of date during the life time of the stream.

` .google.cloud.bigquery.storage.v1.TableSchema table_schema = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TableSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableSchema)` | The tableSchema.  
  
### getTableSchemaOrBuilder()
    
    
    public abstract TableSchemaOrBuilder getTableSchemaOrBuilder()

Output only. The schema of the destination table. It is only returned in `CreateWriteStream` response. Caller should generate data that's compatible with this schema to send in initial `AppendRowsRequest`. The table schema could go out of date during the life time of the stream.

` .google.cloud.bigquery.storage.v1.TableSchema table_schema = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TableSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableSchemaOrBuilder)` |   
  
### getType()
    
    
    public abstract WriteStream.Type getType()

Immutable. Type of the stream.

` .google.cloud.bigquery.storage.v1.WriteStream.Type type = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WriteStream.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Immutable. Type of the stream.

` .google.cloud.bigquery.storage.v1.WriteStream.Type type = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getWriteMode()
    
    
    public abstract WriteStream.WriteMode getWriteMode()

Immutable. Mode of the stream.

` .google.cloud.bigquery.storage.v1.WriteStream.WriteMode write_mode = 7 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WriteStream.WriteMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream.WriteMode)` | The writeMode.  
  
### getWriteModeValue()
    
    
    public abstract int getWriteModeValue()

Immutable. Mode of the stream.

` .google.cloud.bigquery.storage.v1.WriteStream.WriteMode write_mode = 7 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for writeMode.  
  
### hasCommitTime()
    
    
    public abstract boolean hasCommitTime()

Output only. Commit time of the stream. If a stream is of `COMMITTED` type, then it will have a commit_time same as `create_time`. If the stream is of `PENDING` type, empty commit_time means it is not committed.

`.google.protobuf.Timestamp commit_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the commitTime field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Create time of the stream. For the _default stream, this is the creation_time of the table.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasTableSchema()
    
    
    public abstract boolean hasTableSchema()

Output only. The schema of the destination table. It is only returned in `CreateWriteStream` response. Caller should generate data that's compatible with this schema to send in initial `AppendRowsRequest`. The table schema could go out of date during the life time of the stream.

` .google.cloud.bigquery.storage.v1.TableSchema table_schema = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tableSchema field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
