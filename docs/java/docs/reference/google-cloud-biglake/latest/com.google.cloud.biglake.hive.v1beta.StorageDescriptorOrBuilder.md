---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptorOrBuilder
title: Interface StorageDescriptorOrBuilder (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:49.732011+00:00
---

# Interface StorageDescriptorOrBuilder (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptorOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StorageDescriptorOrBuilder (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface StorageDescriptorOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsParameters(String key)
    
    
    public abstract boolean containsParameters(String key)

Optional. Key-value pairs for the storage descriptor. The maximum size is 10Kib.

`map<string, string> parameters = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBucketCols(int index)
    
    
    public abstract String getBucketCols(int index)

Optional. Reducer grouping columns and clustering columns and bucketing columns

`repeated string bucket_cols = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bucketCols at the given index.  
  
### getBucketColsBytes(int index)
    
    
    public abstract ByteString getBucketColsBytes(int index)

Optional. Reducer grouping columns and clustering columns and bucketing columns

`repeated string bucket_cols = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the bucketCols at the given index.  
  
### getBucketColsCount()
    
    
    public abstract int getBucketColsCount()

Optional. Reducer grouping columns and clustering columns and bucketing columns

`repeated string bucket_cols = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of bucketCols.  
  
### getBucketColsList()
    
    
    public abstract List<String> getBucketColsList()

Optional. Reducer grouping columns and clustering columns and bucketing columns

`repeated string bucket_cols = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the bucketCols.  
  
### getColumns(int index)
    
    
    public abstract FieldSchema getColumns(int index)

Required. Specifies the columns of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema columns = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FieldSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchema)` |   
  
### getColumnsCount()
    
    
    public abstract int getColumnsCount()

Required. Specifies the columns of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema columns = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getColumnsList()
    
    
    public abstract List<FieldSchema> getColumnsList()

Required. Specifies the columns of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema columns = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FieldSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchema)>` |   
  
### getColumnsOrBuilder(int index)
    
    
    public abstract FieldSchemaOrBuilder getColumnsOrBuilder(int index)

Required. Specifies the columns of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema columns = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FieldSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchemaOrBuilder)` |   
  
### getColumnsOrBuilderList()
    
    
    public abstract List<? extends FieldSchemaOrBuilder> getColumnsOrBuilderList()

Required. Specifies the columns of the table.

` repeated .google.cloud.biglake.hive.v1beta.FieldSchema columns = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.biglake.hive.v1beta.FieldSchemaOrBuilder>` |   
  
### getCompressed()
    
    
    public abstract boolean getCompressed()

Optional. Whether the table is compressed.

`optional bool compressed = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The compressed.  
  
### getInputFormat()
    
    
    public abstract String getInputFormat()

Optional. The fully qualified Java class name of the input format. The maximum length is 4000 characters.

`string input_format = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inputFormat.  
  
### getInputFormatBytes()
    
    
    public abstract ByteString getInputFormatBytes()

Optional. The fully qualified Java class name of the input format. The maximum length is 4000 characters.

`string input_format = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for inputFormat.  
  
### getLocationUri()
    
    
    public abstract String getLocationUri()

Optional. The Cloud storage uri where the table is located. Defaults to `<database_location_uri>/<table_name>`. The maximum length is 4000 characters.

`string location_uri = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The locationUri.  
  
### getLocationUriBytes()
    
    
    public abstract ByteString getLocationUriBytes()

Optional. The Cloud storage uri where the table is located. Defaults to `<database_location_uri>/<table_name>`. The maximum length is 4000 characters.

`string location_uri = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for locationUri.  
  
### getNumBuckets()
    
    
    public abstract int getNumBuckets()

Optional. The number of buckets in the table.

`optional int32 num_buckets = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The numBuckets.  
  
### getOutputFormat()
    
    
    public abstract String getOutputFormat()

Optional. The fully qualified Java class name of the output format. The maximum length is 4000 characters.

`string output_format = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The outputFormat.  
  
### getOutputFormatBytes()
    
    
    public abstract ByteString getOutputFormatBytes()

Optional. The fully qualified Java class name of the output format. The maximum length is 4000 characters.

`string output_format = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for outputFormat.  
  
### getParameters() (deprecated)
    
    
    public abstract Map<String,String> getParameters()

Use [#getParametersMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptorOrBuilder#com_google_cloud_biglake_hive_v1beta_StorageDescriptorOrBuilder_getParametersMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getParametersCount()
    
    
    public abstract int getParametersCount()

Optional. Key-value pairs for the storage descriptor. The maximum size is 10Kib.

`map<string, string> parameters = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getParametersMap()
    
    
    public abstract Map<String,String> getParametersMap()

Optional. Key-value pairs for the storage descriptor. The maximum size is 10Kib.

`map<string, string> parameters = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getParametersOrDefault(String key, String defaultValue)
    
    
    public abstract String getParametersOrDefault(String key, String defaultValue)

Optional. Key-value pairs for the storage descriptor. The maximum size is 10Kib.

`map<string, string> parameters = 10 [(.google.api.field_behavior) = OPTIONAL]; `

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

Optional. Key-value pairs for the storage descriptor. The maximum size is 10Kib.

`map<string, string> parameters = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSerdeInfo()
    
    
    public abstract SerdeInfo getSerdeInfo()

Optional. Serialization and deserialization information.

` .google.cloud.biglake.hive.v1beta.SerdeInfo serde_info = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SerdeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.SerdeInfo)` | The serdeInfo.  
  
### getSerdeInfoOrBuilder()
    
    
    public abstract SerdeInfoOrBuilder getSerdeInfoOrBuilder()

Optional. Serialization and deserialization information.

` .google.cloud.biglake.hive.v1beta.SerdeInfo serde_info = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SerdeInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.SerdeInfoOrBuilder)` |   
  
### getSkewedInfo()
    
    
    public abstract StorageDescriptor.SkewedInfo getSkewedInfo()

Optional. Table data skew information.

` .google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo skewed_info = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor.SkewedInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo)` | The skewedInfo.  
  
### getSkewedInfoOrBuilder()
    
    
    public abstract StorageDescriptor.SkewedInfoOrBuilder getSkewedInfoOrBuilder()

Optional. Table data skew information.

` .google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo skewed_info = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor.SkewedInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfoOrBuilder)` |   
  
### getSortCols(int index)
    
    
    public abstract StorageDescriptor.Order getSortCols(int index)

Optional. Sort order of the data in each bucket

` repeated .google.cloud.biglake.hive.v1beta.StorageDescriptor.Order sort_cols = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor.Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Order)` |   
  
### getSortColsCount()
    
    
    public abstract int getSortColsCount()

Optional. Sort order of the data in each bucket

` repeated .google.cloud.biglake.hive.v1beta.StorageDescriptor.Order sort_cols = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSortColsList()
    
    
    public abstract List<StorageDescriptor.Order> getSortColsList()

Optional. Sort order of the data in each bucket

` repeated .google.cloud.biglake.hive.v1beta.StorageDescriptor.Order sort_cols = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Order)>` |   
  
### getSortColsOrBuilder(int index)
    
    
    public abstract StorageDescriptor.OrderOrBuilder getSortColsOrBuilder(int index)

Optional. Sort order of the data in each bucket

` repeated .google.cloud.biglake.hive.v1beta.StorageDescriptor.Order sort_cols = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor.OrderOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.OrderOrBuilder)` |   
  
### getSortColsOrBuilderList()
    
    
    public abstract List<? extends StorageDescriptor.OrderOrBuilder> getSortColsOrBuilderList()

Optional. Sort order of the data in each bucket

` repeated .google.cloud.biglake.hive.v1beta.StorageDescriptor.Order sort_cols = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.biglake.hive.v1beta.StorageDescriptor.OrderOrBuilder>` |   
  
### getStoredAsSubDirs()
    
    
    public abstract boolean getStoredAsSubDirs()

Optional. Whether the table is stored as sub directories.

`optional bool stored_as_sub_dirs = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The storedAsSubDirs.  
  
### hasCompressed()
    
    
    public abstract boolean hasCompressed()

Optional. Whether the table is compressed.

`optional bool compressed = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the compressed field is set.  
  
### hasNumBuckets()
    
    
    public abstract boolean hasNumBuckets()

Optional. The number of buckets in the table.

`optional int32 num_buckets = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the numBuckets field is set.  
  
### hasSerdeInfo()
    
    
    public abstract boolean hasSerdeInfo()

Optional. Serialization and deserialization information.

` .google.cloud.biglake.hive.v1beta.SerdeInfo serde_info = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serdeInfo field is set.  
  
### hasSkewedInfo()
    
    
    public abstract boolean hasSkewedInfo()

Optional. Table data skew information.

` .google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo skewed_info = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the skewedInfo field is set.  
  
### hasStoredAsSubDirs()
    
    
    public abstract boolean hasStoredAsSubDirs()

Optional. Whether the table is stored as sub directories.

`optional bool stored_as_sub_dirs = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the storedAsSubDirs field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
