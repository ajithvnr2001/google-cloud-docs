---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient
title: Class FeatureOnlineStoreAdminServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:50.763810+00:00
---

# Class FeatureOnlineStoreAdminServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FeatureOnlineStoreAdminServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/FeatureOnlineStoreAdminServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The service that handles CRUD and List for resources for FeatureOnlineStore.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureOnlineStoreName name =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient.getFeatureOnlineStore(name);
     }
     

Note: close() needs to be called on the FeatureOnlineStoreAdminServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateFeatureOnlineStore |  Creates a new FeatureOnlineStore in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeatureOnlineStoreAsync(CreateFeatureOnlineStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFeatureOnlineStoreAsync(LocationName parent, FeatureOnlineStore featureOnlineStore, String featureOnlineStoreId) 
  * createFeatureOnlineStoreAsync(String parent, FeatureOnlineStore featureOnlineStore, String featureOnlineStoreId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeatureOnlineStoreOperationCallable() 
  * createFeatureOnlineStoreCallable() 

  
GetFeatureOnlineStore |  Gets details of a single FeatureOnlineStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeatureOnlineStore(GetFeatureOnlineStoreRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeatureOnlineStore(FeatureOnlineStoreName name) 
  * getFeatureOnlineStore(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeatureOnlineStoreCallable() 

  
ListFeatureOnlineStores |  Lists FeatureOnlineStores in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatureOnlineStores(ListFeatureOnlineStoresRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatureOnlineStores(LocationName parent) 
  * listFeatureOnlineStores(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeatureOnlineStoresPagedCallable() 
  * listFeatureOnlineStoresCallable() 

  
UpdateFeatureOnlineStore |  Updates the parameters of a single FeatureOnlineStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFeatureOnlineStoreAsync(UpdateFeatureOnlineStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFeatureOnlineStoreAsync(FeatureOnlineStore featureOnlineStore, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFeatureOnlineStoreOperationCallable() 
  * updateFeatureOnlineStoreCallable() 

  
DeleteFeatureOnlineStore |  Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeatureOnlineStoreAsync(DeleteFeatureOnlineStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeatureOnlineStoreAsync(FeatureOnlineStoreName name, boolean force) 
  * deleteFeatureOnlineStoreAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeatureOnlineStoreOperationCallable() 
  * deleteFeatureOnlineStoreCallable() 

  
CreateFeatureView |  Creates a new FeatureView in a given FeatureOnlineStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeatureViewAsync(CreateFeatureViewRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFeatureViewAsync(FeatureOnlineStoreName parent, FeatureView featureView, String featureViewId) 
  * createFeatureViewAsync(String parent, FeatureView featureView, String featureViewId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeatureViewOperationCallable() 
  * createFeatureViewCallable() 

  
GetFeatureView |  Gets details of a single FeatureView. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeatureView(GetFeatureViewRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeatureView(FeatureViewName name) 
  * getFeatureView(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeatureViewCallable() 

  
ListFeatureViews |  Lists FeatureViews in a given FeatureOnlineStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatureViews(ListFeatureViewsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatureViews(FeatureOnlineStoreName parent) 
  * listFeatureViews(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeatureViewsPagedCallable() 
  * listFeatureViewsCallable() 

  
UpdateFeatureView |  Updates the parameters of a single FeatureView. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFeatureViewAsync(UpdateFeatureViewRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFeatureViewAsync(FeatureView featureView, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFeatureViewOperationCallable() 
  * updateFeatureViewCallable() 

  
DeleteFeatureView |  Deletes a single FeatureView. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeatureViewAsync(DeleteFeatureViewRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeatureViewAsync(FeatureViewName name) 
  * deleteFeatureViewAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeatureViewOperationCallable() 
  * deleteFeatureViewCallable() 

  
SyncFeatureView |  Triggers on-demand sync for the FeatureView. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * syncFeatureView(SyncFeatureViewRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * syncFeatureView(FeatureViewName featureView) 
  * syncFeatureView(String featureView) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * syncFeatureViewCallable() 

  
GetFeatureViewSync |  Gets details of a single FeatureViewSync. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeatureViewSync(GetFeatureViewSyncRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeatureViewSync(FeatureViewSyncName name) 
  * getFeatureViewSync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeatureViewSyncCallable() 

  
ListFeatureViewSyncs |  Lists FeatureViewSyncs in a given FeatureView. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatureViewSyncs(ListFeatureViewSyncsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatureViewSyncs(FeatureViewName parent) 
  * listFeatureViewSyncs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeatureViewSyncsPagedCallable() 
  * listFeatureViewSyncsCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of FeatureOnlineStoreAdminServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeatureOnlineStoreAdminServiceSettings featureOnlineStoreAdminServiceSettings =
         FeatureOnlineStoreAdminServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create(featureOnlineStoreAdminServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeatureOnlineStoreAdminServiceSettings featureOnlineStoreAdminServiceSettings =
         FeatureOnlineStoreAdminServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create(featureOnlineStoreAdminServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FeatureOnlineStoreAdminServiceClient

## Static Methods 

### create()
    
    
    public static final FeatureOnlineStoreAdminServiceClient create()

Constructs an instance of FeatureOnlineStoreAdminServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeatureOnlineStoreAdminServiceSettings settings)
    
    
    public static final FeatureOnlineStoreAdminServiceClient create(FeatureOnlineStoreAdminServiceSettings settings)

Constructs an instance of FeatureOnlineStoreAdminServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeatureOnlineStoreAdminServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeatureOnlineStoreAdminServiceStub stub)
    
    
    public static final FeatureOnlineStoreAdminServiceClient create(FeatureOnlineStoreAdminServiceStub stub)

Constructs an instance of FeatureOnlineStoreAdminServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(FeatureOnlineStoreAdminServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeatureOnlineStoreAdminServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeatureOnlineStoreAdminServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient)` |   
  
## Constructors 

### FeatureOnlineStoreAdminServiceClient(FeatureOnlineStoreAdminServiceSettings settings)
    
    
    protected FeatureOnlineStoreAdminServiceClient(FeatureOnlineStoreAdminServiceSettings settings)

Constructs an instance of FeatureOnlineStoreAdminServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeatureOnlineStoreAdminServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceSettings)`  
  
  
### FeatureOnlineStoreAdminServiceClient(FeatureOnlineStoreAdminServiceStub stub)
    
    
    protected FeatureOnlineStoreAdminServiceClient(FeatureOnlineStoreAdminServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeatureOnlineStoreAdminServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeatureOnlineStoreAdminServiceStub)`  
  
  
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

### createFeatureOnlineStoreAsync(@Nullable LocationName parent, FeatureOnlineStore featureOnlineStore, String featureOnlineStoreId)
    
    
    public final OperationFuture<FeatureOnlineStore,CreateFeatureOnlineStoreOperationMetadata> createFeatureOnlineStoreAsync(@Nullable LocationName parent, FeatureOnlineStore featureOnlineStore, String featureOnlineStoreId)

Creates a new FeatureOnlineStore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       FeatureOnlineStore featureOnlineStore = FeatureOnlineStore.newBuilder().build();
       String featureOnlineStoreId = "featureOnlineStoreId1046065331";
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient
               .createFeatureOnlineStoreAsync(parent, featureOnlineStore, featureOnlineStoreId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore),[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreOperationMetadata)>` |   
  
### createFeatureOnlineStoreAsync(CreateFeatureOnlineStoreRequest request)
    
    
    public final OperationFuture<FeatureOnlineStore,CreateFeatureOnlineStoreOperationMetadata> createFeatureOnlineStoreAsync(CreateFeatureOnlineStoreRequest request)

Creates a new FeatureOnlineStore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       CreateFeatureOnlineStoreRequest request =
           CreateFeatureOnlineStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeatureOnlineStore(FeatureOnlineStore.newBuilder().build())
               .setFeatureOnlineStoreId("featureOnlineStoreId1046065331")
               .build();
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient.createFeatureOnlineStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore),[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreOperationMetadata)>` |   
  
### createFeatureOnlineStoreAsync(String parent, FeatureOnlineStore featureOnlineStore, String featureOnlineStoreId)
    
    
    public final OperationFuture<FeatureOnlineStore,CreateFeatureOnlineStoreOperationMetadata> createFeatureOnlineStoreAsync(String parent, FeatureOnlineStore featureOnlineStore, String featureOnlineStoreId)

Creates a new FeatureOnlineStore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       FeatureOnlineStore featureOnlineStore = FeatureOnlineStore.newBuilder().build();
       String featureOnlineStoreId = "featureOnlineStoreId1046065331";
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient
               .createFeatureOnlineStoreAsync(parent, featureOnlineStore, featureOnlineStoreId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore),[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreOperationMetadata)>` |   
  
### createFeatureOnlineStoreCallable()
    
    
    public final UnaryCallable<CreateFeatureOnlineStoreRequest,Operation> createFeatureOnlineStoreCallable()

Creates a new FeatureOnlineStore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       CreateFeatureOnlineStoreRequest request =
           CreateFeatureOnlineStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeatureOnlineStore(FeatureOnlineStore.newBuilder().build())
               .setFeatureOnlineStoreId("featureOnlineStoreId1046065331")
               .build();
       ApiFuture<Operation> future =
           featureOnlineStoreAdminServiceClient
               .createFeatureOnlineStoreCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFeatureOnlineStoreOperationCallable()
    
    
    public final OperationCallable<CreateFeatureOnlineStoreRequest,FeatureOnlineStore,CreateFeatureOnlineStoreOperationMetadata> createFeatureOnlineStoreOperationCallable()

Creates a new FeatureOnlineStore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       CreateFeatureOnlineStoreRequest request =
           CreateFeatureOnlineStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeatureOnlineStore(FeatureOnlineStore.newBuilder().build())
               .setFeatureOnlineStoreId("featureOnlineStoreId1046065331")
               .build();
       OperationFuture<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> future =
           featureOnlineStoreAdminServiceClient
               .createFeatureOnlineStoreOperationCallable()
               .futureCall(request);
       // Do something.
       FeatureOnlineStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreRequest),[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore),[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreOperationMetadata)>` |   
  
### createFeatureViewAsync(@Nullable FeatureOnlineStoreName parent, FeatureView featureView, String featureViewId)
    
    
    public final OperationFuture<FeatureView,CreateFeatureViewOperationMetadata> createFeatureViewAsync(@Nullable FeatureOnlineStoreName parent, FeatureView featureView, String featureViewId)

Creates a new FeatureView in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureOnlineStoreName parent =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
       FeatureView featureView = FeatureView.newBuilder().build();
       String featureViewId = "featureViewId-1437334218";
       FeatureView response =
           featureOnlineStoreAdminServiceClient
               .createFeatureViewAsync(parent, featureView, featureViewId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureOnlineStoreName`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView),[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureViewOperationMetadata)>` |   
  
### createFeatureViewAsync(CreateFeatureViewRequest request)
    
    
    public final OperationFuture<FeatureView,CreateFeatureViewOperationMetadata> createFeatureViewAsync(CreateFeatureViewRequest request)

Creates a new FeatureView in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       CreateFeatureViewRequest request =
           CreateFeatureViewRequest.newBuilder()
               .setParent(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setFeatureView(FeatureView.newBuilder().build())
               .setFeatureViewId("featureViewId-1437334218")
               .setRunSyncImmediately(true)
               .build();
       FeatureView response =
           featureOnlineStoreAdminServiceClient.createFeatureViewAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView),[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureViewOperationMetadata)>` |   
  
### createFeatureViewAsync(String parent, FeatureView featureView, String featureViewId)
    
    
    public final OperationFuture<FeatureView,CreateFeatureViewOperationMetadata> createFeatureViewAsync(String parent, FeatureView featureView, String featureViewId)

Creates a new FeatureView in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String parent =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]").toString();
       FeatureView featureView = FeatureView.newBuilder().build();
       String featureViewId = "featureViewId-1437334218";
       FeatureView response =
           featureOnlineStoreAdminServiceClient
               .createFeatureViewAsync(parent, featureView, featureViewId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView),[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureViewOperationMetadata)>` |   
  
### createFeatureViewCallable()
    
    
    public final UnaryCallable<CreateFeatureViewRequest,Operation> createFeatureViewCallable()

Creates a new FeatureView in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       CreateFeatureViewRequest request =
           CreateFeatureViewRequest.newBuilder()
               .setParent(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setFeatureView(FeatureView.newBuilder().build())
               .setFeatureViewId("featureViewId-1437334218")
               .setRunSyncImmediately(true)
               .build();
       ApiFuture<Operation> future =
           featureOnlineStoreAdminServiceClient.createFeatureViewCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureViewRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFeatureViewOperationCallable()
    
    
    public final OperationCallable<CreateFeatureViewRequest,FeatureView,CreateFeatureViewOperationMetadata> createFeatureViewOperationCallable()

Creates a new FeatureView in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       CreateFeatureViewRequest request =
           CreateFeatureViewRequest.newBuilder()
               .setParent(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setFeatureView(FeatureView.newBuilder().build())
               .setFeatureViewId("featureViewId-1437334218")
               .setRunSyncImmediately(true)
               .build();
       OperationFuture<FeatureView, CreateFeatureViewOperationMetadata> future =
           featureOnlineStoreAdminServiceClient
               .createFeatureViewOperationCallable()
               .futureCall(request);
       // Do something.
       FeatureView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureViewRequest),[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView),[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureViewOperationMetadata)>` |   
  
### deleteFeatureOnlineStoreAsync(@Nullable FeatureOnlineStoreName name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureOnlineStoreAsync(@Nullable FeatureOnlineStoreName name, boolean force)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureOnlineStoreName name =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
       boolean force = true;
       featureOnlineStoreAdminServiceClient.deleteFeatureOnlineStoreAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureOnlineStoreName`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureOnlineStoreAsync(DeleteFeatureOnlineStoreRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureOnlineStoreAsync(DeleteFeatureOnlineStoreRequest request)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       DeleteFeatureOnlineStoreRequest request =
           DeleteFeatureOnlineStoreRequest.newBuilder()
               .setName(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setForce(true)
               .build();
       featureOnlineStoreAdminServiceClient.deleteFeatureOnlineStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureOnlineStoreAsync(String name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureOnlineStoreAsync(String name, boolean force)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String name =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]").toString();
       boolean force = true;
       featureOnlineStoreAdminServiceClient.deleteFeatureOnlineStoreAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureOnlineStoreCallable()
    
    
    public final UnaryCallable<DeleteFeatureOnlineStoreRequest,Operation> deleteFeatureOnlineStoreCallable()

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       DeleteFeatureOnlineStoreRequest request =
           DeleteFeatureOnlineStoreRequest.newBuilder()
               .setName(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           featureOnlineStoreAdminServiceClient
               .deleteFeatureOnlineStoreCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureOnlineStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeatureOnlineStoreOperationCallable()
    
    
    public final OperationCallable<DeleteFeatureOnlineStoreRequest,Empty,DeleteOperationMetadata> deleteFeatureOnlineStoreOperationCallable()

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       DeleteFeatureOnlineStoreRequest request =
           DeleteFeatureOnlineStoreRequest.newBuilder()
               .setName(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featureOnlineStoreAdminServiceClient
               .deleteFeatureOnlineStoreOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureOnlineStoreRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureViewAsync(@Nullable FeatureViewName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureViewAsync(@Nullable FeatureViewName name)

Deletes a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureViewName name =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
       featureOnlineStoreAdminServiceClient.deleteFeatureViewAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureViewName`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureViewAsync(DeleteFeatureViewRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureViewAsync(DeleteFeatureViewRequest request)

Deletes a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       DeleteFeatureViewRequest request =
           DeleteFeatureViewRequest.newBuilder()
               .setName(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       featureOnlineStoreAdminServiceClient.deleteFeatureViewAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureViewAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureViewAsync(String name)

Deletes a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String name =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
               .toString();
       featureOnlineStoreAdminServiceClient.deleteFeatureViewAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureViewCallable()
    
    
    public final UnaryCallable<DeleteFeatureViewRequest,Operation> deleteFeatureViewCallable()

Deletes a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       DeleteFeatureViewRequest request =
           DeleteFeatureViewRequest.newBuilder()
               .setName(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           featureOnlineStoreAdminServiceClient.deleteFeatureViewCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureViewRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeatureViewOperationCallable()
    
    
    public final OperationCallable<DeleteFeatureViewRequest,Empty,DeleteOperationMetadata> deleteFeatureViewOperationCallable()

Deletes a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       DeleteFeatureViewRequest request =
           DeleteFeatureViewRequest.newBuilder()
               .setName(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featureOnlineStoreAdminServiceClient
               .deleteFeatureViewOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureViewRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getFeatureOnlineStore(@Nullable FeatureOnlineStoreName name)
    
    
    public final FeatureOnlineStore getFeatureOnlineStore(@Nullable FeatureOnlineStoreName name)

Gets details of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureOnlineStoreName name =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient.getFeatureOnlineStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureOnlineStoreName`  
Required. The name of the FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore)` |   
  
### getFeatureOnlineStore(GetFeatureOnlineStoreRequest request)
    
    
    public final FeatureOnlineStore getFeatureOnlineStore(GetFeatureOnlineStoreRequest request)

Gets details of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetFeatureOnlineStoreRequest request =
           GetFeatureOnlineStoreRequest.newBuilder()
               .setName(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .build();
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient.getFeatureOnlineStore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore)` |   
  
### getFeatureOnlineStore(String name)
    
    
    public final FeatureOnlineStore getFeatureOnlineStore(String name)

Gets details of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String name =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]").toString();
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient.getFeatureOnlineStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore)` |   
  
### getFeatureOnlineStoreCallable()
    
    
    public final UnaryCallable<GetFeatureOnlineStoreRequest,FeatureOnlineStore> getFeatureOnlineStoreCallable()

Gets details of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetFeatureOnlineStoreRequest request =
           GetFeatureOnlineStoreRequest.newBuilder()
               .setName(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .build();
       ApiFuture<FeatureOnlineStore> future =
           featureOnlineStoreAdminServiceClient.getFeatureOnlineStoreCallable().futureCall(request);
       // Do something.
       FeatureOnlineStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureOnlineStoreRequest),[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore)>` |   
  
### getFeatureView(@Nullable FeatureViewName name)
    
    
    public final FeatureView getFeatureView(@Nullable FeatureViewName name)

Gets details of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureViewName name =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
       FeatureView response = featureOnlineStoreAdminServiceClient.getFeatureView(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureViewName`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView)` |   
  
### getFeatureView(GetFeatureViewRequest request)
    
    
    public final FeatureView getFeatureView(GetFeatureViewRequest request)

Gets details of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetFeatureViewRequest request =
           GetFeatureViewRequest.newBuilder()
               .setName(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       FeatureView response = featureOnlineStoreAdminServiceClient.getFeatureView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView)` |   
  
### getFeatureView(String name)
    
    
    public final FeatureView getFeatureView(String name)

Gets details of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String name =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
               .toString();
       FeatureView response = featureOnlineStoreAdminServiceClient.getFeatureView(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView)` |   
  
### getFeatureViewCallable()
    
    
    public final UnaryCallable<GetFeatureViewRequest,FeatureView> getFeatureViewCallable()

Gets details of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetFeatureViewRequest request =
           GetFeatureViewRequest.newBuilder()
               .setName(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       ApiFuture<FeatureView> future =
           featureOnlineStoreAdminServiceClient.getFeatureViewCallable().futureCall(request);
       // Do something.
       FeatureView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureViewRequest),[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView)>` |   
  
### getFeatureViewSync(@Nullable FeatureViewSyncName name)
    
    
    public final FeatureViewSync getFeatureViewSync(@Nullable FeatureViewSyncName name)

Gets details of a single FeatureViewSync.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureViewSyncName name =
           FeatureViewSyncName.of(
               "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
       FeatureViewSync response = featureOnlineStoreAdminServiceClient.getFeatureViewSync(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureViewSyncName`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureViewSync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureViewSync)` |   
  
### getFeatureViewSync(GetFeatureViewSyncRequest request)
    
    
    public final FeatureViewSync getFeatureViewSync(GetFeatureViewSyncRequest request)

Gets details of a single FeatureViewSync.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetFeatureViewSyncRequest request =
           GetFeatureViewSyncRequest.newBuilder()
               .setName(
                   FeatureViewSyncName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       FeatureViewSync response = featureOnlineStoreAdminServiceClient.getFeatureViewSync(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewSyncRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureViewSyncRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureViewSync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureViewSync)` |   
  
### getFeatureViewSync(String name)
    
    
    public final FeatureViewSync getFeatureViewSync(String name)

Gets details of a single FeatureViewSync.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String name =
           FeatureViewSyncName.of(
                   "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
               .toString();
       FeatureViewSync response = featureOnlineStoreAdminServiceClient.getFeatureViewSync(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureViewSync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureViewSync)` |   
  
### getFeatureViewSyncCallable()
    
    
    public final UnaryCallable<GetFeatureViewSyncRequest,FeatureViewSync> getFeatureViewSyncCallable()

Gets details of a single FeatureViewSync.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetFeatureViewSyncRequest request =
           GetFeatureViewSyncRequest.newBuilder()
               .setName(
                   FeatureViewSyncName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       ApiFuture<FeatureViewSync> future =
           featureOnlineStoreAdminServiceClient.getFeatureViewSyncCallable().futureCall(request);
       // Do something.
       FeatureViewSync response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureViewSyncRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureViewSyncRequest),[FeatureViewSync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureViewSync)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = featureOnlineStoreAdminServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           featureOnlineStoreAdminServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = featureOnlineStoreAdminServiceClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           featureOnlineStoreAdminServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable FeatureOnlineStoreAdminServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceSettings` |   
  
### getStub()
    
    
    public FeatureOnlineStoreAdminServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeatureOnlineStoreAdminServiceStub)` |   
  
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
  
### listFeatureOnlineStores(@Nullable LocationName parent)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse listFeatureOnlineStores(@Nullable LocationName parent)

Lists FeatureOnlineStores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (FeatureOnlineStore element :
           featureOnlineStoreAdminServiceClient.listFeatureOnlineStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse)` |   
  
### listFeatureOnlineStores(ListFeatureOnlineStoresRequest request)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse listFeatureOnlineStores(ListFeatureOnlineStoresRequest request)

Lists FeatureOnlineStores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureOnlineStoresRequest request =
           ListFeatureOnlineStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (FeatureOnlineStore element :
           featureOnlineStoreAdminServiceClient.listFeatureOnlineStores(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureOnlineStoresRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse)` |   
  
### listFeatureOnlineStores(String parent)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse listFeatureOnlineStores(String parent)

Lists FeatureOnlineStores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (FeatureOnlineStore element :
           featureOnlineStoreAdminServiceClient.listFeatureOnlineStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse)` |   
  
### listFeatureOnlineStoresCallable()
    
    
    public final UnaryCallable<ListFeatureOnlineStoresRequest,ListFeatureOnlineStoresResponse> listFeatureOnlineStoresCallable()

Lists FeatureOnlineStores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureOnlineStoresRequest request =
           ListFeatureOnlineStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFeatureOnlineStoresResponse response =
             featureOnlineStoreAdminServiceClient.listFeatureOnlineStoresCallable().call(request);
         for (FeatureOnlineStore element : response.getFeatureOnlineStoresList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureOnlineStoresRequest),[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureOnlineStoresResponse)>` |   
  
### listFeatureOnlineStoresPagedCallable()
    
    
    public final UnaryCallable<ListFeatureOnlineStoresRequest,FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse> listFeatureOnlineStoresPagedCallable()

Lists FeatureOnlineStores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureOnlineStoresRequest request =
           ListFeatureOnlineStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<FeatureOnlineStore> future =
           featureOnlineStoreAdminServiceClient
               .listFeatureOnlineStoresPagedCallable()
               .futureCall(request);
       // Do something.
       for (FeatureOnlineStore element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureOnlineStoresRequest),[ListFeatureOnlineStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresPagedResponse)>` |   
  
### listFeatureViewSyncs(@Nullable FeatureViewName parent)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse listFeatureViewSyncs(@Nullable FeatureViewName parent)

Lists FeatureViewSyncs in a given FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureViewName parent =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
       for (FeatureViewSync element :
           featureOnlineStoreAdminServiceClient.listFeatureViewSyncs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureViewName`  
Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse)` |   
  
### listFeatureViewSyncs(ListFeatureViewSyncsRequest request)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse listFeatureViewSyncs(ListFeatureViewSyncsRequest request)

Lists FeatureViewSyncs in a given FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureViewSyncsRequest request =
           ListFeatureViewSyncsRequest.newBuilder()
               .setParent(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (FeatureViewSync element :
           featureOnlineStoreAdminServiceClient.listFeatureViewSyncs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewSyncsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewSyncsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse)` |   
  
### listFeatureViewSyncs(String parent)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse listFeatureViewSyncs(String parent)

Lists FeatureViewSyncs in a given FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String parent =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
               .toString();
       for (FeatureViewSync element :
           featureOnlineStoreAdminServiceClient.listFeatureViewSyncs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse)` |   
  
### listFeatureViewSyncsCallable()
    
    
    public final UnaryCallable<ListFeatureViewSyncsRequest,ListFeatureViewSyncsResponse> listFeatureViewSyncsCallable()

Lists FeatureViewSyncs in a given FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureViewSyncsRequest request =
           ListFeatureViewSyncsRequest.newBuilder()
               .setParent(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFeatureViewSyncsResponse response =
             featureOnlineStoreAdminServiceClient.listFeatureViewSyncsCallable().call(request);
         for (FeatureViewSync element : response.getFeatureViewSyncsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureViewSyncsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewSyncsRequest),[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewSyncsResponse)>` |   
  
### listFeatureViewSyncsPagedCallable()
    
    
    public final UnaryCallable<ListFeatureViewSyncsRequest,FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse> listFeatureViewSyncsPagedCallable()

Lists FeatureViewSyncs in a given FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureViewSyncsRequest request =
           ListFeatureViewSyncsRequest.newBuilder()
               .setParent(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<FeatureViewSync> future =
           featureOnlineStoreAdminServiceClient
               .listFeatureViewSyncsPagedCallable()
               .futureCall(request);
       // Do something.
       for (FeatureViewSync element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureViewSyncsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewSyncsRequest),[ListFeatureViewSyncsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewSyncsPagedResponse)>` |   
  
### listFeatureViews(@Nullable FeatureOnlineStoreName parent)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse listFeatureViews(@Nullable FeatureOnlineStoreName parent)

Lists FeatureViews in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureOnlineStoreName parent =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
       for (FeatureView element :
           featureOnlineStoreAdminServiceClient.listFeatureViews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureOnlineStoreName`  
Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse)` |   
  
### listFeatureViews(ListFeatureViewsRequest request)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse listFeatureViews(ListFeatureViewsRequest request)

Lists FeatureViews in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureViewsRequest request =
           ListFeatureViewsRequest.newBuilder()
               .setParent(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (FeatureView element :
           featureOnlineStoreAdminServiceClient.listFeatureViews(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse)` |   
  
### listFeatureViews(String parent)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse listFeatureViews(String parent)

Lists FeatureViews in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String parent =
           FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]").toString();
       for (FeatureView element :
           featureOnlineStoreAdminServiceClient.listFeatureViews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse)` |   
  
### listFeatureViewsCallable()
    
    
    public final UnaryCallable<ListFeatureViewsRequest,ListFeatureViewsResponse> listFeatureViewsCallable()

Lists FeatureViews in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureViewsRequest request =
           ListFeatureViewsRequest.newBuilder()
               .setParent(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFeatureViewsResponse response =
             featureOnlineStoreAdminServiceClient.listFeatureViewsCallable().call(request);
         for (FeatureView element : response.getFeatureViewsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewsRequest),[ListFeatureViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewsResponse)>` |   
  
### listFeatureViewsPagedCallable()
    
    
    public final UnaryCallable<ListFeatureViewsRequest,FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse> listFeatureViewsPagedCallable()

Lists FeatureViews in a given FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListFeatureViewsRequest request =
           ListFeatureViewsRequest.newBuilder()
               .setParent(
                   FeatureOnlineStoreName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<FeatureView> future =
           featureOnlineStoreAdminServiceClient.listFeatureViewsPagedCallable().futureCall(request);
       // Do something.
       for (FeatureView element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeatureViewsRequest),[ListFeatureViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListFeatureViewsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final FeatureOnlineStoreAdminServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element :
           featureOnlineStoreAdminServiceClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             featureOnlineStoreAdminServiceClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,FeatureOnlineStoreAdminServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           featureOnlineStoreAdminServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStoreAdminServiceClient.ListLocationsPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = featureOnlineStoreAdminServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           featureOnlineStoreAdminServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### syncFeatureView(@Nullable FeatureViewName featureView)
    
    
    public final SyncFeatureViewResponse syncFeatureView(@Nullable FeatureViewName featureView)

Triggers on-demand sync for the FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureViewName featureView =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
       SyncFeatureViewResponse response =
           featureOnlineStoreAdminServiceClient.syncFeatureView(featureView);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`featureView` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureViewName`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[SyncFeatureViewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SyncFeatureViewResponse)` |   
  
### syncFeatureView(SyncFeatureViewRequest request)
    
    
    public final SyncFeatureViewResponse syncFeatureView(SyncFeatureViewRequest request)

Triggers on-demand sync for the FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       SyncFeatureViewRequest request =
           SyncFeatureViewRequest.newBuilder()
               .setFeatureView(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       SyncFeatureViewResponse response =
           featureOnlineStoreAdminServiceClient.syncFeatureView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SyncFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SyncFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SyncFeatureViewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SyncFeatureViewResponse)` |   
  
### syncFeatureView(String featureView)
    
    
    public final SyncFeatureViewResponse syncFeatureView(String featureView)

Triggers on-demand sync for the FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       String featureView =
           FeatureViewName.of("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
               .toString();
       SyncFeatureViewResponse response =
           featureOnlineStoreAdminServiceClient.syncFeatureView(featureView);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`featureView` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
**Returns**  
---  
**Type** | **Description**  
`[SyncFeatureViewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SyncFeatureViewResponse)` |   
  
### syncFeatureViewCallable()
    
    
    public final UnaryCallable<SyncFeatureViewRequest,SyncFeatureViewResponse> syncFeatureViewCallable()

Triggers on-demand sync for the FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       SyncFeatureViewRequest request =
           SyncFeatureViewRequest.newBuilder()
               .setFeatureView(
                   FeatureViewName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]")
                       .toString())
               .build();
       ApiFuture<SyncFeatureViewResponse> future =
           featureOnlineStoreAdminServiceClient.syncFeatureViewCallable().futureCall(request);
       // Do something.
       SyncFeatureViewResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SyncFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SyncFeatureViewRequest),[SyncFeatureViewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SyncFeatureViewResponse)>` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           featureOnlineStoreAdminServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           featureOnlineStoreAdminServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateFeatureOnlineStoreAsync(FeatureOnlineStore featureOnlineStore, FieldMask updateMask)
    
    
    public final OperationFuture<FeatureOnlineStore,UpdateFeatureOnlineStoreOperationMetadata> updateFeatureOnlineStoreAsync(FeatureOnlineStore featureOnlineStore, FieldMask updateMask)

Updates the parameters of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureOnlineStore featureOnlineStore = FeatureOnlineStore.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient
               .updateFeatureOnlineStoreAsync(featureOnlineStore, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore's `name` field is used to identify the FeatureOnlineStore to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureOnlineStore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `labels` * `description` * `bigtable` * `bigtable.auto_scaling` * `bigtable.enable_multi_region_replica`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore),[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureOnlineStoreOperationMetadata)>` |   
  
### updateFeatureOnlineStoreAsync(UpdateFeatureOnlineStoreRequest request)
    
    
    public final OperationFuture<FeatureOnlineStore,UpdateFeatureOnlineStoreOperationMetadata> updateFeatureOnlineStoreAsync(UpdateFeatureOnlineStoreRequest request)

Updates the parameters of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       UpdateFeatureOnlineStoreRequest request =
           UpdateFeatureOnlineStoreRequest.newBuilder()
               .setFeatureOnlineStore(FeatureOnlineStore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       FeatureOnlineStore response =
           featureOnlineStoreAdminServiceClient.updateFeatureOnlineStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore),[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureOnlineStoreOperationMetadata)>` |   
  
### updateFeatureOnlineStoreCallable()
    
    
    public final UnaryCallable<UpdateFeatureOnlineStoreRequest,Operation> updateFeatureOnlineStoreCallable()

Updates the parameters of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       UpdateFeatureOnlineStoreRequest request =
           UpdateFeatureOnlineStoreRequest.newBuilder()
               .setFeatureOnlineStore(FeatureOnlineStore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           featureOnlineStoreAdminServiceClient
               .updateFeatureOnlineStoreCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureOnlineStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFeatureOnlineStoreOperationCallable()
    
    
    public final OperationCallable<UpdateFeatureOnlineStoreRequest,FeatureOnlineStore,UpdateFeatureOnlineStoreOperationMetadata> updateFeatureOnlineStoreOperationCallable()

Updates the parameters of a single FeatureOnlineStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       UpdateFeatureOnlineStoreRequest request =
           UpdateFeatureOnlineStoreRequest.newBuilder()
               .setFeatureOnlineStore(FeatureOnlineStore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> future =
           featureOnlineStoreAdminServiceClient
               .updateFeatureOnlineStoreOperationCallable()
               .futureCall(request);
       // Do something.
       FeatureOnlineStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureOnlineStoreRequest),[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureOnlineStore),[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureOnlineStoreOperationMetadata)>` |   
  
### updateFeatureViewAsync(FeatureView featureView, FieldMask updateMask)
    
    
    public final OperationFuture<FeatureView,UpdateFeatureViewOperationMetadata> updateFeatureViewAsync(FeatureView featureView, FieldMask updateMask)

Updates the parameters of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       FeatureView featureView = FeatureView.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       FeatureView response =
           featureOnlineStoreAdminServiceClient
               .updateFeatureViewAsync(featureView, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView)`  
Required. The FeatureView's `name` field is used to identify the FeatureView to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureView resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `labels` * `service_agent_type` * `big_query_source` * `big_query_source.uri` * `big_query_source.entity_id_columns` * `feature_registry_source` * `feature_registry_source.feature_groups` * `sync_config` * `sync_config.cron` * `optimized_config.automatic_resources`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView),[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureViewOperationMetadata)>` |   
  
### updateFeatureViewAsync(UpdateFeatureViewRequest request)
    
    
    public final OperationFuture<FeatureView,UpdateFeatureViewOperationMetadata> updateFeatureViewAsync(UpdateFeatureViewRequest request)

Updates the parameters of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       UpdateFeatureViewRequest request =
           UpdateFeatureViewRequest.newBuilder()
               .setFeatureView(FeatureView.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       FeatureView response =
           featureOnlineStoreAdminServiceClient.updateFeatureViewAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView),[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureViewOperationMetadata)>` |   
  
### updateFeatureViewCallable()
    
    
    public final UnaryCallable<UpdateFeatureViewRequest,Operation> updateFeatureViewCallable()

Updates the parameters of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       UpdateFeatureViewRequest request =
           UpdateFeatureViewRequest.newBuilder()
               .setFeatureView(FeatureView.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           featureOnlineStoreAdminServiceClient.updateFeatureViewCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureViewRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFeatureViewOperationCallable()
    
    
    public final OperationCallable<UpdateFeatureViewRequest,FeatureView,UpdateFeatureViewOperationMetadata> updateFeatureViewOperationCallable()

Updates the parameters of a single FeatureView.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient =
         FeatureOnlineStoreAdminServiceClient.create()) {
       UpdateFeatureViewRequest request =
           UpdateFeatureViewRequest.newBuilder()
               .setFeatureView(FeatureView.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<FeatureView, UpdateFeatureViewOperationMetadata> future =
           featureOnlineStoreAdminServiceClient
               .updateFeatureViewOperationCallable()
               .futureCall(request);
       // Do something.
       FeatureView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureViewRequest),[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureView),[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureViewOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
