---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient
title: Class FeatureRegistryServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:49.690739+00:00
---

# Class FeatureRegistryServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FeatureRegistryServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1beta1/FeatureRegistryServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The service that handles CRUD and List for resources for FeatureRegistry.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName name = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       FeatureGroup response = featureRegistryServiceClient.getFeatureGroup(name);
     }
     

Note: close() needs to be called on the FeatureRegistryServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateFeatureGroup |  Creates a new FeatureGroup in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeatureGroupAsync(CreateFeatureGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFeatureGroupAsync(LocationName parent, FeatureGroup featureGroup, String featureGroupId) 
  * createFeatureGroupAsync(String parent, FeatureGroup featureGroup, String featureGroupId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeatureGroupOperationCallable() 
  * createFeatureGroupCallable() 

  
GetFeatureGroup |  Gets details of a single FeatureGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeatureGroup(GetFeatureGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeatureGroup(FeatureGroupName name) 
  * getFeatureGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeatureGroupCallable() 

  
ListFeatureGroups |  Lists FeatureGroups in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatureGroups(ListFeatureGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatureGroups(LocationName parent) 
  * listFeatureGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeatureGroupsPagedCallable() 
  * listFeatureGroupsCallable() 

  
UpdateFeatureGroup |  Updates the parameters of a single FeatureGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFeatureGroupAsync(UpdateFeatureGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFeatureGroupAsync(FeatureGroup featureGroup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFeatureGroupOperationCallable() 
  * updateFeatureGroupCallable() 

  
DeleteFeatureGroup |  Deletes a single FeatureGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeatureGroupAsync(DeleteFeatureGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeatureGroupAsync(FeatureGroupName name, boolean force) 
  * deleteFeatureGroupAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeatureGroupOperationCallable() 
  * deleteFeatureGroupCallable() 

  
CreateFeature |  Creates a new Feature in a given FeatureGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeatureAsync(CreateFeatureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFeatureAsync(EntityTypeName parent, Feature feature, String featureId) 
  * createFeatureAsync(FeatureGroupName parent, Feature feature, String featureId) 
  * createFeatureAsync(String parent, Feature feature, String featureId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeatureOperationCallable() 
  * createFeatureCallable() 

  
BatchCreateFeatures |  Creates a batch of Features in a given FeatureGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

  
ListFeatures |  Lists Features in a given FeatureGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatures(ListFeaturesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatures(EntityTypeName parent) 
  * listFeatures(FeatureGroupName parent) 
  * listFeatures(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeaturesPagedCallable() 
  * listFeaturesCallable() 

  
UpdateFeature |  Updates the parameters of a single Feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFeatureAsync(UpdateFeatureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFeatureAsync(Feature feature, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFeatureOperationCallable() 
  * updateFeatureCallable() 

  
DeleteFeature |  Deletes a single Feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeatureAsync(DeleteFeatureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeatureAsync(FeatureName name) 
  * deleteFeatureAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeatureOperationCallable() 
  * deleteFeatureCallable() 

  
CreateFeatureMonitor |  Creates a new FeatureMonitor in a given project, location and FeatureGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeatureMonitorAsync(CreateFeatureMonitorRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFeatureMonitorAsync(FeatureGroupName parent, FeatureMonitor featureMonitor, String featureMonitorId) 
  * createFeatureMonitorAsync(String parent, FeatureMonitor featureMonitor, String featureMonitorId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeatureMonitorOperationCallable() 
  * createFeatureMonitorCallable() 

  
GetFeatureMonitor |  Gets details of a single FeatureMonitor. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeatureMonitor(GetFeatureMonitorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeatureMonitor(FeatureMonitorName name) 
  * getFeatureMonitor(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeatureMonitorCallable() 

  
ListFeatureMonitors |  Lists FeatureGroups in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatureMonitors(ListFeatureMonitorsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatureMonitors(FeatureGroupName parent) 
  * listFeatureMonitors(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeatureMonitorsPagedCallable() 
  * listFeatureMonitorsCallable() 

  
UpdateFeatureMonitor |  Updates the parameters of a single FeatureMonitor. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFeatureMonitorAsync(UpdateFeatureMonitorRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFeatureMonitorAsync(FeatureMonitor featureMonitor, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFeatureMonitorOperationCallable() 
  * updateFeatureMonitorCallable() 

  
DeleteFeatureMonitor |  Deletes a single FeatureMonitor. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFeatureMonitorAsync(DeleteFeatureMonitorRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFeatureMonitorAsync(FeatureMonitorName name) 
  * deleteFeatureMonitorAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFeatureMonitorOperationCallable() 
  * deleteFeatureMonitorCallable() 

  
CreateFeatureMonitorJob |  Creates a new feature monitor job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFeatureMonitorJob(CreateFeatureMonitorJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createFeatureMonitorJob(FeatureMonitorName parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId) 
  * createFeatureMonitorJob(String parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFeatureMonitorJobCallable() 

  
GetFeatureMonitorJob |  Get a feature monitor job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFeatureMonitorJob(GetFeatureMonitorJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFeatureMonitorJob(FeatureMonitorJobName name) 
  * getFeatureMonitorJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFeatureMonitorJobCallable() 

  
ListFeatureMonitorJobs |  List feature monitor jobs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFeatureMonitorJobs(ListFeatureMonitorJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFeatureMonitorJobs(FeatureMonitorName parent) 
  * listFeatureMonitorJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFeatureMonitorJobsPagedCallable() 
  * listFeatureMonitorJobsCallable() 

  
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

This class can be customized by passing in a custom instance of FeatureRegistryServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeatureRegistryServiceSettings featureRegistryServiceSettings =
         FeatureRegistryServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create(featureRegistryServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeatureRegistryServiceSettings featureRegistryServiceSettings =
         FeatureRegistryServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create(featureRegistryServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FeatureRegistryServiceClient

## Static Methods 

### create()
    
    
    public static final FeatureRegistryServiceClient create()

Constructs an instance of FeatureRegistryServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeatureRegistryServiceSettings settings)
    
    
    public static final FeatureRegistryServiceClient create(FeatureRegistryServiceSettings settings)

Constructs an instance of FeatureRegistryServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeatureRegistryServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeatureRegistryServiceStub stub)
    
    
    public static final FeatureRegistryServiceClient create(FeatureRegistryServiceStub stub)

Constructs an instance of FeatureRegistryServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(FeatureRegistryServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeatureRegistryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.stub.FeatureRegistryServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient)` |   
  
## Constructors 

### FeatureRegistryServiceClient(FeatureRegistryServiceSettings settings)
    
    
    protected FeatureRegistryServiceClient(FeatureRegistryServiceSettings settings)

Constructs an instance of FeatureRegistryServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeatureRegistryServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceSettings)`  
  
  
### FeatureRegistryServiceClient(FeatureRegistryServiceStub stub)
    
    
    protected FeatureRegistryServiceClient(FeatureRegistryServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeatureRegistryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.stub.FeatureRegistryServiceStub)`  
  
  
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

Creates a batch of Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       EntityTypeName parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       List<CreateFeatureRequest> requests = new ArrayList<>();
       BatchCreateFeaturesResponse response =
           featureRegistryServiceClient.batchCreateFeaturesAsync(parent, requests).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.EntityTypeName`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureRequest)>`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesAsync(@Nullable FeatureGroupName parent, List<CreateFeatureRequest> requests)
    
    
    public final OperationFuture<BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesAsync(@Nullable FeatureGroupName parent, List<CreateFeatureRequest> requests)

Creates a batch of Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       List<CreateFeatureRequest> requests = new ArrayList<>();
       BatchCreateFeaturesResponse response =
           featureRegistryServiceClient.batchCreateFeaturesAsync(parent, requests).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureGroupName`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureRequest)>`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesAsync(BatchCreateFeaturesRequest request)
    
    
    public final OperationFuture<BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesAsync(BatchCreateFeaturesRequest request)

Creates a batch of Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       BatchCreateFeaturesRequest request =
           BatchCreateFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateFeatureRequest>())
               .build();
       BatchCreateFeaturesResponse response =
           featureRegistryServiceClient.batchCreateFeaturesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesAsync(String parent, List<CreateFeatureRequest> requests)
    
    
    public final OperationFuture<BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesAsync(String parent, List<CreateFeatureRequest> requests)

Creates a batch of Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       List<CreateFeatureRequest> requests = new ArrayList<>();
       BatchCreateFeaturesResponse response =
           featureRegistryServiceClient.batchCreateFeaturesAsync(parent, requests).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureRequest)>`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesOperationMetadata)>` |   
  
### batchCreateFeaturesCallable()
    
    
    public final UnaryCallable<BatchCreateFeaturesRequest,Operation> batchCreateFeaturesCallable()

Creates a batch of Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       BatchCreateFeaturesRequest request =
           BatchCreateFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateFeatureRequest>())
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.batchCreateFeaturesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchCreateFeaturesOperationCallable()
    
    
    public final OperationCallable<BatchCreateFeaturesRequest,BatchCreateFeaturesResponse,BatchCreateFeaturesOperationMetadata> batchCreateFeaturesOperationCallable()

Creates a batch of Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       BatchCreateFeaturesRequest request =
           BatchCreateFeaturesRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateFeatureRequest>())
               .build();
       OperationFuture<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> future =
           featureRegistryServiceClient.batchCreateFeaturesOperationCallable().futureCall(request);
       // Do something.
       BatchCreateFeaturesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesRequest),[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesResponse),[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesOperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createFeatureAsync(@Nullable EntityTypeName parent, Feature feature, String featureId)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(@Nullable EntityTypeName parent, Feature feature, String featureId)

Creates a new Feature in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       EntityTypeName parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       Feature feature = Feature.newBuilder().build();
       String featureId = "featureId-420503887";
       Feature response =
           featureRegistryServiceClient.createFeatureAsync(parent, feature, featureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.EntityTypeName`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(@Nullable FeatureGroupName parent, Feature feature, String featureId)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(@Nullable FeatureGroupName parent, Feature feature, String featureId)

Creates a new Feature in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       Feature feature = Feature.newBuilder().build();
       String featureId = "featureId-420503887";
       Feature response =
           featureRegistryServiceClient.createFeatureAsync(parent, feature, featureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureGroupName`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(CreateFeatureRequest request)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(CreateFeatureRequest request)

Creates a new Feature in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureRequest request =
           CreateFeatureRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFeature(Feature.newBuilder().build())
               .setFeatureId("featureId-420503887")
               .build();
       Feature response = featureRegistryServiceClient.createFeatureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureAsync(String parent, Feature feature, String featureId)
    
    
    public final OperationFuture<Feature,CreateFeatureOperationMetadata> createFeatureAsync(String parent, Feature feature, String featureId)

Creates a new Feature in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       Feature feature = Feature.newBuilder().build();
       String featureId = "featureId-420503887";
       Feature response =
           featureRegistryServiceClient.createFeatureAsync(parent, feature, featureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureOperationMetadata)>` |   
  
### createFeatureCallable()
    
    
    public final UnaryCallable<CreateFeatureRequest,Operation> createFeatureCallable()

Creates a new Feature in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureRequest request =
           CreateFeatureRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFeature(Feature.newBuilder().build())
               .setFeatureId("featureId-420503887")
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.createFeatureCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFeatureGroupAsync(@Nullable LocationName parent, FeatureGroup featureGroup, String featureGroupId)
    
    
    public final OperationFuture<FeatureGroup,CreateFeatureGroupOperationMetadata> createFeatureGroupAsync(@Nullable LocationName parent, FeatureGroup featureGroup, String featureGroupId)

Creates a new FeatureGroup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       FeatureGroup featureGroup = FeatureGroup.newBuilder().build();
       String featureGroupId = "featureGroupId-1768466396";
       FeatureGroup response =
           featureRegistryServiceClient
               .createFeatureGroupAsync(parent, featureGroup, featureGroupId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.LocationName`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup),[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureGroupOperationMetadata)>` |   
  
### createFeatureGroupAsync(CreateFeatureGroupRequest request)
    
    
    public final OperationFuture<FeatureGroup,CreateFeatureGroupOperationMetadata> createFeatureGroupAsync(CreateFeatureGroupRequest request)

Creates a new FeatureGroup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureGroupRequest request =
           CreateFeatureGroupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeatureGroup(FeatureGroup.newBuilder().build())
               .setFeatureGroupId("featureGroupId-1768466396")
               .build();
       FeatureGroup response = featureRegistryServiceClient.createFeatureGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup),[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureGroupOperationMetadata)>` |   
  
### createFeatureGroupAsync(String parent, FeatureGroup featureGroup, String featureGroupId)
    
    
    public final OperationFuture<FeatureGroup,CreateFeatureGroupOperationMetadata> createFeatureGroupAsync(String parent, FeatureGroup featureGroup, String featureGroupId)

Creates a new FeatureGroup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       FeatureGroup featureGroup = FeatureGroup.newBuilder().build();
       String featureGroupId = "featureGroupId-1768466396";
       FeatureGroup response =
           featureRegistryServiceClient
               .createFeatureGroupAsync(parent, featureGroup, featureGroupId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup),[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureGroupOperationMetadata)>` |   
  
### createFeatureGroupCallable()
    
    
    public final UnaryCallable<CreateFeatureGroupRequest,Operation> createFeatureGroupCallable()

Creates a new FeatureGroup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureGroupRequest request =
           CreateFeatureGroupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeatureGroup(FeatureGroup.newBuilder().build())
               .setFeatureGroupId("featureGroupId-1768466396")
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.createFeatureGroupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFeatureGroupOperationCallable()
    
    
    public final OperationCallable<CreateFeatureGroupRequest,FeatureGroup,CreateFeatureGroupOperationMetadata> createFeatureGroupOperationCallable()

Creates a new FeatureGroup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureGroupRequest request =
           CreateFeatureGroupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFeatureGroup(FeatureGroup.newBuilder().build())
               .setFeatureGroupId("featureGroupId-1768466396")
               .build();
       OperationFuture<FeatureGroup, CreateFeatureGroupOperationMetadata> future =
           featureRegistryServiceClient.createFeatureGroupOperationCallable().futureCall(request);
       // Do something.
       FeatureGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureGroupRequest),[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup),[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureGroupOperationMetadata)>` |   
  
### createFeatureMonitorAsync(@Nullable FeatureGroupName parent, FeatureMonitor featureMonitor, String featureMonitorId)
    
    
    public final OperationFuture<FeatureMonitor,CreateFeatureMonitorOperationMetadata> createFeatureMonitorAsync(@Nullable FeatureGroupName parent, FeatureMonitor featureMonitor, String featureMonitorId)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       FeatureMonitor featureMonitor = FeatureMonitor.newBuilder().build();
       String featureMonitorId = "featureMonitorId1191342527";
       FeatureMonitor response =
           featureRegistryServiceClient
               .createFeatureMonitorAsync(parent, featureMonitor, featureMonitorId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureGroupName`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor),[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorOperationMetadata)>` |   
  
### createFeatureMonitorAsync(CreateFeatureMonitorRequest request)
    
    
    public final OperationFuture<FeatureMonitor,CreateFeatureMonitorOperationMetadata> createFeatureMonitorAsync(CreateFeatureMonitorRequest request)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureMonitorRequest request =
           CreateFeatureMonitorRequest.newBuilder()
               .setParent(
                   FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setFeatureMonitor(FeatureMonitor.newBuilder().build())
               .setFeatureMonitorId("featureMonitorId1191342527")
               .build();
       FeatureMonitor response =
           featureRegistryServiceClient.createFeatureMonitorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor),[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorOperationMetadata)>` |   
  
### createFeatureMonitorAsync(String parent, FeatureMonitor featureMonitor, String featureMonitorId)
    
    
    public final OperationFuture<FeatureMonitor,CreateFeatureMonitorOperationMetadata> createFeatureMonitorAsync(String parent, FeatureMonitor featureMonitor, String featureMonitorId)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString();
       FeatureMonitor featureMonitor = FeatureMonitor.newBuilder().build();
       String featureMonitorId = "featureMonitorId1191342527";
       FeatureMonitor response =
           featureRegistryServiceClient
               .createFeatureMonitorAsync(parent, featureMonitor, featureMonitorId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor),[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorOperationMetadata)>` |   
  
### createFeatureMonitorCallable()
    
    
    public final UnaryCallable<CreateFeatureMonitorRequest,Operation> createFeatureMonitorCallable()

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureMonitorRequest request =
           CreateFeatureMonitorRequest.newBuilder()
               .setParent(
                   FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setFeatureMonitor(FeatureMonitor.newBuilder().build())
               .setFeatureMonitorId("featureMonitorId1191342527")
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.createFeatureMonitorCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFeatureMonitorJob(@Nullable FeatureMonitorName parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId)
    
    
    public final FeatureMonitorJob createFeatureMonitorJob(@Nullable FeatureMonitorName parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId)

Creates a new feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureMonitorName parent =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
       FeatureMonitorJob featureMonitorJob = FeatureMonitorJob.newBuilder().build();
       long featureMonitorJobId = 816328651;
       FeatureMonitorJob response =
           featureRegistryServiceClient.createFeatureMonitorJob(
               parent, featureMonitorJob, featureMonitorJobId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureMonitorName`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. Output only. System-generated ID for feature monitor job.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)` |   
  
### createFeatureMonitorJob(CreateFeatureMonitorJobRequest request)
    
    
    public final FeatureMonitorJob createFeatureMonitorJob(CreateFeatureMonitorJobRequest request)

Creates a new feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureMonitorJobRequest request =
           CreateFeatureMonitorJobRequest.newBuilder()
               .setParent(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .setFeatureMonitorJob(FeatureMonitorJob.newBuilder().build())
               .setFeatureMonitorJobId(816328651)
               .build();
       FeatureMonitorJob response = featureRegistryServiceClient.createFeatureMonitorJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)` |   
  
### createFeatureMonitorJob(String parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId)
    
    
    public final FeatureMonitorJob createFeatureMonitorJob(String parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId)

Creates a new feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
               .toString();
       FeatureMonitorJob featureMonitorJob = FeatureMonitorJob.newBuilder().build();
       long featureMonitorJobId = 816328651;
       FeatureMonitorJob response =
           featureRegistryServiceClient.createFeatureMonitorJob(
               parent, featureMonitorJob, featureMonitorJobId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. Output only. System-generated ID for feature monitor job.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)` |   
  
### createFeatureMonitorJobCallable()
    
    
    public final UnaryCallable<CreateFeatureMonitorJobRequest,FeatureMonitorJob> createFeatureMonitorJobCallable()

Creates a new feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureMonitorJobRequest request =
           CreateFeatureMonitorJobRequest.newBuilder()
               .setParent(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .setFeatureMonitorJob(FeatureMonitorJob.newBuilder().build())
               .setFeatureMonitorJobId(816328651)
               .build();
       ApiFuture<FeatureMonitorJob> future =
           featureRegistryServiceClient.createFeatureMonitorJobCallable().futureCall(request);
       // Do something.
       FeatureMonitorJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorJobRequest),[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)>` |   
  
### createFeatureMonitorOperationCallable()
    
    
    public final OperationCallable<CreateFeatureMonitorRequest,FeatureMonitor,CreateFeatureMonitorOperationMetadata> createFeatureMonitorOperationCallable()

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureMonitorRequest request =
           CreateFeatureMonitorRequest.newBuilder()
               .setParent(
                   FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setFeatureMonitor(FeatureMonitor.newBuilder().build())
               .setFeatureMonitorId("featureMonitorId1191342527")
               .build();
       OperationFuture<FeatureMonitor, CreateFeatureMonitorOperationMetadata> future =
           featureRegistryServiceClient.createFeatureMonitorOperationCallable().futureCall(request);
       // Do something.
       FeatureMonitor response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorRequest),[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor),[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorOperationMetadata)>` |   
  
### createFeatureOperationCallable()
    
    
    public final OperationCallable<CreateFeatureRequest,Feature,CreateFeatureOperationMetadata> createFeatureOperationCallable()

Creates a new Feature in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       CreateFeatureRequest request =
           CreateFeatureRequest.newBuilder()
               .setParent(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setFeature(Feature.newBuilder().build())
               .setFeatureId("featureId-420503887")
               .build();
       OperationFuture<Feature, CreateFeatureOperationMetadata> future =
           featureRegistryServiceClient.createFeatureOperationCallable().futureCall(request);
       // Do something.
       Feature response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureRequest),[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureOperationMetadata)>` |   
  
### deleteFeatureAsync(@Nullable FeatureName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureAsync(@Nullable FeatureName name)

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureName name =
           FeatureName.ofProjectLocationFeatureGroupFeatureName(
               "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE]");
       featureRegistryServiceClient.deleteFeatureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureName`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureAsync(DeleteFeatureRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureAsync(DeleteFeatureRequest request)

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureRequest request =
           DeleteFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeatureGroupFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE]")
                       .toString())
               .build();
       featureRegistryServiceClient.deleteFeatureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureAsync(String name)

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String name =
           FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                   "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
               .toString();
       featureRegistryServiceClient.deleteFeatureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureCallable()
    
    
    public final UnaryCallable<DeleteFeatureRequest,Operation> deleteFeatureCallable()

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureRequest request =
           DeleteFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeatureGroupFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.deleteFeatureCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeatureGroupAsync(@Nullable FeatureGroupName name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureGroupAsync(@Nullable FeatureGroupName name, boolean force)

Deletes a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName name = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       boolean force = true;
       featureRegistryServiceClient.deleteFeatureGroupAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureGroupName`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureGroupAsync(DeleteFeatureGroupRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureGroupAsync(DeleteFeatureGroupRequest request)

Deletes a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureGroupRequest request =
           DeleteFeatureGroupRequest.newBuilder()
               .setName(FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setForce(true)
               .build();
       featureRegistryServiceClient.deleteFeatureGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureGroupAsync(String name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureGroupAsync(String name, boolean force)

Deletes a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String name = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString();
       boolean force = true;
       featureRegistryServiceClient.deleteFeatureGroupAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureGroupCallable()
    
    
    public final UnaryCallable<DeleteFeatureGroupRequest,Operation> deleteFeatureGroupCallable()

Deletes a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureGroupRequest request =
           DeleteFeatureGroupRequest.newBuilder()
               .setName(FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.deleteFeatureGroupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeatureGroupOperationCallable()
    
    
    public final OperationCallable<DeleteFeatureGroupRequest,Empty,DeleteOperationMetadata> deleteFeatureGroupOperationCallable()

Deletes a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureGroupRequest request =
           DeleteFeatureGroupRequest.newBuilder()
               .setName(FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featureRegistryServiceClient.deleteFeatureGroupOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureMonitorAsync(@Nullable FeatureMonitorName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureMonitorAsync(@Nullable FeatureMonitorName name)

Deletes a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureMonitorName name =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
       featureRegistryServiceClient.deleteFeatureMonitorAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureMonitorName`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureMonitorAsync(DeleteFeatureMonitorRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureMonitorAsync(DeleteFeatureMonitorRequest request)

Deletes a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureMonitorRequest request =
           DeleteFeatureMonitorRequest.newBuilder()
               .setName(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .build();
       featureRegistryServiceClient.deleteFeatureMonitorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureMonitorAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteFeatureMonitorAsync(String name)

Deletes a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String name =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
               .toString();
       featureRegistryServiceClient.deleteFeatureMonitorAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureMonitorCallable()
    
    
    public final UnaryCallable<DeleteFeatureMonitorRequest,Operation> deleteFeatureMonitorCallable()

Deletes a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureMonitorRequest request =
           DeleteFeatureMonitorRequest.newBuilder()
               .setName(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.deleteFeatureMonitorCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureMonitorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFeatureMonitorOperationCallable()
    
    
    public final OperationCallable<DeleteFeatureMonitorRequest,Empty,DeleteOperationMetadata> deleteFeatureMonitorOperationCallable()

Deletes a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureMonitorRequest request =
           DeleteFeatureMonitorRequest.newBuilder()
               .setName(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featureRegistryServiceClient.deleteFeatureMonitorOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureMonitorRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### deleteFeatureOperationCallable()
    
    
    public final OperationCallable<DeleteFeatureRequest,Empty,DeleteOperationMetadata> deleteFeatureOperationCallable()

Deletes a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       DeleteFeatureRequest request =
           DeleteFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeatureGroupFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           featureRegistryServiceClient.deleteFeatureOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)>` |   
  
### getFeature(@Nullable FeatureName name)
    
    
    public final Feature getFeature(@Nullable FeatureName name)

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureName name =
           FeatureName.ofProjectLocationFeatureGroupFeatureName(
               "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE]");
       Feature response = featureRegistryServiceClient.getFeature(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureName`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)` |   
  
### getFeature(GetFeatureRequest request)
    
    
    public final Feature getFeature(GetFeatureRequest request)

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureRequest request =
           GetFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeatureGroupFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE]")
                       .toString())
               .setFeatureStatsAndAnomalySpec(FeatureStatsAndAnomalySpec.newBuilder().build())
               .build();
       Feature response = featureRegistryServiceClient.getFeature(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)` |   
  
### getFeature(String name)
    
    
    public final Feature getFeature(String name)

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String name =
           FeatureName.ofProjectLocationFeaturestoreEntityTypeFeatureName(
                   "[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]")
               .toString();
       Feature response = featureRegistryServiceClient.getFeature(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)` |   
  
### getFeatureCallable()
    
    
    public final UnaryCallable<GetFeatureRequest,Feature> getFeatureCallable()

Gets details of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureRequest request =
           GetFeatureRequest.newBuilder()
               .setName(
                   FeatureName.ofProjectLocationFeatureGroupFeatureName(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE]")
                       .toString())
               .setFeatureStatsAndAnomalySpec(FeatureStatsAndAnomalySpec.newBuilder().build())
               .build();
       ApiFuture<Feature> future =
           featureRegistryServiceClient.getFeatureCallable().futureCall(request);
       // Do something.
       Feature response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureRequest),[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)>` |   
  
### getFeatureGroup(@Nullable FeatureGroupName name)
    
    
    public final FeatureGroup getFeatureGroup(@Nullable FeatureGroupName name)

Gets details of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName name = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       FeatureGroup response = featureRegistryServiceClient.getFeatureGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureGroupName`  
Required. The name of the FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup)` |   
  
### getFeatureGroup(GetFeatureGroupRequest request)
    
    
    public final FeatureGroup getFeatureGroup(GetFeatureGroupRequest request)

Gets details of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureGroupRequest request =
           GetFeatureGroupRequest.newBuilder()
               .setName(FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .build();
       FeatureGroup response = featureRegistryServiceClient.getFeatureGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup)` |   
  
### getFeatureGroup(String name)
    
    
    public final FeatureGroup getFeatureGroup(String name)

Gets details of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String name = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString();
       FeatureGroup response = featureRegistryServiceClient.getFeatureGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup)` |   
  
### getFeatureGroupCallable()
    
    
    public final UnaryCallable<GetFeatureGroupRequest,FeatureGroup> getFeatureGroupCallable()

Gets details of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureGroupRequest request =
           GetFeatureGroupRequest.newBuilder()
               .setName(FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .build();
       ApiFuture<FeatureGroup> future =
           featureRegistryServiceClient.getFeatureGroupCallable().futureCall(request);
       // Do something.
       FeatureGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureGroupRequest),[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup)>` |   
  
### getFeatureMonitor(@Nullable FeatureMonitorName name)
    
    
    public final FeatureMonitor getFeatureMonitor(@Nullable FeatureMonitorName name)

Gets details of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureMonitorName name =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
       FeatureMonitor response = featureRegistryServiceClient.getFeatureMonitor(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureMonitorName`  
Required. The name of the FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor)` |   
  
### getFeatureMonitor(GetFeatureMonitorRequest request)
    
    
    public final FeatureMonitor getFeatureMonitor(GetFeatureMonitorRequest request)

Gets details of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureMonitorRequest request =
           GetFeatureMonitorRequest.newBuilder()
               .setName(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .build();
       FeatureMonitor response = featureRegistryServiceClient.getFeatureMonitor(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor)` |   
  
### getFeatureMonitor(String name)
    
    
    public final FeatureMonitor getFeatureMonitor(String name)

Gets details of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String name =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
               .toString();
       FeatureMonitor response = featureRegistryServiceClient.getFeatureMonitor(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor)` |   
  
### getFeatureMonitorCallable()
    
    
    public final UnaryCallable<GetFeatureMonitorRequest,FeatureMonitor> getFeatureMonitorCallable()

Gets details of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureMonitorRequest request =
           GetFeatureMonitorRequest.newBuilder()
               .setName(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .build();
       ApiFuture<FeatureMonitor> future =
           featureRegistryServiceClient.getFeatureMonitorCallable().futureCall(request);
       // Do something.
       FeatureMonitor response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureMonitorRequest),[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor)>` |   
  
### getFeatureMonitorJob(@Nullable FeatureMonitorJobName name)
    
    
    public final FeatureMonitorJob getFeatureMonitorJob(@Nullable FeatureMonitorJobName name)

Get a feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureMonitorJobName name =
           FeatureMonitorJobName.of(
               "[PROJECT]",
               "[LOCATION]",
               "[FEATURE_GROUP]",
               "[FEATURE_MONITOR]",
               "[FEATURE_MONITOR_JOB]");
       FeatureMonitorJob response = featureRegistryServiceClient.getFeatureMonitorJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureMonitorJobName`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)` |   
  
### getFeatureMonitorJob(GetFeatureMonitorJobRequest request)
    
    
    public final FeatureMonitorJob getFeatureMonitorJob(GetFeatureMonitorJobRequest request)

Get a feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureMonitorJobRequest request =
           GetFeatureMonitorJobRequest.newBuilder()
               .setName(
                   FeatureMonitorJobName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[FEATURE_GROUP]",
                           "[FEATURE_MONITOR]",
                           "[FEATURE_MONITOR_JOB]")
                       .toString())
               .build();
       FeatureMonitorJob response = featureRegistryServiceClient.getFeatureMonitorJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)` |   
  
### getFeatureMonitorJob(String name)
    
    
    public final FeatureMonitorJob getFeatureMonitorJob(String name)

Get a feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String name =
           FeatureMonitorJobName.of(
                   "[PROJECT]",
                   "[LOCATION]",
                   "[FEATURE_GROUP]",
                   "[FEATURE_MONITOR]",
                   "[FEATURE_MONITOR_JOB]")
               .toString();
       FeatureMonitorJob response = featureRegistryServiceClient.getFeatureMonitorJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)` |   
  
### getFeatureMonitorJobCallable()
    
    
    public final UnaryCallable<GetFeatureMonitorJobRequest,FeatureMonitorJob> getFeatureMonitorJobCallable()

Get a feature monitor job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetFeatureMonitorJobRequest request =
           GetFeatureMonitorJobRequest.newBuilder()
               .setName(
                   FeatureMonitorJobName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[FEATURE_GROUP]",
                           "[FEATURE_MONITOR]",
                           "[FEATURE_MONITOR_JOB]")
                       .toString())
               .build();
       ApiFuture<FeatureMonitorJob> future =
           featureRegistryServiceClient.getFeatureMonitorJobCallable().futureCall(request);
       // Do something.
       FeatureMonitorJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureMonitorJobRequest),[FeatureMonitorJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitorJob)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = featureRegistryServiceClient.getIamPolicy(request);
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
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           featureRegistryServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = featureRegistryServiceClient.getLocation(request);
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
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           featureRegistryServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable FeatureRegistryServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceSettings` |   
  
### getStub()
    
    
    public FeatureRegistryServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.stub.FeatureRegistryServiceStub)` |   
  
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
  
### listFeatureGroups(@Nullable LocationName parent)
    
    
    public final FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse listFeatureGroups(@Nullable LocationName parent)

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (FeatureGroup element :
           featureRegistryServiceClient.listFeatureGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.LocationName`  
Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse)` |   
  
### listFeatureGroups(ListFeatureGroupsRequest request)
    
    
    public final FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse listFeatureGroups(ListFeatureGroupsRequest request)

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureGroupsRequest request =
           ListFeatureGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (FeatureGroup element :
           featureRegistryServiceClient.listFeatureGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeatureGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse)` |   
  
### listFeatureGroups(String parent)
    
    
    public final FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse listFeatureGroups(String parent)

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (FeatureGroup element :
           featureRegistryServiceClient.listFeatureGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse)` |   
  
### listFeatureGroupsCallable()
    
    
    public final UnaryCallable<ListFeatureGroupsRequest,ListFeatureGroupsResponse> listFeatureGroupsCallable()

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureGroupsRequest request =
           ListFeatureGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFeatureGroupsResponse response =
             featureRegistryServiceClient.listFeatureGroupsCallable().call(request);
         for (FeatureGroup element : response.getFeatureGroupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureGroupsRequest),[ListFeatureGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureGroupsResponse)>` |   
  
### listFeatureGroupsPagedCallable()
    
    
    public final UnaryCallable<ListFeatureGroupsRequest,FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse> listFeatureGroupsPagedCallable()

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureGroupsRequest request =
           ListFeatureGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<FeatureGroup> future =
           featureRegistryServiceClient.listFeatureGroupsPagedCallable().futureCall(request);
       // Do something.
       for (FeatureGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureGroupsRequest),[ListFeatureGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureGroupsPagedResponse)>` |   
  
### listFeatureMonitorJobs(@Nullable FeatureMonitorName parent)
    
    
    public final FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse listFeatureMonitorJobs(@Nullable FeatureMonitorName parent)

List feature monitor jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureMonitorName parent =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
       for (FeatureMonitorJob element :
           featureRegistryServiceClient.listFeatureMonitorJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureMonitorName`  
Required. The resource name of the FeatureMonitor to list FeatureMonitorJobs. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse)` |   
  
### listFeatureMonitorJobs(ListFeatureMonitorJobsRequest request)
    
    
    public final FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse listFeatureMonitorJobs(ListFeatureMonitorJobsRequest request)

List feature monitor jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureMonitorJobsRequest request =
           ListFeatureMonitorJobsRequest.newBuilder()
               .setParent(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (FeatureMonitorJob element :
           featureRegistryServiceClient.listFeatureMonitorJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse)` |   
  
### listFeatureMonitorJobs(String parent)
    
    
    public final FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse listFeatureMonitorJobs(String parent)

List feature monitor jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent =
           FeatureMonitorName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
               .toString();
       for (FeatureMonitorJob element :
           featureRegistryServiceClient.listFeatureMonitorJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the FeatureMonitor to list FeatureMonitorJobs. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse)` |   
  
### listFeatureMonitorJobsCallable()
    
    
    public final UnaryCallable<ListFeatureMonitorJobsRequest,ListFeatureMonitorJobsResponse> listFeatureMonitorJobsCallable()

List feature monitor jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureMonitorJobsRequest request =
           ListFeatureMonitorJobsRequest.newBuilder()
               .setParent(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFeatureMonitorJobsResponse response =
             featureRegistryServiceClient.listFeatureMonitorJobsCallable().call(request);
         for (FeatureMonitorJob element : response.getFeatureMonitorJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorJobsRequest),[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorJobsResponse)>` |   
  
### listFeatureMonitorJobsPagedCallable()
    
    
    public final UnaryCallable<ListFeatureMonitorJobsRequest,FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse> listFeatureMonitorJobsPagedCallable()

List feature monitor jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureMonitorJobsRequest request =
           ListFeatureMonitorJobsRequest.newBuilder()
               .setParent(
                   FeatureMonitorName.of(
                           "[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<FeatureMonitorJob> future =
           featureRegistryServiceClient.listFeatureMonitorJobsPagedCallable().futureCall(request);
       // Do something.
       for (FeatureMonitorJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorJobsRequest),[ListFeatureMonitorJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorJobsPagedResponse)>` |   
  
### listFeatureMonitors(@Nullable FeatureGroupName parent)
    
    
    public final FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse listFeatureMonitors(@Nullable FeatureGroupName parent)

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       for (FeatureMonitor element :
           featureRegistryServiceClient.listFeatureMonitors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureGroupName`  
Required. The resource name of the FeatureGroup to list FeatureMonitors. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse)` |   
  
### listFeatureMonitors(ListFeatureMonitorsRequest request)
    
    
    public final FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse listFeatureMonitors(ListFeatureMonitorsRequest request)

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureMonitorsRequest request =
           ListFeatureMonitorsRequest.newBuilder()
               .setParent(
                   FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (FeatureMonitor element :
           featureRegistryServiceClient.listFeatureMonitors(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse)` |   
  
### listFeatureMonitors(String parent)
    
    
    public final FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse listFeatureMonitors(String parent)

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString();
       for (FeatureMonitor element :
           featureRegistryServiceClient.listFeatureMonitors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the FeatureGroup to list FeatureMonitors. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse)` |   
  
### listFeatureMonitorsCallable()
    
    
    public final UnaryCallable<ListFeatureMonitorsRequest,ListFeatureMonitorsResponse> listFeatureMonitorsCallable()

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureMonitorsRequest request =
           ListFeatureMonitorsRequest.newBuilder()
               .setParent(
                   FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFeatureMonitorsResponse response =
             featureRegistryServiceClient.listFeatureMonitorsCallable().call(request);
         for (FeatureMonitor element : response.getFeatureMonitorsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureMonitorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorsRequest),[ListFeatureMonitorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorsResponse)>` |   
  
### listFeatureMonitorsPagedCallable()
    
    
    public final UnaryCallable<ListFeatureMonitorsRequest,FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse> listFeatureMonitorsPagedCallable()

Lists FeatureGroups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListFeatureMonitorsRequest request =
           ListFeatureMonitorsRequest.newBuilder()
               .setParent(
                   FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<FeatureMonitor> future =
           featureRegistryServiceClient.listFeatureMonitorsPagedCallable().futureCall(request);
       // Do something.
       for (FeatureMonitor element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeatureMonitorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureMonitorsRequest),[ListFeatureMonitorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeatureMonitorsPagedResponse)>` |   
  
### listFeatures(@Nullable EntityTypeName parent)
    
    
    public final FeatureRegistryServiceClient.ListFeaturesPagedResponse listFeatures(@Nullable EntityTypeName parent)

Lists Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       EntityTypeName parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       for (Feature element : featureRegistryServiceClient.listFeatures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.EntityTypeName`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeatures(@Nullable FeatureGroupName parent)
    
    
    public final FeatureRegistryServiceClient.ListFeaturesPagedResponse listFeatures(@Nullable FeatureGroupName parent)

Lists Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroupName parent = FeatureGroupName.of("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
       for (Feature element : featureRegistryServiceClient.listFeatures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.FeatureGroupName`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeatures(ListFeaturesRequest request)
    
    
    public final FeatureRegistryServiceClient.ListFeaturesPagedResponse listFeatures(ListFeaturesRequest request)

Lists Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
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
       for (Feature element : featureRegistryServiceClient.listFeatures(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeatures(String parent)
    
    
    public final FeatureRegistryServiceClient.ListFeaturesPagedResponse listFeatures(String parent)

Lists Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       String parent =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       for (Feature element : featureRegistryServiceClient.listFeatures(parent).iterateAll()) {
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
`[FeatureRegistryServiceClient.ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeaturesPagedResponse)` |   
  
### listFeaturesCallable()
    
    
    public final UnaryCallable<ListFeaturesRequest,ListFeaturesResponse> listFeaturesCallable()

Lists Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
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
             featureRegistryServiceClient.listFeaturesCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeaturesRequest),[ListFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeaturesResponse)>` |   
  
### listFeaturesPagedCallable()
    
    
    public final UnaryCallable<ListFeaturesRequest,FeatureRegistryServiceClient.ListFeaturesPagedResponse> listFeaturesPagedCallable()

Lists Features in a given FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
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
           featureRegistryServiceClient.listFeaturesPagedCallable().futureCall(request);
       // Do something.
       for (Feature element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeaturesRequest),[ListFeaturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListFeaturesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final FeatureRegistryServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : featureRegistryServiceClient.listLocations(request).iterateAll()) {
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
`[FeatureRegistryServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             featureRegistryServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,FeatureRegistryServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           featureRegistryServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureRegistryServiceClient.ListLocationsPagedResponse)>` |   
  
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
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = featureRegistryServiceClient.setIamPolicy(request);
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
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
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
           featureRegistryServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           featureRegistryServiceClient.testIamPermissions(request);
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
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           featureRegistryServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateFeatureAsync(Feature feature, FieldMask updateMask)
    
    
    public final OperationFuture<Feature,UpdateFeatureOperationMetadata> updateFeatureAsync(Feature feature, FieldMask updateMask)

Updates the parameters of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       Feature feature = Feature.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Feature response = featureRegistryServiceClient.updateFeatureAsync(feature, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`feature` | `[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature)`  
Required. The Feature's `name` field is used to identify the Feature to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Features resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `description` * `labels` * `disable_monitoring` (Not supported for FeatureRegistryService Feature) * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureOperationMetadata)>` |   
  
### updateFeatureAsync(UpdateFeatureRequest request)
    
    
    public final OperationFuture<Feature,UpdateFeatureOperationMetadata> updateFeatureAsync(UpdateFeatureRequest request)

Updates the parameters of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureRequest request =
           UpdateFeatureRequest.newBuilder()
               .setFeature(Feature.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Feature response = featureRegistryServiceClient.updateFeatureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureOperationMetadata)>` |   
  
### updateFeatureCallable()
    
    
    public final UnaryCallable<UpdateFeatureRequest,Operation> updateFeatureCallable()

Updates the parameters of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureRequest request =
           UpdateFeatureRequest.newBuilder()
               .setFeature(Feature.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.updateFeatureCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFeatureGroupAsync(FeatureGroup featureGroup, FieldMask updateMask)
    
    
    public final OperationFuture<FeatureGroup,UpdateFeatureGroupOperationMetadata> updateFeatureGroupAsync(FeatureGroup featureGroup, FieldMask updateMask)

Updates the parameters of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureGroup featureGroup = FeatureGroup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       FeatureGroup response =
           featureRegistryServiceClient.updateFeatureGroupAsync(featureGroup, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup)`  
Required. The FeatureGroup's `name` field is used to identify the FeatureGroup to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureGroup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `labels` * `description` * `big_query` * `big_query.entity_id_columns`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup),[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupOperationMetadata)>` |   
  
### updateFeatureGroupAsync(UpdateFeatureGroupRequest request)
    
    
    public final OperationFuture<FeatureGroup,UpdateFeatureGroupOperationMetadata> updateFeatureGroupAsync(UpdateFeatureGroupRequest request)

Updates the parameters of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureGroupRequest request =
           UpdateFeatureGroupRequest.newBuilder()
               .setFeatureGroup(FeatureGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       FeatureGroup response = featureRegistryServiceClient.updateFeatureGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup),[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupOperationMetadata)>` |   
  
### updateFeatureGroupCallable()
    
    
    public final UnaryCallable<UpdateFeatureGroupRequest,Operation> updateFeatureGroupCallable()

Updates the parameters of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureGroupRequest request =
           UpdateFeatureGroupRequest.newBuilder()
               .setFeatureGroup(FeatureGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.updateFeatureGroupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFeatureGroupOperationCallable()
    
    
    public final OperationCallable<UpdateFeatureGroupRequest,FeatureGroup,UpdateFeatureGroupOperationMetadata> updateFeatureGroupOperationCallable()

Updates the parameters of a single FeatureGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureGroupRequest request =
           UpdateFeatureGroupRequest.newBuilder()
               .setFeatureGroup(FeatureGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<FeatureGroup, UpdateFeatureGroupOperationMetadata> future =
           featureRegistryServiceClient.updateFeatureGroupOperationCallable().futureCall(request);
       // Do something.
       FeatureGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFeatureGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupRequest),[FeatureGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureGroup),[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupOperationMetadata)>` |   
  
### updateFeatureMonitorAsync(FeatureMonitor featureMonitor, FieldMask updateMask)
    
    
    public final OperationFuture<FeatureMonitor,UpdateFeatureMonitorOperationMetadata> updateFeatureMonitorAsync(FeatureMonitor featureMonitor, FieldMask updateMask)

Updates the parameters of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       FeatureMonitor featureMonitor = FeatureMonitor.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       FeatureMonitor response =
           featureRegistryServiceClient.updateFeatureMonitorAsync(featureMonitor, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor)`  
Required. The FeatureMonitor's `name` field is used to identify the FeatureMonitor to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the FeatureMonitor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `labels`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor),[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorOperationMetadata)>` |   
  
### updateFeatureMonitorAsync(UpdateFeatureMonitorRequest request)
    
    
    public final OperationFuture<FeatureMonitor,UpdateFeatureMonitorOperationMetadata> updateFeatureMonitorAsync(UpdateFeatureMonitorRequest request)

Updates the parameters of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureMonitorRequest request =
           UpdateFeatureMonitorRequest.newBuilder()
               .setFeatureMonitor(FeatureMonitor.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       FeatureMonitor response =
           featureRegistryServiceClient.updateFeatureMonitorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor),[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorOperationMetadata)>` |   
  
### updateFeatureMonitorCallable()
    
    
    public final UnaryCallable<UpdateFeatureMonitorRequest,Operation> updateFeatureMonitorCallable()

Updates the parameters of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureMonitorRequest request =
           UpdateFeatureMonitorRequest.newBuilder()
               .setFeatureMonitor(FeatureMonitor.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           featureRegistryServiceClient.updateFeatureMonitorCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFeatureMonitorOperationCallable()
    
    
    public final OperationCallable<UpdateFeatureMonitorRequest,FeatureMonitor,UpdateFeatureMonitorOperationMetadata> updateFeatureMonitorOperationCallable()

Updates the parameters of a single FeatureMonitor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureMonitorRequest request =
           UpdateFeatureMonitorRequest.newBuilder()
               .setFeatureMonitor(FeatureMonitor.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> future =
           featureRegistryServiceClient.updateFeatureMonitorOperationCallable().futureCall(request);
       // Do something.
       FeatureMonitor response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorRequest),[FeatureMonitor](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureMonitor),[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorOperationMetadata)>` |   
  
### updateFeatureOperationCallable()
    
    
    public final OperationCallable<UpdateFeatureRequest,Feature,UpdateFeatureOperationMetadata> updateFeatureOperationCallable()

Updates the parameters of a single Feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeatureRegistryServiceClient featureRegistryServiceClient =
         FeatureRegistryServiceClient.create()) {
       UpdateFeatureRequest request =
           UpdateFeatureRequest.newBuilder()
               .setFeature(Feature.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Feature, UpdateFeatureOperationMetadata> future =
           featureRegistryServiceClient.updateFeatureOperationCallable().futureCall(request);
       // Do something.
       Feature response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureRequest),[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Feature),[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
