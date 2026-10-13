---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.TransactionRetryListener
title: Interface TransactionRetryListener (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:07.227511+00:00
---

# Interface TransactionRetryListener (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.TransactionRetryListener

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransactionRetryListener (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface TransactionRetryListener

Cloud Spanner can abort any read/write transaction because of potential deadlocks or other internal reasons. When a transaction is aborted, the entire transaction should be retried. A [Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.Connection) can automatically retry a transaction internally and check whether the results that are returned during a retry attempt are equal to the results during the original transaction. This is done by keeping track of a SHA-256 checksum of all the results that are returned by Spanner during both transactions.

This listener class for internal transaction retries allow client applications to do additional testing or logging of transaction retries. Transaction retry listeners of a [Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.Connection) can be added using [Connection#addTransactionRetryListener(TransactionRetryListener)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.Connection#com_google_cloud_spanner_connection_Connection_addTransactionRetryListener_com_google_cloud_spanner_connection_TransactionRetryListener_).

## Methods 

### retryDmlAsPartitionedDmlFailed(UUID executionId, Statement statement, Throwable exception)
    
    
    public default void retryDmlAsPartitionedDmlFailed(UUID executionId, Statement statement, Throwable exception)

This method is called when an atomic DML statement failed to be retried as a Partitioned DML statement.

**Parameters**  
---  
**Name** | **Description**  
`executionId` | `[UUID](https://docs.oracle.com/javase/8/docs/api/java/util/UUID.html)`  
the unique ID of this statement execution  
`statement` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement)`  
the statement that failed to be retried as Partitioned DML  
`exception` | `[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)`  
the exception that was returned when the statement was executed as Partitioned DML  
  
### retryDmlAsPartitionedDmlFinished(UUID executionId, Statement statement, long lowerBoundUpdateCount)
    
    
    public default void retryDmlAsPartitionedDmlFinished(UUID executionId, Statement statement, long lowerBoundUpdateCount)

This method is called when an atomic DML statement has been successfully retried as a Partitioned DML statement.

**Parameters**  
---  
**Name** | **Description**  
`executionId` | `[UUID](https://docs.oracle.com/javase/8/docs/api/java/util/UUID.html)`  
the unique ID of this statement execution  
`statement` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement)`  
the statement that was successfully retried as Partitioned DML  
`lowerBoundUpdateCount` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the lower-bound update count returned by Spanner after executing the statement as Partitioned DML  
  
### retryDmlAsPartitionedDmlStarting(UUID executionId, Statement statement, TransactionMutationLimitExceededException exception)
    
    
    public default void retryDmlAsPartitionedDmlStarting(UUID executionId, Statement statement, TransactionMutationLimitExceededException exception)

This method is called when an atomic DML statement is retried as a Partitioned DML statement.

**Parameters**  
---  
**Name** | **Description**  
`executionId` | `[UUID](https://docs.oracle.com/javase/8/docs/api/java/util/UUID.html)`  
a generated, unique ID for this execution. The same ID is passed in to the methods [#retryDmlAsPartitionedDmlFinished(UUID, Statement, long)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.TransactionRetryListener#com_google_cloud_spanner_connection_TransactionRetryListener_retryDmlAsPartitionedDmlFinished_java_util_UUID_com_google_cloud_spanner_Statement_long_) and [#retryDmlAsPartitionedDmlFailed(UUID, Statement, Throwable)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.TransactionRetryListener#com_google_cloud_spanner_connection_TransactionRetryListener_retryDmlAsPartitionedDmlFailed_java_util_UUID_com_google_cloud_spanner_Statement_java_lang_Throwable_) when the execution finishes or fails.  
`statement` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement)`  
the statement that is being retried as Partitioned DML  
`exception` | `[TransactionMutationLimitExceededException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.TransactionMutationLimitExceededException)`  
the mutation-limit-exceeded exception that was returned by Spanner during the initial execution.  
  
### retryFinished(Timestamp transactionStarted, long transactionId, int retryAttempt, TransactionRetryListener.RetryResult result)
    
    
    public abstract void retryFinished(Timestamp transactionStarted, long transactionId, int retryAttempt, TransactionRetryListener.RetryResult result)

This method is called when a retry has finished.

**Parameters**  
---  
**Name** | **Description**  
`transactionStarted` | `com.google.cloud.Timestamp`  
The start date/time of the transaction that is retrying.  
`transactionId` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
An internally assigned ID of the transaction (unique during the lifetime of the JVM) that can be used to identify the transaction for logging purposes.  
`retryAttempt` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of retry attempts the current transaction has executed, **including** the current retry attempt.  
`result` | `[TransactionRetryListener.RetryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.connection.TransactionRetryListener.RetryResult)`  
The result of the retry indicating whether the retry was successful or not.  
  
### retryStarting(Timestamp transactionStarted, long transactionId, int retryAttempt)
    
    
    public abstract void retryStarting(Timestamp transactionStarted, long transactionId, int retryAttempt)

This method is called when a retry is about to start.

**Parameters**  
---  
**Name** | **Description**  
`transactionStarted` | `com.google.cloud.Timestamp`  
The start date/time of the transaction that is retrying.  
`transactionId` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
An internally assigned ID of the transaction (unique during the lifetime of the JVM) that can be used to identify the transaction for logging purposes.  
`retryAttempt` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of retry attempts the current transaction has executed, **including** the current retry attempt.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
