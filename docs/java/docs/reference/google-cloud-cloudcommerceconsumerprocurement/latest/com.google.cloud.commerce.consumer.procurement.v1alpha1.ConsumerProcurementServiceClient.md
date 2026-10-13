---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient
title: Class ConsumerProcurementServiceClient (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:54.137940+00:00
---

# Class ConsumerProcurementServiceClient (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConsumerProcurementServiceClient (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudcommerceconsumerprocurement/google-cloud-cloudcommerceconsumerprocurement/src/main/java/com/google/cloud/commerce/consumer/procurement/v1alpha1/ConsumerProcurementServiceClient.java)| [Product Reference](https://cloud.google.com/marketplace/)  
---|---  
  
Service Description: ConsumerProcurementService allows customers to make purchases of products served by the Cloud Commerce platform.

When purchases are made, the ConsumerProcurementService programs the appropriate backends, including both Google's own infrastructure, as well as third-party systems, and to enable billing setup for charging for the procured item.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       String name = "name3373707";
       Order response = consumerProcurementServiceClient.getOrder(name);
     }
     

Note: close() needs to be called on the ConsumerProcurementServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
PlaceOrder |  Creates a new Order.  This API only supports GCP spend-based committed use discounts specified by GCP documentation.  The returned long-running operation is in-progress until the backend completes the creation of the resource. Once completed, the order is in OrderState.ORDER_STATE_ACTIVE. In case of failure, the order resource will be removed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * placeOrderAsync(PlaceOrderRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * placeOrderOperationCallable() 
  * placeOrderCallable() 

  
GetOrder |  Returns the requested Order resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOrder(GetOrderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOrder(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOrderCallable() 

  
ListOrders |  Lists Order resources that the user has access to, within the scope of the parent resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOrders(ListOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOrders(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOrdersPagedCallable() 
  * listOrdersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ConsumerProcurementServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConsumerProcurementServiceSettings consumerProcurementServiceSettings =
         ConsumerProcurementServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create(consumerProcurementServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConsumerProcurementServiceSettings consumerProcurementServiceSettings =
         ConsumerProcurementServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create(consumerProcurementServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConsumerProcurementServiceSettings consumerProcurementServiceSettings =
         ConsumerProcurementServiceSettings.newHttpJsonBuilder().build();
     ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create(consumerProcurementServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConsumerProcurementServiceClient

## Static Methods 

### create()
    
    
    public static final ConsumerProcurementServiceClient create()

Constructs an instance of ConsumerProcurementServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConsumerProcurementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConsumerProcurementServiceSettings settings)
    
    
    public static final ConsumerProcurementServiceClient create(ConsumerProcurementServiceSettings settings)

Constructs an instance of ConsumerProcurementServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConsumerProcurementServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerProcurementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConsumerProcurementServiceStub stub)
    
    
    public static final ConsumerProcurementServiceClient create(ConsumerProcurementServiceStub stub)

Constructs an instance of ConsumerProcurementServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConsumerProcurementServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConsumerProcurementServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.stub.ConsumerProcurementServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerProcurementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient)` |   
  
## Constructors 

### ConsumerProcurementServiceClient(ConsumerProcurementServiceSettings settings)
    
    
    protected ConsumerProcurementServiceClient(ConsumerProcurementServiceSettings settings)

Constructs an instance of ConsumerProcurementServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConsumerProcurementServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceSettings)`  
  
  
### ConsumerProcurementServiceClient(ConsumerProcurementServiceStub stub)
    
    
    protected ConsumerProcurementServiceClient(ConsumerProcurementServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConsumerProcurementServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.stub.ConsumerProcurementServiceStub)`  
  
  
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
  
### close()
    
    
    public final void close()

### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getOrder(GetOrderRequest request)
    
    
    public final Order getOrder(GetOrderRequest request)

Returns the requested Order resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       GetOrderRequest request = GetOrderRequest.newBuilder().setName("name3373707").build();
       Order response = consumerProcurementServiceClient.getOrder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.GetOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.Order)` |   
  
### getOrder(String name)
    
    
    public final Order getOrder(String name)

Returns the requested Order resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       String name = "name3373707";
       Order response = consumerProcurementServiceClient.getOrder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the order to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.Order)` |   
  
### getOrderCallable()
    
    
    public final UnaryCallable<GetOrderRequest,Order> getOrderCallable()

Returns the requested Order resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       GetOrderRequest request = GetOrderRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Order> future =
           consumerProcurementServiceClient.getOrderCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.GetOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.Order)>` |   
  
### getSettings()
    
    
    public final @Nullable ConsumerProcurementServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceSettings` |   
  
### getStub()
    
    
    public ConsumerProcurementServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConsumerProcurementServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.stub.ConsumerProcurementServiceStub)` |   
  
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
  
### listOrders(ListOrdersRequest request)
    
    
    public final ConsumerProcurementServiceClient.ListOrdersPagedResponse listOrders(ListOrdersRequest request)

Lists Order resources that the user has access to, within the scope of the parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Order element : consumerProcurementServiceClient.listOrders(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ListOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerProcurementServiceClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient.ListOrdersPagedResponse)` |   
  
### listOrders(String parent)
    
    
    public final ConsumerProcurementServiceClient.ListOrdersPagedResponse listOrders(String parent)

Lists Order resources that the user has access to, within the scope of the parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       String parent = "parent-995424086";
       for (Order element : consumerProcurementServiceClient.listOrders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource to query for orders. This field has the form `billingAccounts/{billing-account-id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerProcurementServiceClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient.ListOrdersPagedResponse)` |   
  
### listOrdersCallable()
    
    
    public final UnaryCallable<ListOrdersRequest,ListOrdersResponse> listOrdersCallable()

Lists Order resources that the user has access to, within the scope of the parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListOrdersResponse response =
             consumerProcurementServiceClient.listOrdersCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ListOrdersRequest),[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ListOrdersResponse)>` |   
  
### listOrdersPagedCallable()
    
    
    public final UnaryCallable<ListOrdersRequest,ConsumerProcurementServiceClient.ListOrdersPagedResponse> listOrdersPagedCallable()

Lists Order resources that the user has access to, within the scope of the parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Order> future =
           consumerProcurementServiceClient.listOrdersPagedCallable().futureCall(request);
       // Do something.
       for (Order element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ListOrdersRequest),[ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementServiceClient.ListOrdersPagedResponse)>` |   
  
### placeOrderAsync(PlaceOrderRequest request)
    
    
    public final OperationFuture<Order,PlaceOrderMetadata> placeOrderAsync(PlaceOrderRequest request)

Creates a new Order.

This API only supports GCP spend-based committed use discounts specified by GCP documentation.

The returned long-running operation is in-progress until the backend completes the creation of the resource. Once completed, the order is in OrderState.ORDER_STATE_ACTIVE. In case of failure, the order resource will be removed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       PlaceOrderRequest request =
           PlaceOrderRequest.newBuilder()
               .setParent(BillingAccountName.of("[BILLING_ACCOUNT]").toString())
               .setDisplayName("displayName1714148973")
               .addAllLineItemInfo(new ArrayList<LineItemInfo>())
               .setRequestId("requestId693933066")
               .build();
       Order response = consumerProcurementServiceClient.placeOrderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PlaceOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.PlaceOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.Order),[PlaceOrderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.PlaceOrderMetadata)>` |   
  
### placeOrderCallable()
    
    
    public final UnaryCallable<PlaceOrderRequest,Operation> placeOrderCallable()

Creates a new Order.

This API only supports GCP spend-based committed use discounts specified by GCP documentation.

The returned long-running operation is in-progress until the backend completes the creation of the resource. Once completed, the order is in OrderState.ORDER_STATE_ACTIVE. In case of failure, the order resource will be removed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       PlaceOrderRequest request =
           PlaceOrderRequest.newBuilder()
               .setParent(BillingAccountName.of("[BILLING_ACCOUNT]").toString())
               .setDisplayName("displayName1714148973")
               .addAllLineItemInfo(new ArrayList<LineItemInfo>())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           consumerProcurementServiceClient.placeOrderCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PlaceOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.PlaceOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### placeOrderOperationCallable()
    
    
    public final OperationCallable<PlaceOrderRequest,Order,PlaceOrderMetadata> placeOrderOperationCallable()

Creates a new Order.

This API only supports GCP spend-based committed use discounts specified by GCP documentation.

The returned long-running operation is in-progress until the backend completes the creation of the resource. Once completed, the order is in OrderState.ORDER_STATE_ACTIVE. In case of failure, the order resource will be removed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConsumerProcurementServiceClient consumerProcurementServiceClient =
         ConsumerProcurementServiceClient.create()) {
       PlaceOrderRequest request =
           PlaceOrderRequest.newBuilder()
               .setParent(BillingAccountName.of("[BILLING_ACCOUNT]").toString())
               .setDisplayName("displayName1714148973")
               .addAllLineItemInfo(new ArrayList<LineItemInfo>())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Order, PlaceOrderMetadata> future =
           consumerProcurementServiceClient.placeOrderOperationCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PlaceOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.PlaceOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.Order),[PlaceOrderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1alpha1.PlaceOrderMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
