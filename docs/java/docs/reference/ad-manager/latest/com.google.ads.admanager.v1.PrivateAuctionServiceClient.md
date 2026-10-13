---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient
title: Class PrivateAuctionServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:59.498822+00:00
---

# Class PrivateAuctionServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PrivateAuctionServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/PrivateAuctionServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `PrivateAuction` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       PrivateAuctionName name = PrivateAuctionName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION]");
       PrivateAuction response = privateAuctionServiceClient.getPrivateAuction(name);
     }
     

Note: close() needs to be called on the PrivateAuctionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetPrivateAuction |  Retrieves a `PrivateAuction` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateAuction(GetPrivateAuctionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateAuction(PrivateAuctionName name) 
  * getPrivateAuction(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateAuctionCallable() 

  
ListPrivateAuctions |  Lists `PrivateAuction` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateAuctions(ListPrivateAuctionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateAuctions(NetworkName parent) 
  * listPrivateAuctions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateAuctionsPagedCallable() 
  * listPrivateAuctionsCallable() 

  
CreatePrivateAuction |  Creates a `PrivateAuction` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateAuction(CreatePrivateAuctionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPrivateAuction(NetworkName parent, PrivateAuction privateAuction) 
  * createPrivateAuction(String parent, PrivateAuction privateAuction) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateAuctionCallable() 

  
UpdatePrivateAuction |  Updates a `PrivateAuction` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePrivateAuction(UpdatePrivateAuctionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePrivateAuction(PrivateAuction privateAuction, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePrivateAuctionCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PrivateAuctionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PrivateAuctionServiceSettings privateAuctionServiceSettings =
         PrivateAuctionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create(privateAuctionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PrivateAuctionServiceSettings privateAuctionServiceSettings =
         PrivateAuctionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create(privateAuctionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PrivateAuctionServiceClient

## Static Methods 

### create()
    
    
    public static final PrivateAuctionServiceClient create()

Constructs an instance of PrivateAuctionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PrivateAuctionServiceSettings settings)
    
    
    public static final PrivateAuctionServiceClient create(PrivateAuctionServiceSettings settings)

Constructs an instance of PrivateAuctionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PrivateAuctionServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PrivateAuctionServiceStub stub)
    
    
    public static final PrivateAuctionServiceClient create(PrivateAuctionServiceStub stub)

Constructs an instance of PrivateAuctionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PrivateAuctionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PrivateAuctionServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PrivateAuctionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient)` |   
  
## Constructors 

### PrivateAuctionServiceClient(PrivateAuctionServiceSettings settings)
    
    
    protected PrivateAuctionServiceClient(PrivateAuctionServiceSettings settings)

Constructs an instance of PrivateAuctionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PrivateAuctionServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceSettings)`  
  
  
### PrivateAuctionServiceClient(PrivateAuctionServiceStub stub)
    
    
    protected PrivateAuctionServiceClient(PrivateAuctionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PrivateAuctionServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PrivateAuctionServiceStub)`  
  
  
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

### createPrivateAuction(@Nullable NetworkName parent, PrivateAuction privateAuction)
    
    
    public final PrivateAuction createPrivateAuction(@Nullable NetworkName parent, PrivateAuction privateAuction)

Creates a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       PrivateAuction privateAuction = PrivateAuction.newBuilder().build();
       PrivateAuction response =
           privateAuctionServiceClient.createPrivateAuction(parent, privateAuction);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `PrivateAuction` will be created. Format: `networks/{network_code}`  
`privateAuction` | `[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)`  
Required. The `PrivateAuction` to create.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### createPrivateAuction(CreatePrivateAuctionRequest request)
    
    
    public final PrivateAuction createPrivateAuction(CreatePrivateAuctionRequest request)

Creates a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       CreatePrivateAuctionRequest request =
           CreatePrivateAuctionRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPrivateAuction(PrivateAuction.newBuilder().build())
               .build();
       PrivateAuction response = privateAuctionServiceClient.createPrivateAuction(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateAuctionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePrivateAuctionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### createPrivateAuction(String parent, PrivateAuction privateAuction)
    
    
    public final PrivateAuction createPrivateAuction(String parent, PrivateAuction privateAuction)

Creates a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       PrivateAuction privateAuction = PrivateAuction.newBuilder().build();
       PrivateAuction response =
           privateAuctionServiceClient.createPrivateAuction(parent, privateAuction);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `PrivateAuction` will be created. Format: `networks/{network_code}`  
`privateAuction` | `[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)`  
Required. The `PrivateAuction` to create.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### createPrivateAuctionCallable()
    
    
    public final UnaryCallable<CreatePrivateAuctionRequest,PrivateAuction> createPrivateAuctionCallable()

Creates a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       CreatePrivateAuctionRequest request =
           CreatePrivateAuctionRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPrivateAuction(PrivateAuction.newBuilder().build())
               .build();
       ApiFuture<PrivateAuction> future =
           privateAuctionServiceClient.createPrivateAuctionCallable().futureCall(request);
       // Do something.
       PrivateAuction response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateAuctionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePrivateAuctionRequest),[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)>` |   
  
### getPrivateAuction(@Nullable PrivateAuctionName name)
    
    
    public final PrivateAuction getPrivateAuction(@Nullable PrivateAuctionName name)

Retrieves a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       PrivateAuctionName name = PrivateAuctionName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION]");
       PrivateAuction response = privateAuctionServiceClient.getPrivateAuction(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PrivateAuctionName`  
Required. The resource name of the PrivateAuction. Format: `networks/{network_code}/privateAuctions/{private_auction_id}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### getPrivateAuction(GetPrivateAuctionRequest request)
    
    
    public final PrivateAuction getPrivateAuction(GetPrivateAuctionRequest request)

Retrieves a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       GetPrivateAuctionRequest request =
           GetPrivateAuctionRequest.newBuilder()
               .setName(PrivateAuctionName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION]").toString())
               .build();
       PrivateAuction response = privateAuctionServiceClient.getPrivateAuction(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateAuctionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPrivateAuctionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### getPrivateAuction(String name)
    
    
    public final PrivateAuction getPrivateAuction(String name)

Retrieves a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       String name = PrivateAuctionName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION]").toString();
       PrivateAuction response = privateAuctionServiceClient.getPrivateAuction(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the PrivateAuction. Format: `networks/{network_code}/privateAuctions/{private_auction_id}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### getPrivateAuctionCallable()
    
    
    public final UnaryCallable<GetPrivateAuctionRequest,PrivateAuction> getPrivateAuctionCallable()

Retrieves a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       GetPrivateAuctionRequest request =
           GetPrivateAuctionRequest.newBuilder()
               .setName(PrivateAuctionName.of("[NETWORK_CODE]", "[PRIVATE_AUCTION]").toString())
               .build();
       ApiFuture<PrivateAuction> future =
           privateAuctionServiceClient.getPrivateAuctionCallable().futureCall(request);
       // Do something.
       PrivateAuction response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateAuctionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPrivateAuctionRequest),[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)>` |   
  
### getSettings()
    
    
    public final @Nullable PrivateAuctionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PrivateAuctionServiceSettings` |   
  
### getStub()
    
    
    public PrivateAuctionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PrivateAuctionServiceStub)` |   
  
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
  
### listPrivateAuctions(@Nullable NetworkName parent)
    
    
    public final PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse listPrivateAuctions(@Nullable NetworkName parent)

Lists `PrivateAuction` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (PrivateAuction element :
           privateAuctionServiceClient.listPrivateAuctions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of PrivateAuctions. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse)` |   
  
### listPrivateAuctions(ListPrivateAuctionsRequest request)
    
    
    public final PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse listPrivateAuctions(ListPrivateAuctionsRequest request)

Lists `PrivateAuction` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       ListPrivateAuctionsRequest request =
           ListPrivateAuctionsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (PrivateAuction element :
           privateAuctionServiceClient.listPrivateAuctions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateAuctionsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse)` |   
  
### listPrivateAuctions(String parent)
    
    
    public final PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse listPrivateAuctions(String parent)

Lists `PrivateAuction` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (PrivateAuction element :
           privateAuctionServiceClient.listPrivateAuctions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of PrivateAuctions. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse)` |   
  
### listPrivateAuctionsCallable()
    
    
    public final UnaryCallable<ListPrivateAuctionsRequest,ListPrivateAuctionsResponse> listPrivateAuctionsCallable()

Lists `PrivateAuction` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       ListPrivateAuctionsRequest request =
           ListPrivateAuctionsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListPrivateAuctionsResponse response =
             privateAuctionServiceClient.listPrivateAuctionsCallable().call(request);
         for (PrivateAuction element : response.getPrivateAuctionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateAuctionsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionsRequest),[ListPrivateAuctionsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionsResponse)>` |   
  
### listPrivateAuctionsPagedCallable()
    
    
    public final UnaryCallable<ListPrivateAuctionsRequest,PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse> listPrivateAuctionsPagedCallable()

Lists `PrivateAuction` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       ListPrivateAuctionsRequest request =
           ListPrivateAuctionsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<PrivateAuction> future =
           privateAuctionServiceClient.listPrivateAuctionsPagedCallable().futureCall(request);
       // Do something.
       for (PrivateAuction element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateAuctionsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPrivateAuctionsRequest),[ListPrivateAuctionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuctionServiceClient.ListPrivateAuctionsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePrivateAuction(PrivateAuction privateAuction, FieldMask updateMask)
    
    
    public final PrivateAuction updatePrivateAuction(PrivateAuction privateAuction, FieldMask updateMask)

Updates a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       PrivateAuction privateAuction = PrivateAuction.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PrivateAuction response =
           privateAuctionServiceClient.updatePrivateAuction(privateAuction, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`privateAuction` | `[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)`  
Required. The `PrivateAuction` to update. The `PrivateAuction`'s `name` is used to identify the `PrivateAuction` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### updatePrivateAuction(UpdatePrivateAuctionRequest request)
    
    
    public final PrivateAuction updatePrivateAuction(UpdatePrivateAuctionRequest request)

Updates a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       UpdatePrivateAuctionRequest request =
           UpdatePrivateAuctionRequest.newBuilder()
               .setPrivateAuction(PrivateAuction.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       PrivateAuction response = privateAuctionServiceClient.updatePrivateAuction(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePrivateAuctionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePrivateAuctionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)` |   
  
### updatePrivateAuctionCallable()
    
    
    public final UnaryCallable<UpdatePrivateAuctionRequest,PrivateAuction> updatePrivateAuctionCallable()

Updates a `PrivateAuction` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PrivateAuctionServiceClient privateAuctionServiceClient =
         PrivateAuctionServiceClient.create()) {
       UpdatePrivateAuctionRequest request =
           UpdatePrivateAuctionRequest.newBuilder()
               .setPrivateAuction(PrivateAuction.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<PrivateAuction> future =
           privateAuctionServiceClient.updatePrivateAuctionCallable().futureCall(request);
       // Do something.
       PrivateAuction response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePrivateAuctionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePrivateAuctionRequest),[PrivateAuction](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PrivateAuction)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
