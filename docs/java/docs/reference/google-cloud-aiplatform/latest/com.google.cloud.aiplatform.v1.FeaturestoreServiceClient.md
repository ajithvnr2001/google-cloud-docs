---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient
title: Class FeaturestoreServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:59.833214+00:00
---

# Class FeaturestoreServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FeaturestoreServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/FeaturestoreServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The service that handles CRUD and List for resources for Featurestore.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName name = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       Featurestore response = featurestoreServiceClient.getFeaturestore(name);
     }
     

Note: close() needs to be called on the FeaturestoreServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateFeaturestore |  Creates a new Featurestore in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeaturestoreAsync(CreateFeaturestoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFeaturestoreAsync(LocationName parent, Featurestore featurestore) 
  * createFeaturestoreAsync(String parent, Featurestore featurestore) 
  * createFeaturestoreAsync(LocationName parent, Featurestore featurestore, String featurestoreId) 
  * createFeaturestoreAsync(String parent, Featurestore featurestore, String featurestoreId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeaturestoreOperationCallable() 
  * createFeaturestoreCallable() 

  
GetFeaturestore |  Gets details of a single Featurestore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeaturestore(GetFeaturestoreRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeaturestore(FeaturestoreName name) 
  * getFeaturestore(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeaturestoreCallable() 

  
ListFeaturestores |  Lists Featurestores in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeaturestores(ListFeaturestoresRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeaturestores(LocationName parent) 
  * listFeaturestores(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeaturestoresPagedCallable() 
  * listFeaturestoresCallable() 

  
UpdateFeaturestore |  Updates the parameters of a single Featurestore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFeaturestoreAsync(UpdateFeaturestoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFeaturestoreAsync(Featurestore featurestore, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFeaturestoreOperationCallable() 
  * updateFeaturestoreCallable() 

  
DeleteFeaturestore |  Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeaturestoreAsync(DeleteFeaturestoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeaturestoreAsync(FeaturestoreName name) 
  * deleteFeaturestoreAsync(String name) 
  * deleteFeaturestoreAsync(FeaturestoreName name, boolean force) 
  * deleteFeaturestoreAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeaturestoreOperationCallable() 
  * deleteFeaturestoreCallable() 

  
CreateEntityType |  Creates a new EntityType in a given Featurestore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntityTypeAsync(CreateEntityTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEntityTypeAsync(FeaturestoreName parent, EntityType entityType) 
  * createEntityTypeAsync(String parent, EntityType entityType) 
  * createEntityTypeAsync(FeaturestoreName parent, EntityType entityType, String entityTypeId) 
  * createEntityTypeAsync(String parent, EntityType entityType, String entityTypeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntityTypeOperationCallable() 
  * createEntityTypeCallable() 

  
GetEntityType |  Gets details of a single EntityType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntityType(GetEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEntityType(EntityTypeName name) 
  * getEntityType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntityTypeCallable() 

  
ListEntityTypes |  Lists EntityTypes in a given Featurestore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntityTypes(ListEntityTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntityTypes(FeaturestoreName parent) 
  * listEntityTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntityTypesPagedCallable() 
  * listEntityTypesCallable() 

  
UpdateEntityType |  Updates the parameters of a single EntityType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEntityType(UpdateEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEntityType(EntityType entityType, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEntityTypeCallable() 

  
DeleteEntityType |  Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEntityTypeAsync(DeleteEntityTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEntityTypeAsync(EntityTypeName name) 
  * deleteEntityTypeAsync(String name) 
  * deleteEntityTypeAsync(EntityTypeName name, boolean force) 
  * deleteEntityTypeAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEntityTypeOperationCallable() 
  * deleteEntityTypeCallable() 

  
CreateFeature |  Creates a new Feature in a given EntityType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeatureAsync(CreateFeatureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFeatureAsync(EntityTypeName parent, Feature feature) 
  * createFeatureAsync(FeatureGroupName parent, Feature feature) 
  * createFeatureAsync(String parent, Feature feature) 
  * createFeatureAsync(EntityTypeName parent, Feature feature, String featureId) 
  * createFeatureAsync(FeatureGroupName parent, Feature feature, String featureId) 
  * createFeatureAsync(String parent, Feature feature, String featureId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeatureOperationCallable() 
  * createFeatureCallable() 

  
BatchCreateFeatures |  Creates a batch of Features in a given EntityType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateFeaturesAsync(EntityTypeName parent, List<CreateFeatureRequest> requests) 
  * batchCreateFeaturesAsync(FeatureGroupName parent, List<CreateFeatureRequest> requests) 
  * batchCreateFeaturesAsync(String parent, List<CreateFeatureRequest> requests) 
  * batchCreateFeaturesAsync(BatchCreateFeaturesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateFeaturesOperationCallable() 
  * batchCreateFeaturesCallable() 

  
GetFeature |  Gets details of a single Feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeature(GetFeatureRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeature(FeatureName name) 
  * getFeature(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeatureCallable() 

  
ListFeatures |  Lists Features in a given EntityType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatures(ListFeaturesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatures(EntityTypeName parent) 
  * listFeatures(FeatureGroupName parent) 
  * listFeatures(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeaturesPagedCallable() 
  * listFeaturesCallable() 

  
UpdateFeature |  Updates the parameters of a single Feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFeature(UpdateFeatureRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateFeature(Feature feature, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFeatureCallable() 

  
DeleteFeature |  Deletes a single Feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeatureAsync(DeleteFeatureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeatureAsync(FeatureName name) 
  * deleteFeatureAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeatureOperationCallable() 
  * deleteFeatureCallable() 

  
ImportFeatureValues |  Imports Feature values into the Featurestore from a source storage.  The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done.  If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done.  There are also scenarios where the caller can cause inconsistency.  \- Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importFeatureValuesAsync(ImportFeatureValuesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importFeatureValuesAsync(EntityTypeName entityType) 
  * importFeatureValuesAsync(String entityType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importFeatureValuesOperationCallable() 
  * importFeatureValuesCallable() 

  
BatchReadFeatureValues |  Batch reads Feature values from a Featurestore.  This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchReadFeatureValuesAsync(BatchReadFeatureValuesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchReadFeatureValuesAsync(FeaturestoreName featurestore) 
  * batchReadFeatureValuesAsync(String featurestore) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchReadFeatureValuesOperationCallable() 
  * batchReadFeatureValuesCallable() 

  
ExportFeatureValues |  Exports Feature values from all the entities of a target EntityType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportFeatureValuesAsync(ExportFeatureValuesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportFeatureValuesAsync(EntityTypeName entityType) 
  * exportFeatureValuesAsync(String entityType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportFeatureValuesOperationCallable() 
  * exportFeatureValuesCallable() 

  
DeleteFeatureValues |  Delete Feature values from Featurestore.  The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.  If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeatureValuesAsync(DeleteFeatureValuesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeatureValuesAsync(EntityTypeName entityType) 
  * deleteFeatureValuesAsync(String entityType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeatureValuesOperationCallable() 
  * deleteFeatureValuesCallable() 

  
SearchFeatures |  Searches Features matching a query in a given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchFeatures(SearchFeaturesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchFeatures(LocationName location) 
  * searchFeatures(String location) 
  * searchFeatures(LocationName location, String query) 
  * searchFeatures(String location, String query) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchFeaturesPagedCallable() 
  * searchFeaturesCallable() 

  
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

This class can be customized by passing in a custom instance of FeaturestoreServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeaturestoreServiceSettings featurestoreServiceSettings =
         FeaturestoreServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FeaturestoreServiceClient featurestoreServiceClient =
         FeaturestoreServiceClient.create(featurestoreServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeaturestoreServiceSettings featurestoreServiceSettings =
         FeaturestoreServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     FeaturestoreServiceClient featurestoreServiceClient =
         FeaturestoreServiceClient.create(featurestoreServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FeaturestoreServiceClient

## Static Methods 

### create()
    
    
    public static final FeaturestoreServiceClient create()

Constructs an instance of FeaturestoreServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeaturestoreServiceSettings settings)
    
    
    public static final FeaturestoreServiceClient create(FeaturestoreServiceSettings settings)

Constructs an instance of FeaturestoreServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeaturestoreServiceStub stub)
    
    
    public static final FeaturestoreServiceClient create(FeaturestoreServiceStub stub)

Constructs an instance of FeaturestoreServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(FeaturestoreServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeaturestoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeaturestoreServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient)` |   
  
## Constructors 

### FeaturestoreServiceClient(FeaturestoreServiceSettings settings)
    
    
    protected FeaturestoreServiceClient(FeaturestoreServiceSettings settings)

Constructs an instance of FeaturestoreServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings)`  
  
  
### FeaturestoreServiceClient(FeaturestoreServiceStub stub)
    
    
    protected FeaturestoreServiceClient(FeaturestoreServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeaturestoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeaturestoreServiceStub)`  
  
  
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
  
### batchCreateFeaturesAsync(@Nullable EntityTypeName parent, List<CreateFeatureRequest> requests)
    
    
    public final OperationFuture<BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesAsync(@Nullable EntityTypeName parent, List<CreateFeatureRequest> requests)

Creates a batch of Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       List<CreateFeatureRequest> requests = new ArrayList<>();
       BatchCreateFeaturesResponse response =
           featurestoreServiceClient.batchCreateFeaturesAsync(parent, requests).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest)>`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesAsync(@Nullable FeatureGroupName parent, List<CreateFeatureRequest> requests)
    
    
    public final OperationFuture<BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesAsync(@Nullable FeatureGroupName parent, List<CreateFeatureRequest> requests)

Creates a batch of Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       List<CreateFeatureRequest> requests = new ArrayList<>();
       BatchCreateFeaturesResponse response =
           featurestoreServiceClient.batchCreateFeaturesAsync(parent, requests).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureGroupName`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest)>`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesAsync(BatchCreateFeaturesRequest request)
    
    
    public final OperationFuture<BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesAsync(BatchCreateFeaturesRequest request)

Creates a batch of Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       BatchCreateFeaturesRequest request =
           BatchCreateFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateFeatureRequest>())
               .build();
       BatchCreateFeaturesResponse response =
           featurestoreServiceClient.batchCreateFeaturesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesAsync(String parent, List<CreateFeatureRequest> requests)
    
    
    public final OperationFuture<BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesAsync(String parent, List<CreateFeatureRequest> requests)

Creates a batch of Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       List<CreateFeatureRequest> requests = new ArrayList<>();
       BatchCreateFeaturesResponse response =
           featurestoreServiceClient.batchCreateFeaturesAsync(parent, requests).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest)>`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesCallable()
    
    
    public final UnaryCallable<BatchCreateFeaturesRequest,Operation> batchCreateFeaturesCallable()

Creates a batch of Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       BatchCreateFeaturesRequest request =
           BatchCreateFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateFeatureRequest>())
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.batchCreateFeaturesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchCreateFeaturesOperationCallable()
    
    
    public final OperationCallable<BatchCreateFeaturesRequest,BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesOperationCallable()

Creates a batch of Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       BatchCreateFeaturesRequest request =
           BatchCreateFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateFeatureRequest>())
               .build();
       OperationFuture<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> future =
           featurestoreServiceClient.batchCreateFeaturesOperationCallable().futureCall(request);
       // Do something.
       BatchCreateFeaturesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesRequest),[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchReadFeatureValuesAsync(@Nullable FeaturestoreName featurestore)
    
    
    public final OperationFuture<BatchReadFeatureValuesResponse,BatchReadFeatureValuesOperationMetadata> batchReadFeatureValuesAsync(@Nullable FeaturestoreName featurestore)

Batch reads Feature values from a Featurestore.

This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName featurestore =
           FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       BatchReadFeatureValuesResponse response =
           featurestoreServiceClient.batchReadFeatureValuesAsync(featurestore).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`featurestore` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreName`  
Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesResponse),[BatchReadFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesOperationMetadata)>` |   
  
### batchReadFeatureValuesAsync(BatchReadFeatureValuesRequest request)
    
    
    public final OperationFuture<BatchReadFeatureValuesResponse,BatchReadFeatureValuesOperationMetadata> batchReadFeatureValuesAsync(BatchReadFeatureValuesRequest request)

Batch reads Feature values from a Featurestore.

This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       BatchReadFeatureValuesRequest request =
           BatchReadFeatureValuesRequest.newBuilder()
               .setFeaturestore(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setDestination(FeatureValueDestination.newBuilder().build())
               .addAllPassThroughFields(
                   new ArrayList<BatchReadFeatureValuesRequest.PassThroughField>())
               .addAllEntityTypeSpecs(new ArrayList<BatchReadFeatureValuesRequest.EntityTypeSpec>())
               .setStartTime(Timestamp.newBuilder().build())
               .build();
       BatchReadFeatureValuesResponse response =
           featurestoreServiceClient.batchReadFeatureValuesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesResponse),[BatchReadFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesOperationMetadata)>` |   
  
### batchReadFeatureValuesAsync(String featurestore)
    
    
    public final OperationFuture<BatchReadFeatureValuesResponse,BatchReadFeatureValuesOperationMetadata> batchReadFeatureValuesAsync(String featurestore)

Batch reads Feature values from a Featurestore.

This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String featurestore =
           FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString();
       BatchReadFeatureValuesResponse response =
           featurestoreServiceClient.batchReadFeatureValuesAsync(featurestore).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`featurestore` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesResponse),[BatchReadFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesOperationMetadata)>` |   
  
### batchReadFeatureValuesCallable()
    
    
    public final UnaryCallable<BatchReadFeatureValuesRequest,Operation> batchReadFeatureValuesCallable()

Batch reads Feature values from a Featurestore.

This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       BatchReadFeatureValuesRequest request =
           BatchReadFeatureValuesRequest.newBuilder()
               .setFeaturestore(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setDestination(FeatureValueDestination.newBuilder().build())
               .addAllPassThroughFields(
                   new ArrayList<BatchReadFeatureValuesRequest.PassThroughField>())
               .addAllEntityTypeSpecs(new ArrayList<BatchReadFeatureValuesRequest.EntityTypeSpec>())
               .setStartTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.batchReadFeatureValuesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchReadFeatureValuesOperationCallable()
    
    
    public final OperationCallable<BatchReadFeatureValuesRequest,BatchReadFeatureValuesResponse,BatchReadFeatureValuesOperationMetadata> batchReadFeatureValuesOperationCallable()

Batch reads Feature values from a Featurestore.

This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       BatchReadFeatureValuesRequest request =
           BatchReadFeatureValuesRequest.newBuilder()
               .setFeaturestore(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setDestination(FeatureValueDestination.newBuilder().build())
               .addAllPassThroughFields(
                   new ArrayList<BatchReadFeatureValuesRequest.PassThroughField>())
               .addAllEntityTypeSpecs(new ArrayList<BatchReadFeatureValuesRequest.EntityTypeSpec>())
               .setStartTime(Timestamp.newBuilder().build())
               .build();
       OperationFuture<BatchReadFeatureValuesResponse, BatchReadFeatureValuesOperationMetadata>
           future =
               featurestoreServiceClient
                   .batchReadFeatureValuesOperationCallable()
                   .futureCall(request);
       // Do something.
       BatchReadFeatureValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesRequest),[BatchReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesResponse),[BatchReadFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadFeatureValuesOperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createEntityTypeAsync(@Nullable FeaturestoreName parent, EntityType entityType)
    
    
    public final OperationFuture<EntityType,CreateEntityTypeOperationMetadata> createEntityTypeAsync(@Nullable FeaturestoreName parent, EntityType entityType)

Creates a new EntityType in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName parent = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       EntityType entityType = EntityType.newBuilder().build();
       EntityType response =
           featurestoreServiceClient.createEntityTypeAsync(parent, entityType).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreName`  
Required. The resource name of the Featurestore to create EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)`  
The EntityType to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType),[CreateEntityTypeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata)>` |   
  
### createEntityTypeAsync(@Nullable FeaturestoreName parent, EntityType entityType, String entityTypeId)
    
    
    public final OperationFuture<EntityType,CreateEntityTypeOperationMetadata> createEntityTypeAsync(@Nullable FeaturestoreName parent, EntityType entityType, String entityTypeId)

Creates a new EntityType in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName parent = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       EntityType entityType = EntityType.newBuilder().build();
       String entityTypeId = "entityTypeId767740856";
       EntityType response =
           featurestoreServiceClient.createEntityTypeAsync(parent, entityType, entityTypeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreName`  
Required. The resource name of the Featurestore to create EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)`  
The EntityType to create.  
`entityTypeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the EntityType, which will become the final component of the EntityType's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a featurestore.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType),[CreateEntityTypeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata)>` |   
  
### createEntityTypeAsync(CreateEntityTypeRequest request)
    
    
    public final OperationFuture<EntityType,CreateEntityTypeOperationMetadata> createEntityTypeAsync(CreateEntityTypeRequest request)

Creates a new EntityType in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateEntityTypeRequest request =
           CreateEntityTypeRequest.newBuilder()
               .setParent(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setEntityType(EntityType.newBuilder().build())
               .setEntityTypeId("entityTypeId767740856")
               .build();
       EntityType response = featurestoreServiceClient.createEntityTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType),[CreateEntityTypeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata)>` |   
  
### createEntityTypeAsync(String parent, EntityType entityType)
    
    
    public final OperationFuture<EntityType,CreateEntityTypeOperationMetadata> createEntityTypeAsync(String parent, EntityType entityType)

Creates a new EntityType in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString();
       EntityType entityType = EntityType.newBuilder().build();
       EntityType response =
           featurestoreServiceClient.createEntityTypeAsync(parent, entityType).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Featurestore to create EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)`  
The EntityType to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType),[CreateEntityTypeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata)>` |   
  
### createEntityTypeAsync(String parent, EntityType entityType, String entityTypeId)
    
    
    public final OperationFuture<EntityType,CreateEntityTypeOperationMetadata> createEntityTypeAsync(String parent, EntityType entityType, String entityTypeId)

Creates a new EntityType in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString();
       EntityType entityType = EntityType.newBuilder().build();
       String entityTypeId = "entityTypeId767740856";
       EntityType response =
           featurestoreServiceClient.createEntityTypeAsync(parent, entityType, entityTypeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Featurestore to create EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)`  
The EntityType to create.  
`entityTypeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the EntityType, which will become the final component of the EntityType's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a featurestore.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType),[CreateEntityTypeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata)>` |   
  
### createEntityTypeCallable()
    
    
    public final UnaryCallable<CreateEntityTypeRequest,Operation> createEntityTypeCallable()

Creates a new EntityType in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateEntityTypeRequest request =
           CreateEntityTypeRequest.newBuilder()
               .setParent(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setEntityType(EntityType.newBuilder().build())
               .setEntityTypeId("entityTypeId767740856")
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.createEntityTypeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEntityTypeOperationCallable()
    
    
    public final OperationCallable<CreateEntityTypeRequest,EntityType,CreateEntityTypeOperationMetadata> createEntityTypeOperationCallable()

Creates a new EntityType in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateEntityTypeRequest request =
           CreateEntityTypeRequest.newBuilder()
               .setParent(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setEntityType(EntityType.newBuilder().build())
               .setEntityTypeId("entityTypeId767740856")
               .build();
       OperationFuture<EntityType, CreateEntityTypeOperationMetadata> future =
           featurestoreServiceClient.createEntityTypeOperationCallable().futureCall(request);
       // Do something.
       EntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType),[CreateEntityTypeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata)>` |   
  
### createFeatureAsync(@Nullable EntityTypeName parent, Feature feature)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(@Nullable EntityTypeName parent, Feature feature)

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       Feature feature = Feature.newBuilder().build();
       Feature response = featurestoreServiceClient.createFeatureAsync(parent, feature).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)`  
Required. The Feature to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(@Nullable EntityTypeName parent, Feature feature, String featureId)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(@Nullable EntityTypeName parent, Feature feature, String featureId)

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       Feature feature = Feature.newBuilder().build();
       String featureId = "featureId-420503887";
       Feature response =
           featurestoreServiceClient.createFeatureAsync(parent, feature, featureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)`  
Required. The Feature to create.  
`featureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(@Nullable FeatureGroupName parent, Feature feature)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(@Nullable FeatureGroupName parent, Feature feature)

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       Feature feature = Feature.newBuilder().build();
       Feature response = featurestoreServiceClient.createFeatureAsync(parent, feature).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureGroupName`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)`  
Required. The Feature to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(@Nullable FeatureGroupName parent, Feature feature, String featureId)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(@Nullable FeatureGroupName parent, Feature feature, String featureId)

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       Feature feature = Feature.newBuilder().build();
       String featureId = "featureId-420503887";
       Feature response =
           featurestoreServiceClient.createFeatureAsync(parent, feature, featureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureGroupName`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)`  
Required. The Feature to create.  
`featureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(CreateFeatureRequest request)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(CreateFeatureRequest request)

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateFeatureRequest request =
           CreateFeatureRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFeature(Feature.newBuilder().build())
               .setFeatureId("featureId-420503887")
               .build();
       Feature response = featurestoreServiceClient.createFeatureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(String parent, Feature feature)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(String parent, Feature feature)

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       Feature feature = Feature.newBuilder().build();
       Feature response = featurestoreServiceClient.createFeatureAsync(parent, feature).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)`  
Required. The Feature to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(String parent, Feature feature, String featureId)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(String parent, Feature feature, String featureId)

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       Feature feature = Feature.newBuilder().build();
       String featureId = "featureId-420503887";
       Feature response =
           featurestoreServiceClient.createFeatureAsync(parent, feature, featureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)`  
Required. The Feature to create.  
`featureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureCallable()
    
    
    public final UnaryCallable<CreateFeatureRequest,Operation> createFeatureCallable()

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateFeatureRequest request =
           CreateFeatureRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFeature(Feature.newBuilder().build())
               .setFeatureId("featureId-420503887")
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.createFeatureCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFeatureOperationCallable()
    
    
    public final OperationCallable<CreateFeatureRequest,Feature,CreateFeatureOperationMetadata> createFeatureOperationCallable()

Creates a new Feature in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateFeatureRequest request =
           CreateFeatureRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFeature(Feature.newBuilder().build())
               .setFeatureId("featureId-420503887")
               .build();
       OperationFuture<Feature, CreateFeatureOperationMetadata> future =
           featurestoreServiceClient.createFeatureOperationCallable().futureCall(request);
       // Do something.
       Feature response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest),[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata)>` |   
  
### createFeaturestoreAsync(@Nullable LocationName parent, Featurestore featurestore)
    
    
    public final OperationFuture<Featurestore,CreateFeaturestoreOperationMetadata> createFeaturestoreAsync(@Nullable LocationName parent, Featurestore featurestore)

Creates a new Featurestore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Featurestore featurestore = Featurestore.newBuilder().build();
       Featurestore response =
           featurestoreServiceClient.createFeaturestoreAsync(parent, featurestore).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create Featurestores. Format: `projects/{project}/locations/{location}`  
`featurestore` | `[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)`  
Required. The Featurestore to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[CreateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata)>` |   
  
### createFeaturestoreAsync(@Nullable LocationName parent, Featurestore featurestore, String featurestoreId)
    
    
    public final OperationFuture<Featurestore,CreateFeaturestoreOperationMetadata> createFeaturestoreAsync(@Nullable LocationName parent, Featurestore featurestore, String featurestoreId)

Creates a new Featurestore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Featurestore featurestore = Featurestore.newBuilder().build();
       String featurestoreId = "featurestoreId-1315851738";
       Featurestore response =
           featurestoreServiceClient
               .createFeaturestoreAsync(parent, featurestore, featurestoreId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create Featurestores. Format: `projects/{project}/locations/{location}`  
`featurestore` | `[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)`  
Required. The Featurestore to create.  
`featurestoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this Featurestore, which will become the final component of the Featurestore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[CreateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata)>` |   
  
### createFeaturestoreAsync(CreateFeaturestoreRequest request)
    
    
    public final OperationFuture<Featurestore,CreateFeaturestoreOperationMetadata> createFeaturestoreAsync(CreateFeaturestoreRequest request)

Creates a new Featurestore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateFeaturestoreRequest request =
           CreateFeaturestoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeaturestore(Featurestore.newBuilder().build())
               .setFeaturestoreId("featurestoreId-1315851738")
               .build();
       Featurestore response = featurestoreServiceClient.createFeaturestoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[CreateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata)>` |   
  
### createFeaturestoreAsync(String parent, Featurestore featurestore)
    
    
    public final OperationFuture<Featurestore,CreateFeaturestoreOperationMetadata> createFeaturestoreAsync(String parent, Featurestore featurestore)

Creates a new Featurestore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Featurestore featurestore = Featurestore.newBuilder().build();
       Featurestore response =
           featurestoreServiceClient.createFeaturestoreAsync(parent, featurestore).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create Featurestores. Format: `projects/{project}/locations/{location}`  
`featurestore` | `[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)`  
Required. The Featurestore to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[CreateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata)>` |   
  
### createFeaturestoreAsync(String parent, Featurestore featurestore, String featurestoreId)
    
    
    public final OperationFuture<Featurestore,CreateFeaturestoreOperationMetadata> createFeaturestoreAsync(String parent, Featurestore featurestore, String featurestoreId)

Creates a new Featurestore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Featurestore featurestore = Featurestore.newBuilder().build();
       String featurestoreId = "featurestoreId-1315851738";
       Featurestore response =
           featurestoreServiceClient
               .createFeaturestoreAsync(parent, featurestore, featurestoreId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create Featurestores. Format: `projects/{project}/locations/{location}`  
`featurestore` | `[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)`  
Required. The Featurestore to create.  
`featurestoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this Featurestore, which will become the final component of the Featurestore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[CreateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata)>` |   
  
### createFeaturestoreCallable()
    
    
    public final UnaryCallable<CreateFeaturestoreRequest,Operation> createFeaturestoreCallable()

Creates a new Featurestore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateFeaturestoreRequest request =
           CreateFeaturestoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeaturestore(Featurestore.newBuilder().build())
               .setFeaturestoreId("featurestoreId-1315851738")
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.createFeaturestoreCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFeaturestoreOperationCallable()
    
    
    public final OperationCallable<CreateFeaturestoreRequest,Featurestore,CreateFeaturestoreOperationMetadata> createFeaturestoreOperationCallable()

Creates a new Featurestore in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       CreateFeaturestoreRequest request =
           CreateFeaturestoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeaturestore(Featurestore.newBuilder().build())
               .setFeaturestoreId("featurestoreId-1315851738")
               .build();
       OperationFuture<Featurestore, CreateFeaturestoreOperationMetadata> future =
           featurestoreServiceClient.createFeaturestoreOperationCallable().futureCall(request);
       // Do something.
       Featurestore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreRequest),[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[CreateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeaturestoreOperationMetadata)>` |   
  
### deleteEntityTypeAsync(@Nullable EntityTypeName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEntityTypeAsync(@Nullable EntityTypeName name)

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       featurestoreServiceClient.deleteEntityTypeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The name of the EntityType to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEntityTypeAsync(@Nullable EntityTypeName name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEntityTypeAsync(@Nullable EntityTypeName name, boolean force)

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       boolean force = true;
       featurestoreServiceClient.deleteEntityTypeAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The name of the EntityType to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any Features for this EntityType will also be deleted. (Otherwise, the request will only work if the EntityType has no Features.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEntityTypeAsync(DeleteEntityTypeRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEntityTypeAsync(DeleteEntityTypeRequest request)

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteEntityTypeRequest request =
           DeleteEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setForce(true)
               .build();
       featurestoreServiceClient.deleteEntityTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEntityTypeAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEntityTypeAsync(String name)

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       featurestoreServiceClient.deleteEntityTypeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the EntityType to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEntityTypeAsync(String name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEntityTypeAsync(String name, boolean force)

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       boolean force = true;
       featurestoreServiceClient.deleteEntityTypeAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the EntityType to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any Features for this EntityType will also be deleted. (Otherwise, the request will only work if the EntityType has no Features.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEntityTypeCallable()
    
    
    public final UnaryCallable<DeleteEntityTypeRequest,Operation> deleteEntityTypeCallable()

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteEntityTypeRequest request =
           DeleteEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.deleteEntityTypeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEntityTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEntityTypeOperationCallable()
    
    
    public final OperationCallable<DeleteEntityTypeRequest,Empty,DeleteOperationMetadata> deleteEntityTypeOperationCallable()

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteEntityTypeRequest request =
           DeleteEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featurestoreServiceClient.deleteEntityTypeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEntityTypeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureAsync(@Nullable FeatureName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureAsync(@Nullable FeatureName name)

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeatureName name =
           FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
               "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
       featurestoreServiceClient.deleteFeatureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureName`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureAsync(DeleteFeatureRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureAsync(DeleteFeatureRequest request)

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeatureRequest request =
           DeleteFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
                       .toString())
               .build();
       featurestoreServiceClient.deleteFeatureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureAsync(String name)

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name =
           FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                   "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
               .toString();
       featurestoreServiceClient.deleteFeatureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureCallable()
    
    
    public final UnaryCallable<DeleteFeatureRequest,Operation> deleteFeatureCallable()

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeatureRequest request =
           DeleteFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.deleteFeatureCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeatureOperationCallable()
    
    
    public final OperationCallable<DeleteFeatureRequest,Empty,DeleteOperationMetadata> deleteFeatureOperationCallable()

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeatureRequest request =
           DeleteFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featurestoreServiceClient.deleteFeatureOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeatureValuesAsync(@Nullable EntityTypeName entityType)
    
    
    public final OperationFuture<DeleteFeatureValuesResponse,DeleteFeatureValuesOperationMetadata> deleteFeatureValuesAsync(@Nullable EntityTypeName entityType)

Delete Feature values from Featurestore.

The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.

If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       DeleteFeatureValuesResponse response =
           featurestoreServiceClient.deleteFeatureValuesAsync(entityType).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType grouping the Features for which values are being deleted from. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeleteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesResponse),[DeleteFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesOperationMetadata)>` |   
  
### deleteFeatureValuesAsync(DeleteFeatureValuesRequest request)
    
    
    public final OperationFuture<DeleteFeatureValuesResponse,DeleteFeatureValuesOperationMetadata> deleteFeatureValuesAsync(DeleteFeatureValuesRequest request)

Delete Feature values from Featurestore.

The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.

If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeatureValuesRequest request =
           DeleteFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       DeleteFeatureValuesResponse response =
           featurestoreServiceClient.deleteFeatureValuesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeleteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesResponse),[DeleteFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesOperationMetadata)>` |   
  
### deleteFeatureValuesAsync(String entityType)
    
    
    public final OperationFuture<DeleteFeatureValuesResponse,DeleteFeatureValuesOperationMetadata> deleteFeatureValuesAsync(String entityType)

Delete Feature values from Featurestore.

The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.

If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       DeleteFeatureValuesResponse response =
           featurestoreServiceClient.deleteFeatureValuesAsync(entityType).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType grouping the Features for which values are being deleted from. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeleteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesResponse),[DeleteFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesOperationMetadata)>` |   
  
### deleteFeatureValuesCallable()
    
    
    public final UnaryCallable<DeleteFeatureValuesRequest,Operation> deleteFeatureValuesCallable()

Delete Feature values from Featurestore.

The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.

If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeatureValuesRequest request =
           DeleteFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.deleteFeatureValuesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeatureValuesOperationCallable()
    
    
    public final OperationCallable<DeleteFeatureValuesRequest,DeleteFeatureValuesResponse,DeleteFeatureValuesOperationMetadata> deleteFeatureValuesOperationCallable()

Delete Feature values from Featurestore.

The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.

If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeatureValuesRequest request =
           DeleteFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       OperationFuture<DeleteFeatureValuesResponse, DeleteFeatureValuesOperationMetadata> future =
           featurestoreServiceClient.deleteFeatureValuesOperationCallable().futureCall(request);
       // Do something.
       DeleteFeatureValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesRequest),[DeleteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesResponse),[DeleteFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureValuesOperationMetadata)>` |   
  
### deleteFeaturestoreAsync(@Nullable FeaturestoreName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeaturestoreAsync(@Nullable FeaturestoreName name)

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName name = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       featurestoreServiceClient.deleteFeaturestoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreName`  
Required. The name of the Featurestore to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeaturestoreAsync(@Nullable FeaturestoreName name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeaturestoreAsync(@Nullable FeaturestoreName name, boolean force)

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName name = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       boolean force = true;
       featurestoreServiceClient.deleteFeaturestoreAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreName`  
Required. The name of the Featurestore to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any EntityTypes and Features for this Featurestore will also be deleted. (Otherwise, the request will only work if the Featurestore has no EntityTypes.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeaturestoreAsync(DeleteFeaturestoreRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeaturestoreAsync(DeleteFeaturestoreRequest request)

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeaturestoreRequest request =
           DeleteFeaturestoreRequest.newBuilder()
               .setName(FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setForce(true)
               .build();
       featurestoreServiceClient.deleteFeaturestoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeaturestoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeaturestoreAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeaturestoreAsync(String name)

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString();
       featurestoreServiceClient.deleteFeaturestoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Featurestore to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeaturestoreAsync(String name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeaturestoreAsync(String name, boolean force)

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString();
       boolean force = true;
       featurestoreServiceClient.deleteFeaturestoreAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Featurestore to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any EntityTypes and Features for this Featurestore will also be deleted. (Otherwise, the request will only work if the Featurestore has no EntityTypes.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteFeaturestoreCallable()
    
    
    public final UnaryCallable<DeleteFeaturestoreRequest,Operation> deleteFeaturestoreCallable()

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeaturestoreRequest request =
           DeleteFeaturestoreRequest.newBuilder()
               .setName(FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.deleteFeaturestoreCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeaturestoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeaturestoreOperationCallable()
    
    
    public final OperationCallable<DeleteFeaturestoreRequest,Empty,DeleteOperationMetadata> deleteFeaturestoreOperationCallable()

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       DeleteFeaturestoreRequest request =
           DeleteFeaturestoreRequest.newBuilder()
               .setName(FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featurestoreServiceClient.deleteFeaturestoreOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeaturestoreRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### exportFeatureValuesAsync(@Nullable EntityTypeName entityType)
    
    
    public final OperationFuture<ExportFeatureValuesResponse,ExportFeatureValuesOperationMetadata> exportFeatureValuesAsync(@Nullable EntityTypeName entityType)

Exports Feature values from all the entities of a target EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       ExportFeatureValuesResponse response =
           featurestoreServiceClient.exportFeatureValuesAsync(entityType).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType from which to export Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse),[ExportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata)>` |   
  
### exportFeatureValuesAsync(ExportFeatureValuesRequest request)
    
    
    public final OperationFuture<ExportFeatureValuesResponse,ExportFeatureValuesOperationMetadata> exportFeatureValuesAsync(ExportFeatureValuesRequest request)

Exports Feature values from all the entities of a target EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ExportFeatureValuesRequest request =
           ExportFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setDestination(FeatureValueDestination.newBuilder().build())
               .setFeatureSelector(FeatureSelector.newBuilder().build())
               .addAllSettings(new ArrayList<DestinationFeatureSetting>())
               .build();
       ExportFeatureValuesResponse response =
           featurestoreServiceClient.exportFeatureValuesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse),[ExportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata)>` |   
  
### exportFeatureValuesAsync(String entityType)
    
    
    public final OperationFuture<ExportFeatureValuesResponse,ExportFeatureValuesOperationMetadata> exportFeatureValuesAsync(String entityType)

Exports Feature values from all the entities of a target EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       ExportFeatureValuesResponse response =
           featurestoreServiceClient.exportFeatureValuesAsync(entityType).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType from which to export Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse),[ExportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata)>` |   
  
### exportFeatureValuesCallable()
    
    
    public final UnaryCallable<ExportFeatureValuesRequest,Operation> exportFeatureValuesCallable()

Exports Feature values from all the entities of a target EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ExportFeatureValuesRequest request =
           ExportFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setDestination(FeatureValueDestination.newBuilder().build())
               .setFeatureSelector(FeatureSelector.newBuilder().build())
               .addAllSettings(new ArrayList<DestinationFeatureSetting>())
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.exportFeatureValuesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportFeatureValuesOperationCallable()
    
    
    public final OperationCallable<ExportFeatureValuesRequest,ExportFeatureValuesResponse,ExportFeatureValuesOperationMetadata> exportFeatureValuesOperationCallable()

Exports Feature values from all the entities of a target EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ExportFeatureValuesRequest request =
           ExportFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setDestination(FeatureValueDestination.newBuilder().build())
               .setFeatureSelector(FeatureSelector.newBuilder().build())
               .addAllSettings(new ArrayList<DestinationFeatureSetting>())
               .build();
       OperationFuture<ExportFeatureValuesResponse, ExportFeatureValuesOperationMetadata> future =
           featurestoreServiceClient.exportFeatureValuesOperationCallable().futureCall(request);
       // Do something.
       ExportFeatureValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest),[ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse),[ExportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata)>` |   
  
### getEntityType(@Nullable EntityTypeName name)
    
    
    public final EntityType getEntityType(@Nullable EntityTypeName name)

Gets details of a single EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       EntityType response = featurestoreServiceClient.getEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The name of the EntityType resource. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)` |   
  
### getEntityType(GetEntityTypeRequest request)
    
    
    public final EntityType getEntityType(GetEntityTypeRequest request)

Gets details of a single EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetEntityTypeRequest request =
           GetEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       EntityType response = featurestoreServiceClient.getEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)` |   
  
### getEntityType(String name)
    
    
    public final EntityType getEntityType(String name)

Gets details of a single EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       EntityType response = featurestoreServiceClient.getEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the EntityType resource. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)` |   
  
### getEntityTypeCallable()
    
    
    public final UnaryCallable<GetEntityTypeRequest,EntityType> getEntityTypeCallable()

Gets details of a single EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetEntityTypeRequest request =
           GetEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       ApiFuture<EntityType> future =
           featurestoreServiceClient.getEntityTypeCallable().futureCall(request);
       // Do something.
       EntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)>` |   
  
### getFeature(@Nullable FeatureName name)
    
    
    public final Feature getFeature(@Nullable FeatureName name)

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeatureName name =
           FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
               "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
       Feature response = featurestoreServiceClient.getFeature(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureName`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)` |   
  
### getFeature(GetFeatureRequest request)
    
    
    public final Feature getFeature(GetFeatureRequest request)

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetFeatureRequest request =
           GetFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
                       .toString())
               .build();
       Feature response = featurestoreServiceClient.getFeature(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)` |   
  
### getFeature(String name)
    
    
    public final Feature getFeature(String name)

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name =
           FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                   "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
               .toString();
       Feature response = featurestoreServiceClient.getFeature(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)` |   
  
### getFeatureCallable()
    
    
    public final UnaryCallable<GetFeatureRequest,Feature> getFeatureCallable()

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetFeatureRequest request =
           GetFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
                       .toString())
               .build();
       ApiFuture<Feature> future =
           featurestoreServiceClient.getFeatureCallable().futureCall(request);
       // Do something.
       Feature response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureRequest),[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)>` |   
  
### getFeaturestore(@Nullable FeaturestoreName name)
    
    
    public final Featurestore getFeaturestore(@Nullable FeaturestoreName name)

Gets details of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName name = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       Featurestore response = featurestoreServiceClient.getFeaturestore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreName`  
Required. The name of the Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)` |   
  
### getFeaturestore(GetFeaturestoreRequest request)
    
    
    public final Featurestore getFeaturestore(GetFeaturestoreRequest request)

Gets details of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetFeaturestoreRequest request =
           GetFeaturestoreRequest.newBuilder()
               .setName(FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .build();
       Featurestore response = featurestoreServiceClient.getFeaturestore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeaturestoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)` |   
  
### getFeaturestore(String name)
    
    
    public final Featurestore getFeaturestore(String name)

Gets details of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String name = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString();
       Featurestore response = featurestoreServiceClient.getFeaturestore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)` |   
  
### getFeaturestoreCallable()
    
    
    public final UnaryCallable<GetFeaturestoreRequest,Featurestore> getFeaturestoreCallable()

Gets details of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetFeaturestoreRequest request =
           GetFeaturestoreRequest.newBuilder()
               .setName(FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .build();
       ApiFuture<Featurestore> future =
           featurestoreServiceClient.getFeaturestoreCallable().futureCall(request);
       // Do something.
       Featurestore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeaturestoreRequest),[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = featurestoreServiceClient.getIamPolicy(request);
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
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           featurestoreServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = featurestoreServiceClient.getLocation(request);
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
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           featurestoreServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable FeaturestoreServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings` |   
  
### getStub()
    
    
    public FeaturestoreServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeaturestoreServiceStub)` |   
  
### importFeatureValuesAsync(@Nullable EntityTypeName entityType)
    
    
    public final OperationFuture<ImportFeatureValuesResponse,ImportFeatureValuesOperationMetadata> importFeatureValuesAsync(@Nullable EntityTypeName entityType)

Imports Feature values into the Featurestore from a source storage.

The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done.

If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done.

There are also scenarios where the caller can cause inconsistency.

\- Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       ImportFeatureValuesResponse response =
           featurestoreServiceClient.importFeatureValuesAsync(entityType).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType grouping the Features for which values are being imported. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesResponse),[ImportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesOperationMetadata)>` |   
  
### importFeatureValuesAsync(ImportFeatureValuesRequest request)
    
    
    public final OperationFuture<ImportFeatureValuesResponse,ImportFeatureValuesOperationMetadata> importFeatureValuesAsync(ImportFeatureValuesRequest request)

Imports Feature values into the Featurestore from a source storage.

The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done.

If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done.

There are also scenarios where the caller can cause inconsistency.

\- Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ImportFeatureValuesRequest request =
           ImportFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setEntityIdField("entityIdField512670524")
               .addAllFeatureSpecs(new ArrayList<ImportFeatureValuesRequest.FeatureSpec>())
               .setDisableOnlineServing(true)
               .setWorkerCount(372044046)
               .setDisableIngestionAnalysis(true)
               .build();
       ImportFeatureValuesResponse response =
           featurestoreServiceClient.importFeatureValuesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesResponse),[ImportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesOperationMetadata)>` |   
  
### importFeatureValuesAsync(String entityType)
    
    
    public final OperationFuture<ImportFeatureValuesResponse,ImportFeatureValuesOperationMetadata> importFeatureValuesAsync(String entityType)

Imports Feature values into the Featurestore from a source storage.

The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done.

If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done.

There are also scenarios where the caller can cause inconsistency.

\- Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       ImportFeatureValuesResponse response =
           featurestoreServiceClient.importFeatureValuesAsync(entityType).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType grouping the Features for which values are being imported. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesResponse),[ImportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesOperationMetadata)>` |   
  
### importFeatureValuesCallable()
    
    
    public final UnaryCallable<ImportFeatureValuesRequest,Operation> importFeatureValuesCallable()

Imports Feature values into the Featurestore from a source storage.

The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done.

If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done.

There are also scenarios where the caller can cause inconsistency.

\- Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ImportFeatureValuesRequest request =
           ImportFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setEntityIdField("entityIdField512670524")
               .addAllFeatureSpecs(new ArrayList<ImportFeatureValuesRequest.FeatureSpec>())
               .setDisableOnlineServing(true)
               .setWorkerCount(372044046)
               .setDisableIngestionAnalysis(true)
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.importFeatureValuesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importFeatureValuesOperationCallable()
    
    
    public final OperationCallable<ImportFeatureValuesRequest,ImportFeatureValuesResponse,ImportFeatureValuesOperationMetadata> importFeatureValuesOperationCallable()

Imports Feature values into the Featurestore from a source storage.

The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done.

If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done.

There are also scenarios where the caller can cause inconsistency.

\- Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ImportFeatureValuesRequest request =
           ImportFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setEntityIdField("entityIdField512670524")
               .addAllFeatureSpecs(new ArrayList<ImportFeatureValuesRequest.FeatureSpec>())
               .setDisableOnlineServing(true)
               .setWorkerCount(372044046)
               .setDisableIngestionAnalysis(true)
               .build();
       OperationFuture<ImportFeatureValuesResponse, ImportFeatureValuesOperationMetadata> future =
           featurestoreServiceClient.importFeatureValuesOperationCallable().futureCall(request);
       // Do something.
       ImportFeatureValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest),[ImportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesResponse),[ImportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesOperationMetadata)>` |   
  
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
  
### listEntityTypes(@Nullable FeaturestoreName parent)
    
    
    public final FeaturestoreServiceClient.ListEntityTypesPagedResponse listEntityTypes(@Nullable FeaturestoreName parent)

Lists EntityTypes in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeaturestoreName parent = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]");
       for (EntityType element : featurestoreServiceClient.listEntityTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreName`  
Required. The resource name of the Featurestore to list EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListEntityTypesPagedResponse)` |   
  
### listEntityTypes(ListEntityTypesRequest request)
    
    
    public final FeaturestoreServiceClient.ListEntityTypesPagedResponse listEntityTypes(ListEntityTypesRequest request)

Lists EntityTypes in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListEntityTypesRequest request =
           ListEntityTypesRequest.newBuilder()
               .setParent(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (EntityType element : featurestoreServiceClient.listEntityTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListEntityTypesPagedResponse)` |   
  
### listEntityTypes(String parent)
    
    
    public final FeaturestoreServiceClient.ListEntityTypesPagedResponse listEntityTypes(String parent)

Lists EntityTypes in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent = FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString();
       for (EntityType element : featurestoreServiceClient.listEntityTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Featurestore to list EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListEntityTypesPagedResponse)` |   
  
### listEntityTypesCallable()
    
    
    public final UnaryCallable<ListEntityTypesRequest,ListEntityTypesResponse> listEntityTypesCallable()

Lists EntityTypes in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListEntityTypesRequest request =
           ListEntityTypesRequest.newBuilder()
               .setParent(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListEntityTypesResponse response =
             featurestoreServiceClient.listEntityTypesCallable().call(request);
         for (EntityType element : response.getEntityTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEntityTypesRequest),[ListEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEntityTypesResponse)>` |   
  
### listEntityTypesPagedCallable()
    
    
    public final UnaryCallable<ListEntityTypesRequest,FeaturestoreServiceClient.ListEntityTypesPagedResponse> listEntityTypesPagedCallable()

Lists EntityTypes in a given Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListEntityTypesRequest request =
           ListEntityTypesRequest.newBuilder()
               .setParent(
                   FeaturestoreName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<EntityType> future =
           featurestoreServiceClient.listEntityTypesPagedCallable().futureCall(request);
       // Do something.
       for (EntityType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEntityTypesRequest),[ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListEntityTypesPagedResponse)>` |   
  
### listFeatures(@Nullable EntityTypeName parent)
    
    
    public final FeaturestoreServiceClient.ListFeaturesPagedResponse listFeatures(@Nullable EntityTypeName parent)

Lists Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityTypeName parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       for (Feature element : featurestoreServiceClient.listFeatures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeatures(@Nullable FeatureGroupName parent)
    
    
    public final FeaturestoreServiceClient.ListFeaturesPagedResponse listFeatures(@Nullable FeatureGroupName parent)

Lists Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       for (Feature element : featurestoreServiceClient.listFeatures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeatureGroupName`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeatures(ListFeaturesRequest request)
    
    
    public final FeaturestoreServiceClient.ListFeaturesPagedResponse listFeatures(ListFeaturesRequest request)

Lists Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListFeaturesRequest request =
           ListFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .setLatestStatsCount(-878108489)
               .build();
       for (Feature element : featurestoreServiceClient.listFeatures(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeatures(String parent)
    
    
    public final FeaturestoreServiceClient.ListFeaturesPagedResponse listFeatures(String parent)

Lists Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       for (Feature element : featurestoreServiceClient.listFeatures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeaturesCallable()
    
    
    public final UnaryCallable<ListFeaturesRequest,ListFeaturesResponse> listFeaturesCallable()

Lists Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListFeaturesRequest request =
           ListFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .setLatestStatsCount(-878108489)
               .build();
       while (true) {
         ListFeaturesResponse response =
             featurestoreServiceClient.listFeaturesCallable().call(request);
         for (Feature element : response.getFeaturesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturesRequest),[ListFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturesResponse)>` |   
  
### listFeaturesPagedCallable()
    
    
    public final UnaryCallable<ListFeaturesRequest,FeaturestoreServiceClient.ListFeaturesPagedResponse> listFeaturesPagedCallable()

Lists Features in a given EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListFeaturesRequest request =
           ListFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .setLatestStatsCount(-878108489)
               .build();
       ApiFuture<Feature> future =
           featurestoreServiceClient.listFeaturesPagedCallable().futureCall(request);
       // Do something.
       for (Feature element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturesRequest),[ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturesPagedResponse)>` |   
  
### listFeaturestores(@Nullable LocationName parent)
    
    
    public final FeaturestoreServiceClient.ListFeaturestoresPagedResponse listFeaturestores(@Nullable LocationName parent)

Lists Featurestores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Featurestore element :
           featurestoreServiceClient.listFeaturestores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list Featurestores. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListFeaturestoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturestoresPagedResponse)` |   
  
### listFeaturestores(ListFeaturestoresRequest request)
    
    
    public final FeaturestoreServiceClient.ListFeaturestoresPagedResponse listFeaturestores(ListFeaturestoresRequest request)

Lists Featurestores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListFeaturestoresRequest request =
           ListFeaturestoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (Featurestore element :
           featurestoreServiceClient.listFeaturestores(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeaturestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturestoresRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListFeaturestoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturestoresPagedResponse)` |   
  
### listFeaturestores(String parent)
    
    
    public final FeaturestoreServiceClient.ListFeaturestoresPagedResponse listFeaturestores(String parent)

Lists Featurestores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Featurestore element :
           featurestoreServiceClient.listFeaturestores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list Featurestores. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.ListFeaturestoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturestoresPagedResponse)` |   
  
### listFeaturestoresCallable()
    
    
    public final UnaryCallable<ListFeaturestoresRequest,ListFeaturestoresResponse> listFeaturestoresCallable()

Lists Featurestores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListFeaturestoresRequest request =
           ListFeaturestoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListFeaturestoresResponse response =
             featurestoreServiceClient.listFeaturestoresCallable().call(request);
         for (Featurestore element : response.getFeaturestoresList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeaturestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturestoresRequest),[ListFeaturestoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturestoresResponse)>` |   
  
### listFeaturestoresPagedCallable()
    
    
    public final UnaryCallable<ListFeaturestoresRequest,FeaturestoreServiceClient.ListFeaturestoresPagedResponse> listFeaturestoresPagedCallable()

Lists Featurestores in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListFeaturestoresRequest request =
           ListFeaturestoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Featurestore> future =
           featurestoreServiceClient.listFeaturestoresPagedCallable().futureCall(request);
       // Do something.
       for (Featurestore element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeaturestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturestoresRequest),[ListFeaturestoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListFeaturestoresPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final FeaturestoreServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : featurestoreServiceClient.listLocations(request).iterateAll()) {
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
`[FeaturestoreServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             featurestoreServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,FeaturestoreServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           featurestoreServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.ListLocationsPagedResponse)>` |   
  
### searchFeatures(@Nullable LocationName location)
    
    
    public final FeaturestoreServiceClient.SearchFeaturesPagedResponse searchFeatures(@Nullable LocationName location)

Searches Features matching a query in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       LocationName location = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Feature element : featurestoreServiceClient.searchFeatures(location).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`location` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.SearchFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.SearchFeaturesPagedResponse)` |   
  
### searchFeatures(@Nullable LocationName location, String query)
    
    
    public final FeaturestoreServiceClient.SearchFeaturesPagedResponse searchFeatures(@Nullable LocationName location, String query)

Searches Features matching a query in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       LocationName location = LocationName.of("[PROJECT]", "[LOCATION]");
       String query = "query107944136";
       for (Feature element :
           featurestoreServiceClient.searchFeatures(location, query).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using `AND` to form a conjunction. A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature's FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by: * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric `[a-zA-Z0-9]`, underscore `_`, or asterisk `*` are treated as delimiters for tokens. `*` is treated as a wildcard that matches characters within a token. * Ignoring case. * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY. A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks ("). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively. Supported FIELDs for field-restricted queries: 

  * `feature_id`
  * `description`
  * `entity_type_id`

Examples: 

  * `feature_id: foo` \--> Matches a Feature with ID containing the substring `foo` (eg. `foo`, `foofeature`, `barfoo`). 
  * `feature_id: foo*feature` \--> Matches a Feature with ID containing the substring `foo*feature` (eg. `foobarfeature`). 
  * `feature_id: foo AND description: bar` \--> Matches a Feature with ID containing the substring `foo` and description containing the substring `bar`. 

Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive. 

  * `feature_id`: Supports = comparisons. 
  * `description`: Supports = comparisons. Multi-token filters should be enclosed in quotes. 
  * `entity_type_id`: Supports = comparisons. 
  * `value_type`: Supports = and != comparisons. 
  * `labels`: Supports key-value equality as well as key presence. 
  * `featurestore_id`: Supports = comparisons. 

Examples: 

  * `description = "foo bar"` \--> Any Feature with description exactly equal to `foo bar`
  * `value_type = DOUBLE` \--> Features whose type is DOUBLE. 
  * `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels. 
  * `labels.env: *` \--> Any Feature which has a label with `env` as the key. 

  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.SearchFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.SearchFeaturesPagedResponse)` |   
  
### searchFeatures(SearchFeaturesRequest request)
    
    
    public final FeaturestoreServiceClient.SearchFeaturesPagedResponse searchFeatures(SearchFeaturesRequest request)

Searches Features matching a query in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       SearchFeaturesRequest request =
           SearchFeaturesRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Feature element : featurestoreServiceClient.searchFeatures(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.SearchFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.SearchFeaturesPagedResponse)` |   
  
### searchFeatures(String location)
    
    
    public final FeaturestoreServiceClient.SearchFeaturesPagedResponse searchFeatures(String location)

Searches Features matching a query in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String location = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Feature element : featurestoreServiceClient.searchFeatures(location).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.SearchFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.SearchFeaturesPagedResponse)` |   
  
### searchFeatures(String location, String query)
    
    
    public final FeaturestoreServiceClient.SearchFeaturesPagedResponse searchFeatures(String location, String query)

Searches Features matching a query in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       String location = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String query = "query107944136";
       for (Feature element :
           featurestoreServiceClient.searchFeatures(location, query).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using `AND` to form a conjunction. A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature's FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by: * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric `[a-zA-Z0-9]`, underscore `_`, or asterisk `*` are treated as delimiters for tokens. `*` is treated as a wildcard that matches characters within a token. * Ignoring case. * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY. A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks ("). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively. Supported FIELDs for field-restricted queries: 

  * `feature_id`
  * `description`
  * `entity_type_id`

Examples: 

  * `feature_id: foo` \--> Matches a Feature with ID containing the substring `foo` (eg. `foo`, `foofeature`, `barfoo`). 
  * `feature_id: foo*feature` \--> Matches a Feature with ID containing the substring `foo*feature` (eg. `foobarfeature`). 
  * `feature_id: foo AND description: bar` \--> Matches a Feature with ID containing the substring `foo` and description containing the substring `bar`. 

Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive. 

  * `feature_id`: Supports = comparisons. 
  * `description`: Supports = comparisons. Multi-token filters should be enclosed in quotes. 
  * `entity_type_id`: Supports = comparisons. 
  * `value_type`: Supports = and != comparisons. 
  * `labels`: Supports key-value equality as well as key presence. 
  * `featurestore_id`: Supports = comparisons. 

Examples: 

  * `description = "foo bar"` \--> Any Feature with description exactly equal to `foo bar`
  * `value_type = DOUBLE` \--> Features whose type is DOUBLE. 
  * `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels. 
  * `labels.env: *` \--> Any Feature which has a label with `env` as the key. 

  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreServiceClient.SearchFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.SearchFeaturesPagedResponse)` |   
  
### searchFeaturesCallable()
    
    
    public final UnaryCallable<SearchFeaturesRequest,SearchFeaturesResponse> searchFeaturesCallable()

Searches Features matching a query in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       SearchFeaturesRequest request =
           SearchFeaturesRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         SearchFeaturesResponse response =
             featurestoreServiceClient.searchFeaturesCallable().call(request);
         for (Feature element : response.getFeaturesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchFeaturesRequest),[SearchFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchFeaturesResponse)>` |   
  
### searchFeaturesPagedCallable()
    
    
    public final UnaryCallable<SearchFeaturesRequest,FeaturestoreServiceClient.SearchFeaturesPagedResponse> searchFeaturesPagedCallable()

Searches Features matching a query in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       SearchFeaturesRequest request =
           SearchFeaturesRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Feature> future =
           featurestoreServiceClient.searchFeaturesPagedCallable().futureCall(request);
       // Do something.
       for (Feature element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchFeaturesRequest),[SearchFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.SearchFeaturesPagedResponse)>` |   
  
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
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = featurestoreServiceClient.setIamPolicy(request);
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
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
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
           featurestoreServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = featurestoreServiceClient.testIamPermissions(request);
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
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           featurestoreServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateEntityType(EntityType entityType, FieldMask updateMask)
    
    
    public final EntityType updateEntityType(EntityType entityType, FieldMask updateMask)

Updates the parameters of a single EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       EntityType entityType = EntityType.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EntityType response = featurestoreServiceClient.updateEntityType(entityType, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)`  
Required. The EntityType's `name` field is used to identify the EntityType to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the EntityType resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `description` * `labels` * `monitoring_config.snapshot_analysis.disabled` * `monitoring_config.snapshot_analysis.monitoring_interval_days` * `monitoring_config.snapshot_analysis.staleness_days` * `monitoring_config.import_features_analysis.state` * `monitoring_config.import_features_analysis.anomaly_detection_baseline` * `monitoring_config.numerical_threshold_config.value` * `monitoring_config.categorical_threshold_config.value` * `offline_storage_ttl_days`  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)` |   
  
### updateEntityType(UpdateEntityTypeRequest request)
    
    
    public final EntityType updateEntityType(UpdateEntityTypeRequest request)

Updates the parameters of a single EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       UpdateEntityTypeRequest request =
           UpdateEntityTypeRequest.newBuilder()
               .setEntityType(EntityType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       EntityType response = featurestoreServiceClient.updateEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)` |   
  
### updateEntityTypeCallable()
    
    
    public final UnaryCallable<UpdateEntityTypeRequest,EntityType> updateEntityTypeCallable()

Updates the parameters of a single EntityType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       UpdateEntityTypeRequest request =
           UpdateEntityTypeRequest.newBuilder()
               .setEntityType(EntityType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<EntityType> future =
           featurestoreServiceClient.updateEntityTypeCallable().futureCall(request);
       // Do something.
       EntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType)>` |   
  
### updateFeature(Feature feature, FieldMask updateMask)
    
    
    public final Feature updateFeature(Feature feature, FieldMask updateMask)

Updates the parameters of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       Feature feature = Feature.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Feature response = featurestoreServiceClient.updateFeature(feature, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)`  
Required. The Feature's `name` field is used to identify the Feature to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Features resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `description` * `labels` * `disable_monitoring` (Not supported for FeatureRegistryService Feature) * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)` |   
  
### updateFeature(UpdateFeatureRequest request)
    
    
    public final Feature updateFeature(UpdateFeatureRequest request)

Updates the parameters of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       UpdateFeatureRequest request =
           UpdateFeatureRequest.newBuilder()
               .setFeature(Feature.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Feature response = featurestoreServiceClient.updateFeature(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)` |   
  
### updateFeatureCallable()
    
    
    public final UnaryCallable<UpdateFeatureRequest,Feature> updateFeatureCallable()

Updates the parameters of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       UpdateFeatureRequest request =
           UpdateFeatureRequest.newBuilder()
               .setFeature(Feature.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Feature> future =
           featurestoreServiceClient.updateFeatureCallable().futureCall(request);
       // Do something.
       Feature response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeatureRequest),[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature)>` |   
  
### updateFeaturestoreAsync(Featurestore featurestore, FieldMask updateMask)
    
    
    public final OperationFuture<Featurestore,UpdateFeaturestoreOperationMetadata> updateFeaturestoreAsync(Featurestore featurestore, FieldMask updateMask)

Updates the parameters of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       Featurestore featurestore = Featurestore.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Featurestore response =
           featurestoreServiceClient.updateFeaturestoreAsync(featurestore, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`featurestore` | `[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore)`  
Required. The Featurestore's `name` field is used to identify the Featurestore to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Featurestore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `labels` * `online_serving_config.fixed_node_count` * `online_serving_config.scaling` * `online_storage_ttl_days`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[UpdateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreOperationMetadata)>` |   
  
### updateFeaturestoreAsync(UpdateFeaturestoreRequest request)
    
    
    public final OperationFuture<Featurestore,UpdateFeaturestoreOperationMetadata> updateFeaturestoreAsync(UpdateFeaturestoreRequest request)

Updates the parameters of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       UpdateFeaturestoreRequest request =
           UpdateFeaturestoreRequest.newBuilder()
               .setFeaturestore(Featurestore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Featurestore response = featurestoreServiceClient.updateFeaturestoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[UpdateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreOperationMetadata)>` |   
  
### updateFeaturestoreCallable()
    
    
    public final UnaryCallable<UpdateFeaturestoreRequest,Operation> updateFeaturestoreCallable()

Updates the parameters of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       UpdateFeaturestoreRequest request =
           UpdateFeaturestoreRequest.newBuilder()
               .setFeaturestore(Featurestore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           featurestoreServiceClient.updateFeaturestoreCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFeaturestoreOperationCallable()
    
    
    public final OperationCallable<UpdateFeaturestoreRequest,Featurestore,UpdateFeaturestoreOperationMetadata> updateFeaturestoreOperationCallable()

Updates the parameters of a single Featurestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreServiceClient featurestoreServiceClient = FeaturestoreServiceClient.create()) {
       UpdateFeaturestoreRequest request =
           UpdateFeaturestoreRequest.newBuilder()
               .setFeaturestore(Featurestore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Featurestore, UpdateFeaturestoreOperationMetadata> future =
           featurestoreServiceClient.updateFeaturestoreOperationCallable().futureCall(request);
       // Do something.
       Featurestore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFeaturestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreRequest),[Featurestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Featurestore),[UpdateFeaturestoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateFeaturestoreOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
