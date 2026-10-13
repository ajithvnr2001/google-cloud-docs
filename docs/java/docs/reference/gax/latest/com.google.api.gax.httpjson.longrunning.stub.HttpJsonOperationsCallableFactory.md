---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.stub.HttpJsonOperationsCallableFactory
title: Class HttpJsonOperationsCallableFactory (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:10.733542+00:00
---

# Class HttpJsonOperationsCallableFactory (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.stub.HttpJsonOperationsCallableFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonOperationsCallableFactory (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 
    
    
    public class HttpJsonOperationsCallableFactory implements HttpJsonStubCallableFactory<Operation,BackgroundResource>

REST callable factory implementation for the Operations service API.

This class is for advanced usage.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HttpJsonOperationsCallableFactory

## Implements

com.google.api.gax.httpjson.HttpJsonStubCallableFactory<com.google.longrunning.Operation,com.google.api.gax.core.BackgroundResource>

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

### HttpJsonOperationsCallableFactory()
    
    
    public HttpJsonOperationsCallableFactory()

## Methods 

### <RequestT,ResponseT,MetadataT>createOperationCallable(HttpJsonCallSettings<RequestT,Operation> httpJsonCallSettings, OperationCallSettings<RequestT,ResponseT,MetadataT> callSettings, ClientContext clientContext, BackgroundResource operationsStub)
    
    
    public OperationCallable<RequestT,ResponseT,MetadataT> <RequestT,ResponseT,MetadataT>createOperationCallable(HttpJsonCallSettings<RequestT,Operation> httpJsonCallSettings, OperationCallSettings<RequestT,ResponseT,MetadataT> callSettings, ClientContext clientContext, BackgroundResource operationsStub)

**Parameters**  
---  
**Name** | **Description**  
`httpJsonCallSettings` | `[HttpJsonCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonCallSettings)<RequestT,[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation)>`  
  
`callSettings` | `[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings)<RequestT,ResponseT,MetadataT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
  
`operationsStub` | `[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable)<RequestT,ResponseT,MetadataT>` |   
  
### <RequestT,ResponseT,PagedListResponseT>createPagedCallable(HttpJsonCallSettings<RequestT,ResponseT> httpJsonCallSettings, PagedCallSettings<RequestT,ResponseT,PagedListResponseT> callSettings, ClientContext clientContext)
    
    
    public UnaryCallable<RequestT,PagedListResponseT> <RequestT,ResponseT,PagedListResponseT>createPagedCallable(HttpJsonCallSettings<RequestT,ResponseT> httpJsonCallSettings, PagedCallSettings<RequestT,ResponseT,PagedListResponseT> callSettings, ClientContext clientContext)

Create a paged callable object that represents a paged API method. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`httpJsonCallSettings` | `[HttpJsonCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonCallSettings)<RequestT,ResponseT>`  
  
`callSettings` | `[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings)<RequestT,ResponseT,PagedListResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,PagedListResponseT>` |   
  
### <RequestT,ResponseT>createBatchingCallable(HttpJsonCallSettings<RequestT,ResponseT> httpJsonCallSettings, BatchingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)
    
    
    public UnaryCallable<RequestT,ResponseT> <RequestT,ResponseT>createBatchingCallable(HttpJsonCallSettings<RequestT,ResponseT> httpJsonCallSettings, BatchingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

Create a callable object that represents a batching API method. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`httpJsonCallSettings` | `[HttpJsonCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonCallSettings)<RequestT,ResponseT>`  
  
`callSettings` | `[BatchingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchingCallSettings)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>` |   
  
### <RequestT,ResponseT>createUnaryCallable(HttpJsonCallSettings<RequestT,ResponseT> httpJsonCallSettings, UnaryCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)
    
    
    public UnaryCallable<RequestT,ResponseT> <RequestT,ResponseT>createUnaryCallable(HttpJsonCallSettings<RequestT,ResponseT> httpJsonCallSettings, UnaryCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

Create a callable object with http/json-specific functionality. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`httpJsonCallSettings` | `[HttpJsonCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonCallSettings)<RequestT,ResponseT>`  
  
`callSettings` | `[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
