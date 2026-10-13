---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptionsOrBuilder
title: Interface ReadSession.TableReadOptionsOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:04.145491+00:00
---

# Interface ReadSession.TableReadOptionsOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReadSession.TableReadOptionsOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static interface ReadSession.TableReadOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArrowSerializationOptions()
    
    
    public abstract ArrowSerializationOptions getArrowSerializationOptions()

Optional. Options specific to the Apache Arrow output format.

` .google.cloud.bigquery.storage.v1.ArrowSerializationOptions arrow_serialization_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSerializationOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSerializationOptions)` | The arrowSerializationOptions.  
  
### getArrowSerializationOptionsOrBuilder()
    
    
    public abstract ArrowSerializationOptionsOrBuilder getArrowSerializationOptionsOrBuilder()

Optional. Options specific to the Apache Arrow output format.

` .google.cloud.bigquery.storage.v1.ArrowSerializationOptions arrow_serialization_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSerializationOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSerializationOptionsOrBuilder)` |   
  
### getAvroSerializationOptions()
    
    
    public abstract AvroSerializationOptions getAvroSerializationOptions()

Optional. Options specific to the Apache Avro output format

` .google.cloud.bigquery.storage.v1.AvroSerializationOptions avro_serialization_options = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSerializationOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSerializationOptions)` | The avroSerializationOptions.  
  
### getAvroSerializationOptionsOrBuilder()
    
    
    public abstract AvroSerializationOptionsOrBuilder getAvroSerializationOptionsOrBuilder()

Optional. Options specific to the Apache Avro output format

` .google.cloud.bigquery.storage.v1.AvroSerializationOptions avro_serialization_options = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSerializationOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSerializationOptionsOrBuilder)` |   
  
### getOutputFormatSerializationOptionsCase()
    
    
    public abstract ReadSession.TableReadOptions.OutputFormatSerializationOptionsCase getOutputFormatSerializationOptionsCase()

**Returns**  
---  
**Type** | **Description**  
`[ReadSession.TableReadOptions.OutputFormatSerializationOptionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.OutputFormatSerializationOptionsCase)` |   
  
### getResponseCompressionCodec()
    
    
    public abstract ReadSession.TableReadOptions.ResponseCompressionCodec getResponseCompressionCodec()

Optional. Set response_compression_codec when creating a read session to enable application-level compression of ReadRows responses.

` optional .google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.ResponseCompressionCodec response_compression_codec = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadSession.TableReadOptions.ResponseCompressionCodec](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.ResponseCompressionCodec)` | The responseCompressionCodec.  
  
### getResponseCompressionCodecValue()
    
    
    public abstract int getResponseCompressionCodecValue()

Optional. Set response_compression_codec when creating a read session to enable application-level compression of ReadRows responses.

` optional .google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.ResponseCompressionCodec response_compression_codec = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for responseCompressionCodec.  
  
### getRowRestriction()
    
    
    public abstract String getRowRestriction()

SQL text filtering statement, similar to a WHERE clause in a query. Aggregates are not supported.

Examples: "int_field > 5" "date_field = CAST('2014-9-27' as DATE)" "nullable_field is not NULL" "st_equals(geo_field, st_geofromtext("POINT(2, 2)"))" "numeric_field BETWEEN 1.0 AND 5.0"

Restricted to a maximum length for 1 MB.

`string row_restriction = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The rowRestriction.  
  
### getRowRestrictionBytes()
    
    
    public abstract ByteString getRowRestrictionBytes()

SQL text filtering statement, similar to a WHERE clause in a query. Aggregates are not supported.

Examples: "int_field > 5" "date_field = CAST('2014-9-27' as DATE)" "nullable_field is not NULL" "st_equals(geo_field, st_geofromtext("POINT(2, 2)"))" "numeric_field BETWEEN 1.0 AND 5.0"

Restricted to a maximum length for 1 MB.

`string row_restriction = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for rowRestriction.  
  
### getSamplePercentage()
    
    
    public abstract double getSamplePercentage()

Optional. Specifies a table sampling percentage. Specifically, the query planner will use TABLESAMPLE SYSTEM (sample_percentage PERCENT). The sampling percentage is applied at the data block granularity. It will randomly choose for each data block whether to read the rows in that data block. For more details, see <https://cloud.google.com/bigquery/docs/table-sampling>)

`optional double sample_percentage = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The samplePercentage.  
  
### getSelectedFields(int index)
    
    
    public abstract String getSelectedFields(int index)

Optional. The names of the fields in the table to be returned. If no field names are specified, then all fields in the table are returned.

Nested fields -- the child elements of a STRUCT field -- can be selected individually using their fully-qualified names, and will be returned as record fields containing only the selected nested fields. If a STRUCT field is specified in the selected fields list, all of the child elements will be returned.

As an example, consider a table with the following schema:

{ "name": "struct_field", "type": "RECORD", "mode": "NULLABLE", "fields": [ { "name": "string_field1", "type": "STRING", . "mode": "NULLABLE" }, { "name": "string_field2", "type": "STRING", "mode": "NULLABLE" } ] }

Specifying "struct_field" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 string_field2 }

Specifying "struct_field.string_field1" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 }

The order of the fields in the read session schema is derived from the table schema and does not correspond to the order in which the fields are specified in this list.

`repeated string selected_fields = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selectedFields at the given index.  
  
### getSelectedFieldsBytes(int index)
    
    
    public abstract ByteString getSelectedFieldsBytes(int index)

Optional. The names of the fields in the table to be returned. If no field names are specified, then all fields in the table are returned.

Nested fields -- the child elements of a STRUCT field -- can be selected individually using their fully-qualified names, and will be returned as record fields containing only the selected nested fields. If a STRUCT field is specified in the selected fields list, all of the child elements will be returned.

As an example, consider a table with the following schema:

{ "name": "struct_field", "type": "RECORD", "mode": "NULLABLE", "fields": [ { "name": "string_field1", "type": "STRING", . "mode": "NULLABLE" }, { "name": "string_field2", "type": "STRING", "mode": "NULLABLE" } ] }

Specifying "struct_field" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 string_field2 }

Specifying "struct_field.string_field1" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 }

The order of the fields in the read session schema is derived from the table schema and does not correspond to the order in which the fields are specified in this list.

`repeated string selected_fields = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the selectedFields at the given index.  
  
### getSelectedFieldsCount()
    
    
    public abstract int getSelectedFieldsCount()

Optional. The names of the fields in the table to be returned. If no field names are specified, then all fields in the table are returned.

Nested fields -- the child elements of a STRUCT field -- can be selected individually using their fully-qualified names, and will be returned as record fields containing only the selected nested fields. If a STRUCT field is specified in the selected fields list, all of the child elements will be returned.

As an example, consider a table with the following schema:

{ "name": "struct_field", "type": "RECORD", "mode": "NULLABLE", "fields": [ { "name": "string_field1", "type": "STRING", . "mode": "NULLABLE" }, { "name": "string_field2", "type": "STRING", "mode": "NULLABLE" } ] }

Specifying "struct_field" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 string_field2 }

Specifying "struct_field.string_field1" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 }

The order of the fields in the read session schema is derived from the table schema and does not correspond to the order in which the fields are specified in this list.

`repeated string selected_fields = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of selectedFields.  
  
### getSelectedFieldsList()
    
    
    public abstract List<String> getSelectedFieldsList()

Optional. The names of the fields in the table to be returned. If no field names are specified, then all fields in the table are returned.

Nested fields -- the child elements of a STRUCT field -- can be selected individually using their fully-qualified names, and will be returned as record fields containing only the selected nested fields. If a STRUCT field is specified in the selected fields list, all of the child elements will be returned.

As an example, consider a table with the following schema:

{ "name": "struct_field", "type": "RECORD", "mode": "NULLABLE", "fields": [ { "name": "string_field1", "type": "STRING", . "mode": "NULLABLE" }, { "name": "string_field2", "type": "STRING", "mode": "NULLABLE" } ] }

Specifying "struct_field" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 string_field2 }

Specifying "struct_field.string_field1" in the selected fields list will result in a read session schema with the following logical structure:

struct_field { string_field1 }

The order of the fields in the read session schema is derived from the table schema and does not correspond to the order in which the fields are specified in this list.

`repeated string selected_fields = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the selectedFields.  
  
### hasArrowSerializationOptions()
    
    
    public abstract boolean hasArrowSerializationOptions()

Optional. Options specific to the Apache Arrow output format.

` .google.cloud.bigquery.storage.v1.ArrowSerializationOptions arrow_serialization_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowSerializationOptions field is set.  
  
### hasAvroSerializationOptions()
    
    
    public abstract boolean hasAvroSerializationOptions()

Optional. Options specific to the Apache Avro output format

` .google.cloud.bigquery.storage.v1.AvroSerializationOptions avro_serialization_options = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avroSerializationOptions field is set.  
  
### hasResponseCompressionCodec()
    
    
    public abstract boolean hasResponseCompressionCodec()

Optional. Set response_compression_codec when creating a read session to enable application-level compression of ReadRows responses.

` optional .google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.ResponseCompressionCodec response_compression_codec = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the responseCompressionCodec field is set.  
  
### hasSamplePercentage()
    
    
    public abstract boolean hasSamplePercentage()

Optional. Specifies a table sampling percentage. Specifically, the query planner will use TABLESAMPLE SYSTEM (sample_percentage PERCENT). The sampling percentage is applied at the data block granularity. It will randomly choose for each data block whether to read the rows in that data block. For more details, see <https://cloud.google.com/bigquery/docs/table-sampling>)

`optional double sample_percentage = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the samplePercentage field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
