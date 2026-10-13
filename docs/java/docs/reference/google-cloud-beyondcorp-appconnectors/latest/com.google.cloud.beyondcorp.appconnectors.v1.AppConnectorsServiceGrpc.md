---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceGrpc
title: Class AppConnectorsServiceGrpc (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:25.871576+00:00
---

# Class AppConnectorsServiceGrpc (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AppConnectorsServiceGrpc (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class AppConnectorsServiceGrpc

API Overview: The `beyondcorp.googleapis.com` service implements the Google Cloud BeyondCorp API. Data Model: The AppConnectorsService exposes the following resource:

  * AppConnectors, named as follows: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}`. The AppConnectorsService provides methods to manage (create/read/update/delete) BeyondCorp AppConnectors.



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AppConnectorsServiceGrpc

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

### bindService(AppConnectorsServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(AppConnectorsServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[AppConnectorsServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateAppConnectorMethod()
    
    
    public static MethodDescriptor<CreateAppConnectorRequest,Operation> getCreateAppConnectorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.CreateAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteAppConnectorMethod()
    
    
    public static MethodDescriptor<DeleteAppConnectorRequest,Operation> getDeleteAppConnectorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.DeleteAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetAppConnectorMethod()
    
    
    public static MethodDescriptor<GetAppConnectorRequest,AppConnector> getGetAppConnectorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.GetAppConnectorRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)>` |   
  
### getListAppConnectorsMethod()
    
    
    public static MethodDescriptor<ListAppConnectorsRequest,ListAppConnectorsResponse> getListAppConnectorsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAppConnectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsRequest),[ListAppConnectorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsResponse)>` |   
  
### getReportStatusMethod()
    
    
    public static MethodDescriptor<ReportStatusRequest,Operation> getReportStatusMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ReportStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ReportStatusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateAppConnectorMethod()
    
    
    public static MethodDescriptor<UpdateAppConnectorRequest,Operation> getUpdateAppConnectorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.UpdateAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static AppConnectorsServiceGrpc.AppConnectorsServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceGrpc.AppConnectorsServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceGrpc.AppConnectorsServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static AppConnectorsServiceGrpc.AppConnectorsServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceGrpc.AppConnectorsServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceGrpc.AppConnectorsServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static AppConnectorsServiceGrpc.AppConnectorsServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceGrpc.AppConnectorsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceGrpc.AppConnectorsServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static AppConnectorsServiceGrpc.AppConnectorsServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceGrpc.AppConnectorsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceGrpc.AppConnectorsServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
