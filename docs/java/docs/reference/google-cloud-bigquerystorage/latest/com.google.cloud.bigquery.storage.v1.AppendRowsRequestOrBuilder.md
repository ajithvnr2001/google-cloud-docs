---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequestOrBuilder
title: Interface AppendRowsRequestOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:58.292262+00:00
---

# Interface AppendRowsRequestOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AppendRowsRequestOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface AppendRowsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsMissingValueInterpretations(String key)
    
    
    public abstract boolean containsMissingValueInterpretations(String key)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getArrowRows()
    
    
    public abstract AppendRowsRequest.ArrowData getArrowRows()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ArrowData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData)` | The arrowRows.  
  
### getArrowRowsOrBuilder()
    
    
    public abstract AppendRowsRequest.ArrowDataOrBuilder getArrowRowsOrBuilder()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ArrowDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowDataOrBuilder)` |   
  
### getClientStats()
    
    
    public abstract ClientStats getClientStats()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats)` | The clientStats.  
  
### getClientStatsOrBuilder()
    
    
    public abstract ClientStatsOrBuilder getClientStatsOrBuilder()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientStatsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStatsOrBuilder)` |   
  
### getDefaultMissingValueInterpretation()
    
    
    public abstract AppendRowsRequest.MissingValueInterpretation getDefaultMissingValueInterpretation()

Optional. Default missing value interpretation for all columns in the table. When a value is specified on an `AppendRowsRequest`, it is applied to all requests from that point forward, until a subsequent `AppendRowsRequest` sets it to a different value. `missing_value_interpretation` can override `default_missing_value_interpretation`. For example, if you want to write `NULL` instead of using default values for some columns, you can set `default_missing_value_interpretation` to `DEFAULT_VALUE` and at the same time, set `missing_value_interpretations` to `NULL_VALUE` on those columns.

` .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation default_missing_value_interpretation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)` | The defaultMissingValueInterpretation.  
  
### getDefaultMissingValueInterpretationValue()
    
    
    public abstract int getDefaultMissingValueInterpretationValue()

Optional. Default missing value interpretation for all columns in the table. When a value is specified on an `AppendRowsRequest`, it is applied to all requests from that point forward, until a subsequent `AppendRowsRequest` sets it to a different value. `missing_value_interpretation` can override `default_missing_value_interpretation`. For example, if you want to write `NULL` instead of using default values for some columns, you can set `default_missing_value_interpretation` to `DEFAULT_VALUE` and at the same time, set `missing_value_interpretations` to `NULL_VALUE` on those columns.

` .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation default_missing_value_interpretation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for defaultMissingValueInterpretation.  
  
### getMissingValueInterpretations() (deprecated)
    
    
    public abstract Map<String,AppendRowsRequest.MissingValueInterpretation> getMissingValueInterpretations()

Use [#getMissingValueInterpretationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequestOrBuilder#com_google_cloud_bigquery_storage_v1_AppendRowsRequestOrBuilder_getMissingValueInterpretationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>` |   
  
### getMissingValueInterpretationsCount()
    
    
    public abstract int getMissingValueInterpretationsCount()

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMissingValueInterpretationsMap()
    
    
    public abstract Map<String,AppendRowsRequest.MissingValueInterpretation> getMissingValueInterpretationsMap()

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>` |   
  
### getMissingValueInterpretationsOrDefault(String key, AppendRowsRequest.MissingValueInterpretation defaultValue)
    
    
    public abstract AppendRowsRequest.MissingValueInterpretation getMissingValueInterpretationsOrDefault(String key, AppendRowsRequest.MissingValueInterpretation defaultValue)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)` |   
  
### getMissingValueInterpretationsOrThrow(String key)
    
    
    public abstract AppendRowsRequest.MissingValueInterpretation getMissingValueInterpretationsOrThrow(String key)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)` |   
  
### getMissingValueInterpretationsValue() (deprecated)
    
    
    public abstract Map<String,Integer> getMissingValueInterpretationsValue()

Use [#getMissingValueInterpretationsValueMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequestOrBuilder#com_google_cloud_bigquery_storage_v1_AppendRowsRequestOrBuilder_getMissingValueInterpretationsValueMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>` |   
  
### getMissingValueInterpretationsValueMap()
    
    
    public abstract Map<String,Integer> getMissingValueInterpretationsValueMap()

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>` |   
  
### getMissingValueInterpretationsValueOrDefault(String key, int defaultValue)
    
    
    public abstract int getMissingValueInterpretationsValueOrDefault(String key, int defaultValue)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMissingValueInterpretationsValueOrThrow(String key)
    
    
    public abstract int getMissingValueInterpretationsValueOrThrow(String key)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOffset()
    
    
    public abstract Int64Value getOffset()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The offset.  
  
### getOffsetOrBuilder()
    
    
    public abstract Int64ValueOrBuilder getOffsetOrBuilder()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getProtoRows()
    
    
    public abstract AppendRowsRequest.ProtoData getProtoRows()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ProtoData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData)` | The protoRows.  
  
### getProtoRowsOrBuilder()
    
    
    public abstract AppendRowsRequest.ProtoDataOrBuilder getProtoRowsOrBuilder()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ProtoDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoDataOrBuilder)` |   
  
### getRowsCase()
    
    
    public abstract AppendRowsRequest.RowsCase getRowsCase()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.RowsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.RowsCase)` |   
  
### getTraceId()
    
    
    public abstract String getTraceId()

Id set by client to annotate its identity. Only initial request setting is respected.

`string trace_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The traceId.  
  
### getTraceIdBytes()
    
    
    public abstract ByteString getTraceIdBytes()

Id set by client to annotate its identity. Only initial request setting is respected.

`string trace_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for traceId.  
  
### getWriteStream()
    
    
    public abstract String getWriteStream()

Required. The write_stream identifies the append operation. It must be provided in the following scenarios:

  * In the first request to an AppendRows connection.

  * In all subsequent requests to an AppendRows connection, if you use the same connection to write to multiple tables or change the input schema for default streams.

For explicitly created write streams, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}`

For the special default stream, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/_default`.

An example of a possible sequence of requests with write_stream fields within a single connection:

  * r1: {write_stream: stream_name_1}

  * r2: {write_stream: /*omit*/}

  * r3: {write_stream: /*omit*/}

  * r4: {write_stream: stream_name_2}

  * r5: {write_stream: stream_name_2}

The destination changed in request_4, so the write_stream field must be populated in all subsequent requests in this stream.




` string write_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The writeStream.  
  
### getWriteStreamBytes()
    
    
    public abstract ByteString getWriteStreamBytes()

Required. The write_stream identifies the append operation. It must be provided in the following scenarios:

  * In the first request to an AppendRows connection.

  * In all subsequent requests to an AppendRows connection, if you use the same connection to write to multiple tables or change the input schema for default streams.

For explicitly created write streams, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}`

For the special default stream, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/_default`.

An example of a possible sequence of requests with write_stream fields within a single connection:

  * r1: {write_stream: stream_name_1}

  * r2: {write_stream: /*omit*/}

  * r3: {write_stream: /*omit*/}

  * r4: {write_stream: stream_name_2}

  * r5: {write_stream: stream_name_2}

The destination changed in request_4, so the write_stream field must be populated in all subsequent requests in this stream.




` string write_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for writeStream.  
  
### hasArrowRows()
    
    
    public abstract boolean hasArrowRows()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowRows field is set.  
  
### hasClientStats()
    
    
    public abstract boolean hasClientStats()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clientStats field is set.  
  
### hasOffset()
    
    
    public abstract boolean hasOffset()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the offset field is set.  
  
### hasProtoRows()
    
    
    public abstract boolean hasProtoRows()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the protoRows field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
