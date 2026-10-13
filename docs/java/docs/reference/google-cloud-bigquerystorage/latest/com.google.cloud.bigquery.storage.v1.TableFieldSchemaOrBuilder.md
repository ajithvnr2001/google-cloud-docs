---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchemaOrBuilder
title: Interface TableFieldSchemaOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:06.224835+00:00
---

# Interface TableFieldSchemaOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchemaOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TableFieldSchemaOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface TableFieldSchemaOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDefaultValueExpression()
    
    
    public abstract String getDefaultValueExpression()

Optional. A SQL expression to specify the [default value](https://cloud.google.com/bigquery/docs/default-values) for this field.

`string default_value_expression = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The defaultValueExpression.  
  
### getDefaultValueExpressionBytes()
    
    
    public abstract ByteString getDefaultValueExpressionBytes()

Optional. A SQL expression to specify the [default value](https://cloud.google.com/bigquery/docs/default-values) for this field.

`string default_value_expression = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for defaultValueExpression.  
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. The field description. The maximum length is 1,024 characters.

`string description = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. The field description. The maximum length is 1,024 characters.

`string description = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getFields(int index)
    
    
    public abstract TableFieldSchema getFields(int index)

Optional. Describes the nested schema fields if the type property is set to STRUCT.

` repeated .google.cloud.bigquery.storage.v1.TableFieldSchema fields = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema)` |   
  
### getFieldsCount()
    
    
    public abstract int getFieldsCount()

Optional. Describes the nested schema fields if the type property is set to STRUCT.

` repeated .google.cloud.bigquery.storage.v1.TableFieldSchema fields = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFieldsList()
    
    
    public abstract List<TableFieldSchema> getFieldsList()

Optional. Describes the nested schema fields if the type property is set to STRUCT.

` repeated .google.cloud.bigquery.storage.v1.TableFieldSchema fields = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TableFieldSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema)>` |   
  
### getFieldsOrBuilder(int index)
    
    
    public abstract TableFieldSchemaOrBuilder getFieldsOrBuilder(int index)

Optional. Describes the nested schema fields if the type property is set to STRUCT.

` repeated .google.cloud.bigquery.storage.v1.TableFieldSchema fields = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchemaOrBuilder)` |   
  
### getFieldsOrBuilderList()
    
    
    public abstract List<? extends TableFieldSchemaOrBuilder> getFieldsOrBuilderList()

Optional. Describes the nested schema fields if the type property is set to STRUCT.

` repeated .google.cloud.bigquery.storage.v1.TableFieldSchema fields = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.storage.v1.TableFieldSchemaOrBuilder>` |   
  
### getMaxLength()
    
    
    public abstract long getMaxLength()

Optional. Maximum length of values of this field for STRINGS or BYTES.

If max_length is not specified, no maximum length constraint is imposed on this field.

If type = "STRING", then max_length represents the maximum UTF-8 length of strings in this field.

If type = "BYTES", then max_length represents the maximum number of bytes in this field.

It is invalid to set this field if type is not "STRING" or "BYTES".

`int64 max_length = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxLength.  
  
### getMode()
    
    
    public abstract TableFieldSchema.Mode getMode()

Optional. The field mode. The default value is NULLABLE.

` .google.cloud.bigquery.storage.v1.TableFieldSchema.Mode mode = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema.Mode](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema.Mode)` | The mode.  
  
### getModeValue()
    
    
    public abstract int getModeValue()

Optional. The field mode. The default value is NULLABLE.

` .google.cloud.bigquery.storage.v1.TableFieldSchema.Mode mode = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for mode.  
  
### getName()
    
    
    public abstract String getName()

Required. The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPrecision()
    
    
    public abstract long getPrecision()

Optional. Precision (maximum number of total digits in base 10) and scale (maximum number of digits in the fractional part in base 10) constraints for values of this field for NUMERIC or BIGNUMERIC.

It is invalid to set precision or scale if type is not "NUMERIC" or "BIGNUMERIC".

If precision and scale are not specified, no value range constraint is imposed on this field insofar as values are permitted by the type.

Values of this NUMERIC or BIGNUMERIC field must be in this range when:

  * Precision (P) and scale (S) are specified: [-10^(P-S) + 10^(-S), 10^(P-S) - 10^(-S)]
  * Precision (P) is specified but not scale (and thus scale is interpreted to be equal to zero): [-10^P + 1, 10^P - 1].

Acceptable values for precision and scale if both are specified:

  * If type = "NUMERIC": 1 <= precision - scale <= 29 and 0 <= scale <= 9.

  * If type = "BIGNUMERIC": 1 <= precision - scale <= 38 and 0 <= scale <= 38.

Acceptable values for precision if only precision is specified but not scale (and thus scale is interpreted to be equal to zero):

  * If type = "NUMERIC": 1 <= precision <= 29.

  * If type = "BIGNUMERIC": 1 <= precision <= 38.

If scale is specified but not precision, then it is invalid.




`int64 precision = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The precision.  
  
### getRangeElementType()
    
    
    public abstract TableFieldSchema.FieldElementType getRangeElementType()

Optional. The subtype of the RANGE, if the type of this field is RANGE. If the type is RANGE, this field is required. Possible values for the field element type of a RANGE include:

  * DATE
  * DATETIME
  * TIMESTAMP



` .google.cloud.bigquery.storage.v1.TableFieldSchema.FieldElementType range_element_type = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema.FieldElementType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema.FieldElementType)` | The rangeElementType.  
  
### getRangeElementTypeOrBuilder()
    
    
    public abstract TableFieldSchema.FieldElementTypeOrBuilder getRangeElementTypeOrBuilder()

Optional. The subtype of the RANGE, if the type of this field is RANGE. If the type is RANGE, this field is required. Possible values for the field element type of a RANGE include:

  * DATE
  * DATETIME
  * TIMESTAMP



` .google.cloud.bigquery.storage.v1.TableFieldSchema.FieldElementType range_element_type = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema.FieldElementTypeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema.FieldElementTypeOrBuilder)` |   
  
### getScale()
    
    
    public abstract long getScale()

Optional. See documentation for precision.

`int64 scale = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The scale.  
  
### getTimestampPrecision()
    
    
    public abstract Int64Value getTimestampPrecision()

Optional. Precision (maximum number of total digits in base 10) for seconds of TIMESTAMP type.

Possible values include:

  * 6 (Default, for TIMESTAMP type with microsecond precision)
  * 12 (For TIMESTAMP type with picosecond precision)



` .google.protobuf.Int64Value timestamp_precision = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The timestampPrecision.  
  
### getTimestampPrecisionOrBuilder()
    
    
    public abstract Int64ValueOrBuilder getTimestampPrecisionOrBuilder()

Optional. Precision (maximum number of total digits in base 10) for seconds of TIMESTAMP type.

Possible values include:

  * 6 (Default, for TIMESTAMP type with microsecond precision)
  * 12 (For TIMESTAMP type with picosecond precision)



` .google.protobuf.Int64Value timestamp_precision = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getType()
    
    
    public abstract TableFieldSchema.Type getType()

Required. The field data type.

` .google.cloud.bigquery.storage.v1.TableFieldSchema.Type type = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Required. The field data type.

` .google.cloud.bigquery.storage.v1.TableFieldSchema.Type type = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasRangeElementType()
    
    
    public abstract boolean hasRangeElementType()

Optional. The subtype of the RANGE, if the type of this field is RANGE. If the type is RANGE, this field is required. Possible values for the field element type of a RANGE include:

  * DATE
  * DATETIME
  * TIMESTAMP



` .google.cloud.bigquery.storage.v1.TableFieldSchema.FieldElementType range_element_type = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rangeElementType field is set.  
  
### hasTimestampPrecision()
    
    
    public abstract boolean hasTimestampPrecision()

Optional. Precision (maximum number of total digits in base 10) for seconds of TIMESTAMP type.

Possible values include:

  * 6 (Default, for TIMESTAMP type with microsecond precision)
  * 12 (For TIMESTAMP type with picosecond precision)



` .google.protobuf.Int64Value timestamp_precision = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timestampPrecision field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
