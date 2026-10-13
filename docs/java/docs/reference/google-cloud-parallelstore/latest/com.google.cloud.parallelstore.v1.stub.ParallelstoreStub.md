---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.stub.ParallelstoreStub
title: Class ParallelstoreStub (0.62.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:17.272958+00:00
---

# Class ParallelstoreStub (0.62.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.stub.ParallelstoreStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParallelstoreStub (0.62.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class ParallelstoreStub implements BackgroundResource

Base stub class for the Parallelstore service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ParallelstoreStub

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

### ParallelstoreStub()
    
    
    public ParallelstoreStub()

## Methods 

### close()
    
    
    public abstract void close()

### createInstanceCallable()
    
    
    public UnaryCallable<CreateInstanceRequest,Operation> createInstanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInstanceOperationCallable()
    
    
    public OperationCallable<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### deleteInstanceCallable()
    
    
    public UnaryCallable<DeleteInstanceRequest,Operation> deleteInstanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationCallable()
    
    
    public OperationCallable<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### exportDataCallable()
    
    
    public UnaryCallable<ExportDataRequest,Operation> exportDataCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportDataOperationCallable()
    
    
    public OperationCallable<ExportDataRequest,ExportDataResponse,ExportDataMetadata> exportDataOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataRequest),[ExportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataResponse),[ExportDataMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataMetadata)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)>` |   
  
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
  
### importDataCallable()
    
    
    public UnaryCallable<ImportDataRequest,Operation> importDataCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDataOperationCallable()
    
    
    public OperationCallable<ImportDataRequest,ImportDataResponse,ImportDataMetadata> importDataOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataRequest),[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataResponse),[ImportDataMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataMetadata)>` |   
  
### listInstancesCallable()
    
    
    public UnaryCallable<ListInstancesRequest,ListInstancesResponse> listInstancesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ListInstancesResponse)>` |   
  
### listInstancesPagedCallable()
    
    
    public UnaryCallable<ListInstancesRequest,ParallelstoreClient.ListInstancesPagedResponse> listInstancesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ListInstancesRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListInstancesPagedResponse)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ParallelstoreClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListLocationsPagedResponse)>` |   
  
### updateInstanceCallable()
    
    
    public UnaryCallable<UpdateInstanceRequest,Operation> updateInstanceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstanceOperationCallable()
    
    
    public OperationCallable<UpdateInstanceRequest,Instance,OperationMetadata> updateInstanceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.UpdateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
