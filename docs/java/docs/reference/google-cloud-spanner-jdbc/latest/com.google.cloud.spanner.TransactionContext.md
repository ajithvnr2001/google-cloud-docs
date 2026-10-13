---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.TransactionContext
title: Interface TransactionContext (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:29.581554+00:00
---

# Interface TransactionContext (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.TransactionContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransactionContext (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 
    
    
    public interface TransactionContext extends ReadContext

## Implements

[ReadContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ReadContext)

## Methods 

### analyzeUpdate(Statement arg0, ReadContext.QueryAnalyzeMode arg1, Options.UpdateOption[] arg2) (deprecated)
    
    
    public default ResultSetStats analyzeUpdate(Statement arg0, ReadContext.QueryAnalyzeMode arg1, Options.UpdateOption[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)`  
  
`arg1` | `[QueryAnalyzeMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ReadContext.QueryAnalyzeMode)`  
  
`arg2` | `[UpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.UpdateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.spanner.v1.ResultSetStats` |   
  
### analyzeUpdateStatement(Statement arg0, ReadContext.QueryAnalyzeMode arg1, Options.UpdateOption[] arg2)
    
    
    public default ResultSet analyzeUpdateStatement(Statement arg0, ReadContext.QueryAnalyzeMode arg1, Options.UpdateOption[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)`  
  
`arg1` | `[QueryAnalyzeMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ReadContext.QueryAnalyzeMode)`  
  
`arg2` | `[UpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.UpdateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ResultSet)` |   
  
### batchUpdate(Iterable<Statement> arg0, Options.UpdateOption[] arg1)
    
    
    public abstract long[] batchUpdate(Iterable<Statement> arg0, Options.UpdateOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)>`  
  
`arg1` | `[UpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.UpdateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` |   
  
### batchUpdateAsync(Iterable<Statement> arg0, Options.UpdateOption[] arg1)
    
    
    public abstract ApiFuture<long[]> batchUpdateAsync(Iterable<Statement> arg0, Options.UpdateOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)>`  
  
`arg1` | `[UpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.UpdateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]>` |   
  
### buffer(Mutation arg0)
    
    
    public abstract void buffer(Mutation arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation)`  
  
  
### buffer(Iterable<Mutation> arg0)
    
    
    public abstract void buffer(Iterable<Mutation> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation)>`  
  
  
### bufferAsync(Mutation arg0)
    
    
    public default ApiFuture<Void> bufferAsync(Mutation arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### bufferAsync(Iterable<Mutation> arg0)
    
    
    public default ApiFuture<Void> bufferAsync(Iterable<Mutation> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### executeUpdate(Statement arg0, Options.UpdateOption[] arg1)
    
    
    public abstract long executeUpdate(Statement arg0, Options.UpdateOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)`  
  
`arg1` | `[UpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.UpdateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### executeUpdateAsync(Statement arg0, Options.UpdateOption[] arg1)
    
    
    public abstract ApiFuture<Long> executeUpdateAsync(Statement arg0, Options.UpdateOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)`  
  
`arg1` | `[UpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.UpdateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
