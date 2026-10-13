---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.HttpJsonImageVersionsStub
title: Class HttpJsonImageVersionsStub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:42.996272+00:00
---

# Class HttpJsonImageVersionsStub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.HttpJsonImageVersionsStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonImageVersionsStub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class HttpJsonImageVersionsStub extends ImageVersionsStub

REST stub implementation for the ImageVersions service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ImageVersionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStub) > HttpJsonImageVersionsStub

## Inherited Members

[ImageVersionsStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStub#com_google_cloud_orchestration_airflow_service_v1beta1_stub_ImageVersionsStub_close__)

[ImageVersionsStub.listImageVersionsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStub#com_google_cloud_orchestration_airflow_service_v1beta1_stub_ImageVersionsStub_listImageVersionsCallable__)

[ImageVersionsStub.listImageVersionsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStub#com_google_cloud_orchestration_airflow_service_v1beta1_stub_ImageVersionsStub_listImageVersionsPagedCallable__)

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

### create(ClientContext clientContext)
    
    
    public static final HttpJsonImageVersionsStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonImageVersionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.HttpJsonImageVersionsStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonImageVersionsStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonImageVersionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.HttpJsonImageVersionsStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ImageVersionsStubSettings settings)
    
    
    public static final HttpJsonImageVersionsStub create(ImageVersionsStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ImageVersionsStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonImageVersionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.HttpJsonImageVersionsStub)` |   
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

### HttpJsonImageVersionsStub(ImageVersionsStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonImageVersionsStub(ImageVersionsStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonImageVersionsStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[ImageVersionsStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonImageVersionsStub(ImageVersionsStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonImageVersionsStub(ImageVersionsStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonImageVersionsStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[ImageVersionsStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStubSettings)`  
  
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

[ImageVersionsStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStub#com_google_cloud_orchestration_airflow_service_v1beta1_stub_ImageVersionsStub_close__)

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
  
### listImageVersionsCallable()
    
    
    public UnaryCallable<ListImageVersionsRequest,ListImageVersionsResponse> listImageVersionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImageVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListImageVersionsRequest),[ListImageVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListImageVersionsResponse)>` |   
**Overrides**

[ImageVersionsStub.listImageVersionsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStub#com_google_cloud_orchestration_airflow_service_v1beta1_stub_ImageVersionsStub_listImageVersionsCallable__)

### listImageVersionsPagedCallable()
    
    
    public UnaryCallable<ListImageVersionsRequest,ImageVersionsClient.ListImageVersionsPagedResponse> listImageVersionsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImageVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListImageVersionsRequest),[ListImageVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ImageVersionsClient.ListImageVersionsPagedResponse)>` |   
**Overrides**

[ImageVersionsStub.listImageVersionsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.stub.ImageVersionsStub#com_google_cloud_orchestration_airflow_service_v1beta1_stub_ImageVersionsStub_listImageVersionsPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
