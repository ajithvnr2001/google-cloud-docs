---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchClient
title: Interface BatchClient (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:33.910230+00:00
---

# Interface BatchClient (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchClient (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface BatchClient

Interface for the Batch Client that is used to read data from a Cloud Spanner database. An instance of this is tied to a specific database.

`BatchClient` is useful when one wants to read or query a large amount of data from Cloud Spanner across multiple processes, even across different machines. It allows to create partitions of Cloud Spanner database and then read or query over each partition independently yet at the same snapshot.

## Methods 

### batchReadOnlyTransaction(BatchTransactionId batchTransactionId)
    
    
    public abstract BatchReadOnlyTransaction batchReadOnlyTransaction(BatchTransactionId batchTransactionId)

Returns a [BatchReadOnlyTransaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchReadOnlyTransaction) context in which multiple reads and/or queries can be performed. This is a non-blocking method. All reads/queries will use the same timestamp, and the timestamp can be inspected after this transaction is created successfully.

This method is useful to recreate a BatchReadOnlyTransaction object from an existing batchTransactionId. For example one might send the transaction id to a different process or machine and recreate the transaction object there.

**Parameter**  
---  
**Name** | **Description**  
`batchTransactionId` | `[BatchTransactionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchTransactionId)`  
to re-initialize the transaction, re-using the timestamp for successive read/query.  
**Returns**  
---  
**Type** | **Description**  
`[BatchReadOnlyTransaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchReadOnlyTransaction)` |   
  
### batchReadOnlyTransaction(TimestampBound bound)
    
    
    public abstract BatchReadOnlyTransaction batchReadOnlyTransaction(TimestampBound bound)

Returns a [BatchReadOnlyTransaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchReadOnlyTransaction) context in which multiple reads and/or queries can be performed. All reads/queries will use the same timestamp, and the timestamp can be inspected after this transaction is created successfully. This is a blocking method since it waits to finish the rpcs.

Note that the bounded staleness modes, [TimestampBound.Mode#MIN_READ_TIMESTAMP](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.TimestampBound.Mode#com_google_cloud_spanner_TimestampBound_Mode_MIN_READ_TIMESTAMP) and [TimestampBound.Mode#MAX_STALENESS](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.TimestampBound.Mode#com_google_cloud_spanner_TimestampBound_Mode_MAX_STALENESS), are not supported for [BatchReadOnlyTransaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchReadOnlyTransaction).

**Parameter**  
---  
**Name** | **Description**  
`bound` | `[TimestampBound](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.TimestampBound)`  
the timestamp bound at which to perform the read 
    
    
     BatchReadOnlyTransaction txn = batchClient.batchReadOnlyTransaction(TimestampBound.strong());
     
    
    
     <!--SNIPPET batch_client_strong_read-->
      
  
**Returns**  
---  
**Type** | **Description**  
`[BatchReadOnlyTransaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.BatchReadOnlyTransaction)` |   
  
### getDatabaseRole()
    
    
    public default String getDatabaseRole()

Returns the [DatabaseRole](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseRole) used by the client connection. The database role that is used determines the access permissions that a connection has. This can for example be used to create connections that are only permitted to access certain tables.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
