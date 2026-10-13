---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTableOrBuilder
title: Interface HiveTableOrBuilder (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:34:56.083577+00:00
---

# Interface HiveTableOrBuilder (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTableOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HiveTableOrBuilder (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface HiveTableOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsParameters(String key)
    
    
    public abstract boolean containsParameters(String key)

Optional. Stores the properties associated with the table. The maximum size is 4MiB.

`map<string, string> parameters = 8 [(.google.api.field_behavior) = OPTIONAL]; `

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

Output only. The creation time of the table.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The creation time of the table.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description of the table. The maximum length is 4000 characters.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description of the table. The maximum length is 4000 characters.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getParameters() (deprecated)
    
    
    public abstract Map<String,String> getParameters()

Use [#getParametersMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTableOrBuilder#com_google_cloud_biglake_hive_v1beta_HiveTableOrBuilder_getParametersMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getParametersCount()
    
    
    public abstract int getParametersCount()

Optional. Stores the properties associated with the table. The maximum size is 4MiB.

`map<string, string> parameters = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getParametersMap()
    
    
    public abstract Map<String,String> getParametersMap()

Optional. Stores the properties associated with the table. The maximum size is 4MiB.

`map<string, string> parameters = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getParametersOrDefault(String key, String defaultValue)
    
    
    public abstract String getParametersOrDefault(String key, String defaultValue)

Optional. Stores the properties associated with the table. The maximum size is 4MiB.

`map<string, string> parameters = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getParametersOrThrow(String key)
    
    
    public abstract String getParametersOrThrow(String key)

Optional. Stores the properties associated with the table. The maximum size is 4MiB.

`map<string, string> parameters = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getPartitionKeys(int index)
    
    
    public abstract FieldSchema getPartitionKeys(int index)

Optional. The partition keys of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema partition_keys = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FieldSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchema)` |   
  
### getPartitionKeysCount()
    
    
    public abstract int getPartitionKeysCount()

Optional. The partition keys of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema partition_keys = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPartitionKeysList()
    
    
    public abstract List<FieldSchema> getPartitionKeysList()

Optional. The partition keys of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema partition_keys = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FieldSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchema)>` |   
  
### getPartitionKeysOrBuilder(int index)
    
    
    public abstract FieldSchemaOrBuilder getPartitionKeysOrBuilder(int index)

Optional. The partition keys of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema partition_keys = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FieldSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchemaOrBuilder)` |   
  
### getPartitionKeysOrBuilderList()
    
    
    public abstract List<? extends FieldSchemaOrBuilder> getPartitionKeysOrBuilderList()

Optional. The partition keys of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema partition_keys = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.biglake.hive.v1beta.FieldSchemaOrBuilder>` |   
  
### getStorageDescriptor()
    
    
    public abstract StorageDescriptor getStorageDescriptor()

Required. Storage descriptor of the table.

` .google.cloud.biglake.hive.v1beta.StorageDescriptor storage_descriptor = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor)` | The storageDescriptor.  
  
### getStorageDescriptorOrBuilder()
    
    
    public abstract StorageDescriptorOrBuilder getStorageDescriptorOrBuilder()

Required. Storage descriptor of the table.

` .google.cloud.biglake.hive.v1beta.StorageDescriptor storage_descriptor = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptorOrBuilder)` |   
  
### getTableType()
    
    
    public abstract String getTableType()

Output only. The type of the table. This is EXTERNAL for BigLake hive tables.

`string table_type = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tableType.  
  
### getTableTypeBytes()
    
    
    public abstract ByteString getTableTypeBytes()

Output only. The type of the table. This is EXTERNAL for BigLake hive tables.

`string table_type = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tableType.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The update time of the table.

`.google.protobuf.Timestamp update_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The update time of the table.

`.google.protobuf.Timestamp update_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getViewExpandedText()
    
    
    public abstract String getViewExpandedText()

Optional. The expanded view text. Empty for non-view. The maximum size is 16MiB.

`string view_expanded_text = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The viewExpandedText.  
  
### getViewExpandedTextBytes()
    
    
    public abstract ByteString getViewExpandedTextBytes()

Optional. The expanded view text. Empty for non-view. The maximum size is 16MiB.

`string view_expanded_text = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for viewExpandedText.  
  
### getViewOriginalText()
    
    
    public abstract String getViewOriginalText()

Optional. The original view text. Empty for non-view. The maximum size is 16MiB.

`string view_original_text = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The viewOriginalText.  
  
### getViewOriginalTextBytes()
    
    
    public abstract ByteString getViewOriginalTextBytes()

Optional. The original view text. Empty for non-view. The maximum size is 16MiB.

`string view_original_text = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for viewOriginalText.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The creation time of the table.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasStorageDescriptor()
    
    
    public abstract boolean hasStorageDescriptor()

Required. Storage descriptor of the table.

` .google.cloud.biglake.hive.v1beta.StorageDescriptor storage_descriptor = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the storageDescriptor field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The update time of the table.

`.google.protobuf.Timestamp update_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
