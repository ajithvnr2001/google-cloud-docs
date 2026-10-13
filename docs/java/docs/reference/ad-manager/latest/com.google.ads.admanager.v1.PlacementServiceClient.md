---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient
title: Class PlacementServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:57.684344+00:00
---

# Class PlacementServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PlacementServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/PlacementServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Placement` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       PlacementName name = PlacementName.of("[NETWORK_CODE]", "[PLACEMENT]");
       Placement response = placementServiceClient.getPlacement(name);
     }
     

Note: close() needs to be called on the PlacementServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetPlacement |  Retrieves a `Placement` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPlacement(GetPlacementRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPlacement(PlacementName name) 
  * getPlacement(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPlacementCallable() 

  
ListPlacements |  Lists `Placement` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPlacements(ListPlacementsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPlacements(NetworkName parent) 
  * listPlacements(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPlacementsPagedCallable() 
  * listPlacementsCallable() 

  
CreatePlacement |  Creates an `Placement` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPlacement(CreatePlacementRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPlacement(NetworkName parent, Placement placement) 
  * createPlacement(String parent, Placement placement) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPlacementCallable() 

  
UpdatePlacement |  Updates an `Placement` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePlacement(UpdatePlacementRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePlacement(Placement placement, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePlacementCallable() 

  
BatchCreatePlacements |  Creates `Placement` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreatePlacements(NetworkName parent, List<CreatePlacementRequest> requests) 
  * batchCreatePlacements(String parent, List<CreatePlacementRequest> requests) 
  * batchCreatePlacements(BatchCreatePlacementsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreatePlacementsCallable() 

  
BatchUpdatePlacements |  Batch updates `Placement` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdatePlacements(NetworkName parent, List<UpdatePlacementRequest> requests) 
  * batchUpdatePlacements(String parent, List<UpdatePlacementRequest> requests) 
  * batchUpdatePlacements(BatchUpdatePlacementsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdatePlacementsCallable() 

  
BatchActivatePlacements |  Activates a list of `Placement` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivatePlacements(BatchActivatePlacementsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivatePlacements(NetworkName parent, List<String> names) 
  * batchActivatePlacements(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivatePlacementsCallable() 

  
BatchDeactivatePlacements |  Deactivates a list of `Placement` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivatePlacements(BatchDeactivatePlacementsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivatePlacements(NetworkName parent, List<String> names) 
  * batchDeactivatePlacements(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivatePlacementsCallable() 

  
BatchArchivePlacements |  Archives a list of `Placement` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchivePlacements(BatchArchivePlacementsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchivePlacements(NetworkName parent, List<String> names) 
  * batchArchivePlacements(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchivePlacementsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PlacementServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PlacementServiceSettings placementServiceSettings =
         PlacementServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PlacementServiceClient placementServiceClient =
         PlacementServiceClient.create(placementServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PlacementServiceSettings placementServiceSettings =
         PlacementServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PlacementServiceClient placementServiceClient =
         PlacementServiceClient.create(placementServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PlacementServiceClient

## Static Methods 

### create()
    
    
    public static final PlacementServiceClient create()

Constructs an instance of PlacementServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PlacementServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PlacementServiceSettings settings)
    
    
    public static final PlacementServiceClient create(PlacementServiceSettings settings)

Constructs an instance of PlacementServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PlacementServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlacementServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PlacementServiceStub stub)
    
    
    public static final PlacementServiceClient create(PlacementServiceStub stub)

Constructs an instance of PlacementServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PlacementServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PlacementServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PlacementServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlacementServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient)` |   
  
## Constructors 

### PlacementServiceClient(PlacementServiceSettings settings)
    
    
    protected PlacementServiceClient(PlacementServiceSettings settings)

Constructs an instance of PlacementServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PlacementServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceSettings)`  
  
  
### PlacementServiceClient(PlacementServiceStub stub)
    
    
    protected PlacementServiceClient(PlacementServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PlacementServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PlacementServiceStub)`  
  
  
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
  
### batchActivatePlacements(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivatePlacementsResponse batchActivatePlacements(@Nullable NetworkName parent, List<String> names)

Activates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivatePlacementsResponse response =
           placementServiceClient.batchActivatePlacements(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the `Placement` objects to activate. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivatePlacementsResponse)` |   
  
### batchActivatePlacements(BatchActivatePlacementsRequest request)
    
    
    public final BatchActivatePlacementsResponse batchActivatePlacements(BatchActivatePlacementsRequest request)

Activates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchActivatePlacementsRequest request =
           BatchActivatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivatePlacementsResponse response =
           placementServiceClient.batchActivatePlacements(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivatePlacementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivatePlacementsResponse)` |   
  
### batchActivatePlacements(String parent, List<String> names)
    
    
    public final BatchActivatePlacementsResponse batchActivatePlacements(String parent, List<String> names)

Activates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivatePlacementsResponse response =
           placementServiceClient.batchActivatePlacements(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the `Placement` objects to activate. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivatePlacementsResponse)` |   
  
### batchActivatePlacementsCallable()
    
    
    public final UnaryCallable<BatchActivatePlacementsRequest,BatchActivatePlacementsResponse> batchActivatePlacementsCallable()

Activates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchActivatePlacementsRequest request =
           BatchActivatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivatePlacementsResponse> future =
           placementServiceClient.batchActivatePlacementsCallable().futureCall(request);
       // Do something.
       BatchActivatePlacementsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivatePlacementsRequest),[BatchActivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivatePlacementsResponse)>` |   
  
### batchArchivePlacements(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchivePlacementsResponse batchArchivePlacements(@Nullable NetworkName parent, List<String> names)

Archives a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchivePlacementsResponse response =
           placementServiceClient.batchArchivePlacements(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the `Placement` objects to archive. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchivePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchivePlacementsResponse)` |   
  
### batchArchivePlacements(BatchArchivePlacementsRequest request)
    
    
    public final BatchArchivePlacementsResponse batchArchivePlacements(BatchArchivePlacementsRequest request)

Archives a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchArchivePlacementsRequest request =
           BatchArchivePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchivePlacementsResponse response =
           placementServiceClient.batchArchivePlacements(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchivePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchivePlacementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchivePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchivePlacementsResponse)` |   
  
### batchArchivePlacements(String parent, List<String> names)
    
    
    public final BatchArchivePlacementsResponse batchArchivePlacements(String parent, List<String> names)

Archives a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchivePlacementsResponse response =
           placementServiceClient.batchArchivePlacements(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the `Placement` objects to archive. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchivePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchivePlacementsResponse)` |   
  
### batchArchivePlacementsCallable()
    
    
    public final UnaryCallable<BatchArchivePlacementsRequest,BatchArchivePlacementsResponse> batchArchivePlacementsCallable()

Archives a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchArchivePlacementsRequest request =
           BatchArchivePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchivePlacementsResponse> future =
           placementServiceClient.batchArchivePlacementsCallable().futureCall(request);
       // Do something.
       BatchArchivePlacementsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchivePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchivePlacementsRequest),[BatchArchivePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchivePlacementsResponse)>` |   
  
### batchCreatePlacements(@Nullable NetworkName parent, List<CreatePlacementRequest> requests)
    
    
    public final BatchCreatePlacementsResponse batchCreatePlacements(@Nullable NetworkName parent, List<CreatePlacementRequest> requests)

Creates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreatePlacementRequest> requests = new ArrayList<>();
       BatchCreatePlacementsResponse response =
           placementServiceClient.batchCreatePlacements(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where the `Placement`s will be created. Format: `networks/{network_code}` The parent field in the CreatePlacementRequest messages match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePlacementRequest)>`  
Required. The `Placement` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreatePlacementsResponse)` |   
  
### batchCreatePlacements(BatchCreatePlacementsRequest request)
    
    
    public final BatchCreatePlacementsResponse batchCreatePlacements(BatchCreatePlacementsRequest request)

Creates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchCreatePlacementsRequest request =
           BatchCreatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreatePlacementRequest>())
               .build();
       BatchCreatePlacementsResponse response =
           placementServiceClient.batchCreatePlacements(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreatePlacementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreatePlacementsResponse)` |   
  
### batchCreatePlacements(String parent, List<CreatePlacementRequest> requests)
    
    
    public final BatchCreatePlacementsResponse batchCreatePlacements(String parent, List<CreatePlacementRequest> requests)

Creates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreatePlacementRequest> requests = new ArrayList<>();
       BatchCreatePlacementsResponse response =
           placementServiceClient.batchCreatePlacements(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the `Placement`s will be created. Format: `networks/{network_code}` The parent field in the CreatePlacementRequest messages match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePlacementRequest)>`  
Required. The `Placement` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreatePlacementsResponse)` |   
  
### batchCreatePlacementsCallable()
    
    
    public final UnaryCallable<BatchCreatePlacementsRequest,BatchCreatePlacementsResponse> batchCreatePlacementsCallable()

Creates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchCreatePlacementsRequest request =
           BatchCreatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreatePlacementRequest>())
               .build();
       ApiFuture<BatchCreatePlacementsResponse> future =
           placementServiceClient.batchCreatePlacementsCallable().futureCall(request);
       // Do something.
       BatchCreatePlacementsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreatePlacementsRequest),[BatchCreatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreatePlacementsResponse)>` |   
  
### batchDeactivatePlacements(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivatePlacementsResponse batchDeactivatePlacements(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivatePlacementsResponse response =
           placementServiceClient.batchDeactivatePlacements(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the `Placement` objects to deactivate. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivatePlacementsResponse)` |   
  
### batchDeactivatePlacements(BatchDeactivatePlacementsRequest request)
    
    
    public final BatchDeactivatePlacementsResponse batchDeactivatePlacements(BatchDeactivatePlacementsRequest request)

Deactivates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchDeactivatePlacementsRequest request =
           BatchDeactivatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivatePlacementsResponse response =
           placementServiceClient.batchDeactivatePlacements(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivatePlacementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivatePlacementsResponse)` |   
  
### batchDeactivatePlacements(String parent, List<String> names)
    
    
    public final BatchDeactivatePlacementsResponse batchDeactivatePlacements(String parent, List<String> names)

Deactivates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivatePlacementsResponse response =
           placementServiceClient.batchDeactivatePlacements(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the `Placement` objects to deactivate. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivatePlacementsResponse)` |   
  
### batchDeactivatePlacementsCallable()
    
    
    public final UnaryCallable<BatchDeactivatePlacementsRequest,BatchDeactivatePlacementsResponse> batchDeactivatePlacementsCallable()

Deactivates a list of `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchDeactivatePlacementsRequest request =
           BatchDeactivatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivatePlacementsResponse> future =
           placementServiceClient.batchDeactivatePlacementsCallable().futureCall(request);
       // Do something.
       BatchDeactivatePlacementsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivatePlacementsRequest),[BatchDeactivatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivatePlacementsResponse)>` |   
  
### batchUpdatePlacements(@Nullable NetworkName parent, List<UpdatePlacementRequest> requests)
    
    
    public final BatchUpdatePlacementsResponse batchUpdatePlacements(@Nullable NetworkName parent, List<UpdatePlacementRequest> requests)

Batch updates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdatePlacementRequest> requests = new ArrayList<>();
       BatchUpdatePlacementsResponse response =
           placementServiceClient.batchUpdatePlacements(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Placements` will be updated. Format: `networks/{network_code}` The parent field in the UpdatePlacementsRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePlacementRequest)>`  
Required. The `Placement` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePlacementsResponse)` |   
  
### batchUpdatePlacements(BatchUpdatePlacementsRequest request)
    
    
    public final BatchUpdatePlacementsResponse batchUpdatePlacements(BatchUpdatePlacementsRequest request)

Batch updates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchUpdatePlacementsRequest request =
           BatchUpdatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdatePlacementRequest>())
               .build();
       BatchUpdatePlacementsResponse response =
           placementServiceClient.batchUpdatePlacements(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePlacementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePlacementsResponse)` |   
  
### batchUpdatePlacements(String parent, List<UpdatePlacementRequest> requests)
    
    
    public final BatchUpdatePlacementsResponse batchUpdatePlacements(String parent, List<UpdatePlacementRequest> requests)

Batch updates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdatePlacementRequest> requests = new ArrayList<>();
       BatchUpdatePlacementsResponse response =
           placementServiceClient.batchUpdatePlacements(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Placements` will be updated. Format: `networks/{network_code}` The parent field in the UpdatePlacementsRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePlacementRequest)>`  
Required. The `Placement` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePlacementsResponse)` |   
  
### batchUpdatePlacementsCallable()
    
    
    public final UnaryCallable<BatchUpdatePlacementsRequest,BatchUpdatePlacementsResponse> batchUpdatePlacementsCallable()

Batch updates `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       BatchUpdatePlacementsRequest request =
           BatchUpdatePlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdatePlacementRequest>())
               .build();
       ApiFuture<BatchUpdatePlacementsResponse> future =
           placementServiceClient.batchUpdatePlacementsCallable().futureCall(request);
       // Do something.
       BatchUpdatePlacementsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdatePlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePlacementsRequest),[BatchUpdatePlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePlacementsResponse)>` |   
  
### close()
    
    
    public final void close()

### createPlacement(@Nullable NetworkName parent, Placement placement)
    
    
    public final Placement createPlacement(@Nullable NetworkName parent, Placement placement)

Creates an `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Placement placement = Placement.newBuilder().build();
       Placement response = placementServiceClient.createPlacement(parent, placement);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Placement` will be created. Format: `networks/{network_code}`  
`placement` | `[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)`  
Required. The `Placement` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### createPlacement(CreatePlacementRequest request)
    
    
    public final Placement createPlacement(CreatePlacementRequest request)

Creates an `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       CreatePlacementRequest request =
           CreatePlacementRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPlacement(Placement.newBuilder().build())
               .build();
       Placement response = placementServiceClient.createPlacement(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePlacementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### createPlacement(String parent, Placement placement)
    
    
    public final Placement createPlacement(String parent, Placement placement)

Creates an `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Placement placement = Placement.newBuilder().build();
       Placement response = placementServiceClient.createPlacement(parent, placement);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Placement` will be created. Format: `networks/{network_code}`  
`placement` | `[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)`  
Required. The `Placement` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### createPlacementCallable()
    
    
    public final UnaryCallable<CreatePlacementRequest,Placement> createPlacementCallable()

Creates an `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       CreatePlacementRequest request =
           CreatePlacementRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPlacement(Placement.newBuilder().build())
               .build();
       ApiFuture<Placement> future =
           placementServiceClient.createPlacementCallable().futureCall(request);
       // Do something.
       Placement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreatePlacementRequest),[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)>` |   
  
### getPlacement(@Nullable PlacementName name)
    
    
    public final Placement getPlacement(@Nullable PlacementName name)

Retrieves a `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       PlacementName name = PlacementName.of("[NETWORK_CODE]", "[PLACEMENT]");
       Placement response = placementServiceClient.getPlacement(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PlacementName`  
Required. The resource name of the Placement. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### getPlacement(GetPlacementRequest request)
    
    
    public final Placement getPlacement(GetPlacementRequest request)

Retrieves a `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       GetPlacementRequest request =
           GetPlacementRequest.newBuilder()
               .setName(PlacementName.of("[NETWORK_CODE]", "[PLACEMENT]").toString())
               .build();
       Placement response = placementServiceClient.getPlacement(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPlacementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### getPlacement(String name)
    
    
    public final Placement getPlacement(String name)

Retrieves a `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String name = PlacementName.of("[NETWORK_CODE]", "[PLACEMENT]").toString();
       Placement response = placementServiceClient.getPlacement(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Placement. Format: `networks/{network_code}/placements/{placement_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### getPlacementCallable()
    
    
    public final UnaryCallable<GetPlacementRequest,Placement> getPlacementCallable()

Retrieves a `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       GetPlacementRequest request =
           GetPlacementRequest.newBuilder()
               .setName(PlacementName.of("[NETWORK_CODE]", "[PLACEMENT]").toString())
               .build();
       ApiFuture<Placement> future =
           placementServiceClient.getPlacementCallable().futureCall(request);
       // Do something.
       Placement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPlacementRequest),[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)>` |   
  
### getSettings()
    
    
    public final @Nullable PlacementServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PlacementServiceSettings` |   
  
### getStub()
    
    
    public PlacementServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PlacementServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PlacementServiceStub)` |   
  
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
  
### listPlacements(@Nullable NetworkName parent)
    
    
    public final PlacementServiceClient.ListPlacementsPagedResponse listPlacements(@Nullable NetworkName parent)

Lists `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Placement element : placementServiceClient.listPlacements(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Placements. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PlacementServiceClient.ListPlacementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient.ListPlacementsPagedResponse)` |   
  
### listPlacements(ListPlacementsRequest request)
    
    
    public final PlacementServiceClient.ListPlacementsPagedResponse listPlacements(ListPlacementsRequest request)

Lists `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       ListPlacementsRequest request =
           ListPlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Placement element : placementServiceClient.listPlacements(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPlacementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PlacementServiceClient.ListPlacementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient.ListPlacementsPagedResponse)` |   
  
### listPlacements(String parent)
    
    
    public final PlacementServiceClient.ListPlacementsPagedResponse listPlacements(String parent)

Lists `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Placement element : placementServiceClient.listPlacements(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Placements. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PlacementServiceClient.ListPlacementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient.ListPlacementsPagedResponse)` |   
  
### listPlacementsCallable()
    
    
    public final UnaryCallable<ListPlacementsRequest,ListPlacementsResponse> listPlacementsCallable()

Lists `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       ListPlacementsRequest request =
           ListPlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListPlacementsResponse response =
             placementServiceClient.listPlacementsCallable().call(request);
         for (Placement element : response.getPlacementsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPlacementsRequest),[ListPlacementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPlacementsResponse)>` |   
  
### listPlacementsPagedCallable()
    
    
    public final UnaryCallable<ListPlacementsRequest,PlacementServiceClient.ListPlacementsPagedResponse> listPlacementsPagedCallable()

Lists `Placement` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       ListPlacementsRequest request =
           ListPlacementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Placement> future =
           placementServiceClient.listPlacementsPagedCallable().futureCall(request);
       // Do something.
       for (Placement element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPlacementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPlacementsRequest),[ListPlacementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PlacementServiceClient.ListPlacementsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePlacement(Placement placement, FieldMask updateMask)
    
    
    public final Placement updatePlacement(Placement placement, FieldMask updateMask)

Updates an `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       Placement placement = Placement.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Placement response = placementServiceClient.updatePlacement(placement, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`placement` | `[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)`  
Required. The `Placement` to update. The `Placement`'s name is used to identify the `Placement` to update. Format: `networks/{network_code}/placements/{placement_id}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### updatePlacement(UpdatePlacementRequest request)
    
    
    public final Placement updatePlacement(UpdatePlacementRequest request)

Updates an `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       UpdatePlacementRequest request =
           UpdatePlacementRequest.newBuilder()
               .setPlacement(Placement.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Placement response = placementServiceClient.updatePlacement(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePlacementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)` |   
  
### updatePlacementCallable()
    
    
    public final UnaryCallable<UpdatePlacementRequest,Placement> updatePlacementCallable()

Updates an `Placement` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlacementServiceClient placementServiceClient = PlacementServiceClient.create()) {
       UpdatePlacementRequest request =
           UpdatePlacementRequest.newBuilder()
               .setPlacement(Placement.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Placement> future =
           placementServiceClient.updatePlacementCallable().futureCall(request);
       // Do something.
       Placement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePlacementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePlacementRequest),[Placement](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Placement)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
