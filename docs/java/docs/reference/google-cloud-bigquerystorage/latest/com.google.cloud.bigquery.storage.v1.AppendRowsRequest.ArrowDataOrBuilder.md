---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowDataOrBuilder
title: Interface AppendRowsRequest.ArrowDataOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:57.912705+00:00
---

# Interface AppendRowsRequest.ArrowDataOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowDataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AppendRowsRequest.ArrowDataOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static interface AppendRowsRequest.ArrowDataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getRows()
    
    
    public abstract ArrowRecordBatch getRows()

Required. Serialized row data in Arrow format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch rows = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch)` | The rows.  
  
### getRowsOrBuilder()
    
    
    public abstract ArrowRecordBatchOrBuilder getRowsOrBuilder()

Required. Serialized row data in Arrow format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch rows = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowRecordBatchOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatchOrBuilder)` |   
  
### getWriterSchema()
    
    
    public abstract ArrowSchema getWriterSchema()

Optional. Arrow Schema used to serialize the data.

`.google.cloud.bigquery.storage.v1.ArrowSchema writer_schema = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema)` | The writerSchema.  
  
### getWriterSchemaOrBuilder()
    
    
    public abstract ArrowSchemaOrBuilder getWriterSchemaOrBuilder()

Optional. Arrow Schema used to serialize the data.

`.google.cloud.bigquery.storage.v1.ArrowSchema writer_schema = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchemaOrBuilder)` |   
  
### hasRows()
    
    
    public abstract boolean hasRows()

Required. Serialized row data in Arrow format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch rows = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rows field is set.  
  
### hasWriterSchema()
    
    
    public abstract boolean hasWriterSchema()

Optional. Arrow Schema used to serialize the data.

`.google.cloud.bigquery.storage.v1.ArrowSchema writer_schema = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the writerSchema field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
