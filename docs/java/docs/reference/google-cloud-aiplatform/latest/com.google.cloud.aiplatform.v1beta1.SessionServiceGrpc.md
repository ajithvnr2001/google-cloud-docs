---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SessionServiceGrpc
title: Class SessionServiceGrpc (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:29.881849+00:00
---

# Class SessionServiceGrpc (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SessionServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SessionServiceGrpc (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public final class SessionServiceGrpc

The service that manages Vertex Session related resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SessionServiceGrpc

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

### bindService(SessionServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(SessionServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[SessionServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SessionServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAppendEventMethod()
    
    
    public static MethodDescriptor<AppendEventRequest,AppendEventResponse> getAppendEventMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AppendEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AppendEventRequest),[AppendEventResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AppendEventResponse)>` |   
  
### getCreateSessionMethod()
    
    
    public static MethodDescriptor<CreateSessionRequest,Operation> getCreateSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteSessionMethod()
    
    
    public static MethodDescriptor<DeleteSessionRequest,Operation> getDeleteSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetSessionMethod()
    
    
    public static MethodDescriptor<GetSessionRequest,Session> getGetSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Session)>` |   
  
### getListEventsMethod()
    
    
    public static MethodDescriptor<ListEventsRequest,ListEventsResponse> getListEventsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListEventsRequest),[ListEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListEventsResponse)>` |   
  
### getListSessionsMethod()
    
    
    public static MethodDescriptor<ListSessionsRequest,ListSessionsResponse> getListSessionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListSessionsRequest),[ListSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListSessionsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateSessionMethod()
    
    
    public static MethodDescriptor<UpdateSessionRequest,Session> getUpdateSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Session)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static SessionServiceGrpc.SessionServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceGrpc.SessionServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SessionServiceGrpc.SessionServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static SessionServiceGrpc.SessionServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceGrpc.SessionServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SessionServiceGrpc.SessionServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static SessionServiceGrpc.SessionServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceGrpc.SessionServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SessionServiceGrpc.SessionServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static SessionServiceGrpc.SessionServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceGrpc.SessionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SessionServiceGrpc.SessionServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
