---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Callables
title: Class Callables (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:39.407082+00:00
---

# Class Callables (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Callables

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Callables (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class Callables

Class with utility methods to create callable objects using provided settings.

The callable objects wrap a given direct callable with features like retry and exception translation.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Callables

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

## Static Methods 

### <RequestT,ResponseT,MetadataT>longRunningOperation(UnaryCallable<RequestT,OperationSnapshot> initialCallable, OperationCallSettings<RequestT,ResponseT,MetadataT> operationCallSettings, ClientContext clientContext, LongRunningClient longRunningClient)
    
    
    public static OperationCallable<RequestT,ResponseT,MetadataT> <RequestT,ResponseT,MetadataT>longRunningOperation(UnaryCallable<RequestT,OperationSnapshot> initialCallable, OperationCallSettings<RequestT,ResponseT,MetadataT> operationCallSettings, ClientContext clientContext, LongRunningClient longRunningClient)

Creates a callable object that represents a long-running operation. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`initialCallable` | `[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,[OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot)>`  
the callable that initiates the operation  
`operationCallSettings` | `[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings)<RequestT,ResponseT,MetadataT>`  
[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings) to configure the method-level settings with.  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext) to use to connect to the service.  
`longRunningClient` | `[LongRunningClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LongRunningClient)`  
[LongRunningClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LongRunningClient) to use to poll for updates on the Operation.  
**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable)<RequestT,ResponseT,MetadataT>` | [OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable) callable object.  
  
### <RequestT,ResponseT,PagedListResponseT>paged(UnaryCallable<RequestT,ResponseT> innerCallable, PagedCallSettings<RequestT,ResponseT,PagedListResponseT> pagedCallSettings)
    
    
    public static UnaryCallable<RequestT,PagedListResponseT> <RequestT,ResponseT,PagedListResponseT>paged(UnaryCallable<RequestT,ResponseT> innerCallable, PagedCallSettings<RequestT,ResponseT,PagedListResponseT> pagedCallSettings)

Create a paged callable object that represents a paged API method. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`innerCallable` | `[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>`  
the callable to issue calls  
`pagedCallSettings` | `[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings)<RequestT,ResponseT,PagedListResponseT>`  
[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings) to configure the paged settings with.  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,PagedListResponseT>` | [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) callable object.  
  
### <RequestT,ResponseT>batching(UnaryCallable<RequestT,ResponseT> innerCallable, BatchingCallSettings<RequestT,ResponseT> batchingCallSettings, ClientContext context)
    
    
    public static UnaryCallable<RequestT,ResponseT> <RequestT,ResponseT>batching(UnaryCallable<RequestT,ResponseT> innerCallable, BatchingCallSettings<RequestT,ResponseT> batchingCallSettings, ClientContext context)

Create a callable object that represents a batching API method. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`innerCallable` | `[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>`  
the callable to issue calls  
`batchingCallSettings` | `[BatchingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchingCallSettings)<RequestT,ResponseT>`  
[BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings) to configure the batching related settings with.  
`context` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext) to use to connect to the service.  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>` | [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) callable object.  
  
### <RequestT,ResponseT>resumableUpload(ResumableUploadClient<RequestT,ResponseT> uploadClient, UnaryCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)
    
    
    public static ResumableUploadCallable<RequestT,ResponseT> <RequestT,ResponseT>resumableUpload(ResumableUploadClient<RequestT,ResponseT> uploadClient, UnaryCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Internal Only** : This feature is not stable for application use.

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Creates a [ResumableUploadCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadCallable) to execute resumable uploads. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`uploadClient` | `[ResumableUploadClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.resumable.ResumableUploadClient)<RequestT,ResponseT>`  
client executing the wire-level upload protocol  
`callSettings` | `[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings)<RequestT,ResponseT>`  
[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings) to configure the method-level settings with  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext) to use to connect to the service.  
**Returns**  
---  
**Type** | **Description**  
`[ResumableUploadCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadCallable)<RequestT,ResponseT>` | [ResumableUploadCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadCallable) callable object  
  
### <RequestT,ResponseT>retrying(ServerStreamingCallable<RequestT,ResponseT> innerCallable, ServerStreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)
    
    
    public static ServerStreamingCallable<RequestT,ResponseT> <RequestT,ResponseT>retrying(ServerStreamingCallable<RequestT,ResponseT> innerCallable, ServerStreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`innerCallable` | `[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable)<RequestT,ResponseT>`  
  
`callSettings` | `[ServerStreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable)<RequestT,ResponseT>` |   
  
### <RequestT,ResponseT>retrying(UnaryCallable<RequestT,ResponseT> innerCallable, UnaryCallSettings<?,?> callSettings, ClientContext clientContext)
    
    
    public static UnaryCallable<RequestT,ResponseT> <RequestT,ResponseT>retrying(UnaryCallable<RequestT,ResponseT> innerCallable, UnaryCallSettings<?,?> callSettings, ClientContext clientContext)

Create a callable object that represents a Unary API method. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`innerCallable` | `[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>`  
the callable to issue calls  
`callSettings` | `[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings)<?,?>`  
[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings) to configure the unary call-related settings with.  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext) to use to connect to the service.  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>` | [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) callable object.  
  
### <RequestT,ResponseT>retrying(UnaryCallable<RequestT,ResponseT> innerCallable, UnaryCallSettings<?,?> callSettings, ClientContext clientContext, RequestMutator requestMutator)
    
    
    public static UnaryCallable<RequestT,ResponseT> <RequestT,ResponseT>retrying(UnaryCallable<RequestT,ResponseT> innerCallable, UnaryCallSettings<?,?> callSettings, ClientContext clientContext, RequestMutator requestMutator)

Create a callable object that represents a Unary API method that contains a Request Mutator. Designed for use by generated code.

**Parameters**  
---  
**Name** | **Description**  
`innerCallable` | `[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>`  
the callable to issue calls  
`callSettings` | `[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings)<?,?>`  
[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings) to configure the unary call-related settings with.  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext) to use to connect to the service.  
`requestMutator` | `[RequestMutator](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestMutator)`  
[RequestMutator](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestMutator) to modify the request. Currently only used for autopopulated fields.  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<RequestT,ResponseT>` | [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) callable object.  
  
### <RequestT,ResponseT>watched(ServerStreamingCallable<RequestT,ResponseT> callable, ServerStreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)
    
    
    public static ServerStreamingCallable<RequestT,ResponseT> <RequestT,ResponseT>watched(ServerStreamingCallable<RequestT,ResponseT> callable, ServerStreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`callable` | `[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable)<RequestT,ResponseT>`  
  
`callSettings` | `[ServerStreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable)<RequestT,ResponseT>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
