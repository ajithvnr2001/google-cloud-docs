---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.HttpJsonMaintenanceStub
title: Class HttpJsonMaintenanceStub (0.33.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:28.184267+00:00
---

# Class HttpJsonMaintenanceStub (0.33.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.HttpJsonMaintenanceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonMaintenanceStub (0.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.33.0 (latest)  0.29.0  0.28.0  0.27.0  0.25.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public class HttpJsonMaintenanceStub extends MaintenanceStub

REST stub implementation for the Maintenance service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [MaintenanceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub) > HttpJsonMaintenanceStub

## Inherited Members

[MaintenanceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_close__)

[MaintenanceStub.getLocationCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_getLocationCallable__)

[MaintenanceStub.getResourceMaintenanceCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_getResourceMaintenanceCallable__)

[MaintenanceStub.listLocationsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listLocationsCallable__)

[MaintenanceStub.listLocationsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listLocationsPagedCallable__)

[MaintenanceStub.listResourceMaintenancesCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listResourceMaintenancesCallable__)

[MaintenanceStub.listResourceMaintenancesPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listResourceMaintenancesPagedCallable__)

[MaintenanceStub.summarizeMaintenancesCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_summarizeMaintenancesCallable__)

[MaintenanceStub.summarizeMaintenancesPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_summarizeMaintenancesPagedCallable__)

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
    
    
    public static final HttpJsonMaintenanceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonMaintenanceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.HttpJsonMaintenanceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonMaintenanceStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonMaintenanceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.HttpJsonMaintenanceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MaintenanceStubSettings settings)
    
    
    public static final HttpJsonMaintenanceStub create(MaintenanceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MaintenanceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonMaintenanceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.HttpJsonMaintenanceStub)` |   
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

### HttpJsonMaintenanceStub(MaintenanceStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonMaintenanceStub(MaintenanceStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonMaintenanceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[MaintenanceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonMaintenanceStub(MaintenanceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonMaintenanceStub(MaintenanceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonMaintenanceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[MaintenanceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStubSettings)`  
  
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

[MaintenanceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_close__)

### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
**Overrides**

[MaintenanceStub.getLocationCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_getLocationCallable__)

### getResourceMaintenanceCallable()
    
    
    public UnaryCallable<GetResourceMaintenanceRequest,ResourceMaintenance> getResourceMaintenanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetResourceMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.GetResourceMaintenanceRequest),[ResourceMaintenance](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ResourceMaintenance)>` |   
**Overrides**

[MaintenanceStub.getResourceMaintenanceCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_getResourceMaintenanceCallable__)

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
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
**Overrides**

[MaintenanceStub.listLocationsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listLocationsCallable__)

### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,MaintenanceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.MaintenanceClient.ListLocationsPagedResponse)>` |   
**Overrides**

[MaintenanceStub.listLocationsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listLocationsPagedCallable__)

### listResourceMaintenancesCallable()
    
    
    public UnaryCallable<ListResourceMaintenancesRequest,ListResourceMaintenancesResponse> listResourceMaintenancesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ListResourceMaintenancesRequest),[ListResourceMaintenancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ListResourceMaintenancesResponse)>` |   
**Overrides**

[MaintenanceStub.listResourceMaintenancesCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listResourceMaintenancesCallable__)

### listResourceMaintenancesPagedCallable()
    
    
    public UnaryCallable<ListResourceMaintenancesRequest,MaintenanceClient.ListResourceMaintenancesPagedResponse> listResourceMaintenancesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ListResourceMaintenancesRequest),[ListResourceMaintenancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.MaintenanceClient.ListResourceMaintenancesPagedResponse)>` |   
**Overrides**

[MaintenanceStub.listResourceMaintenancesPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_listResourceMaintenancesPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### summarizeMaintenancesCallable()
    
    
    public UnaryCallable<SummarizeMaintenancesRequest,SummarizeMaintenancesResponse> summarizeMaintenancesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SummarizeMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.SummarizeMaintenancesRequest),[SummarizeMaintenancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.SummarizeMaintenancesResponse)>` |   
**Overrides**

[MaintenanceStub.summarizeMaintenancesCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_summarizeMaintenancesCallable__)

### summarizeMaintenancesPagedCallable()
    
    
    public UnaryCallable<SummarizeMaintenancesRequest,MaintenanceClient.SummarizeMaintenancesPagedResponse> summarizeMaintenancesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SummarizeMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.SummarizeMaintenancesRequest),[SummarizeMaintenancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.MaintenanceClient.SummarizeMaintenancesPagedResponse)>` |   
**Overrides**

[MaintenanceStub.summarizeMaintenancesPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub#com_google_cloud_maintenance_api_v1_stub_MaintenanceStub_summarizeMaintenancesPagedCallable__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
