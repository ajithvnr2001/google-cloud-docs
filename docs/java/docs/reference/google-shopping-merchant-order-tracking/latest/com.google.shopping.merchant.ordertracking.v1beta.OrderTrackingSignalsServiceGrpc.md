---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalsServiceGrpc
title: Class OrderTrackingSignalsServiceGrpc (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:01.999499+00:00
---

# Class OrderTrackingSignalsServiceGrpc (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalsServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrderTrackingSignalsServiceGrpc (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public final class OrderTrackingSignalsServiceGrpc

Service to serve order tracking signals public API.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OrderTrackingSignalsServiceGrpc

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

### bindService(OrderTrackingSignalsServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(OrderTrackingSignalsServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[OrderTrackingSignalsServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalsServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateOrderTrackingSignalMethod()
    
    
    public static MethodDescriptor<CreateOrderTrackingSignalRequest,OrderTrackingSignal> getCreateOrderTrackingSignalMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateOrderTrackingSignalRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.CreateOrderTrackingSignalRequest),[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### newBlockingStub(Channel channel)
    
    
    public static OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalsServiceGrpc.OrderTrackingSignalsServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
