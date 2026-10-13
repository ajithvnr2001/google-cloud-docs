---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.HttpJsonContentServiceStub
title: Class HttpJsonContentServiceStub (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:00.364990+00:00
---

# Class HttpJsonContentServiceStub (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.HttpJsonContentServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonContentServiceStub (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class HttpJsonContentServiceStub extends ContentServiceStub

REST stub implementation for the ContentService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ContentServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub) > HttpJsonContentServiceStub

## Inherited Members

[ContentServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_close__)

[ContentServiceStub.getContentCallable()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_getContentCallable__)

[ContentServiceStub.listContentCallable()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_listContentCallable__)

[ContentServiceStub.listContentPagedCallable()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_listContentPagedCallable__)

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

### create(ContentServiceStubSettings settings)
    
    
    public static final HttpJsonContentServiceStub create(ContentServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ContentServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonContentServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.HttpJsonContentServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext)
    
    
    public static final HttpJsonContentServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonContentServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.HttpJsonContentServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonContentServiceStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonContentServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.HttpJsonContentServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getMethodDescriptors()
    
    
    public static List<ApiMethodDescriptor> getMethodDescriptors()

**Internal Only** : This feature is not stable for application use.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ApiMethodDescriptor](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.ApiMethodDescriptor.html)>` |   
  
## Constructors 

### HttpJsonContentServiceStub(ContentServiceStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonContentServiceStub(ContentServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonContentServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[ContentServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonContentServiceStub(ContentServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonContentServiceStub(ContentServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonContentServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[ContentServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

**Overrides**

[ContentServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_close__)

### getContentCallable()
    
    
    public UnaryCallable<GetContentRequest,Content> getContentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetContentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetContentRequest),[Content](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Content)>` |   
**Overrides**

[ContentServiceStub.getContentCallable()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_getContentCallable__)

### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listContentCallable()
    
    
    public UnaryCallable<ListContentRequest,ListContentResponse> listContentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentRequest),[ListContentResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentResponse)>` |   
**Overrides**

[ContentServiceStub.listContentCallable()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_listContentCallable__)

### listContentPagedCallable()
    
    
    public UnaryCallable<ListContentRequest,ContentServiceClient.ListContentPagedResponse> listContentPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentRequest),[ListContentPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentServiceClient.ListContentPagedResponse)>` |   
**Overrides**

[ContentServiceStub.listContentPagedCallable()](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentServiceStub#com_google_ads_admanager_v1_stub_ContentServiceStub_listContentPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
