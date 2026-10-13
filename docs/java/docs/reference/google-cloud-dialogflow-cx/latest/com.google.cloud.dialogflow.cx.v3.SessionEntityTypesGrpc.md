---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesGrpc
title: Class SessionEntityTypesGrpc (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:06.849165+00:00
---

# Class SessionEntityTypesGrpc (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SessionEntityTypesGrpc (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public final class SessionEntityTypesGrpc

Service for managing SessionEntityTypes.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SessionEntityTypesGrpc

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

### bindService(SessionEntityTypesGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(SessionEntityTypesGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[SessionEntityTypesGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateSessionEntityTypeMethod()
    
    
    public static MethodDescriptor<CreateSessionEntityTypeRequest,SessionEntityType> getCreateSessionEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateSessionEntityTypeRequest),[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityType)>` |   
  
### getDeleteSessionEntityTypeMethod()
    
    
    public static MethodDescriptor<DeleteSessionEntityTypeRequest,Empty> getDeleteSessionEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteSessionEntityTypeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetSessionEntityTypeMethod()
    
    
    public static MethodDescriptor<GetSessionEntityTypeRequest,SessionEntityType> getGetSessionEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetSessionEntityTypeRequest),[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityType)>` |   
  
### getListSessionEntityTypesMethod()
    
    
    public static MethodDescriptor<ListSessionEntityTypesRequest,ListSessionEntityTypesResponse> getListSessionEntityTypesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSessionEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListSessionEntityTypesRequest),[ListSessionEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListSessionEntityTypesResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateSessionEntityTypeMethod()
    
    
    public static MethodDescriptor<UpdateSessionEntityTypeRequest,SessionEntityType> getUpdateSessionEntityTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateSessionEntityTypeRequest),[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityType)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static SessionEntityTypesGrpc.SessionEntityTypesBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesGrpc.SessionEntityTypesBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesGrpc.SessionEntityTypesBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static SessionEntityTypesGrpc.SessionEntityTypesBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesGrpc.SessionEntityTypesBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesGrpc.SessionEntityTypesBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static SessionEntityTypesGrpc.SessionEntityTypesFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesGrpc.SessionEntityTypesFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesGrpc.SessionEntityTypesFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static SessionEntityTypesGrpc.SessionEntityTypesStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesGrpc.SessionEntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesGrpc.SessionEntityTypesStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
