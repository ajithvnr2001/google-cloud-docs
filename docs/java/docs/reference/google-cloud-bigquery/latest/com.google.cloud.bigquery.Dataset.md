---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset
title: Class Dataset (2.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:33.137066+00:00
---

# Class Dataset (2.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Dataset (2.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.73.0 (latest)  2.69.0  2.68.0  2.67.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.2  2.56.0  2.55.3  2.54.2  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.1  2.47.0  2.46.0  2.45.0  2.44.0  2.43.3  2.42.3  2.41.0  2.40.3  2.39.1  2.38.2  2.37.2  2.36.0  2.35.0  2.34.2  2.33.2 
    
    
    public class Dataset extends DatasetInfo

A Google BigQuery Dataset.

Objects of this class are immutable. Operations that modify the dataset like [#update](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset#com_google_cloud_bigquery_Dataset_update_) return a new object. To get a `Dataset` object with the most recent information use [#reload](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset#com_google_cloud_bigquery_Dataset_reload_). `Dataset` adds a layer of service-related functionality over [DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo).

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo) > Dataset

## Inherited Members

[DatasetInfo.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_equals_java_lang_Object_)

[DatasetInfo.getAcl()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getAcl__)

[DatasetInfo.getCreationTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getCreationTime__)

[DatasetInfo.getDatasetId()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getDatasetId__)

[DatasetInfo.getDefaultCollation()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getDefaultCollation__)

[DatasetInfo.getDefaultEncryptionConfiguration()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getDefaultEncryptionConfiguration__)

[DatasetInfo.getDefaultPartitionExpirationMs()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getDefaultPartitionExpirationMs__)

[DatasetInfo.getDefaultTableLifetime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getDefaultTableLifetime__)

[DatasetInfo.getDescription()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getDescription__)

[DatasetInfo.getEtag()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getEtag__)

[DatasetInfo.getExternalDatasetReference()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getExternalDatasetReference__)

[DatasetInfo.getFriendlyName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getFriendlyName__)

[DatasetInfo.getGeneratedId()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getGeneratedId__)

[DatasetInfo.getLabels()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getLabels__)

[DatasetInfo.getLastModified()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getLastModified__)

[DatasetInfo.getLocation()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getLocation__)

[DatasetInfo.getMaxTimeTravelHours()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getMaxTimeTravelHours__)

[DatasetInfo.getOtelAttributes()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getOtelAttributes__)

[DatasetInfo.getResourceTags()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getResourceTags__)

[DatasetInfo.getSelfLink()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getSelfLink__)

[DatasetInfo.getStorageBillingModel()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_getStorageBillingModel__)

[DatasetInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_hashCode__)

[DatasetInfo.newBuilder(DatasetId)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_newBuilder_com_google_cloud_bigquery_DatasetId_)

[DatasetInfo.newBuilder(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_newBuilder_java_lang_String_)

[DatasetInfo.newBuilder(String,String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_newBuilder_java_lang_String_java_lang_String_)

[DatasetInfo.of(DatasetId)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_of_com_google_cloud_bigquery_DatasetId_)

[DatasetInfo.of(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_of_java_lang_String_)

[DatasetInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_toBuilder__)

[DatasetInfo.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### create(String tableId, TableDefinition definition, BigQuery.TableOption[] options)
    
    
    public Table create(String tableId, TableDefinition definition, BigQuery.TableOption[] options)

Creates a new table in this dataset.

Example of creating a table in the dataset with schema and time partitioning.
    
    
     String tableName = “my_table”;
     String fieldName = “my_field”;
     Schema schema = Schema.of(Field.of(fieldName, LegacySQLTypeName.STRING));
     StandardTableDefinition definition = StandardTableDefinition.newBuilder()
         .setSchema(schema)
         .setTimePartitioning(TimePartitioning.of(TimePartitioning.Type.DAY))
         .build();
     Table table = dataset.create(tableName, definition);
     

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the table's user-defined id  
`definition` | `[TableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDefinition)`  
the table's definition  
`options` | `[TableOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableOption)[]`  
options for table creation  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)` | a `Table` object for the created table  
  
### delete(BigQuery.DatasetDeleteOption[] options)
    
    
    public boolean delete(BigQuery.DatasetDeleteOption[] options)

Deletes this dataset.

Example of deleting a dataset.
    
    
     boolean deleted = dataset.delete();
     if (deleted) {
       // The dataset was deleted
     } else {
       // The dataset was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[DatasetDeleteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetDeleteOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if dataset was deleted, `false` if it was not found  
  
### equals(Object obj)
    
    
    public final boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[DatasetInfo.equals(Object obj)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_equals_java_lang_Object_)

### exists()
    
    
    public boolean exists()

Checks if this dataset exists.

Example of checking whether a dataset exists.
    
    
     boolean exists = dataset.exists();
     if (exists) {
       // the dataset exists
     } else {
       // the dataset was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if this dataset exists, `false` otherwise  
  
### get(String tableId, BigQuery.TableOption[] options)
    
    
    public Table get(String tableId, BigQuery.TableOption[] options)

Returns the requested table in this dataset or `null` if not found.

Example of getting a table in the dataset.
    
    
     String tableName = “my_table”;
     Table table = dataset.get(tableName);
     

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
user-defined id of the requested table  
`options` | `[TableOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableOption)[]`  
table options  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)` |   
  
### getBigQuery()
    
    
    public BigQuery getBigQuery()

Returns the dataset's `BigQuery` object used to issue requests.

**Returns**  
---  
**Type** | **Description**  
`[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery)` |   
  
### hashCode()
    
    
    public final int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[DatasetInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_hashCode__)

### list(BigQuery.TableListOption[] options)
    
    
    public Page<Table> list(BigQuery.TableListOption[] options)

Returns the paginated list of tables in this dataset.

Example of listing tables in the dataset.
    
    
     Page<Table> tables = dataset.list();
     for (Table table : tables.iterateAll()) {
       // do something with the table
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[TableListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableListOption)[]`  
options for listing tables  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)>` |   
  
### reload(BigQuery.DatasetOption[] options)
    
    
    public Dataset reload(BigQuery.DatasetOption[] options)

Fetches current dataset's latest information. Returns `null` if the dataset does not exist.

Example of reloading a dataset.
    
    
     Dataset latestDataset = dataset.reload();
     if (latestDataset == null) {
       // The dataset was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[DatasetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetOption)[]`  
dataset options  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)` | a `Dataset` object with latest information or `null` if not found  
  
### toBuilder()
    
    
    public Dataset.Builder toBuilder()

Returns a builder for the dataset object.

**Returns**  
---  
**Type** | **Description**  
`[Dataset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.Builder)` |   
**Overrides**

[DatasetInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo#com_google_cloud_bigquery_DatasetInfo_toBuilder__)

### update(BigQuery.DatasetOption[] options)
    
    
    public Dataset update(BigQuery.DatasetOption[] options)

Updates the dataset's information with this dataset's information. Dataset's user-defined id cannot be changed. A new `Dataset` object is returned.

Example of updating a dataset.
    
    
     String friendlyName = "my_friendly_name";
     Builder builder = dataset.toBuilder();
     builder.setFriendlyName(friendlyName);
     Dataset updatedDataset = builder.build().update();
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[DatasetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetOption)[]`  
dataset options  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)` | a `Dataset` object with updated information  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
