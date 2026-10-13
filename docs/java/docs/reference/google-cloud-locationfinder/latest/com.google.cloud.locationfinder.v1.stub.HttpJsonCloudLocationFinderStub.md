---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.HttpJsonCloudLocationFinderStub
title: Class HttpJsonCloudLocationFinderStub (0.24.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:34.003437+00:00
---

# Class HttpJsonCloudLocationFinderStub (0.24.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.HttpJsonCloudLocationFinderStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonCloudLocationFinderStub (0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.20.0  0.19.0  0.18.0  0.16.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public class HttpJsonCloudLocationFinderStub extends CloudLocationFinderStub

REST stub implementation for the CloudLocationFinder service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [CloudLocationFinderStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub) > HttpJsonCloudLocationFinderStub

## Inherited Members

[CloudLocationFinderStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_close__)

[CloudLocationFinderStub.getCloudLocationCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_getCloudLocationCallable__)

[CloudLocationFinderStub.listCloudLocationsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_listCloudLocationsCallable__)

[CloudLocationFinderStub.listCloudLocationsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_listCloudLocationsPagedCallable__)

[CloudLocationFinderStub.searchCloudLocationsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_searchCloudLocationsCallable__)

[CloudLocationFinderStub.searchCloudLocationsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_searchCloudLocationsPagedCallable__)

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
    
    
    public static final HttpJsonCloudLocationFinderStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonCloudLocationFinderStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.HttpJsonCloudLocationFinderStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonCloudLocationFinderStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonCloudLocationFinderStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.HttpJsonCloudLocationFinderStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudLocationFinderStubSettings settings)
    
    
    public static final HttpJsonCloudLocationFinderStub create(CloudLocationFinderStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudLocationFinderStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonCloudLocationFinderStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.HttpJsonCloudLocationFinderStub)` |   
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

### HttpJsonCloudLocationFinderStub(CloudLocationFinderStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonCloudLocationFinderStub(CloudLocationFinderStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonCloudLocationFinderStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[CloudLocationFinderStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonCloudLocationFinderStub(CloudLocationFinderStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonCloudLocationFinderStub(CloudLocationFinderStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonCloudLocationFinderStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[CloudLocationFinderStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStubSettings)`  
  
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

[CloudLocationFinderStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_close__)

### getCloudLocationCallable()
    
    
    public UnaryCallable<GetCloudLocationRequest,CloudLocation> getCloudLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCloudLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.GetCloudLocationRequest),[CloudLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.CloudLocation)>` |   
**Overrides**

[CloudLocationFinderStub.getCloudLocationCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_getCloudLocationCallable__)

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
  
### listCloudLocationsCallable()
    
    
    public UnaryCallable<ListCloudLocationsRequest,ListCloudLocationsResponse> listCloudLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.ListCloudLocationsRequest),[ListCloudLocationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.ListCloudLocationsResponse)>` |   
**Overrides**

[CloudLocationFinderStub.listCloudLocationsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_listCloudLocationsCallable__)

### listCloudLocationsPagedCallable()
    
    
    public UnaryCallable<ListCloudLocationsRequest,CloudLocationFinderClient.ListCloudLocationsPagedResponse> listCloudLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.ListCloudLocationsRequest),[ListCloudLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.CloudLocationFinderClient.ListCloudLocationsPagedResponse)>` |   
**Overrides**

[CloudLocationFinderStub.listCloudLocationsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_listCloudLocationsPagedCallable__)

### searchCloudLocationsCallable()
    
    
    public UnaryCallable<SearchCloudLocationsRequest,SearchCloudLocationsResponse> searchCloudLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchCloudLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.SearchCloudLocationsRequest),[SearchCloudLocationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.SearchCloudLocationsResponse)>` |   
**Overrides**

[CloudLocationFinderStub.searchCloudLocationsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_searchCloudLocationsCallable__)

### searchCloudLocationsPagedCallable()
    
    
    public UnaryCallable<SearchCloudLocationsRequest,CloudLocationFinderClient.SearchCloudLocationsPagedResponse> searchCloudLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchCloudLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.SearchCloudLocationsRequest),[SearchCloudLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.CloudLocationFinderClient.SearchCloudLocationsPagedResponse)>` |   
**Overrides**

[CloudLocationFinderStub.searchCloudLocationsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-locationfinder/latest/com.google.cloud.locationfinder.v1.stub.CloudLocationFinderStub#com_google_cloud_locationfinder_v1_stub_CloudLocationFinderStub_searchCloudLocationsPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
