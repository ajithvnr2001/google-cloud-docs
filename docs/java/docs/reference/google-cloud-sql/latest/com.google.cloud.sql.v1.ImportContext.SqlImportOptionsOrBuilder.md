---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlImportOptionsOrBuilder
title: Interface ImportContext.SqlImportOptionsOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:29.278824+00:00
---

# Interface ImportContext.SqlImportOptionsOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlImportOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportContext.SqlImportOptionsOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface ImportContext.SqlImportOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParallel()
    
    
    public abstract BoolValue getParallel()

Optional. Whether or not the import should be parallel.

`.google.protobuf.BoolValue parallel = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The parallel.  
  
### getParallelOrBuilder()
    
    
    public abstract BoolValueOrBuilder getParallelOrBuilder()

Optional. Whether or not the import should be parallel.

`.google.protobuf.BoolValue parallel = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getPostgresImportOptions()
    
    
    public abstract ImportContext.SqlImportOptions.PostgresImportOptions getPostgresImportOptions()

Optional. Options for importing from a Cloud SQL for PostgreSQL instance.

` .google.cloud.sql.v1.ImportContext.SqlImportOptions.PostgresImportOptions postgres_import_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlImportOptions.PostgresImportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlImportOptions.PostgresImportOptions)` | The postgresImportOptions.  
  
### getPostgresImportOptionsOrBuilder()
    
    
    public abstract ImportContext.SqlImportOptions.PostgresImportOptionsOrBuilder getPostgresImportOptionsOrBuilder()

Optional. Options for importing from a Cloud SQL for PostgreSQL instance.

` .google.cloud.sql.v1.ImportContext.SqlImportOptions.PostgresImportOptions postgres_import_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlImportOptions.PostgresImportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlImportOptions.PostgresImportOptionsOrBuilder)` |   
  
### getThreads()
    
    
    public abstract Int32Value getThreads()

Optional. The number of threads to use for parallel import.

`.google.protobuf.Int32Value threads = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Int32Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32Value.html)` | The threads.  
  
### getThreadsOrBuilder()
    
    
    public abstract Int32ValueOrBuilder getThreadsOrBuilder()

Optional. The number of threads to use for parallel import.

`.google.protobuf.Int32Value threads = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Int32ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32ValueOrBuilder.html)` |   
  
### hasParallel()
    
    
    public abstract boolean hasParallel()

Optional. Whether or not the import should be parallel.

`.google.protobuf.BoolValue parallel = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parallel field is set.  
  
### hasPostgresImportOptions()
    
    
    public abstract boolean hasPostgresImportOptions()

Optional. Options for importing from a Cloud SQL for PostgreSQL instance.

` .google.cloud.sql.v1.ImportContext.SqlImportOptions.PostgresImportOptions postgres_import_options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postgresImportOptions field is set.  
  
### hasThreads()
    
    
    public abstract boolean hasThreads()

Optional. The number of threads to use for parallel import.

`.google.protobuf.Int32Value threads = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the threads field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
