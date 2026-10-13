---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.stub.readrows.ReadRowsResumptionStrategy
title: Class ReadRowsResumptionStrategy (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:39.305286+00:00
---

# Class ReadRowsResumptionStrategy (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.stub.readrows.ReadRowsResumptionStrategy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReadRowsResumptionStrategy (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public class ReadRowsResumptionStrategy implements StreamResumptionStrategy<Storage.ReadRowsRequest,Storage.ReadRowsResponse>

An implementation of a [StreamResumptionStrategy](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.StreamResumptionStrategy.html) for the ReadRows API. This class tracks the offset of the last row received and, upon retry, attempts to resume the stream at the next offset.

This class is considered an internal implementation detail and not meant to be used by applications.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReadRowsResumptionStrategy

## Implements

[StreamResumptionStrategy](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.StreamResumptionStrategy.html)<[ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsRequest),[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsResponse)>

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

### ReadRowsResumptionStrategy()
    
    
    public ReadRowsResumptionStrategy()

## Methods 

### canResume()
    
    
    public boolean canResume()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### createNew()
    
    
    public StreamResumptionStrategy<Storage.ReadRowsRequest,Storage.ReadRowsResponse> createNew()

**Returns**  
---  
**Type** | **Description**  
`[StreamResumptionStrategy](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.StreamResumptionStrategy.html)<[ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsRequest),[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsResponse)>` |   
  
### getResumeRequest(Storage.ReadRowsRequest originalRequest)
    
    
    public Storage.ReadRowsRequest getResumeRequest(Storage.ReadRowsRequest originalRequest)

Given the initial/original request, this implementation generates a request that will yield a new stream whose first response would come right after the last response received by processResponse. It takes into account the offset from the original request.

**Parameter**  
---  
**Name** | **Description**  
`originalRequest` | `[Storage.ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsRequest)` |   
  
### processResponse(Storage.ReadRowsResponse response)
    
    
    public Storage.ReadRowsResponse processResponse(Storage.ReadRowsResponse response)

**Parameter**  
---  
**Name** | **Description**  
`response` | `[Storage.ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsResponse)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadRowsResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
