---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSessionOrBuilder
title: Interface ReadSessionOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:04.489773+00:00
---

# Interface ReadSessionOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSessionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReadSessionOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface ReadSessionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArrowSchema()
    
    
    public abstract ArrowSchema getArrowSchema()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema)` | The arrowSchema.  
  
### getArrowSchemaOrBuilder()
    
    
    public abstract ArrowSchemaOrBuilder getArrowSchemaOrBuilder()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchemaOrBuilder)` |   
  
### getAvroSchema()
    
    
    public abstract AvroSchema getAvroSchema()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchema)` | The avroSchema.  
  
### getAvroSchemaOrBuilder()
    
    
    public abstract AvroSchemaOrBuilder getAvroSchemaOrBuilder()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchemaOrBuilder)` |   
  
### getDataFormat()
    
    
    public abstract DataFormat getDataFormat()

Immutable. Data format of the output data. DATA_FORMAT_UNSPECIFIED not supported.

` .google.cloud.bigquery.storage.v1.DataFormat data_format = 3 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[DataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.DataFormat)` | The dataFormat.  
  
### getDataFormatValue()
    
    
    public abstract int getDataFormatValue()

Immutable. Data format of the output data. DATA_FORMAT_UNSPECIFIED not supported.

` .google.cloud.bigquery.storage.v1.DataFormat data_format = 3 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for dataFormat.  
  
### getEstimatedRowCount()
    
    
    public abstract long getEstimatedRowCount()

Output only. An estimate on the number of rows present in this session's streams. This estimate is based on metadata from the table which might be incomplete or stale.

`int64 estimated_row_count = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The estimatedRowCount.  
  
### getEstimatedTotalBytesScanned()
    
    
    public abstract long getEstimatedTotalBytesScanned()

Output only. An estimate on the number of bytes this session will scan when all streams are completely consumed. This estimate is based on metadata from the table which might be incomplete or stale.

`int64 estimated_total_bytes_scanned = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The estimatedTotalBytesScanned.  
  
### getEstimatedTotalPhysicalFileSize()
    
    
    public abstract long getEstimatedTotalPhysicalFileSize()

Output only. A pre-projected estimate of the total physical size of files (in bytes) that this session will scan when all streams are consumed. This estimate is independent of the selected columns and can be based on incomplete or stale metadata from the table. This field is only set for BigLake tables.

` int64 estimated_total_physical_file_size = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The estimatedTotalPhysicalFileSize.  
  
### getExpireTime()
    
    
    public abstract Timestamp getExpireTime()

Output only. Time at which the session becomes invalid. After this time, subsequent requests to read this Session will return errors. The expire_time is automatically assigned and currently cannot be specified or updated.

`.google.protobuf.Timestamp expire_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The expireTime.  
  
### getExpireTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getExpireTimeOrBuilder()

Output only. Time at which the session becomes invalid. After this time, subsequent requests to read this Session will return errors. The expire_time is automatically assigned and currently cannot be specified or updated.

`.google.protobuf.Timestamp expire_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. Unique identifier for the session, in the form `projects/{project_id}/locations/{location}/sessions/{session_id}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Unique identifier for the session, in the form `projects/{project_id}/locations/{location}/sessions/{session_id}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getReadOptions()
    
    
    public abstract ReadSession.TableReadOptions getReadOptions()

Optional. Read options for this session (e.g. column selection, filters).

` .google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions read_options = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadSession.TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions)` | The readOptions.  
  
### getReadOptionsOrBuilder()
    
    
    public abstract ReadSession.TableReadOptionsOrBuilder getReadOptionsOrBuilder()

Optional. Read options for this session (e.g. column selection, filters).

` .google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions read_options = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadSession.TableReadOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptionsOrBuilder)` |   
  
### getSchemaCase()
    
    
    public abstract ReadSession.SchemaCase getSchemaCase()

**Returns**  
---  
**Type** | **Description**  
`[ReadSession.SchemaCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.SchemaCase)` |   
  
### getStreams(int index)
    
    
    public abstract ReadStream getStreams(int index)

Output only. A list of streams created with the session.

At least one stream is created with the session. In the future, larger request_stream_count values _may_ result in this list being unpopulated, in that case, the user will need to use a List method to get the streams instead, which is not yet available.

` repeated .google.cloud.bigquery.storage.v1.ReadStream streams = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadStream)` |   
  
### getStreamsCount()
    
    
    public abstract int getStreamsCount()

Output only. A list of streams created with the session.

At least one stream is created with the session. In the future, larger request_stream_count values _may_ result in this list being unpopulated, in that case, the user will need to use a List method to get the streams instead, which is not yet available.

` repeated .google.cloud.bigquery.storage.v1.ReadStream streams = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStreamsList()
    
    
    public abstract List<ReadStream> getStreamsList()

Output only. A list of streams created with the session.

At least one stream is created with the session. In the future, larger request_stream_count values _may_ result in this list being unpopulated, in that case, the user will need to use a List method to get the streams instead, which is not yet available.

` repeated .google.cloud.bigquery.storage.v1.ReadStream streams = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ReadStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadStream)>` |   
  
### getStreamsOrBuilder(int index)
    
    
    public abstract ReadStreamOrBuilder getStreamsOrBuilder(int index)

Output only. A list of streams created with the session.

At least one stream is created with the session. In the future, larger request_stream_count values _may_ result in this list being unpopulated, in that case, the user will need to use a List method to get the streams instead, which is not yet available.

` repeated .google.cloud.bigquery.storage.v1.ReadStream streams = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadStreamOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadStreamOrBuilder)` |   
  
### getStreamsOrBuilderList()
    
    
    public abstract List<? extends ReadStreamOrBuilder> getStreamsOrBuilderList()

Output only. A list of streams created with the session.

At least one stream is created with the session. In the future, larger request_stream_count values _may_ result in this list being unpopulated, in that case, the user will need to use a List method to get the streams instead, which is not yet available.

` repeated .google.cloud.bigquery.storage.v1.ReadStream streams = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.storage.v1.ReadStreamOrBuilder>` |   
  
### getTable()
    
    
    public abstract String getTable()

Immutable. Table that this ReadSession is reading from, in the form `projects/{project_id}/datasets/{dataset_id}/tables/{table_id}`

` string table = 6 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The table.  
  
### getTableBytes()
    
    
    public abstract ByteString getTableBytes()

Immutable. Table that this ReadSession is reading from, in the form `projects/{project_id}/datasets/{dataset_id}/tables/{table_id}`

` string table = 6 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for table.  
  
### getTableModifiers()
    
    
    public abstract ReadSession.TableModifiers getTableModifiers()

Optional. Any modifiers which are applied when reading from the specified table.

` .google.cloud.bigquery.storage.v1.ReadSession.TableModifiers table_modifiers = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadSession.TableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers)` | The tableModifiers.  
  
### getTableModifiersOrBuilder()
    
    
    public abstract ReadSession.TableModifiersOrBuilder getTableModifiersOrBuilder()

Optional. Any modifiers which are applied when reading from the specified table.

` .google.cloud.bigquery.storage.v1.ReadSession.TableModifiers table_modifiers = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadSession.TableModifiersOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiersOrBuilder)` |   
  
### getTraceId()
    
    
    public abstract String getTraceId()

Optional. ID set by client to annotate a session identity. This does not need to be strictly unique, but instead the same ID should be used to group logically connected sessions (e.g. All using the same ID for all sessions needed to complete a Spark SQL query is reasonable).

Maximum length is 256 bytes.

`string trace_id = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The traceId.  
  
### getTraceIdBytes()
    
    
    public abstract ByteString getTraceIdBytes()

Optional. ID set by client to annotate a session identity. This does not need to be strictly unique, but instead the same ID should be used to group logically connected sessions (e.g. All using the same ID for all sessions needed to complete a Spark SQL query is reasonable).

Maximum length is 256 bytes.

`string trace_id = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for traceId.  
  
### hasArrowSchema()
    
    
    public abstract boolean hasArrowSchema()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowSchema field is set.  
  
### hasAvroSchema()
    
    
    public abstract boolean hasAvroSchema()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avroSchema field is set.  
  
### hasExpireTime()
    
    
    public abstract boolean hasExpireTime()

Output only. Time at which the session becomes invalid. After this time, subsequent requests to read this Session will return errors. The expire_time is automatically assigned and currently cannot be specified or updated.

`.google.protobuf.Timestamp expire_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expireTime field is set.  
  
### hasReadOptions()
    
    
    public abstract boolean hasReadOptions()

Optional. Read options for this session (e.g. column selection, filters).

` .google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions read_options = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readOptions field is set.  
  
### hasTableModifiers()
    
    
    public abstract boolean hasTableModifiers()

Optional. Any modifiers which are applied when reading from the specified table.

` .google.cloud.bigquery.storage.v1.ReadSession.TableModifiers table_modifiers = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tableModifiers field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
