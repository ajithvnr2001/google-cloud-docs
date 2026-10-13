---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CollectionOrBuilder
title: Interface CollectionOrBuilder (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:32.747858+00:00
---

# Interface CollectionOrBuilder (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CollectionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CollectionOrBuilder (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface CollectionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels as key value pairs.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsVectorSchema(String key)
    
    
    public abstract boolean containsVectorSchema(String key)

Optional. Schema for vector fields. Only vector fields in this schema will be searchable. Field names must contain only alphanumeric characters, underscores, and hyphens.

` map<string, .google.cloud.vectorsearch.v1.VectorField> vector_schema = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. [Output only] Create time stamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. [Output only] Create time stamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDataSchema()
    
    
    public abstract Struct getDataSchema()

Optional. JSON Schema for data. Field names must contain only alphanumeric characters, underscores, and hyphens. The schema must be compliant with [JSON Schema Draft 7](https://json-schema.org/draft-07/schema).

`.google.protobuf.Struct data_schema = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The dataSchema.  
  
### getDataSchemaOrBuilder()
    
    
    public abstract StructOrBuilder getDataSchemaOrBuilder()

Optional. JSON Schema for data. Field names must contain only alphanumeric characters, underscores, and hyphens. The schema must be compliant with [JSON Schema Draft 7](https://json-schema.org/draft-07/schema).

`.google.protobuf.Struct data_schema = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. User-specified description of the collection

`string description = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. User-specified description of the collection

`string description = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. User-specified display name of the collection

`string display_name = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. User-specified display name of the collection

`string display_name = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEncryptionSpec()
    
    
    public abstract EncryptionSpec getEncryptionSpec()

Optional. Immutable. Specifies the customer-managed encryption key spec for a Collection. If set, this Collection and all sub-resources of this Collection will be secured by this key.

` .google.cloud.vectorsearch.v1.EncryptionSpec encryption_spec = 11 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.EncryptionSpec)` | The encryptionSpec.  
  
### getEncryptionSpecOrBuilder()
    
    
    public abstract EncryptionSpecOrBuilder getEncryptionSpecOrBuilder()

Optional. Immutable. Specifies the customer-managed encryption key spec for a Collection. If set, this Collection and all sub-resources of this Collection will be secured by this key.

` .google.cloud.vectorsearch.v1.EncryptionSpec encryption_spec = 11 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.EncryptionSpecOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CollectionOrBuilder#com_google_cloud_vectorsearch_v1_CollectionOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels as key value pairs.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels as key value pairs.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels as key value pairs.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. Labels as key value pairs.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. name of resource

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. name of resource

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. [Output only] Update time stamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. [Output only] Update time stamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getVectorSchema() (deprecated)
    
    
    public abstract Map<String,VectorField> getVectorSchema()

Use [#getVectorSchemaMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CollectionOrBuilder#com_google_cloud_vectorsearch_v1_CollectionOrBuilder_getVectorSchemaMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[VectorField](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorField)>` |   
  
### getVectorSchemaCount()
    
    
    public abstract int getVectorSchemaCount()

Optional. Schema for vector fields. Only vector fields in this schema will be searchable. Field names must contain only alphanumeric characters, underscores, and hyphens.

` map<string, .google.cloud.vectorsearch.v1.VectorField> vector_schema = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVectorSchemaMap()
    
    
    public abstract Map<String,VectorField> getVectorSchemaMap()

Optional. Schema for vector fields. Only vector fields in this schema will be searchable. Field names must contain only alphanumeric characters, underscores, and hyphens.

` map<string, .google.cloud.vectorsearch.v1.VectorField> vector_schema = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[VectorField](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorField)>` |   
  
### getVectorSchemaOrDefault(String key, VectorField defaultValue)
    
    
    public abstract VectorField getVectorSchemaOrDefault(String key, VectorField defaultValue)

Optional. Schema for vector fields. Only vector fields in this schema will be searchable. Field names must contain only alphanumeric characters, underscores, and hyphens.

` map<string, .google.cloud.vectorsearch.v1.VectorField> vector_schema = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[VectorField](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorField)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VectorField](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorField)` |   
  
### getVectorSchemaOrThrow(String key)
    
    
    public abstract VectorField getVectorSchemaOrThrow(String key)

Optional. Schema for vector fields. Only vector fields in this schema will be searchable. Field names must contain only alphanumeric characters, underscores, and hyphens.

` map<string, .google.cloud.vectorsearch.v1.VectorField> vector_schema = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VectorField](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorField)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. [Output only] Create time stamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDataSchema()
    
    
    public abstract boolean hasDataSchema()

Optional. JSON Schema for data. Field names must contain only alphanumeric characters, underscores, and hyphens. The schema must be compliant with [JSON Schema Draft 7](https://json-schema.org/draft-07/schema).

`.google.protobuf.Struct data_schema = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataSchema field is set.  
  
### hasEncryptionSpec()
    
    
    public abstract boolean hasEncryptionSpec()

Optional. Immutable. Specifies the customer-managed encryption key spec for a Collection. If set, this Collection and all sub-resources of this Collection will be secured by this key.

` .google.cloud.vectorsearch.v1.EncryptionSpec encryption_spec = 11 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionSpec field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. [Output only] Update time stamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
