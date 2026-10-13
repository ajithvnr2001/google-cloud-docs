---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerSourceConfigOrBuilder
title: Interface SqlServerSourceConfigOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:21.757378+00:00
---

# Interface SqlServerSourceConfigOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerSourceConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SqlServerSourceConfigOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.1  1.0.0  0.4.2 
    
    
    public interface SqlServerSourceConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCdcMethodCase()
    
    
    public abstract SqlServerSourceConfig.CdcMethodCase getCdcMethodCase()

**Returns**  
---  
**Type** | **Description**  
`[SqlServerSourceConfig.CdcMethodCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerSourceConfig.CdcMethodCase)` |   
  
### getChangeTables()
    
    
    public abstract SqlServerChangeTables getChangeTables()

CDC reader reads from change tables.

`.google.cloud.datastream.v1.SqlServerChangeTables change_tables = 102;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerChangeTables](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerChangeTables)` | The changeTables.  
  
### getChangeTablesOrBuilder()
    
    
    public abstract SqlServerChangeTablesOrBuilder getChangeTablesOrBuilder()

CDC reader reads from change tables.

`.google.cloud.datastream.v1.SqlServerChangeTables change_tables = 102;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerChangeTablesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerChangeTablesOrBuilder)` |   
  
### getExcludeObjects()
    
    
    public abstract SqlServerRdbms getExcludeObjects()

SQLServer objects to exclude from the stream.

`.google.cloud.datastream.v1.SqlServerRdbms exclude_objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerRdbms](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerRdbms)` | The excludeObjects.  
  
### getExcludeObjectsOrBuilder()
    
    
    public abstract SqlServerRdbmsOrBuilder getExcludeObjectsOrBuilder()

SQLServer objects to exclude from the stream.

`.google.cloud.datastream.v1.SqlServerRdbms exclude_objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerRdbmsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerRdbmsOrBuilder)` |   
  
### getIncludeObjects()
    
    
    public abstract SqlServerRdbms getIncludeObjects()

SQLServer objects to include in the stream.

`.google.cloud.datastream.v1.SqlServerRdbms include_objects = 1;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerRdbms](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerRdbms)` | The includeObjects.  
  
### getIncludeObjectsOrBuilder()
    
    
    public abstract SqlServerRdbmsOrBuilder getIncludeObjectsOrBuilder()

SQLServer objects to include in the stream.

`.google.cloud.datastream.v1.SqlServerRdbms include_objects = 1;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerRdbmsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerRdbmsOrBuilder)` |   
  
### getMaxConcurrentBackfillTasks()
    
    
    public abstract int getMaxConcurrentBackfillTasks()

Max concurrent backfill tasks.

`int32 max_concurrent_backfill_tasks = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxConcurrentBackfillTasks.  
  
### getMaxConcurrentCdcTasks()
    
    
    public abstract int getMaxConcurrentCdcTasks()

Max concurrent CDC tasks.

`int32 max_concurrent_cdc_tasks = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxConcurrentCdcTasks.  
  
### getTransactionLogs()
    
    
    public abstract SqlServerTransactionLogs getTransactionLogs()

CDC reader reads from transaction logs.

`.google.cloud.datastream.v1.SqlServerTransactionLogs transaction_logs = 101;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerTransactionLogs](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerTransactionLogs)` | The transactionLogs.  
  
### getTransactionLogsOrBuilder()
    
    
    public abstract SqlServerTransactionLogsOrBuilder getTransactionLogsOrBuilder()

CDC reader reads from transaction logs.

`.google.cloud.datastream.v1.SqlServerTransactionLogs transaction_logs = 101;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerTransactionLogsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerTransactionLogsOrBuilder)` |   
  
### hasChangeTables()
    
    
    public abstract boolean hasChangeTables()

CDC reader reads from change tables.

`.google.cloud.datastream.v1.SqlServerChangeTables change_tables = 102;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the changeTables field is set.  
  
### hasExcludeObjects()
    
    
    public abstract boolean hasExcludeObjects()

SQLServer objects to exclude from the stream.

`.google.cloud.datastream.v1.SqlServerRdbms exclude_objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the excludeObjects field is set.  
  
### hasIncludeObjects()
    
    
    public abstract boolean hasIncludeObjects()

SQLServer objects to include in the stream.

`.google.cloud.datastream.v1.SqlServerRdbms include_objects = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the includeObjects field is set.  
  
### hasTransactionLogs()
    
    
    public abstract boolean hasTransactionLogs()

CDC reader reads from transaction logs.

`.google.cloud.datastream.v1.SqlServerTransactionLogs transaction_logs = 101;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transactionLogs field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
