---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityTypesGrpc
title: Class EntityTypesGrpc (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:44.452431+00:00
---

# Class EntityTypesGrpc (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityTypesGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EntityTypesGrpc (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public final class EntityTypesGrpc

Service for managing EntityTypes.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EntityTypesGrpc

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(EntityTypesGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(EntityTypesGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[EntityTypesGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityTypesGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getBatchCreateEntitiesMethod()
    
    
    public static MethodDescriptor<BatchCreateEntitiesRequest,Operation> getBatchCreateEntitiesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchCreateEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BatchCreateEntitiesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBatchDeleteEntitiesMethod()
    
    
    public static MethodDescriptor<BatchDeleteEntitiesRequest,Operation> getBatchDeleteEntitiesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchDeleteEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BatchDeleteEntitiesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBatchDeleteEntityTypesMethod()
    
    
    public static MethodDescriptor<BatchDeleteEntityTypesRequest,Operation> getBatchDeleteEntityTypesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchDeleteEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BatchDeleteEntityTypesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBatchUpdateEntitiesMethod()
    
    
    public static MethodDescriptor<BatchUpdateEntitiesRequest,Operation> getBatchUpdateEntitiesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchUpdateEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BatchUpdateEntitiesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBatchUpdateEntityTypesMethod()
    
    
    public static MethodDescriptor<BatchUpdateEntityTypesRequest,Operation> getBatchUpdateEntityTypesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BatchUpdateEntityTypesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateEntityTypeMethod()
    
    
    public static MethodDescriptor<CreateEntityTypeRequest,EntityType> getCreateEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.CreateEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityType)>` |   
  
### getDeleteEntityTypeMethod()
    
    
    public static MethodDescriptor<DeleteEntityTypeRequest,Empty> getDeleteEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.DeleteEntityTypeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetEntityTypeMethod()
    
    
    public static MethodDescriptor<GetEntityTypeRequest,EntityType> getGetEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.GetEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityType)>` |   
  
### getListEntityTypesMethod()
    
    
    public static MethodDescriptor<ListEntityTypesRequest,ListEntityTypesResponse> getListEntityTypesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListEntityTypesRequest),[ListEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListEntityTypesResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateEntityTypeMethod()
    
    
    public static MethodDescriptor<UpdateEntityTypeRequest,EntityType> getUpdateEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.UpdateEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityType)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static EntityTypesGrpc.EntityTypesBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesGrpc.EntityTypesBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityTypesGrpc.EntityTypesBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static EntityTypesGrpc.EntityTypesBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesGrpc.EntityTypesBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityTypesGrpc.EntityTypesBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static EntityTypesGrpc.EntityTypesFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesGrpc.EntityTypesFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityTypesGrpc.EntityTypesFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static EntityTypesGrpc.EntityTypesStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesGrpc.EntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.EntityTypesGrpc.EntityTypesStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
