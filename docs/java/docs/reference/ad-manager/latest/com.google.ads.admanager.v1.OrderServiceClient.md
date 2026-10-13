---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient
title: Class OrderServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:56.634430+00:00
---

# Class OrderServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrderServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/OrderServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Order` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       OrderName name = OrderName.of("[NETWORK_CODE]", "[ORDER]");
       Order response = orderServiceClient.getOrder(name);
     }
     

Note: close() needs to be called on the OrderServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetOrder |  Retrieves an `Order` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOrder(GetOrderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOrder(OrderName name) 
  * getOrder(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOrderCallable() 

  
ListOrders |  Lists `Order` objects.  Fields used for literal matching in filter string: 

  * `order_id`
  * `display_name`
  * `external_order_id`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOrders(ListOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOrders(NetworkName parent) 
  * listOrders(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOrdersPagedCallable() 
  * listOrdersCallable() 

  
BatchCreateOrders |  Creates `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateOrders(NetworkName parent, List<CreateOrderRequest> requests) 
  * batchCreateOrders(String parent, List<CreateOrderRequest> requests) 
  * batchCreateOrders(BatchCreateOrdersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateOrdersCallable() 

  
BatchUpdateOrders |  Batch updates `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateOrders(NetworkName parent, List<UpdateOrderRequest> requests) 
  * batchUpdateOrders(String parent, List<UpdateOrderRequest> requests) 
  * batchUpdateOrders(BatchUpdateOrdersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateOrdersCallable() 

  
BatchApproveOrders |  Approves a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchApproveOrders(BatchApproveOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchApproveOrders(NetworkName parent, List<String> names) 
  * batchApproveOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchApproveOrdersCallable() 

  
BatchApproveAndOverbookOrders |  Approves and overbooks a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchApproveAndOverbookOrders(BatchApproveAndOverbookOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchApproveAndOverbookOrders(NetworkName parent, List<String> names) 
  * batchApproveAndOverbookOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchApproveAndOverbookOrdersCallable() 

  
BatchSubmitOrdersForApproval |  Submits a list of `Order` objects for approval. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchSubmitOrdersForApproval(BatchSubmitOrdersForApprovalRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchSubmitOrdersForApproval(NetworkName parent, List<String> names) 
  * batchSubmitOrdersForApproval(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchSubmitOrdersForApprovalCallable() 

  
BatchSubmitOrdersForApprovalAndOverbook |  Submits and overbooks a list of `Order` objects for approval. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchSubmitOrdersForApprovalAndOverbook(BatchSubmitOrdersForApprovalAndOverbookRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchSubmitOrdersForApprovalAndOverbook(NetworkName parent, List<String> names) 
  * batchSubmitOrdersForApprovalAndOverbook(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchSubmitOrdersForApprovalAndOverbookCallable() 

  
BatchSubmitOrdersForApprovalWithoutReservationChanges |  Submits a list of `Order` objects for approval without changing reservation status. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchSubmitOrdersForApprovalWithoutReservationChanges(BatchSubmitOrdersForApprovalWithoutReservationChangesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchSubmitOrdersForApprovalWithoutReservationChanges(NetworkName parent, List<String> names) 
  * batchSubmitOrdersForApprovalWithoutReservationChanges(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchSubmitOrdersForApprovalWithoutReservationChangesCallable() 

  
BatchPauseOrders |  Pauses a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchPauseOrders(BatchPauseOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchPauseOrders(NetworkName parent, List<String> names) 
  * batchPauseOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchPauseOrdersCallable() 

  
BatchResumeOrders |  Resumes a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchResumeOrders(BatchResumeOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchResumeOrders(NetworkName parent, List<String> names) 
  * batchResumeOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchResumeOrdersCallable() 

  
BatchResumeAndOverbookOrders |  Resumes and overbooks a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchResumeAndOverbookOrders(BatchResumeAndOverbookOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchResumeAndOverbookOrders(NetworkName parent, List<String> names) 
  * batchResumeAndOverbookOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchResumeAndOverbookOrdersCallable() 

  
BatchApproveOrdersWithoutReservation |  Approves a list of `Order` objects without changing reservation status. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchApproveOrdersWithoutReservation(BatchApproveOrdersWithoutReservationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchApproveOrdersWithoutReservation(NetworkName parent, List<String> names) 
  * batchApproveOrdersWithoutReservation(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchApproveOrdersWithoutReservationCallable() 

  
BatchArchiveOrders |  Archives a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveOrders(BatchArchiveOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchiveOrders(NetworkName parent, List<String> names) 
  * batchArchiveOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveOrdersCallable() 

  
BatchUnarchiveOrders |  Unarchives a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUnarchiveOrders(BatchUnarchiveOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchUnarchiveOrders(NetworkName parent, List<String> names) 
  * batchUnarchiveOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUnarchiveOrdersCallable() 

  
BatchDeleteOrders |  Deletes a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeleteOrders(BatchDeleteOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeleteOrders(NetworkName parent, List<String> names) 
  * batchDeleteOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeleteOrdersCallable() 

  
BatchDisapproveOrders |  Disapproves a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDisapproveOrders(BatchDisapproveOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDisapproveOrders(NetworkName parent, List<String> names) 
  * batchDisapproveOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDisapproveOrdersCallable() 

  
BatchDisapproveOrdersWithoutReservationChanges |  Disapproves a list of `Order` objects without changing reservation status. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDisapproveOrdersWithoutReservationChanges(BatchDisapproveOrdersWithoutReservationChangesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDisapproveOrdersWithoutReservationChanges(NetworkName parent, List<String> names) 
  * batchDisapproveOrdersWithoutReservationChanges(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDisapproveOrdersWithoutReservationChangesCallable() 

  
BatchRetractOrders |  Retracts a list of `Order` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRetractOrders(BatchRetractOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchRetractOrders(NetworkName parent, List<String> names) 
  * batchRetractOrders(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRetractOrdersCallable() 

  
BatchRetractOrdersWithoutReservationChanges |  Retracts a list of `Order` objects without changing reservation status. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRetractOrdersWithoutReservationChanges(BatchRetractOrdersWithoutReservationChangesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchRetractOrdersWithoutReservationChanges(NetworkName parent, List<String> names) 
  * batchRetractOrdersWithoutReservationChanges(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRetractOrdersWithoutReservationChangesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of OrderServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrderServiceSettings orderServiceSettings =
         OrderServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     OrderServiceClient orderServiceClient = OrderServiceClient.create(orderServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrderServiceSettings orderServiceSettings =
         OrderServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     OrderServiceClient orderServiceClient = OrderServiceClient.create(orderServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OrderServiceClient

## Static Methods 

### create()
    
    
    public static final OrderServiceClient create()

Constructs an instance of OrderServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[OrderServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OrderServiceSettings settings)
    
    
    public static final OrderServiceClient create(OrderServiceSettings settings)

Constructs an instance of OrderServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OrderServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OrderServiceStub stub)
    
    
    public static final OrderServiceClient create(OrderServiceStub stub)

Constructs an instance of OrderServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(OrderServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrderServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OrderServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient)` |   
  
## Constructors 

### OrderServiceClient(OrderServiceSettings settings)
    
    
    protected OrderServiceClient(OrderServiceSettings settings)

Constructs an instance of OrderServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OrderServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceSettings)`  
  
  
### OrderServiceClient(OrderServiceStub stub)
    
    
    protected OrderServiceClient(OrderServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrderServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OrderServiceStub)`  
  
  
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
  
### batchApproveAndOverbookOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchApproveAndOverbookOrdersResponse batchApproveAndOverbookOrders(@Nullable NetworkName parent, List<String> names)

Approves and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchApproveAndOverbookOrdersResponse response =
           orderServiceClient.batchApproveAndOverbookOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to approve and overbook. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersResponse)` |   
  
### batchApproveAndOverbookOrders(BatchApproveAndOverbookOrdersRequest request)
    
    
    public final BatchApproveAndOverbookOrdersResponse batchApproveAndOverbookOrders(BatchApproveAndOverbookOrdersRequest request)

Approves and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchApproveAndOverbookOrdersRequest request =
           BatchApproveAndOverbookOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       BatchApproveAndOverbookOrdersResponse response =
           orderServiceClient.batchApproveAndOverbookOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchApproveAndOverbookOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersResponse)` |   
  
### batchApproveAndOverbookOrders(String parent, List<String> names)
    
    
    public final BatchApproveAndOverbookOrdersResponse batchApproveAndOverbookOrders(String parent, List<String> names)

Approves and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchApproveAndOverbookOrdersResponse response =
           orderServiceClient.batchApproveAndOverbookOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to approve and overbook. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersResponse)` |   
  
### batchApproveAndOverbookOrdersCallable()
    
    
    public final UnaryCallable<BatchApproveAndOverbookOrdersRequest,BatchApproveAndOverbookOrdersResponse> batchApproveAndOverbookOrdersCallable()

Approves and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchApproveAndOverbookOrdersRequest request =
           BatchApproveAndOverbookOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       ApiFuture<BatchApproveAndOverbookOrdersResponse> future =
           orderServiceClient.batchApproveAndOverbookOrdersCallable().futureCall(request);
       // Do something.
       BatchApproveAndOverbookOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchApproveAndOverbookOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersRequest),[BatchApproveAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersResponse)>` |   
  
### batchApproveOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchApproveOrdersResponse batchApproveOrders(@Nullable NetworkName parent, List<String> names)

Approves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchApproveOrdersResponse response = orderServiceClient.batchApproveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to approve. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersResponse)` |   
  
### batchApproveOrders(BatchApproveOrdersRequest request)
    
    
    public final BatchApproveOrdersResponse batchApproveOrders(BatchApproveOrdersRequest request)

Approves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchApproveOrdersRequest request =
           BatchApproveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       BatchApproveOrdersResponse response = orderServiceClient.batchApproveOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchApproveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersResponse)` |   
  
### batchApproveOrders(String parent, List<String> names)
    
    
    public final BatchApproveOrdersResponse batchApproveOrders(String parent, List<String> names)

Approves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchApproveOrdersResponse response = orderServiceClient.batchApproveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to approve. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersResponse)` |   
  
### batchApproveOrdersCallable()
    
    
    public final UnaryCallable<BatchApproveOrdersRequest,BatchApproveOrdersResponse> batchApproveOrdersCallable()

Approves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchApproveOrdersRequest request =
           BatchApproveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       ApiFuture<BatchApproveOrdersResponse> future =
           orderServiceClient.batchApproveOrdersCallable().futureCall(request);
       // Do something.
       BatchApproveOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchApproveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersRequest),[BatchApproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersResponse)>` |   
  
### batchApproveOrdersWithoutReservation(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchApproveOrdersWithoutReservationResponse batchApproveOrdersWithoutReservation(@Nullable NetworkName parent, List<String> names)

Approves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchApproveOrdersWithoutReservationResponse response =
           orderServiceClient.batchApproveOrdersWithoutReservation(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to approve. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveOrdersWithoutReservationResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationResponse)` |   
  
### batchApproveOrdersWithoutReservation(BatchApproveOrdersWithoutReservationRequest request)
    
    
    public final BatchApproveOrdersWithoutReservationResponse batchApproveOrdersWithoutReservation(BatchApproveOrdersWithoutReservationRequest request)

Approves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchApproveOrdersWithoutReservationRequest request =
           BatchApproveOrdersWithoutReservationRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchApproveOrdersWithoutReservationResponse response =
           orderServiceClient.batchApproveOrdersWithoutReservation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchApproveOrdersWithoutReservationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveOrdersWithoutReservationResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationResponse)` |   
  
### batchApproveOrdersWithoutReservation(String parent, List<String> names)
    
    
    public final BatchApproveOrdersWithoutReservationResponse batchApproveOrdersWithoutReservation(String parent, List<String> names)

Approves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchApproveOrdersWithoutReservationResponse response =
           orderServiceClient.batchApproveOrdersWithoutReservation(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to approve. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveOrdersWithoutReservationResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationResponse)` |   
  
### batchApproveOrdersWithoutReservationCallable()
    
    
    public final UnaryCallable<BatchApproveOrdersWithoutReservationRequest,BatchApproveOrdersWithoutReservationResponse> batchApproveOrdersWithoutReservationCallable()

Approves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchApproveOrdersWithoutReservationRequest request =
           BatchApproveOrdersWithoutReservationRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchApproveOrdersWithoutReservationResponse> future =
           orderServiceClient.batchApproveOrdersWithoutReservationCallable().futureCall(request);
       // Do something.
       BatchApproveOrdersWithoutReservationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchApproveOrdersWithoutReservationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationRequest),[BatchApproveOrdersWithoutReservationResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationResponse)>` |   
  
### batchArchiveOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchiveOrdersResponse batchArchiveOrders(@Nullable NetworkName parent, List<String> names)

Archives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchiveOrdersResponse response = orderServiceClient.batchArchiveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to archive. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersResponse)` |   
  
### batchArchiveOrders(BatchArchiveOrdersRequest request)
    
    
    public final BatchArchiveOrdersResponse batchArchiveOrders(BatchArchiveOrdersRequest request)

Archives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchArchiveOrdersRequest request =
           BatchArchiveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchiveOrdersResponse response = orderServiceClient.batchArchiveOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersResponse)` |   
  
### batchArchiveOrders(String parent, List<String> names)
    
    
    public final BatchArchiveOrdersResponse batchArchiveOrders(String parent, List<String> names)

Archives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchiveOrdersResponse response = orderServiceClient.batchArchiveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to archive. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersResponse)` |   
  
### batchArchiveOrdersCallable()
    
    
    public final UnaryCallable<BatchArchiveOrdersRequest,BatchArchiveOrdersResponse> batchArchiveOrdersCallable()

Archives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchArchiveOrdersRequest request =
           BatchArchiveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchiveOrdersResponse> future =
           orderServiceClient.batchArchiveOrdersCallable().futureCall(request);
       // Do something.
       BatchArchiveOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersRequest),[BatchArchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersResponse)>` |   
  
### batchCreateOrders(@Nullable NetworkName parent, List<CreateOrderRequest> requests)
    
    
    public final BatchCreateOrdersResponse batchCreateOrders(@Nullable NetworkName parent, List<CreateOrderRequest> requests)

Creates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateOrderRequest> requests = new ArrayList<>();
       BatchCreateOrdersResponse response = orderServiceClient.batchCreateOrders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Orders` will be created. Format: `networks/{network_code}` The parent field in the CreateOrderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateOrderRequest)>`  
Required. The `Order` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersResponse)` |   
  
### batchCreateOrders(BatchCreateOrdersRequest request)
    
    
    public final BatchCreateOrdersResponse batchCreateOrders(BatchCreateOrdersRequest request)

Creates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchCreateOrdersRequest request =
           BatchCreateOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateOrderRequest>())
               .build();
       BatchCreateOrdersResponse response = orderServiceClient.batchCreateOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersResponse)` |   
  
### batchCreateOrders(String parent, List<CreateOrderRequest> requests)
    
    
    public final BatchCreateOrdersResponse batchCreateOrders(String parent, List<CreateOrderRequest> requests)

Creates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateOrderRequest> requests = new ArrayList<>();
       BatchCreateOrdersResponse response = orderServiceClient.batchCreateOrders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Orders` will be created. Format: `networks/{network_code}` The parent field in the CreateOrderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateOrderRequest)>`  
Required. The `Order` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersResponse)` |   
  
### batchCreateOrdersCallable()
    
    
    public final UnaryCallable<BatchCreateOrdersRequest,BatchCreateOrdersResponse> batchCreateOrdersCallable()

Creates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchCreateOrdersRequest request =
           BatchCreateOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateOrderRequest>())
               .build();
       ApiFuture<BatchCreateOrdersResponse> future =
           orderServiceClient.batchCreateOrdersCallable().futureCall(request);
       // Do something.
       BatchCreateOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersRequest),[BatchCreateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersResponse)>` |   
  
### batchDeleteOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeleteOrdersResponse batchDeleteOrders(@Nullable NetworkName parent, List<String> names)

Deletes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeleteOrdersResponse response = orderServiceClient.batchDeleteOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to delete. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeleteOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersResponse)` |   
  
### batchDeleteOrders(BatchDeleteOrdersRequest request)
    
    
    public final BatchDeleteOrdersResponse batchDeleteOrders(BatchDeleteOrdersRequest request)

Deletes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchDeleteOrdersRequest request =
           BatchDeleteOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeleteOrdersResponse response = orderServiceClient.batchDeleteOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeleteOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersResponse)` |   
  
### batchDeleteOrders(String parent, List<String> names)
    
    
    public final BatchDeleteOrdersResponse batchDeleteOrders(String parent, List<String> names)

Deletes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeleteOrdersResponse response = orderServiceClient.batchDeleteOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to delete. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeleteOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersResponse)` |   
  
### batchDeleteOrdersCallable()
    
    
    public final UnaryCallable<BatchDeleteOrdersRequest,BatchDeleteOrdersResponse> batchDeleteOrdersCallable()

Deletes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchDeleteOrdersRequest request =
           BatchDeleteOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeleteOrdersResponse> future =
           orderServiceClient.batchDeleteOrdersCallable().futureCall(request);
       // Do something.
       BatchDeleteOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersRequest),[BatchDeleteOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersResponse)>` |   
  
### batchDisapproveOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDisapproveOrdersResponse batchDisapproveOrders(@Nullable NetworkName parent, List<String> names)

Disapproves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDisapproveOrdersResponse response =
           orderServiceClient.batchDisapproveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to disapprove. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDisapproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersResponse)` |   
  
### batchDisapproveOrders(BatchDisapproveOrdersRequest request)
    
    
    public final BatchDisapproveOrdersResponse batchDisapproveOrders(BatchDisapproveOrdersRequest request)

Disapproves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchDisapproveOrdersRequest request =
           BatchDisapproveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDisapproveOrdersResponse response = orderServiceClient.batchDisapproveOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDisapproveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDisapproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersResponse)` |   
  
### batchDisapproveOrders(String parent, List<String> names)
    
    
    public final BatchDisapproveOrdersResponse batchDisapproveOrders(String parent, List<String> names)

Disapproves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDisapproveOrdersResponse response =
           orderServiceClient.batchDisapproveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to disapprove. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDisapproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersResponse)` |   
  
### batchDisapproveOrdersCallable()
    
    
    public final UnaryCallable<BatchDisapproveOrdersRequest,BatchDisapproveOrdersResponse> batchDisapproveOrdersCallable()

Disapproves a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchDisapproveOrdersRequest request =
           BatchDisapproveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDisapproveOrdersResponse> future =
           orderServiceClient.batchDisapproveOrdersCallable().futureCall(request);
       // Do something.
       BatchDisapproveOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDisapproveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersRequest),[BatchDisapproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersResponse)>` |   
  
### batchDisapproveOrdersWithoutReservationChanges(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDisapproveOrdersWithoutReservationChangesResponse batchDisapproveOrdersWithoutReservationChanges(@Nullable NetworkName parent, List<String> names)

Disapproves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDisapproveOrdersWithoutReservationChangesResponse response =
           orderServiceClient.batchDisapproveOrdersWithoutReservationChanges(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to disapprove without reservation changes. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDisapproveOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesResponse)` |   
  
### batchDisapproveOrdersWithoutReservationChanges(BatchDisapproveOrdersWithoutReservationChangesRequest request)
    
    
    public final BatchDisapproveOrdersWithoutReservationChangesResponse batchDisapproveOrdersWithoutReservationChanges(BatchDisapproveOrdersWithoutReservationChangesRequest request)

Disapproves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchDisapproveOrdersWithoutReservationChangesRequest request =
           BatchDisapproveOrdersWithoutReservationChangesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDisapproveOrdersWithoutReservationChangesResponse response =
           orderServiceClient.batchDisapproveOrdersWithoutReservationChanges(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDisapproveOrdersWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDisapproveOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesResponse)` |   
  
### batchDisapproveOrdersWithoutReservationChanges(String parent, List<String> names)
    
    
    public final BatchDisapproveOrdersWithoutReservationChangesResponse batchDisapproveOrdersWithoutReservationChanges(String parent, List<String> names)

Disapproves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDisapproveOrdersWithoutReservationChangesResponse response =
           orderServiceClient.batchDisapproveOrdersWithoutReservationChanges(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to disapprove without reservation changes. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDisapproveOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesResponse)` |   
  
### batchDisapproveOrdersWithoutReservationChangesCallable()
    
    
    public final UnaryCallable<BatchDisapproveOrdersWithoutReservationChangesRequest,BatchDisapproveOrdersWithoutReservationChangesResponse> batchDisapproveOrdersWithoutReservationChangesCallable()

Disapproves a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchDisapproveOrdersWithoutReservationChangesRequest request =
           BatchDisapproveOrdersWithoutReservationChangesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDisapproveOrdersWithoutReservationChangesResponse> future =
           orderServiceClient
               .batchDisapproveOrdersWithoutReservationChangesCallable()
               .futureCall(request);
       // Do something.
       BatchDisapproveOrdersWithoutReservationChangesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDisapproveOrdersWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesRequest),[BatchDisapproveOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesResponse)>` |   
  
### batchPauseOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchPauseOrdersResponse batchPauseOrders(@Nullable NetworkName parent, List<String> names)

Pauses a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchPauseOrdersResponse response = orderServiceClient.batchPauseOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to pause. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersResponse)` |   
  
### batchPauseOrders(BatchPauseOrdersRequest request)
    
    
    public final BatchPauseOrdersResponse batchPauseOrders(BatchPauseOrdersRequest request)

Pauses a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchPauseOrdersRequest request =
           BatchPauseOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchPauseOrdersResponse response = orderServiceClient.batchPauseOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchPauseOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersResponse)` |   
  
### batchPauseOrders(String parent, List<String> names)
    
    
    public final BatchPauseOrdersResponse batchPauseOrders(String parent, List<String> names)

Pauses a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchPauseOrdersResponse response = orderServiceClient.batchPauseOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to pause. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersResponse)` |   
  
### batchPauseOrdersCallable()
    
    
    public final UnaryCallable<BatchPauseOrdersRequest,BatchPauseOrdersResponse> batchPauseOrdersCallable()

Pauses a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchPauseOrdersRequest request =
           BatchPauseOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchPauseOrdersResponse> future =
           orderServiceClient.batchPauseOrdersCallable().futureCall(request);
       // Do something.
       BatchPauseOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchPauseOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersRequest),[BatchPauseOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersResponse)>` |   
  
### batchResumeAndOverbookOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchResumeAndOverbookOrdersResponse batchResumeAndOverbookOrders(@Nullable NetworkName parent, List<String> names)

Resumes and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchResumeAndOverbookOrdersResponse response =
           orderServiceClient.batchResumeAndOverbookOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to resume and overbook. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchResumeAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersResponse)` |   
  
### batchResumeAndOverbookOrders(BatchResumeAndOverbookOrdersRequest request)
    
    
    public final BatchResumeAndOverbookOrdersResponse batchResumeAndOverbookOrders(BatchResumeAndOverbookOrdersRequest request)

Resumes and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchResumeAndOverbookOrdersRequest request =
           BatchResumeAndOverbookOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchResumeAndOverbookOrdersResponse response =
           orderServiceClient.batchResumeAndOverbookOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchResumeAndOverbookOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchResumeAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersResponse)` |   
  
### batchResumeAndOverbookOrders(String parent, List<String> names)
    
    
    public final BatchResumeAndOverbookOrdersResponse batchResumeAndOverbookOrders(String parent, List<String> names)

Resumes and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchResumeAndOverbookOrdersResponse response =
           orderServiceClient.batchResumeAndOverbookOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to resume and overbook. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchResumeAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersResponse)` |   
  
### batchResumeAndOverbookOrdersCallable()
    
    
    public final UnaryCallable<BatchResumeAndOverbookOrdersRequest,BatchResumeAndOverbookOrdersResponse> batchResumeAndOverbookOrdersCallable()

Resumes and overbooks a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchResumeAndOverbookOrdersRequest request =
           BatchResumeAndOverbookOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchResumeAndOverbookOrdersResponse> future =
           orderServiceClient.batchResumeAndOverbookOrdersCallable().futureCall(request);
       // Do something.
       BatchResumeAndOverbookOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchResumeAndOverbookOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersRequest),[BatchResumeAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersResponse)>` |   
  
### batchResumeOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchResumeOrdersResponse batchResumeOrders(@Nullable NetworkName parent, List<String> names)

Resumes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchResumeOrdersResponse response = orderServiceClient.batchResumeOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to resume. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchResumeOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersResponse)` |   
  
### batchResumeOrders(BatchResumeOrdersRequest request)
    
    
    public final BatchResumeOrdersResponse batchResumeOrders(BatchResumeOrdersRequest request)

Resumes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchResumeOrdersRequest request =
           BatchResumeOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       BatchResumeOrdersResponse response = orderServiceClient.batchResumeOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchResumeOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchResumeOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersResponse)` |   
  
### batchResumeOrders(String parent, List<String> names)
    
    
    public final BatchResumeOrdersResponse batchResumeOrders(String parent, List<String> names)

Resumes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchResumeOrdersResponse response = orderServiceClient.batchResumeOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to resume. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchResumeOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersResponse)` |   
  
### batchResumeOrdersCallable()
    
    
    public final UnaryCallable<BatchResumeOrdersRequest,BatchResumeOrdersResponse> batchResumeOrdersCallable()

Resumes a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchResumeOrdersRequest request =
           BatchResumeOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       ApiFuture<BatchResumeOrdersResponse> future =
           orderServiceClient.batchResumeOrdersCallable().futureCall(request);
       // Do something.
       BatchResumeOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchResumeOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersRequest),[BatchResumeOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersResponse)>` |   
  
### batchRetractOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchRetractOrdersResponse batchRetractOrders(@Nullable NetworkName parent, List<String> names)

Retracts a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchRetractOrdersResponse response = orderServiceClient.batchRetractOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to retract. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRetractOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersResponse)` |   
  
### batchRetractOrders(BatchRetractOrdersRequest request)
    
    
    public final BatchRetractOrdersResponse batchRetractOrders(BatchRetractOrdersRequest request)

Retracts a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchRetractOrdersRequest request =
           BatchRetractOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchRetractOrdersResponse response = orderServiceClient.batchRetractOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRetractOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRetractOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersResponse)` |   
  
### batchRetractOrders(String parent, List<String> names)
    
    
    public final BatchRetractOrdersResponse batchRetractOrders(String parent, List<String> names)

Retracts a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchRetractOrdersResponse response = orderServiceClient.batchRetractOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to retract. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRetractOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersResponse)` |   
  
### batchRetractOrdersCallable()
    
    
    public final UnaryCallable<BatchRetractOrdersRequest,BatchRetractOrdersResponse> batchRetractOrdersCallable()

Retracts a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchRetractOrdersRequest request =
           BatchRetractOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchRetractOrdersResponse> future =
           orderServiceClient.batchRetractOrdersCallable().futureCall(request);
       // Do something.
       BatchRetractOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRetractOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersRequest),[BatchRetractOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersResponse)>` |   
  
### batchRetractOrdersWithoutReservationChanges(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchRetractOrdersWithoutReservationChangesResponse batchRetractOrdersWithoutReservationChanges(@Nullable NetworkName parent, List<String> names)

Retracts a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchRetractOrdersWithoutReservationChangesResponse response =
           orderServiceClient.batchRetractOrdersWithoutReservationChanges(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to retract. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRetractOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesResponse)` |   
  
### batchRetractOrdersWithoutReservationChanges(BatchRetractOrdersWithoutReservationChangesRequest request)
    
    
    public final BatchRetractOrdersWithoutReservationChangesResponse batchRetractOrdersWithoutReservationChanges(BatchRetractOrdersWithoutReservationChangesRequest request)

Retracts a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchRetractOrdersWithoutReservationChangesRequest request =
           BatchRetractOrdersWithoutReservationChangesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchRetractOrdersWithoutReservationChangesResponse response =
           orderServiceClient.batchRetractOrdersWithoutReservationChanges(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRetractOrdersWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRetractOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesResponse)` |   
  
### batchRetractOrdersWithoutReservationChanges(String parent, List<String> names)
    
    
    public final BatchRetractOrdersWithoutReservationChangesResponse batchRetractOrdersWithoutReservationChanges(String parent, List<String> names)

Retracts a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchRetractOrdersWithoutReservationChangesResponse response =
           orderServiceClient.batchRetractOrdersWithoutReservationChanges(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to retract. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRetractOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesResponse)` |   
  
### batchRetractOrdersWithoutReservationChangesCallable()
    
    
    public final UnaryCallable<BatchRetractOrdersWithoutReservationChangesRequest,BatchRetractOrdersWithoutReservationChangesResponse> batchRetractOrdersWithoutReservationChangesCallable()

Retracts a list of `Order` objects without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchRetractOrdersWithoutReservationChangesRequest request =
           BatchRetractOrdersWithoutReservationChangesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchRetractOrdersWithoutReservationChangesResponse> future =
           orderServiceClient
               .batchRetractOrdersWithoutReservationChangesCallable()
               .futureCall(request);
       // Do something.
       BatchRetractOrdersWithoutReservationChangesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRetractOrdersWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesRequest),[BatchRetractOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesResponse)>` |   
  
### batchSubmitOrdersForApproval(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchSubmitOrdersForApprovalResponse batchSubmitOrdersForApproval(@Nullable NetworkName parent, List<String> names)

Submits a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchSubmitOrdersForApprovalResponse response =
           orderServiceClient.batchSubmitOrdersForApproval(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to submit for approval. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalResponse)` |   
  
### batchSubmitOrdersForApproval(BatchSubmitOrdersForApprovalRequest request)
    
    
    public final BatchSubmitOrdersForApprovalResponse batchSubmitOrdersForApproval(BatchSubmitOrdersForApprovalRequest request)

Submits a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchSubmitOrdersForApprovalRequest request =
           BatchSubmitOrdersForApprovalRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       BatchSubmitOrdersForApprovalResponse response =
           orderServiceClient.batchSubmitOrdersForApproval(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchSubmitOrdersForApprovalRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalResponse)` |   
  
### batchSubmitOrdersForApproval(String parent, List<String> names)
    
    
    public final BatchSubmitOrdersForApprovalResponse batchSubmitOrdersForApproval(String parent, List<String> names)

Submits a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchSubmitOrdersForApprovalResponse response =
           orderServiceClient.batchSubmitOrdersForApproval(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to submit for approval. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalResponse)` |   
  
### batchSubmitOrdersForApprovalAndOverbook(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchSubmitOrdersForApprovalAndOverbookResponse batchSubmitOrdersForApprovalAndOverbook(@Nullable NetworkName parent, List<String> names)

Submits and overbooks a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchSubmitOrdersForApprovalAndOverbookResponse response =
           orderServiceClient.batchSubmitOrdersForApprovalAndOverbook(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to submit for approval and overbook. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalAndOverbookResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookResponse)` |   
  
### batchSubmitOrdersForApprovalAndOverbook(BatchSubmitOrdersForApprovalAndOverbookRequest request)
    
    
    public final BatchSubmitOrdersForApprovalAndOverbookResponse batchSubmitOrdersForApprovalAndOverbook(BatchSubmitOrdersForApprovalAndOverbookRequest request)

Submits and overbooks a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchSubmitOrdersForApprovalAndOverbookRequest request =
           BatchSubmitOrdersForApprovalAndOverbookRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchSubmitOrdersForApprovalAndOverbookResponse response =
           orderServiceClient.batchSubmitOrdersForApprovalAndOverbook(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchSubmitOrdersForApprovalAndOverbookRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalAndOverbookResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookResponse)` |   
  
### batchSubmitOrdersForApprovalAndOverbook(String parent, List<String> names)
    
    
    public final BatchSubmitOrdersForApprovalAndOverbookResponse batchSubmitOrdersForApprovalAndOverbook(String parent, List<String> names)

Submits and overbooks a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchSubmitOrdersForApprovalAndOverbookResponse response =
           orderServiceClient.batchSubmitOrdersForApprovalAndOverbook(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to submit for approval and overbook. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalAndOverbookResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookResponse)` |   
  
### batchSubmitOrdersForApprovalAndOverbookCallable()
    
    
    public final UnaryCallable<BatchSubmitOrdersForApprovalAndOverbookRequest,BatchSubmitOrdersForApprovalAndOverbookResponse> batchSubmitOrdersForApprovalAndOverbookCallable()

Submits and overbooks a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchSubmitOrdersForApprovalAndOverbookRequest request =
           BatchSubmitOrdersForApprovalAndOverbookRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchSubmitOrdersForApprovalAndOverbookResponse> future =
           orderServiceClient.batchSubmitOrdersForApprovalAndOverbookCallable().futureCall(request);
       // Do something.
       BatchSubmitOrdersForApprovalAndOverbookResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSubmitOrdersForApprovalAndOverbookRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookRequest),[BatchSubmitOrdersForApprovalAndOverbookResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookResponse)>` |   
  
### batchSubmitOrdersForApprovalCallable()
    
    
    public final UnaryCallable<BatchSubmitOrdersForApprovalRequest,BatchSubmitOrdersForApprovalResponse> batchSubmitOrdersForApprovalCallable()

Submits a list of `Order` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchSubmitOrdersForApprovalRequest request =
           BatchSubmitOrdersForApprovalRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .setSkipInventoryCheck(true)
               .build();
       ApiFuture<BatchSubmitOrdersForApprovalResponse> future =
           orderServiceClient.batchSubmitOrdersForApprovalCallable().futureCall(request);
       // Do something.
       BatchSubmitOrdersForApprovalResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSubmitOrdersForApprovalRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalRequest),[BatchSubmitOrdersForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalResponse)>` |   
  
### batchSubmitOrdersForApprovalWithoutReservationChanges(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchSubmitOrdersForApprovalWithoutReservationChangesResponse batchSubmitOrdersForApprovalWithoutReservationChanges(@Nullable NetworkName parent, List<String> names)

Submits a list of `Order` objects for approval without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchSubmitOrdersForApprovalWithoutReservationChangesResponse response =
           orderServiceClient.batchSubmitOrdersForApprovalWithoutReservationChanges(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to submit for approval. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse)` |   
  
### batchSubmitOrdersForApprovalWithoutReservationChanges(BatchSubmitOrdersForApprovalWithoutReservationChangesRequest request)
    
    
    public final BatchSubmitOrdersForApprovalWithoutReservationChangesResponse batchSubmitOrdersForApprovalWithoutReservationChanges(BatchSubmitOrdersForApprovalWithoutReservationChangesRequest request)

Submits a list of `Order` objects for approval without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchSubmitOrdersForApprovalWithoutReservationChangesRequest request =
           BatchSubmitOrdersForApprovalWithoutReservationChangesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchSubmitOrdersForApprovalWithoutReservationChangesResponse response =
           orderServiceClient.batchSubmitOrdersForApprovalWithoutReservationChanges(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchSubmitOrdersForApprovalWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse)` |   
  
### batchSubmitOrdersForApprovalWithoutReservationChanges(String parent, List<String> names)
    
    
    public final BatchSubmitOrdersForApprovalWithoutReservationChangesResponse batchSubmitOrdersForApprovalWithoutReservationChanges(String parent, List<String> names)

Submits a list of `Order` objects for approval without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchSubmitOrdersForApprovalWithoutReservationChangesResponse response =
           orderServiceClient.batchSubmitOrdersForApprovalWithoutReservationChanges(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to submit for approval. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitOrdersForApprovalWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse)` |   
  
### batchSubmitOrdersForApprovalWithoutReservationChangesCallable()
    
    
    public final UnaryCallable<BatchSubmitOrdersForApprovalWithoutReservationChangesRequest,BatchSubmitOrdersForApprovalWithoutReservationChangesResponse> batchSubmitOrdersForApprovalWithoutReservationChangesCallable()

Submits a list of `Order` objects for approval without changing reservation status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchSubmitOrdersForApprovalWithoutReservationChangesRequest request =
           BatchSubmitOrdersForApprovalWithoutReservationChangesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchSubmitOrdersForApprovalWithoutReservationChangesResponse> future =
           orderServiceClient
               .batchSubmitOrdersForApprovalWithoutReservationChangesCallable()
               .futureCall(request);
       // Do something.
       BatchSubmitOrdersForApprovalWithoutReservationChangesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSubmitOrdersForApprovalWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest),[BatchSubmitOrdersForApprovalWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse)>` |   
  
### batchUnarchiveOrders(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchUnarchiveOrdersResponse batchUnarchiveOrders(@Nullable NetworkName parent, List<String> names)

Unarchives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchUnarchiveOrdersResponse response =
           orderServiceClient.batchUnarchiveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to extract. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersResponse)` |   
  
### batchUnarchiveOrders(BatchUnarchiveOrdersRequest request)
    
    
    public final BatchUnarchiveOrdersResponse batchUnarchiveOrders(BatchUnarchiveOrdersRequest request)

Unarchives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchUnarchiveOrdersRequest request =
           BatchUnarchiveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchUnarchiveOrdersResponse response = orderServiceClient.batchUnarchiveOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUnarchiveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersResponse)` |   
  
### batchUnarchiveOrders(String parent, List<String> names)
    
    
    public final BatchUnarchiveOrdersResponse batchUnarchiveOrders(String parent, List<String> names)

Unarchives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchUnarchiveOrdersResponse response =
           orderServiceClient.batchUnarchiveOrders(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the orders to extract. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersResponse)` |   
  
### batchUnarchiveOrdersCallable()
    
    
    public final UnaryCallable<BatchUnarchiveOrdersRequest,BatchUnarchiveOrdersResponse> batchUnarchiveOrdersCallable()

Unarchives a list of `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchUnarchiveOrdersRequest request =
           BatchUnarchiveOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchUnarchiveOrdersResponse> future =
           orderServiceClient.batchUnarchiveOrdersCallable().futureCall(request);
       // Do something.
       BatchUnarchiveOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUnarchiveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersRequest),[BatchUnarchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersResponse)>` |   
  
### batchUpdateOrders(@Nullable NetworkName parent, List<UpdateOrderRequest> requests)
    
    
    public final BatchUpdateOrdersResponse batchUpdateOrders(@Nullable NetworkName parent, List<UpdateOrderRequest> requests)

Batch updates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateOrderRequest> requests = new ArrayList<>();
       BatchUpdateOrdersResponse response = orderServiceClient.batchUpdateOrders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Orders` will be updated. Format: `networks/{network_code}` The parent field in the UpdateOrderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateOrderRequest)>`  
Required. The `Order` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersResponse)` |   
  
### batchUpdateOrders(BatchUpdateOrdersRequest request)
    
    
    public final BatchUpdateOrdersResponse batchUpdateOrders(BatchUpdateOrdersRequest request)

Batch updates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchUpdateOrdersRequest request =
           BatchUpdateOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateOrderRequest>())
               .build();
       BatchUpdateOrdersResponse response = orderServiceClient.batchUpdateOrders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersResponse)` |   
  
### batchUpdateOrders(String parent, List<UpdateOrderRequest> requests)
    
    
    public final BatchUpdateOrdersResponse batchUpdateOrders(String parent, List<UpdateOrderRequest> requests)

Batch updates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateOrderRequest> requests = new ArrayList<>();
       BatchUpdateOrdersResponse response = orderServiceClient.batchUpdateOrders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Orders` will be updated. Format: `networks/{network_code}` The parent field in the UpdateOrderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateOrderRequest)>`  
Required. The `Order` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersResponse)` |   
  
### batchUpdateOrdersCallable()
    
    
    public final UnaryCallable<BatchUpdateOrdersRequest,BatchUpdateOrdersResponse> batchUpdateOrdersCallable()

Batch updates `Order` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       BatchUpdateOrdersRequest request =
           BatchUpdateOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateOrderRequest>())
               .build();
       ApiFuture<BatchUpdateOrdersResponse> future =
           orderServiceClient.batchUpdateOrdersCallable().futureCall(request);
       // Do something.
       BatchUpdateOrdersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersRequest),[BatchUpdateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersResponse)>` |   
  
### close()
    
    
    public final void close()

### getOrder(@Nullable OrderName name)
    
    
    public final Order getOrder(@Nullable OrderName name)

Retrieves an `Order` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       OrderName name = OrderName.of("[NETWORK_CODE]", "[ORDER]");
       Order response = orderServiceClient.getOrder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.OrderName`  
Required. The resource name of the Order. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Order)` |   
  
### getOrder(GetOrderRequest request)
    
    
    public final Order getOrder(GetOrderRequest request)

Retrieves an `Order` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       GetOrderRequest request =
           GetOrderRequest.newBuilder()
               .setName(OrderName.of("[NETWORK_CODE]", "[ORDER]").toString())
               .build();
       Order response = orderServiceClient.getOrder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Order)` |   
  
### getOrder(String name)
    
    
    public final Order getOrder(String name)

Retrieves an `Order` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String name = OrderName.of("[NETWORK_CODE]", "[ORDER]").toString();
       Order response = orderServiceClient.getOrder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Order. Format: `networks/{network_code}/orders/{order_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Order)` |   
  
### getOrderCallable()
    
    
    public final UnaryCallable<GetOrderRequest,Order> getOrderCallable()

Retrieves an `Order` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       GetOrderRequest request =
           GetOrderRequest.newBuilder()
               .setName(OrderName.of("[NETWORK_CODE]", "[ORDER]").toString())
               .build();
       ApiFuture<Order> future = orderServiceClient.getOrderCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Order)>` |   
  
### getSettings()
    
    
    public final @Nullable OrderServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.OrderServiceSettings` |   
  
### getStub()
    
    
    public OrderServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[OrderServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OrderServiceStub)` |   
  
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
  
### listOrders(@Nullable NetworkName parent)
    
    
    public final OrderServiceClient.ListOrdersPagedResponse listOrders(@Nullable NetworkName parent)

Lists `Order` objects.

Fields used for literal matching in filter string:

  * `order_id`
  * `display_name`
  * `external_order_id`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Order element : orderServiceClient.listOrders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[OrderServiceClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient.ListOrdersPagedResponse)` |   
  
### listOrders(ListOrdersRequest request)
    
    
    public final OrderServiceClient.ListOrdersPagedResponse listOrders(ListOrdersRequest request)

Lists `Order` objects.

Fields used for literal matching in filter string:

  * `order_id`
  * `display_name`
  * `external_order_id`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Order element : orderServiceClient.listOrders(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OrderServiceClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient.ListOrdersPagedResponse)` |   
  
### listOrders(String parent)
    
    
    public final OrderServiceClient.ListOrdersPagedResponse listOrders(String parent)

Lists `Order` objects.

Fields used for literal matching in filter string:

  * `order_id`
  * `display_name`
  * `external_order_id`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Order element : orderServiceClient.listOrders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Orders. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[OrderServiceClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient.ListOrdersPagedResponse)` |   
  
### listOrdersCallable()
    
    
    public final UnaryCallable<ListOrdersRequest,ListOrdersResponse> listOrdersCallable()

Lists `Order` objects.

Fields used for literal matching in filter string:

  * `order_id`
  * `display_name`
  * `external_order_id`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListOrdersResponse response = orderServiceClient.listOrdersCallable().call(request);
         for (Order element : response.getOrdersList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOrdersRequest),[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOrdersResponse)>` |   
  
### listOrdersPagedCallable()
    
    
    public final UnaryCallable<ListOrdersRequest,OrderServiceClient.ListOrdersPagedResponse> listOrdersPagedCallable()

Lists `Order` objects.

Fields used for literal matching in filter string:

  * `order_id`
  * `display_name`
  * `external_order_id`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrderServiceClient orderServiceClient = OrderServiceClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Order> future = orderServiceClient.listOrdersPagedCallable().futureCall(request);
       // Do something.
       for (Order element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOrdersRequest),[ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient.ListOrdersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
