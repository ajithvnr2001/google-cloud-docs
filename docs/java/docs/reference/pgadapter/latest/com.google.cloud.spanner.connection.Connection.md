---
url: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.Connection
title: Interface Connection (0.27.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:53.316794+00:00
---

# Interface Connection (0.27.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.Connection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Connection (0.27.1) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.27.1 (latest) ](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.Connection)
  * [ 0.27.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.27.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.26.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.26.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.25.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.25.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.24.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.24.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.23.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.23.1/com.google.cloud.spanner.connection.Connection)
  * [ 0.22.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.22.1/com.google.cloud.spanner.connection.Connection)
  * [ 0.21.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.21.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.20.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.20.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.19.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.19.1/com.google.cloud.spanner.connection.Connection)
  * [ 0.18.4 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.18.4/com.google.cloud.spanner.connection.Connection)
  * [ 0.17.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.17.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.16.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.16.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.15.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.14.1/com.google.cloud.spanner.connection.Connection)
  * [ 0.9.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.9.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.8.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.8.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.7.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.7.0/com.google.cloud.spanner.connection.Connection)
  * [ 0.6.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.6.1/com.google.cloud.spanner.connection.Connection)
  * [ 0.5.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.5.1/com.google.cloud.spanner.connection.Connection)


    
    
    public interface Connection extends AutoCloseable

## Implements

[AutoCloseable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html)

## Methods 

### abortBatch()
    
    
    public abstract void abortBatch()

### addTransactionRetryListener(TransactionRetryListener arg0)
    
    
    public abstract void addTransactionRetryListener(TransactionRetryListener arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[TransactionRetryListener](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.TransactionRetryListener)`  
  
  
### analyzeQuery(Statement arg0, ReadContext.QueryAnalyzeMode arg1)
    
    
    public abstract ResultSet analyzeQuery(Statement arg0, ReadContext.QueryAnalyzeMode arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `com.google.cloud.spanner.ReadContext.QueryAnalyzeMode`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.ResultSet` |   
  
### analyzeUpdate(Statement arg0, ReadContext.QueryAnalyzeMode arg1)
    
    
    public default ResultSetStats analyzeUpdate(Statement arg0, ReadContext.QueryAnalyzeMode arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `com.google.cloud.spanner.ReadContext.QueryAnalyzeMode`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.spanner.v1.ResultSetStats` |   
  
### analyzeUpdateStatement(Statement arg0, ReadContext.QueryAnalyzeMode arg1, Options.UpdateOption[] arg2)
    
    
    public default ResultSet analyzeUpdateStatement(Statement arg0, ReadContext.QueryAnalyzeMode arg1, Options.UpdateOption[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `com.google.cloud.spanner.ReadContext.QueryAnalyzeMode`  
  
`arg2` | `com.google.cloud.spanner.Options.UpdateOption[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.ResultSet` |   
  
### beginTransaction()
    
    
    public abstract void beginTransaction()

### beginTransactionAsync()
    
    
    public abstract ApiFuture<Void> beginTransactionAsync()

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### bufferedWrite(Mutation arg0)
    
    
    public abstract void bufferedWrite(Mutation arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Mutation`  
  
  
### bufferedWrite(Iterable<Mutation> arg0)
    
    
    public abstract void bufferedWrite(Iterable<Mutation> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<com.google.cloud.spanner.Mutation>`  
  
  
### cancel()
    
    
    public abstract void cancel()

### clearStatementTimeout()
    
    
    public abstract void clearStatementTimeout()

### close()
    
    
    public abstract void close()

### closeAsync()
    
    
    public abstract ApiFuture<Void> closeAsync()

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### commit()
    
    
    public abstract void commit()

### commitAsync()
    
    
    public abstract ApiFuture<Void> commitAsync()

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### execute(Statement arg0)
    
    
    public abstract StatementResult execute(Statement arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatementResult](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.StatementResult)` |   
  
### execute(Statement arg0, Set<StatementResult.ResultType> arg1)
    
    
    public default StatementResult execute(Statement arg0, Set<StatementResult.ResultType> arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[ResultType](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.StatementResult.ResultType)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatementResult](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.StatementResult)` |   
  
### executeAsync(Statement arg0)
    
    
    public abstract AsyncStatementResult executeAsync(Statement arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
**Returns**  
---  
**Type** | **Description**  
`[AsyncStatementResult](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.AsyncStatementResult)` |   
  
### executeBatchUpdate(Iterable<Statement> arg0)
    
    
    public abstract long[] executeBatchUpdate(Iterable<Statement> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<com.google.cloud.spanner.Statement>`  
  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` |   
  
### executeBatchUpdateAsync(Iterable<Statement> arg0)
    
    
    public abstract ApiFuture<long[]> executeBatchUpdateAsync(Iterable<Statement> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<com.google.cloud.spanner.Statement>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]>` |   
  
### executeQuery(Statement arg0, Options.QueryOption[] arg1)
    
    
    public abstract ResultSet executeQuery(Statement arg0, Options.QueryOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `com.google.cloud.spanner.Options.QueryOption[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.ResultSet` |   
  
### executeQueryAsync(Statement arg0, Options.QueryOption[] arg1)
    
    
    public abstract AsyncResultSet executeQueryAsync(Statement arg0, Options.QueryOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `com.google.cloud.spanner.Options.QueryOption[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.AsyncResultSet` |   
  
### executeUpdate(Statement arg0)
    
    
    public abstract long executeUpdate(Statement arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### executeUpdateAsync(Statement arg0)
    
    
    public abstract ApiFuture<Long> executeUpdateAsync(Statement arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` |   
  
### getAutocommitDmlMode()
    
    
    public abstract AutocommitDmlMode getAutocommitDmlMode()

**Returns**  
---  
**Type** | **Description**  
`[AutocommitDmlMode](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.AutocommitDmlMode)` |   
  
### getCommitResponse()
    
    
    public abstract CommitResponse getCommitResponse()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.CommitResponse` |   
  
### getCommitTimestamp()
    
    
    public abstract Timestamp getCommitTimestamp()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Timestamp` |   
  
### getDatabaseClient()
    
    
    public default DatabaseClient getDatabaseClient()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.DatabaseClient` |   
  
### getDialect()
    
    
    public default Dialect getDialect()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.Dialect` |   
  
### getMaxPartitionedParallelism()
    
    
    public abstract int getMaxPartitionedParallelism()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMaxPartitions()
    
    
    public abstract int getMaxPartitions()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOptimizerStatisticsPackage()
    
    
    public default String getOptimizerStatisticsPackage()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getOptimizerVersion()
    
    
    public abstract String getOptimizerVersion()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRPCPriority()
    
    
    public default Options.RpcPriority getRPCPriority()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.Options.RpcPriority` |   
  
### getReadOnlyStaleness()
    
    
    public abstract TimestampBound getReadOnlyStaleness()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.TimestampBound` |   
  
### getReadTimestamp()
    
    
    public abstract Timestamp getReadTimestamp()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Timestamp` |   
  
### getSavepointSupport()
    
    
    public abstract SavepointSupport getSavepointSupport()

**Returns**  
---  
**Type** | **Description**  
`[SavepointSupport](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.SavepointSupport)` |   
  
### getStatementTag()
    
    
    public default String getStatementTag()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getStatementTimeout(TimeUnit arg0)
    
    
    public abstract long getStatementTimeout(TimeUnit arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTransactionMode()
    
    
    public abstract TransactionMode getTransactionMode()

**Returns**  
---  
**Type** | **Description**  
`[TransactionMode](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.TransactionMode)` |   
  
### getTransactionRetryListeners()
    
    
    public abstract Iterator<TransactionRetryListener> getTransactionRetryListeners()

**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<[TransactionRetryListener](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.TransactionRetryListener)>` |   
  
### getTransactionTag()
    
    
    public default String getTransactionTag()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasStatementTimeout()
    
    
    public abstract boolean hasStatementTimeout()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isAutoPartitionMode()
    
    
    public abstract boolean isAutoPartitionMode()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isAutocommit()
    
    
    public abstract boolean isAutocommit()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isClosed()
    
    
    public abstract boolean isClosed()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isDataBoostEnabled()
    
    
    public abstract boolean isDataBoostEnabled()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isDdlBatchActive()
    
    
    public abstract boolean isDdlBatchActive()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isDelayTransactionStartUntilFirstWrite()
    
    
    public default boolean isDelayTransactionStartUntilFirstWrite()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isDmlBatchActive()
    
    
    public abstract boolean isDmlBatchActive()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isInTransaction()
    
    
    public abstract boolean isInTransaction()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isReadOnly()
    
    
    public abstract boolean isReadOnly()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isRetryAbortsInternally()
    
    
    public abstract boolean isRetryAbortsInternally()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isReturnCommitStats()
    
    
    public abstract boolean isReturnCommitStats()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTransactionStarted()
    
    
    public abstract boolean isTransactionStarted()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### partitionQuery(Statement arg0, PartitionOptions arg1, Options.QueryOption[] arg2)
    
    
    public abstract ResultSet partitionQuery(Statement arg0, PartitionOptions arg1, Options.QueryOption[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `com.google.cloud.spanner.PartitionOptions`  
  
`arg2` | `com.google.cloud.spanner.Options.QueryOption[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.ResultSet` |   
  
### releaseSavepoint(String arg0)
    
    
    public abstract void releaseSavepoint(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### removeTransactionRetryListener(TransactionRetryListener arg0)
    
    
    public abstract boolean removeTransactionRetryListener(TransactionRetryListener arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[TransactionRetryListener](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.TransactionRetryListener)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### rollback()
    
    
    public abstract void rollback()

### rollbackAsync()
    
    
    public abstract ApiFuture<Void> rollbackAsync()

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### rollbackToSavepoint(String arg0)
    
    
    public abstract void rollbackToSavepoint(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### runBatch()
    
    
    public abstract long[] runBatch()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` |   
  
### runBatchAsync()
    
    
    public abstract ApiFuture<long[]> runBatchAsync()

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]>` |   
  
### runPartition(String arg0)
    
    
    public abstract ResultSet runPartition(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.ResultSet` |   
  
### runPartitionedQuery(Statement arg0, PartitionOptions arg1, Options.QueryOption[] arg2)
    
    
    public abstract PartitionedQueryResultSet runPartitionedQuery(Statement arg0, PartitionOptions arg1, Options.QueryOption[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Statement`  
  
`arg1` | `com.google.cloud.spanner.PartitionOptions`  
  
`arg2` | `com.google.cloud.spanner.Options.QueryOption[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[PartitionedQueryResultSet](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.PartitionedQueryResultSet)` |   
  
### savepoint(String arg0)
    
    
    public abstract void savepoint(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setAutoPartitionMode(boolean arg0)
    
    
    public abstract void setAutoPartitionMode(boolean arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setAutocommit(boolean arg0)
    
    
    public abstract void setAutocommit(boolean arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setAutocommitDmlMode(AutocommitDmlMode arg0)
    
    
    public abstract void setAutocommitDmlMode(AutocommitDmlMode arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[AutocommitDmlMode](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.AutocommitDmlMode)`  
  
  
### setDataBoostEnabled(boolean arg0)
    
    
    public abstract void setDataBoostEnabled(boolean arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setDelayTransactionStartUntilFirstWrite(boolean arg0)
    
    
    public default void setDelayTransactionStartUntilFirstWrite(boolean arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setMaxPartitionedParallelism(int arg0)
    
    
    public abstract void setMaxPartitionedParallelism(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setMaxPartitions(int arg0)
    
    
    public abstract void setMaxPartitions(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setOptimizerStatisticsPackage(String arg0)
    
    
    public default void setOptimizerStatisticsPackage(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setOptimizerVersion(String arg0)
    
    
    public abstract void setOptimizerVersion(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setRPCPriority(Options.RpcPriority arg0)
    
    
    public default void setRPCPriority(Options.RpcPriority arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Options.RpcPriority`  
  
  
### setReadOnly(boolean arg0)
    
    
    public abstract void setReadOnly(boolean arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setReadOnlyStaleness(TimestampBound arg0)
    
    
    public abstract void setReadOnlyStaleness(TimestampBound arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.TimestampBound`  
  
  
### setRetryAbortsInternally(boolean arg0)
    
    
    public abstract void setRetryAbortsInternally(boolean arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setReturnCommitStats(boolean arg0)
    
    
    public abstract void setReturnCommitStats(boolean arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setSavepointSupport(SavepointSupport arg0)
    
    
    public abstract void setSavepointSupport(SavepointSupport arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[SavepointSupport](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.SavepointSupport)`  
  
  
### setStatementTag(String arg0)
    
    
    public default void setStatementTag(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setStatementTimeout(long arg0, TimeUnit arg1)
    
    
    public abstract void setStatementTimeout(long arg0, TimeUnit arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`arg1` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
  
### setTransactionMode(TransactionMode arg0)
    
    
    public abstract void setTransactionMode(TransactionMode arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[TransactionMode](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.TransactionMode)`  
  
  
### setTransactionTag(String arg0)
    
    
    public default void setTransactionTag(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### startBatchDdl()
    
    
    public abstract void startBatchDdl()

### startBatchDml()
    
    
    public abstract void startBatchDml()

### write(Mutation arg0)
    
    
    public abstract void write(Mutation arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Mutation`  
  
  
### write(Iterable<Mutation> arg0)
    
    
    public abstract void write(Iterable<Mutation> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<com.google.cloud.spanner.Mutation>`  
  
  
### writeAsync(Mutation arg0)
    
    
    public abstract ApiFuture<Void> writeAsync(Mutation arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.cloud.spanner.Mutation`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### writeAsync(Iterable<Mutation> arg0)
    
    
    public abstract ApiFuture<Void> writeAsync(Iterable<Mutation> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<com.google.cloud.spanner.Mutation>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
