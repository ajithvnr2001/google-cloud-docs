---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.BatchReadOnlyTransaction
title: Interface BatchReadOnlyTransaction (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:10.794641+00:00
---

# Interface BatchReadOnlyTransaction (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.BatchReadOnlyTransaction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchReadOnlyTransaction (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 
    
    
    public interface BatchReadOnlyTransaction extends ReadOnlyTransaction

## Implements

[ReadOnlyTransaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ReadOnlyTransaction)

## Methods 

### cleanup()
    
    
    public default void cleanup()

### execute(Partition arg0)
    
    
    public abstract ResultSet execute(Partition arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Partition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ResultSet)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### getBatchTransactionId()
    
    
    public abstract BatchTransactionId getBatchTransactionId()

**Returns**  
---  
**Type** | **Description**  
`[BatchTransactionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.BatchTransactionId)` |   
  
### partitionQuery(PartitionOptions arg0, Statement arg1, Options.QueryOption[] arg2)
    
    
    public abstract List<Partition> partitionQuery(PartitionOptions arg0, Statement arg1, Options.QueryOption[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[PartitionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.PartitionOptions)`  
  
`arg1` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)`  
  
`arg2` | `[QueryOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.QueryOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Partition)>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### partitionRead(PartitionOptions arg0, String arg1, KeySet arg2, Iterable<String> arg3, Options.ReadOption[] arg4)
    
    
    public abstract List<Partition> partitionRead(PartitionOptions arg0, String arg1, KeySet arg2, Iterable<String> arg3, Options.ReadOption[] arg4)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[PartitionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.PartitionOptions)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[KeySet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.KeySet)`  
  
`arg3` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
`arg4` | `[ReadOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.ReadOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Partition)>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### partitionReadUsingIndex(PartitionOptions arg0, String arg1, String arg2, KeySet arg3, Iterable<String> arg4, Options.ReadOption[] arg5)
    
    
    public abstract List<Partition> partitionReadUsingIndex(PartitionOptions arg0, String arg1, String arg2, KeySet arg3, Iterable<String> arg4, Options.ReadOption[] arg5)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[PartitionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.PartitionOptions)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg3` | `[KeySet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.KeySet)`  
  
`arg4` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
`arg5` | `[ReadOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.ReadOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Partition)>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
