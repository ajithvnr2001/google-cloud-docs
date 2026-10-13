---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponseOrBuilder
title: Interface ReadRowsResponseOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:03.807637+00:00
---

# Interface ReadRowsResponseOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReadRowsResponseOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface ReadRowsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArrowRecordBatch()
    
    
    public abstract ArrowRecordBatch getArrowRecordBatch()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch)` | The arrowRecordBatch.  
  
### getArrowRecordBatchOrBuilder()
    
    
    public abstract ArrowRecordBatchOrBuilder getArrowRecordBatchOrBuilder()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowRecordBatchOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatchOrBuilder)` |   
  
### getArrowSchema()
    
    
    public abstract ArrowSchema getArrowSchema()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema)` | The arrowSchema.  
  
### getArrowSchemaOrBuilder()
    
    
    public abstract ArrowSchemaOrBuilder getArrowSchemaOrBuilder()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchemaOrBuilder)` |   
  
### getAvroRows()
    
    
    public abstract AvroRows getAvroRows()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AvroRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows)` | The avroRows.  
  
### getAvroRowsOrBuilder()
    
    
    public abstract AvroRowsOrBuilder getAvroRowsOrBuilder()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AvroRowsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRowsOrBuilder)` |   
  
### getAvroSchema()
    
    
    public abstract AvroSchema getAvroSchema()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchema)` | The avroSchema.  
  
### getAvroSchemaOrBuilder()
    
    
    public abstract AvroSchemaOrBuilder getAvroSchemaOrBuilder()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchemaOrBuilder)` |   
  
### getRowCount()
    
    
    public abstract long getRowCount()

Number of serialized rows in the rows block.

`int64 row_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The rowCount.  
  
### getRowsCase()
    
    
    public abstract ReadRowsResponse.RowsCase getRowsCase()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.RowsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.RowsCase)` |   
  
### getSchemaCase()
    
    
    public abstract ReadRowsResponse.SchemaCase getSchemaCase()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.SchemaCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.SchemaCase)` |   
  
### getStats()
    
    
    public abstract StreamStats getStats()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StreamStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStats)` | The stats.  
  
### getStatsOrBuilder()
    
    
    public abstract StreamStatsOrBuilder getStatsOrBuilder()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StreamStatsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStatsOrBuilder)` |   
  
### getThrottleState()
    
    
    public abstract ThrottleState getThrottleState()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ThrottleState](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleState)` | The throttleState.  
  
### getThrottleStateOrBuilder()
    
    
    public abstract ThrottleStateOrBuilder getThrottleStateOrBuilder()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ThrottleStateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleStateOrBuilder)` |   
  
### getTotalEstimatedRowCount()
    
    
    public abstract long getTotalEstimatedRowCount()

Output only. The total estimated number of rows in the query results. Only populated when reading data from a BigQuery job.

This feature is not yet available.

` optional int64 total_estimated_row_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalEstimatedRowCount.  
  
### getUncompressedByteSize()
    
    
    public abstract long getUncompressedByteSize()

Optional. If the row data in this ReadRowsResponse is compressed, then uncompressed byte size is the original size of the uncompressed row data. If it is set to a value greater than 0, then decompress into a buffer of size uncompressed_byte_size using the compression codec that was requested during session creation time and which is specified in TableReadOptions.response_compression_codec in ReadSession. This value is not set if no response_compression_codec was not requested and it is -1 if the requested compression would not have reduced the size of this ReadRowsResponse's row data. This attempts to match Apache Arrow's behavior described here <https://github.com/apache/arrow/issues/15102> where the uncompressed length may be set to -1 to indicate that the data that follows is not compressed, which can be useful for cases where compression does not yield appreciable savings. When uncompressed_byte_size is not greater than 0, the client should skip decompression.

`optional int64 uncompressed_byte_size = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The uncompressedByteSize.  
  
### hasArrowRecordBatch()
    
    
    public abstract boolean hasArrowRecordBatch()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowRecordBatch field is set.  
  
### hasArrowSchema()
    
    
    public abstract boolean hasArrowSchema()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowSchema field is set.  
  
### hasAvroRows()
    
    
    public abstract boolean hasAvroRows()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avroRows field is set.  
  
### hasAvroSchema()
    
    
    public abstract boolean hasAvroSchema()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avroSchema field is set.  
  
### hasStats()
    
    
    public abstract boolean hasStats()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stats field is set.  
  
### hasThrottleState()
    
    
    public abstract boolean hasThrottleState()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the throttleState field is set.  
  
### hasTotalEstimatedRowCount()
    
    
    public abstract boolean hasTotalEstimatedRowCount()

Output only. The total estimated number of rows in the query results. Only populated when reading data from a BigQuery job.

This feature is not yet available.

` optional int64 total_estimated_row_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the totalEstimatedRowCount field is set.  
  
### hasUncompressedByteSize()
    
    
    public abstract boolean hasUncompressedByteSize()

Optional. If the row data in this ReadRowsResponse is compressed, then uncompressed byte size is the original size of the uncompressed row data. If it is set to a value greater than 0, then decompress into a buffer of size uncompressed_byte_size using the compression codec that was requested during session creation time and which is specified in TableReadOptions.response_compression_codec in ReadSession. This value is not set if no response_compression_codec was not requested and it is -1 if the requested compression would not have reduced the size of this ReadRowsResponse's row data. This attempts to match Apache Arrow's behavior described here <https://github.com/apache/arrow/issues/15102> where the uncompressed length may be set to -1 to indicate that the data that follows is not compressed, which can be useful for cases where compression does not yield appreciable savings. When uncompressed_byte_size is not greater than 0, the client should skip decompression.

`optional int64 uncompressed_byte_size = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the uncompressedByteSize field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
