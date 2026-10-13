---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder
title: Class ExtractJobConfiguration.Builder (2.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:59.450691+00:00
---

# Class ExtractJobConfiguration.Builder (2.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ExtractJobConfiguration.Builder (2.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.73.0 (latest)  2.69.0  2.68.0  2.67.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.2  2.56.0  2.55.3  2.54.2  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.1  2.47.0  2.46.0  2.45.0  2.44.0  2.43.3  2.42.3  2.41.0  2.40.3  2.39.1  2.38.2  2.37.2  2.36.0  2.35.0  2.34.2  2.33.2 
    
    
    public static final class ExtractJobConfiguration.Builder extends JobConfiguration.Builder<ExtractJobConfiguration,ExtractJobConfiguration.Builder>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [JobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobConfiguration.Builder) > ExtractJobConfiguration.Builder

## Inherited Members

[JobConfiguration.Builder.build()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobConfiguration.Builder#com_google_cloud_bigquery_JobConfiguration_Builder_build__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build()
    
    
    public ExtractJobConfiguration build()

Creates an object.

**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration)` |   
**Overrides**

[JobConfiguration.Builder<T,B>.build()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobConfiguration.Builder#com_google_cloud_bigquery_JobConfiguration_Builder_build__)

### setCompression(String compression)
    
    
    public ExtractJobConfiguration.Builder setCompression(String compression)

Sets the compression value to use for exported files. If not set exported files are not compressed.

[ Compression](https://cloud.google.com/bigquery/docs/reference/v2/jobs#configuration.extract.compression)

**Parameter**  
---  
**Name** | **Description**  
`compression` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setDestinationUris(List<String> destinationUris)
    
    
    public ExtractJobConfiguration.Builder setDestinationUris(List<String> destinationUris)

Sets the list of fully-qualified Google Cloud Storage URIs (e.g. gs://bucket/path) where the extracted table should be written.

**Parameter**  
---  
**Name** | **Description**  
`destinationUris` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setFieldDelimiter(String fieldDelimiter)
    
    
    public ExtractJobConfiguration.Builder setFieldDelimiter(String fieldDelimiter)

Sets the delimiter to use between fields in the exported data. By default "," is used.

**Parameter**  
---  
**Name** | **Description**  
`fieldDelimiter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setFormat(String format)
    
    
    public ExtractJobConfiguration.Builder setFormat(String format)

Sets the exported file format. If not set table is exported in CSV format.

[ Destination Format](https://cloud.google.com/bigquery/docs/reference/v2/jobs#configuration.extract.destinationFormat)

**Parameter**  
---  
**Name** | **Description**  
`format` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setJobTimeoutMs(Long jobTimeoutMs)
    
    
    public ExtractJobConfiguration.Builder setJobTimeoutMs(Long jobTimeoutMs)

[Optional] Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.

**Parameter**  
---  
**Name** | **Description**  
`jobTimeoutMs` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
jobTimeoutMs or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setLabels(Map<String,String> labels)
    
    
    public ExtractJobConfiguration.Builder setLabels(Map<String,String> labels)

The labels associated with this job. You can use these to organize and group your jobs. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key.

**Parameter**  
---  
**Name** | **Description**  
`labels` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
labels or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setPrintHeader(Boolean printHeader)
    
    
    public ExtractJobConfiguration.Builder setPrintHeader(Boolean printHeader)

Sets whether to print out a header row in the results. By default an header is printed.

**Parameter**  
---  
**Name** | **Description**  
`printHeader` | `[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setReservation(String reservation)
    
    
    public ExtractJobConfiguration.Builder setReservation(String reservation)

[Optional] The reservation that job would use. User can specify a reservation to execute the job. If reservation is not set, reservation is determined based on the rules defined by the reservation assignments. The expected format is `projects/{project}/locations/{location}/reservations/{reservation}`.

**Parameter**  
---  
**Name** | **Description**  
`reservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
reservation or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setSourceModel(ModelId sourceModel)
    
    
    public ExtractJobConfiguration.Builder setSourceModel(ModelId sourceModel)

Sets the model to export.

**Parameter**  
---  
**Name** | **Description**  
`sourceModel` | `[ModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ModelId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setSourceTable(TableId sourceTable)
    
    
    public ExtractJobConfiguration.Builder setSourceTable(TableId sourceTable)

Sets the table to export.

**Parameter**  
---  
**Name** | **Description**  
`sourceTable` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
### setUseAvroLogicalTypes(Boolean useAvroLogicalTypes)
    
    
    public ExtractJobConfiguration.Builder setUseAvroLogicalTypes(Boolean useAvroLogicalTypes)

[Optional] If destinationFormat is set to "AVRO", this flag indicates whether to enable extracting applicable column types (such as TIMESTAMP) to their corresponding AVRO logical types (timestamp-micros), instead of only using their raw types (avro-long).

**Parameter**  
---  
**Name** | **Description**  
`useAvroLogicalTypes` | `[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)`  
useAvroLogicalTypes or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExtractJobConfiguration.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
