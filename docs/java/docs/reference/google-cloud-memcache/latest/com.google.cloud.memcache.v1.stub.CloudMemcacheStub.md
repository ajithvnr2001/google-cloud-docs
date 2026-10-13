---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.stub.CloudMemcacheStub
title: Class CloudMemcacheStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:36.626718+00:00
---

# Class CloudMemcacheStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.stub.CloudMemcacheStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudMemcacheStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.6  2.2.1  2.1.11 
    
    
    public abstract class CloudMemcacheStub implements BackgroundResource

Base stub class for the CloudMemcache service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudMemcacheStub

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

### CloudMemcacheStub()
    
    
    public CloudMemcacheStub()

## Methods 

### applyParametersCallable()
    
    
    public UnaryCallable<ApplyParametersRequest,Operation> applyParametersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ApplyParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.ApplyParametersRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### applyParametersOperationCallable()
    
    
    public OperationCallable<ApplyParametersRequest,Instance,OperationMetadata> applyParametersOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ApplyParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.ApplyParametersRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.OperationMetadata)>` |   
  
### close()
    
    
    public abstract void close()

### createInstanceCallable()
    
    
    public UnaryCallable<CreateInstanceRequest,Operation> createInstanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInstanceOperationCallable()
    
    
    public OperationCallable<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.OperationMetadata)>` |   
  
### deleteInstanceCallable()
    
    
    public UnaryCallable<DeleteInstanceRequest,Operation> deleteInstanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationCallable()
    
    
    public OperationCallable<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.OperationMetadata)>` |   
  
### getHttpJsonOperationsStub()
    
    
    public @Nullable OperationsStub getHttpJsonOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.gax.httpjson.longrunning.stub.OperationsStub` |   
  
### getInstanceCallable()
    
    
    public UnaryCallable<GetInstanceRequest,Instance> getInstanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.Instance)>` |   
  
### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### listInstancesCallable()
    
    
    public UnaryCallable<ListInstancesRequest,ListInstancesResponse> listInstancesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.ListInstancesResponse)>` |   
  
### listInstancesPagedCallable()
    
    
    public UnaryCallable<ListInstancesRequest,CloudMemcacheClient.ListInstancesPagedResponse> listInstancesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.ListInstancesRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.CloudMemcacheClient.ListInstancesPagedResponse)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,CloudMemcacheClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.CloudMemcacheClient.ListLocationsPagedResponse)>` |   
  
### rescheduleMaintenanceCallable()
    
    
    public UnaryCallable<RescheduleMaintenanceRequest,Operation> rescheduleMaintenanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.RescheduleMaintenanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rescheduleMaintenanceOperationCallable()
    
    
    public OperationCallable<RescheduleMaintenanceRequest,Instance,OperationMetadata> rescheduleMaintenanceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.RescheduleMaintenanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.OperationMetadata)>` |   
  
### updateInstanceCallable()
    
    
    public UnaryCallable<UpdateInstanceRequest,Operation> updateInstanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstanceOperationCallable()
    
    
    public OperationCallable<UpdateInstanceRequest,Instance,OperationMetadata> updateInstanceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.UpdateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.OperationMetadata)>` |   
  
### updateParametersCallable()
    
    
    public UnaryCallable<UpdateParametersRequest,Operation> updateParametersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.UpdateParametersRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateParametersOperationCallable()
    
    
    public OperationCallable<UpdateParametersRequest,Instance,OperationMetadata> updateParametersOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.UpdateParametersRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-memcache/latest/com.google.cloud.memcache.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
