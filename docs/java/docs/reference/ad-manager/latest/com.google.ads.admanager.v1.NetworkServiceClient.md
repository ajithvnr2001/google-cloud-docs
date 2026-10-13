---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceClient
title: Class NetworkServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:53.970326+00:00
---

# Class NetworkServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/NetworkServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Network` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       NetworkName name = NetworkName.of("[NETWORK_CODE]");
       Network response = networkServiceClient.getNetwork(name);
     }
     

Note: close() needs to be called on the NetworkServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetNetwork |  Retrieves a `Network` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNetwork(GetNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNetwork(NetworkName name) 
  * getNetwork(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNetworkCallable() 

  
ListNetworks |  Retrieves all the networks the current user has access to. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNetworks(ListNetworksRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNetworksPagedCallable() 
  * listNetworksCallable() 

  
UpdateNetwork |  Updates a `Network` object. Currently, only the network display name can be updated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNetwork(UpdateNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateNetwork(Network network, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNetworkCallable() 

  
ProvisionTestNetwork |  Provisions a test network associated with the current user. Only one test network can be provisioned per user.  Before the test network can be used, you must complete setup in the Ad Manager UI. If the test network's owner is a service account, you must add a non-service account user by calling UserService.CreateUser.  Test networks are limited in the following ways:  * Test networks have a maximum of 10,000 objects per entity type. * Test networks cannot serve ads. * Reports on serving data have zero rows. * Forecast service results contain mock data. * Test networks do not have Ad Manager 360 or premium features enabled. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * provisionTestNetwork(ProvisionTestNetworkRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * provisionTestNetworkCallable() 

  
GetDefaultThirdPartyDataDeclaration |  Returns the [DefaultThirdPartyDataDeclaration] for this network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDefaultThirdPartyDataDeclaration(GetDefaultThirdPartyDataDeclarationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDefaultThirdPartyDataDeclaration(DefaultThirdPartyDataDeclarationName name) 
  * getDefaultThirdPartyDataDeclaration(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDefaultThirdPartyDataDeclarationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NetworkServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkServiceSettings networkServiceSettings =
         NetworkServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NetworkServiceClient networkServiceClient = NetworkServiceClient.create(networkServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkServiceSettings networkServiceSettings =
         NetworkServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     NetworkServiceClient networkServiceClient = NetworkServiceClient.create(networkServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworkServiceClient

## Static Methods 

### create()
    
    
    public static final NetworkServiceClient create()

Constructs an instance of NetworkServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NetworkServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkServiceSettings settings)
    
    
    public static final NetworkServiceClient create(NetworkServiceSettings settings)

Constructs an instance of NetworkServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkServiceStub stub)
    
    
    public static final NetworkServiceClient create(NetworkServiceStub stub)

Constructs an instance of NetworkServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(NetworkServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.NetworkServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceClient)` |   
  
## Constructors 

### NetworkServiceClient(NetworkServiceSettings settings)
    
    
    protected NetworkServiceClient(NetworkServiceSettings settings)

Constructs an instance of NetworkServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceSettings)`  
  
  
### NetworkServiceClient(NetworkServiceStub stub)
    
    
    protected NetworkServiceClient(NetworkServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.NetworkServiceStub)`  
  
  
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

### getDefaultThirdPartyDataDeclaration(@Nullable DefaultThirdPartyDataDeclarationName name)
    
    
    public final DefaultThirdPartyDataDeclaration getDefaultThirdPartyDataDeclaration(@Nullable DefaultThirdPartyDataDeclarationName name)

Returns the [DefaultThirdPartyDataDeclaration] for this network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       DefaultThirdPartyDataDeclarationName name =
           DefaultThirdPartyDataDeclarationName.of("[NETWORK_CODE]");
       DefaultThirdPartyDataDeclaration response =
           networkServiceClient.getDefaultThirdPartyDataDeclaration(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DefaultThirdPartyDataDeclarationName`  
Required. Resource name of DefaultThirdPartyDataDeclaration. Format: networks/{network_code}/defaultThirdPartyDataDeclaration  
**Returns**  
---  
**Type** | **Description**  
`[DefaultThirdPartyDataDeclaration](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DefaultThirdPartyDataDeclaration)` |   
  
### getDefaultThirdPartyDataDeclaration(GetDefaultThirdPartyDataDeclarationRequest request)
    
    
    public final DefaultThirdPartyDataDeclaration getDefaultThirdPartyDataDeclaration(GetDefaultThirdPartyDataDeclarationRequest request)

Returns the [DefaultThirdPartyDataDeclaration] for this network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       GetDefaultThirdPartyDataDeclarationRequest request =
           GetDefaultThirdPartyDataDeclarationRequest.newBuilder()
               .setName(DefaultThirdPartyDataDeclarationName.of("[NETWORK_CODE]").toString())
               .build();
       DefaultThirdPartyDataDeclaration response =
           networkServiceClient.getDefaultThirdPartyDataDeclaration(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDefaultThirdPartyDataDeclarationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDefaultThirdPartyDataDeclarationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DefaultThirdPartyDataDeclaration](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DefaultThirdPartyDataDeclaration)` |   
  
### getDefaultThirdPartyDataDeclaration(String name)
    
    
    public final DefaultThirdPartyDataDeclaration getDefaultThirdPartyDataDeclaration(String name)

Returns the [DefaultThirdPartyDataDeclaration] for this network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       String name = DefaultThirdPartyDataDeclarationName.of("[NETWORK_CODE]").toString();
       DefaultThirdPartyDataDeclaration response =
           networkServiceClient.getDefaultThirdPartyDataDeclaration(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of DefaultThirdPartyDataDeclaration. Format: networks/{network_code}/defaultThirdPartyDataDeclaration  
**Returns**  
---  
**Type** | **Description**  
`[DefaultThirdPartyDataDeclaration](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DefaultThirdPartyDataDeclaration)` |   
  
### getDefaultThirdPartyDataDeclarationCallable()
    
    
    public final UnaryCallable<GetDefaultThirdPartyDataDeclarationRequest,DefaultThirdPartyDataDeclaration> getDefaultThirdPartyDataDeclarationCallable()

Returns the [DefaultThirdPartyDataDeclaration] for this network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       GetDefaultThirdPartyDataDeclarationRequest request =
           GetDefaultThirdPartyDataDeclarationRequest.newBuilder()
               .setName(DefaultThirdPartyDataDeclarationName.of("[NETWORK_CODE]").toString())
               .build();
       ApiFuture<DefaultThirdPartyDataDeclaration> future =
           networkServiceClient.getDefaultThirdPartyDataDeclarationCallable().futureCall(request);
       // Do something.
       DefaultThirdPartyDataDeclaration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDefaultThirdPartyDataDeclarationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDefaultThirdPartyDataDeclarationRequest),[DefaultThirdPartyDataDeclaration](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DefaultThirdPartyDataDeclaration)>` |   
  
### getNetwork(@Nullable NetworkName name)
    
    
    public final Network getNetwork(@Nullable NetworkName name)

Retrieves a `Network` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       NetworkName name = NetworkName.of("[NETWORK_CODE]");
       Network response = networkServiceClient.getNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Resource name of Network. Format: networks/{network_code}  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)` |   
  
### getNetwork(GetNetworkRequest request)
    
    
    public final Network getNetwork(GetNetworkRequest request)

Retrieves a `Network` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       GetNetworkRequest request =
           GetNetworkRequest.newBuilder()
               .setName(NetworkName.of("[NETWORK_CODE]").toString())
               .build();
       Network response = networkServiceClient.getNetwork(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)` |   
  
### getNetwork(String name)
    
    
    public final Network getNetwork(String name)

Retrieves a `Network` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       String name = NetworkName.of("[NETWORK_CODE]").toString();
       Network response = networkServiceClient.getNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of Network. Format: networks/{network_code}  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)` |   
  
### getNetworkCallable()
    
    
    public final UnaryCallable<GetNetworkRequest,Network> getNetworkCallable()

Retrieves a `Network` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       GetNetworkRequest request =
           GetNetworkRequest.newBuilder()
               .setName(NetworkName.of("[NETWORK_CODE]").toString())
               .build();
       ApiFuture<Network> future = networkServiceClient.getNetworkCallable().futureCall(request);
       // Do something.
       Network response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)>` |   
  
### getSettings()
    
    
    public final @Nullable NetworkServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkServiceSettings` |   
  
### getStub()
    
    
    public NetworkServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NetworkServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.NetworkServiceStub)` |   
  
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
  
### listNetworks(ListNetworksRequest request)
    
    
    public final NetworkServiceClient.ListNetworksPagedResponse listNetworks(ListNetworksRequest request)

Retrieves all the networks the current user has access to.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSkip(3532159)
               .build();
       for (Network element : networkServiceClient.listNetworks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServiceClient.ListNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceClient.ListNetworksPagedResponse)` |   
  
### listNetworksCallable()
    
    
    public final UnaryCallable<ListNetworksRequest,ListNetworksResponse> listNetworksCallable()

Retrieves all the networks the current user has access to.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSkip(3532159)
               .build();
       while (true) {
         ListNetworksResponse response = networkServiceClient.listNetworksCallable().call(request);
         for (Network element : response.getNetworksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNetworksRequest),[ListNetworksResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNetworksResponse)>` |   
  
### listNetworksPagedCallable()
    
    
    public final UnaryCallable<ListNetworksRequest,NetworkServiceClient.ListNetworksPagedResponse> listNetworksPagedCallable()

Retrieves all the networks the current user has access to.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSkip(3532159)
               .build();
       ApiFuture<Network> future =
           networkServiceClient.listNetworksPagedCallable().futureCall(request);
       // Do something.
       for (Network element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNetworksRequest),[ListNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NetworkServiceClient.ListNetworksPagedResponse)>` |   
  
### provisionTestNetwork(ProvisionTestNetworkRequest request)
    
    
    public final Network provisionTestNetwork(ProvisionTestNetworkRequest request)

Provisions a test network associated with the current user. Only one test network can be provisioned per user.

Before the test network can be used, you must complete setup in the Ad Manager UI. If the test network's owner is a service account, you must add a non-service account user by calling UserService.CreateUser.

Test networks are limited in the following ways:

* Test networks have a maximum of 10,000 objects per entity type. * Test networks cannot serve ads. * Reports on serving data have zero rows. * Forecast service results contain mock data. * Test networks do not have Ad Manager 360 or premium features enabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       ProvisionTestNetworkRequest request = ProvisionTestNetworkRequest.newBuilder().build();
       Network response = networkServiceClient.provisionTestNetwork(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ProvisionTestNetworkRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProvisionTestNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)` |   
  
### provisionTestNetworkCallable()
    
    
    public final UnaryCallable<ProvisionTestNetworkRequest,Network> provisionTestNetworkCallable()

Provisions a test network associated with the current user. Only one test network can be provisioned per user.

Before the test network can be used, you must complete setup in the Ad Manager UI. If the test network's owner is a service account, you must add a non-service account user by calling UserService.CreateUser.

Test networks are limited in the following ways:

* Test networks have a maximum of 10,000 objects per entity type. * Test networks cannot serve ads. * Reports on serving data have zero rows. * Forecast service results contain mock data. * Test networks do not have Ad Manager 360 or premium features enabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       ProvisionTestNetworkRequest request = ProvisionTestNetworkRequest.newBuilder().build();
       ApiFuture<Network> future =
           networkServiceClient.provisionTestNetworkCallable().futureCall(request);
       // Do something.
       Network response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ProvisionTestNetworkRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProvisionTestNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateNetwork(Network network, FieldMask updateMask)
    
    
    public final Network updateNetwork(Network network, FieldMask updateMask)

Updates a `Network` object. Currently, only the network display name can be updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       Network network = Network.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Network response = networkServiceClient.updateNetwork(network, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`network` | `[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)`  
Required. The `Network` to update. The `Network`'s `name` is used to identify the `Network` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)` |   
  
### updateNetwork(UpdateNetworkRequest request)
    
    
    public final Network updateNetwork(UpdateNetworkRequest request)

Updates a `Network` object. Currently, only the network display name can be updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       UpdateNetworkRequest request =
           UpdateNetworkRequest.newBuilder()
               .setNetwork(Network.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Network response = networkServiceClient.updateNetwork(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)` |   
  
### updateNetworkCallable()
    
    
    public final UnaryCallable<UpdateNetworkRequest,Network> updateNetworkCallable()

Updates a `Network` object. Currently, only the network display name can be updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServiceClient networkServiceClient = NetworkServiceClient.create()) {
       UpdateNetworkRequest request =
           UpdateNetworkRequest.newBuilder()
               .setNetwork(Network.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Network> future = networkServiceClient.updateNetworkCallable().futureCall(request);
       // Do something.
       Network response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Network)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
