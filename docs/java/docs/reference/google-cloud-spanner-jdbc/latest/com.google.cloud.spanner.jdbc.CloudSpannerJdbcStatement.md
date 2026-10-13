---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcStatement
title: Interface CloudSpannerJdbcStatement (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:49.070298+00:00
---

# Interface CloudSpannerJdbcStatement (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcStatement

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudSpannerJdbcStatement (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 
    
    
    public interface CloudSpannerJdbcStatement extends Statement

This interface is implemented by [Statement](https://docs.oracle.com/javase/8/docs/api/java/sql/Statement.html)s that are created on Cloud Spanner JDBC connections.

## Implements

[Statement](https://docs.oracle.com/javase/8/docs/api/java/sql/Statement.html)

## Methods 

### partitionQuery(String query, PartitionOptions partitionOptions, Options.QueryOption[] options)
    
    
    public abstract ResultSet partitionQuery(String query, PartitionOptions partitionOptions, Options.QueryOption[] options)

Partitions the given query, so it can be executed in parallel. This method returns a [ResultSet](https://docs.oracle.com/javase/8/docs/api/java/sql/ResultSet.html) with a string-representation of the partitions that were created. These strings can be used to execute a partition either on this connection or an any other connection (on this host or an any other host) by calling the method [#runPartition(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcStatement#com_google_cloud_spanner_jdbc_CloudSpannerJdbcStatement_runPartition_java_lang_String_). This method will automatically enable data boost for the query if [CloudSpannerJdbcConnection#isDataBoostEnabled()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcConnection#com_google_cloud_spanner_jdbc_CloudSpannerJdbcConnection_isDataBoostEnabled__) returns true.

**Parameters**  
---  
**Name** | **Description**  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`partitionOptions` | `[PartitionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.PartitionOptions)`  
  
`options` | `[QueryOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.QueryOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResultSet](https://docs.oracle.com/javase/8/docs/api/java/sql/ResultSet.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SQLException](https://docs.oracle.com/javase/8/docs/api/java/sql/SQLException.html)` |   
  
### runPartition(String encodedPartitionId)
    
    
    public abstract ResultSet runPartition(String encodedPartitionId)

Executes the given partition of a query. The encodedPartitionId should be a string that was returned by [#partitionQuery(String, PartitionOptions, QueryOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcStatement#com_google_cloud_spanner_jdbc_CloudSpannerJdbcStatement_partitionQuery_).

**Parameter**  
---  
**Name** | **Description**  
`encodedPartitionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResultSet](https://docs.oracle.com/javase/8/docs/api/java/sql/ResultSet.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SQLException](https://docs.oracle.com/javase/8/docs/api/java/sql/SQLException.html)` |   
  
### runPartitionedQuery(String query, PartitionOptions partitionOptions, Options.QueryOption[] options)
    
    
    public abstract CloudSpannerJdbcPartitionedQueryResultSet runPartitionedQuery(String query, PartitionOptions partitionOptions, Options.QueryOption[] options)

Executes the given query as a partitioned query. The query will first be partitioned using the [#partitionQuery(String, PartitionOptions, QueryOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcStatement#com_google_cloud_spanner_jdbc_CloudSpannerJdbcStatement_partitionQuery_) method. Each of the partitions will then be executed in the background, and the results will be merged into a single result set.

This method will use [CloudSpannerJdbcConnection#getMaxPartitionedParallelism()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcConnection#com_google_cloud_spanner_jdbc_CloudSpannerJdbcConnection_getMaxPartitionedParallelism__) threads to execute the partitioned query. Set this variable to a higher/lower value to increase/decrease the degree of parallelism used for execution.

**Parameters**  
---  
**Name** | **Description**  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`partitionOptions` | `[PartitionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.PartitionOptions)`  
  
`options` | `[QueryOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.QueryOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudSpannerJdbcPartitionedQueryResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc.CloudSpannerJdbcPartitionedQueryResultSet)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SQLException](https://docs.oracle.com/javase/8/docs/api/java/sql/SQLException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
