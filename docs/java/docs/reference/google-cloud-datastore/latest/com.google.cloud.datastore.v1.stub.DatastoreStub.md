---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.v1.stub.DatastoreStub
title: Class DatastoreStub (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:56.244492+00:00
---

# Class DatastoreStub (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.v1.stub.DatastoreStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DatastoreStub (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public abstract class DatastoreStub implements BackgroundResource

Base stub class for the Datastore service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatastoreStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

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

### DatastoreStub()
    
    
    public DatastoreStub()

## Methods 

### allocateIdsCallable()
    
    
    public UnaryCallable<AllocateIdsRequest,AllocateIdsResponse> allocateIdsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AllocateIdsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.AllocateIdsRequest),[AllocateIdsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.AllocateIdsResponse)>` |   
  
### beginTransactionCallable()
    
    
    public UnaryCallable<BeginTransactionRequest,BeginTransactionResponse> beginTransactionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BeginTransactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.BeginTransactionRequest),[BeginTransactionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.BeginTransactionResponse)>` |   
  
### close()
    
    
    public abstract void close()

### commitCallable()
    
    
    public UnaryCallable<CommitRequest,CommitResponse> commitCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CommitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.CommitRequest),[CommitResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.CommitResponse)>` |   
  
### lookupCallable()
    
    
    public UnaryCallable<LookupRequest,LookupResponse> lookupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.LookupRequest),[LookupResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.LookupResponse)>` |   
  
### reserveIdsCallable()
    
    
    public UnaryCallable<ReserveIdsRequest,ReserveIdsResponse> reserveIdsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReserveIdsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.ReserveIdsRequest),[ReserveIdsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.ReserveIdsResponse)>` |   
  
### rollbackCallable()
    
    
    public UnaryCallable<RollbackRequest,RollbackResponse> rollbackCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RollbackRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RollbackRequest),[RollbackResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RollbackResponse)>` |   
  
### runAggregationQueryCallable()
    
    
    public UnaryCallable<RunAggregationQueryRequest,RunAggregationQueryResponse> runAggregationQueryCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunAggregationQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunAggregationQueryRequest),[RunAggregationQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunAggregationQueryResponse)>` |   
  
### runQueryCallable()
    
    
    public UnaryCallable<RunQueryRequest,RunQueryResponse> runQueryCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunQueryRequest),[RunQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.RunQueryResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
