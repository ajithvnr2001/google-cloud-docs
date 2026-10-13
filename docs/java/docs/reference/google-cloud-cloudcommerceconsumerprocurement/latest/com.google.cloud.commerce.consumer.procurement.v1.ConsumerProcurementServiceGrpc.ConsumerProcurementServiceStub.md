---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub
title: Class ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:48.366710+00:00
---

# Class ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 
    
    
    public static final class ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub extends AbstractAsyncStub<ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub>

A stub to allow clients to do asynchronous rpc calls to service ConsumerProcurementService.

ConsumerProcurementService allows customers to make purchases of products served by the Cloud Commerce platform. When purchases are made, the ConsumerProcurementService programs the appropriate backends, including both Google's own infrastructure, as well as third-party systems, and to enable billing setup for charging for the procured item.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementServiceGrpc.ConsumerProcurementServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelOrder(CancelOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void cancelOrder(CancelOrderRequest request, StreamObserver<Operation> responseObserver)

Cancels an existing Order. Every product procured in the Order will be cancelled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.CancelOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getOrder(GetOrderRequest request, StreamObserver<Order> responseObserver)
    
    
    public void getOrder(GetOrderRequest request, StreamObserver<Order> responseObserver)

Returns the requested Order resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.GetOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.Order)>`  
  
  
### listOrders(ListOrdersRequest request, StreamObserver<ListOrdersResponse> responseObserver)
    
    
    public void listOrders(ListOrdersRequest request, StreamObserver<ListOrdersResponse> responseObserver)

Lists Order resources that the user has access to, within the scope of the parent resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ListOrdersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ListOrdersResponse)>`  
  
  
### modifyOrder(ModifyOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void modifyOrder(ModifyOrderRequest request, StreamObserver<Operation> responseObserver)

Modifies an existing Order resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ModifyOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### placeOrder(PlaceOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void placeOrder(PlaceOrderRequest request, StreamObserver<Operation> responseObserver)

Creates a new Order. This API only supports GCP spend-based committed use discounts specified by GCP documentation. The returned long-running operation is in-progress until the backend completes the creation of the resource. Once completed, the order is in OrderState.ORDER_STATE_ACTIVE. In case of failure, the order resource will be removed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PlaceOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.PlaceOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
