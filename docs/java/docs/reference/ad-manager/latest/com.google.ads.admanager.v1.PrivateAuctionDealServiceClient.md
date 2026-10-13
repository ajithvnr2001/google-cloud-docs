---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient
title: Class PrivateAuctionDealServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:59.038181+00:00
---

# Class PrivateAuctionDealServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PrivateAuctionDealServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/PrivateAuctionDealServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `PrivateAuctionDeal` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       PrivateAuctionDealName name =
           PrivateAuctionDealName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION_DEAL]");
       PrivateAuctionDeal response = privateAuctionDealServiceClient.getPrivateAuctionDeal(name);
     }
     

Note: close() needs to be called on the PrivateAuctionDealServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetPrivateAuctionDeal |  Retrieves a `PrivateAuctionDeal` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateAuctionDeal(GetPrivateAuctionDealRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateAuctionDeal(PrivateAuctionDealName name) 
  * getPrivateAuctionDeal(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateAuctionDealCallable() 

  
ListPrivateAuctionDeals |  Lists `PrivateAuctionDeal` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateAuctionDeals(ListPrivateAuctionDealsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateAuctionDeals(NetworkName parent) 
  * listPrivateAuctionDeals(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateAuctionDealsPagedCallable() 
  * listPrivateAuctionDealsCallable() 

  
CreatePrivateAuctionDeal |  Creates a `PrivateAuctionDeal` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateAuctionDeal(CreatePrivateAuctionDealRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPrivateAuctionDeal(NetworkName parent, PrivateAuctionDeal privateAuctionDeal) 
  * createPrivateAuctionDeal(String parent, PrivateAuctionDeal privateAuctionDeal) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateAuctionDealCallable() 

  
UpdatePrivateAuctionDeal |  Updates a `PrivateAuctionDeal` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePrivateAuctionDeal(UpdatePrivateAuctionDealRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePrivateAuctionDeal(PrivateAuctionDeal privateAuctionDeal, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePrivateAuctionDealCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PrivateAuctionDealServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PrivateAuctionDealServiceSettings privateAuctionDealServiceSettings =
         PrivateAuctionDealServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create(privateAuctionDealServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PrivateAuctionDealServiceSettings privateAuctionDealServiceSettings =
         PrivateAuctionDealServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create(privateAuctionDealServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PrivateAuctionDealServiceClient

## Static Methods 

### create()
    
    
    public static final PrivateAuctionDealServiceClient create()

Constructs an instance of PrivateAuctionDealServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDealServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PrivateAuctionDealServiceSettings settings)
    
    
    public static final PrivateAuctionDealServiceClient create(PrivateAuctionDealServiceSettings settings)

Constructs an instance of PrivateAuctionDealServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PrivateAuctionDealServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDealServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PrivateAuctionDealServiceStub stub)
    
    
    public static final PrivateAuctionDealServiceClient create(PrivateAuctionDealServiceStub stub)

Constructs an instance of PrivateAuctionDealServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PrivateAuctionDealServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PrivateAuctionDealServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PrivateAuctionDealServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDealServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient)` |   
  
## Constructors 

### PrivateAuctionDealServiceClient(PrivateAuctionDealServiceSettings settings)
    
    
    protected PrivateAuctionDealServiceClient(PrivateAuctionDealServiceSettings settings)

Constructs an instance of PrivateAuctionDealServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PrivateAuctionDealServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceSettings)`  
  
  
### PrivateAuctionDealServiceClient(PrivateAuctionDealServiceStub stub)
    
    
    protected PrivateAuctionDealServiceClient(PrivateAuctionDealServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PrivateAuctionDealServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PrivateAuctionDealServiceStub)`  
  
  
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

### createPrivateAuctionDeal(@Nullable NetworkName parent, PrivateAuctionDeal privateAuctionDeal)
    
    
    public final PrivateAuctionDeal createPrivateAuctionDeal(@Nullable NetworkName parent, PrivateAuctionDeal privateAuctionDeal)

Creates a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       PrivateAuctionDeal privateAuctionDeal = PrivateAuctionDeal.newBuilder().build();
       PrivateAuctionDeal response =
           privateAuctionDealServiceClient.createPrivateAuctionDeal(parent, privateAuctionDeal);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `PrivateAuctionDeal` will be created. Format: `networks/{network_code}`  
`privateAuctionDeal` | `[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)`  
Required. The `PrivateAuctionDeal` to create.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### createPrivateAuctionDeal(CreatePrivateAuctionDealRequest request)
    
    
    public final PrivateAuctionDeal createPrivateAuctionDeal(CreatePrivateAuctionDealRequest request)

Creates a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       CreatePrivateAuctionDealRequest request =
           CreatePrivateAuctionDealRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPrivateAuctionDeal(PrivateAuctionDeal.newBuilder().build())
               .build();
       PrivateAuctionDeal response =
           privateAuctionDealServiceClient.createPrivateAuctionDeal(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateAuctionDealRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePrivateAuctionDealRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### createPrivateAuctionDeal(String parent, PrivateAuctionDeal privateAuctionDeal)
    
    
    public final PrivateAuctionDeal createPrivateAuctionDeal(String parent, PrivateAuctionDeal privateAuctionDeal)

Creates a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       PrivateAuctionDeal privateAuctionDeal = PrivateAuctionDeal.newBuilder().build();
       PrivateAuctionDeal response =
           privateAuctionDealServiceClient.createPrivateAuctionDeal(parent, privateAuctionDeal);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `PrivateAuctionDeal` will be created. Format: `networks/{network_code}`  
`privateAuctionDeal` | `[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)`  
Required. The `PrivateAuctionDeal` to create.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### createPrivateAuctionDealCallable()
    
    
    public final UnaryCallable<CreatePrivateAuctionDealRequest,PrivateAuctionDeal> createPrivateAuctionDealCallable()

Creates a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       CreatePrivateAuctionDealRequest request =
           CreatePrivateAuctionDealRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPrivateAuctionDeal(PrivateAuctionDeal.newBuilder().build())
               .build();
       ApiFuture<PrivateAuctionDeal> future =
           privateAuctionDealServiceClient.createPrivateAuctionDealCallable().futureCall(request);
       // Do something.
       PrivateAuctionDeal response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateAuctionDealRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePrivateAuctionDealRequest),[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)>` |   
  
### getPrivateAuctionDeal(@Nullable PrivateAuctionDealName name)
    
    
    public final PrivateAuctionDeal getPrivateAuctionDeal(@Nullable PrivateAuctionDealName name)

Retrieves a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       PrivateAuctionDealName name =
           PrivateAuctionDealName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION_DEAL]");
       PrivateAuctionDeal response = privateAuctionDealServiceClient.getPrivateAuctionDeal(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PrivateAuctionDealName`  
Required. The resource name of the PrivateAuctionDeal. Format: `networks/{network_code}/privateAuctionDeals/{private_auction_deal_id}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### getPrivateAuctionDeal(GetPrivateAuctionDealRequest request)
    
    
    public final PrivateAuctionDeal getPrivateAuctionDeal(GetPrivateAuctionDealRequest request)

Retrieves a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       GetPrivateAuctionDealRequest request =
           GetPrivateAuctionDealRequest.newBuilder()
               .setName(
                   PrivateAuctionDealName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION_DEAL]").toString())
               .build();
       PrivateAuctionDeal response = privateAuctionDealServiceClient.getPrivateAuctionDeal(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateAuctionDealRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPrivateAuctionDealRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### getPrivateAuctionDeal(String name)
    
    
    public final PrivateAuctionDeal getPrivateAuctionDeal(String name)

Retrieves a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       String name =
           PrivateAuctionDealName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION_DEAL]").toString();
       PrivateAuctionDeal response = privateAuctionDealServiceClient.getPrivateAuctionDeal(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the PrivateAuctionDeal. Format: `networks/{network_code}/privateAuctionDeals/{private_auction_deal_id}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### getPrivateAuctionDealCallable()
    
    
    public final UnaryCallable<GetPrivateAuctionDealRequest,PrivateAuctionDeal> getPrivateAuctionDealCallable()

Retrieves a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       GetPrivateAuctionDealRequest request =
           GetPrivateAuctionDealRequest.newBuilder()
               .setName(
                   PrivateAuctionDealName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION_DEAL]").toString())
               .build();
       ApiFuture<PrivateAuctionDeal> future =
           privateAuctionDealServiceClient.getPrivateAuctionDealCallable().futureCall(request);
       // Do something.
       PrivateAuctionDeal response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateAuctionDealRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPrivateAuctionDealRequest),[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)>` |   
  
### getSettings()
    
    
    public final @Nullable PrivateAuctionDealServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PrivateAuctionDealServiceSettings` |   
  
### getStub()
    
    
    public PrivateAuctionDealServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDealServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PrivateAuctionDealServiceStub)` |   
  
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
  
### listPrivateAuctionDeals(@Nullable NetworkName parent)
    
    
    public final PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse listPrivateAuctionDeals(@Nullable NetworkName parent)

Lists `PrivateAuctionDeal` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (PrivateAuctionDeal element :
           privateAuctionDealServiceClient.listPrivateAuctionDeals(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of PrivateAuctionDeals. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse)` |   
  
### listPrivateAuctionDeals(ListPrivateAuctionDealsRequest request)
    
    
    public final PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse listPrivateAuctionDeals(ListPrivateAuctionDealsRequest request)

Lists `PrivateAuctionDeal` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       ListPrivateAuctionDealsRequest request =
           ListPrivateAuctionDealsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (PrivateAuctionDeal element :
           privateAuctionDealServiceClient.listPrivateAuctionDeals(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateAuctionDealsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionDealsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse)` |   
  
### listPrivateAuctionDeals(String parent)
    
    
    public final PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse listPrivateAuctionDeals(String parent)

Lists `PrivateAuctionDeal` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (PrivateAuctionDeal element :
           privateAuctionDealServiceClient.listPrivateAuctionDeals(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of PrivateAuctionDeals. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse)` |   
  
### listPrivateAuctionDealsCallable()
    
    
    public final UnaryCallable<ListPrivateAuctionDealsRequest,ListPrivateAuctionDealsResponse> listPrivateAuctionDealsCallable()

Lists `PrivateAuctionDeal` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       ListPrivateAuctionDealsRequest request =
           ListPrivateAuctionDealsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListPrivateAuctionDealsResponse response =
             privateAuctionDealServiceClient.listPrivateAuctionDealsCallable().call(request);
         for (PrivateAuctionDeal element : response.getPrivateAuctionDealsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateAuctionDealsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionDealsRequest),[ListPrivateAuctionDealsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionDealsResponse)>` |   
  
### listPrivateAuctionDealsPagedCallable()
    
    
    public final UnaryCallable<ListPrivateAuctionDealsRequest,PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse> listPrivateAuctionDealsPagedCallable()

Lists `PrivateAuctionDeal` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       ListPrivateAuctionDealsRequest request =
           ListPrivateAuctionDealsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<PrivateAuctionDeal> future =
           privateAuctionDealServiceClient
               .listPrivateAuctionDealsPagedCallable()
               .futureCall(request);
       // Do something.
       for (PrivateAuctionDeal element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateAuctionDealsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionDealsRequest),[ListPrivateAuctionDealsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDealServiceClient.ListPrivateAuctionDealsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePrivateAuctionDeal(PrivateAuctionDeal privateAuctionDeal, FieldMask updateMask)
    
    
    public final PrivateAuctionDeal updatePrivateAuctionDeal(PrivateAuctionDeal privateAuctionDeal, FieldMask updateMask)

Updates a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       PrivateAuctionDeal privateAuctionDeal = PrivateAuctionDeal.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PrivateAuctionDeal response =
           privateAuctionDealServiceClient.updatePrivateAuctionDeal(privateAuctionDeal, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`privateAuctionDeal` | `[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)`  
Required. The `PrivateAuctionDeal` to update. The `PrivateAuctionDeal`'s `name` is used to identify the `PrivateAuctionDeal` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### updatePrivateAuctionDeal(UpdatePrivateAuctionDealRequest request)
    
    
    public final PrivateAuctionDeal updatePrivateAuctionDeal(UpdatePrivateAuctionDealRequest request)

Updates a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       UpdatePrivateAuctionDealRequest request =
           UpdatePrivateAuctionDealRequest.newBuilder()
               .setPrivateAuctionDeal(PrivateAuctionDeal.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       PrivateAuctionDeal response =
           privateAuctionDealServiceClient.updatePrivateAuctionDeal(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePrivateAuctionDealRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePrivateAuctionDealRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)` |   
  
### updatePrivateAuctionDealCallable()
    
    
    public final UnaryCallable<UpdatePrivateAuctionDealRequest,PrivateAuctionDeal> updatePrivateAuctionDealCallable()

Updates a `PrivateAuctionDeal` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionDealServiceClient privateAuctionDealServiceClient =
         PrivateAuctionDealServiceClient.create()) {
       UpdatePrivateAuctionDealRequest request =
           UpdatePrivateAuctionDealRequest.newBuilder()
               .setPrivateAuctionDeal(PrivateAuctionDeal.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<PrivateAuctionDeal> future =
           privateAuctionDealServiceClient.updatePrivateAuctionDealCallable().futureCall(request);
       // Do something.
       PrivateAuctionDeal response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePrivateAuctionDealRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePrivateAuctionDealRequest),[PrivateAuctionDeal](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionDeal)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
