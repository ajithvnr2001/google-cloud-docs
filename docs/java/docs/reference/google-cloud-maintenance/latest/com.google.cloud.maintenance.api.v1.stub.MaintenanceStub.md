---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub
title: Class MaintenanceStub (0.33.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:05.821305+00:00
---

# Class MaintenanceStub (0.33.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.stub.MaintenanceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MaintenanceStub (0.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.33.0 (latest)  0.29.0  0.28.0  0.27.0  0.25.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public abstract class MaintenanceStub implements BackgroundResource

Base stub class for the Maintenance service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MaintenanceStub

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

### MaintenanceStub()
    
    
    public MaintenanceStub()

## Methods 

### close()
    
    
    public abstract void close()

### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getResourceMaintenanceCallable()
    
    
    public UnaryCallable<GetResourceMaintenanceRequest,ResourceMaintenance> getResourceMaintenanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetResourceMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.GetResourceMaintenanceRequest),[ResourceMaintenance](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ResourceMaintenance)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,MaintenanceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.MaintenanceClient.ListLocationsPagedResponse)>` |   
  
### listResourceMaintenancesCallable()
    
    
    public UnaryCallable<ListResourceMaintenancesRequest,ListResourceMaintenancesResponse> listResourceMaintenancesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ListResourceMaintenancesRequest),[ListResourceMaintenancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ListResourceMaintenancesResponse)>` |   
  
### listResourceMaintenancesPagedCallable()
    
    
    public UnaryCallable<ListResourceMaintenancesRequest,MaintenanceClient.ListResourceMaintenancesPagedResponse> listResourceMaintenancesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.ListResourceMaintenancesRequest),[ListResourceMaintenancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.MaintenanceClient.ListResourceMaintenancesPagedResponse)>` |   
  
### summarizeMaintenancesCallable()
    
    
    public UnaryCallable<SummarizeMaintenancesRequest,SummarizeMaintenancesResponse> summarizeMaintenancesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SummarizeMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.SummarizeMaintenancesRequest),[SummarizeMaintenancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.SummarizeMaintenancesResponse)>` |   
  
### summarizeMaintenancesPagedCallable()
    
    
    public UnaryCallable<SummarizeMaintenancesRequest,MaintenanceClient.SummarizeMaintenancesPagedResponse> summarizeMaintenancesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SummarizeMaintenancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.SummarizeMaintenancesRequest),[SummarizeMaintenancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-maintenance/latest/com.google.cloud.maintenance.api.v1.MaintenanceClient.SummarizeMaintenancesPagedResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
