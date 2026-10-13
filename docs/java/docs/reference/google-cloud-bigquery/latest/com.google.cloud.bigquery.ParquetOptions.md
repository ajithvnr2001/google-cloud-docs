---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ParquetOptions
title: Class ParquetOptions (2.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:38.986078+00:00
---

# Class ParquetOptions (2.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ParquetOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParquetOptions (2.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.73.0 (latest)  2.69.0  2.68.0  2.67.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.2  2.56.0  2.55.3  2.54.2  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.1  2.47.0  2.46.0  2.45.0  2.44.0  2.43.3  2.42.3  2.41.0  2.40.3  2.39.1  2.38.2  2.37.2  2.36.0  2.35.0  2.34.2  2.33.2 
    
    
    public class ParquetOptions extends FormatOptions

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions) > ParquetOptions

## Inherited Members

[FormatOptions.avro()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_avro__)

[FormatOptions.bigtable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_bigtable__)

[FormatOptions.csv()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_csv__)

[FormatOptions.datastoreBackup()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_datastoreBackup__)

[FormatOptions.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_equals_java_lang_Object_)

[FormatOptions.getType()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_getType__)

[FormatOptions.googleSheets()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_googleSheets__)

[FormatOptions.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_hashCode__)

[FormatOptions.iceberg()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_iceberg__)

[FormatOptions.json()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_json__)

[FormatOptions.of(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_of_java_lang_String_)

[FormatOptions.orc()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_orc__)

[FormatOptions.parquet()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_parquet__)

[FormatOptions.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### newBuilder()
    
    
    public static ParquetOptions.Builder newBuilder()

Returns a builder for a [ParquetOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ParquetOptions) object.

**Returns**  
---  
**Type** | **Description**  
`[ParquetOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ParquetOptions.Builder)` |   
  
## Methods 

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

[FormatOptions.equals(Object obj)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_equals_java_lang_Object_)

### getEnableListInference()
    
    
    public Boolean getEnableListInference()

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getEnumAsString()
    
    
    public Boolean getEnumAsString()

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getMapTargetType()
    
    
    public String getMapTargetType()

Returns how the Parquet map is represented.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hashCode()
    
    
    public final int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[FormatOptions.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_hashCode__)

### toBuilder()
    
    
    public ParquetOptions.Builder toBuilder()

Returns a builder for the [ParquetOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ParquetOptions) object.

**Returns**  
---  
**Type** | **Description**  
`[ParquetOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ParquetOptions.Builder)` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[FormatOptions.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions#com_google_cloud_bigquery_FormatOptions_toString__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
