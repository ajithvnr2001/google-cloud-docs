---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.spi.v1.HttpDatastoreRpc
title: Class HttpDatastoreRpc (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:44.015857+00:00
---

# Class HttpDatastoreRpc (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.spi.v1.HttpDatastoreRpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpDatastoreRpc (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public class HttpDatastoreRpc implements DatastoreRpc

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HttpDatastoreRpc

## Implements

[DatastoreRpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.spi.v1.DatastoreRpc)

## Inherited Members

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

## Constructors 

### HttpDatastoreRpc(DatastoreOptions options)
    
    
    public HttpDatastoreRpc(DatastoreOptions options)

**Parameter**  
---  
**Name** | **Description**  
`options` | `[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions)`  
  
  
## Methods 

### allocateIds(AllocateIdsRequest request)
    
    
    public AllocateIdsResponse allocateIds(AllocateIdsRequest request)

Sends an allocate IDs request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AllocateIdsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.AllocateIdsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocateIdsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.AllocateIdsResponse)` |   
  
### beginTransaction(BeginTransactionRequest request)
    
    
    public BeginTransactionResponse beginTransaction(BeginTransactionRequest request)

Sends a begin transaction request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BeginTransactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.BeginTransactionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BeginTransactionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.BeginTransactionResponse)` |   
  
### close()
    
    
    public void close()

**Exceptions**  
---  
**Type** | **Description**  
`[Exception](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)` |   
  
### commit(CommitRequest request)
    
    
    public CommitResponse commit(CommitRequest request)

Sends a commit request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CommitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.CommitRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CommitResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.CommitResponse)` |   
  
### isClosed()
    
    
    public boolean isClosed()

Returns true if this background resource has been shut down.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### lookup(LookupRequest request)
    
    
    public LookupResponse lookup(LookupRequest request)

Sends a lookup request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.LookupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LookupResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.LookupResponse)` |   
  
### reserveIds(ReserveIdsRequest request)
    
    
    public ReserveIdsResponse reserveIds(ReserveIdsRequest request)

Sends a reserveIds request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReserveIdsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.ReserveIdsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReserveIdsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.ReserveIdsResponse)` |   
  
### rollback(RollbackRequest request)
    
    
    public RollbackResponse rollback(RollbackRequest request)

Sends a rollback request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RollbackRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RollbackRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RollbackResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RollbackResponse)` |   
  
### runAggregationQuery(RunAggregationQueryRequest request)
    
    
    public RunAggregationQueryResponse runAggregationQuery(RunAggregationQueryRequest request)

Sends a request to run an aggregation query.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunAggregationQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunAggregationQueryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RunAggregationQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunAggregationQueryResponse)` |   
  
### runQuery(RunQueryRequest request)
    
    
    public RunQueryResponse runQuery(RunQueryRequest request)

Sends a request to run a query.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunQueryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RunQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunQueryResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
