---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient
title: Class MetadataServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:20.161572+00:00
---

# Class MetadataServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MetadataServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/MetadataServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for reading and writing metadata entries.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName name = MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       MetadataStore response = metadataServiceClient.getMetadataStore(name);
     }
     

Note: close() needs to be called on the MetadataServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateMetadataStore |  Initializes a MetadataStore, including allocation of resources. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMetadataStoreAsync(CreateMetadataStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMetadataStoreAsync(LocationName parent, MetadataStore metadataStore, String metadataStoreId) 
  * createMetadataStoreAsync(String parent, MetadataStore metadataStore, String metadataStoreId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMetadataStoreOperationCallable() 
  * createMetadataStoreCallable() 

  
GetMetadataStore |  Retrieves a specific MetadataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMetadataStore(GetMetadataStoreRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMetadataStore(MetadataStoreName name) 
  * getMetadataStore(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMetadataStoreCallable() 

  
ListMetadataStores |  Lists MetadataStores for a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMetadataStores(ListMetadataStoresRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMetadataStores(LocationName parent) 
  * listMetadataStores(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMetadataStoresPagedCallable() 
  * listMetadataStoresCallable() 

  
DeleteMetadataStore |  Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMetadataStoreAsync(DeleteMetadataStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteMetadataStoreAsync(MetadataStoreName name) 
  * deleteMetadataStoreAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMetadataStoreOperationCallable() 
  * deleteMetadataStoreCallable() 

  
CreateArtifact |  Creates an Artifact associated with a MetadataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createArtifact(CreateArtifactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createArtifact(MetadataStoreName parent, Artifact artifact, String artifactId) 
  * createArtifact(String parent, Artifact artifact, String artifactId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createArtifactCallable() 

  
GetArtifact |  Retrieves a specific Artifact. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getArtifact(GetArtifactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getArtifact(ArtifactName name) 
  * getArtifact(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getArtifactCallable() 

  
ListArtifacts |  Lists Artifacts in the MetadataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listArtifacts(ListArtifactsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listArtifacts(MetadataStoreName parent) 
  * listArtifacts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listArtifactsPagedCallable() 
  * listArtifactsCallable() 

  
UpdateArtifact |  Updates a stored Artifact. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateArtifact(UpdateArtifactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateArtifact(Artifact artifact, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateArtifactCallable() 

  
DeleteArtifact |  Deletes an Artifact. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteArtifactAsync(DeleteArtifactRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteArtifactAsync(ArtifactName name) 
  * deleteArtifactAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteArtifactOperationCallable() 
  * deleteArtifactCallable() 

  
PurgeArtifacts |  Purges Artifacts. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeArtifactsAsync(PurgeArtifactsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * purgeArtifactsAsync(MetadataStoreName parent) 
  * purgeArtifactsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeArtifactsOperationCallable() 
  * purgeArtifactsCallable() 

  
CreateContext |  Creates a Context associated with a MetadataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createContext(CreateContextRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createContext(MetadataStoreName parent, Context context, String contextId) 
  * createContext(String parent, Context context, String contextId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createContextCallable() 

  
GetContext |  Retrieves a specific Context. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getContext(GetContextRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getContext(ContextName name) 
  * getContext(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getContextCallable() 

  
ListContexts |  Lists Contexts on the MetadataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listContexts(ListContextsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listContexts(MetadataStoreName parent) 
  * listContexts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listContextsPagedCallable() 
  * listContextsCallable() 

  
UpdateContext |  Updates a stored Context. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateContext(UpdateContextRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateContext(Context context, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateContextCallable() 

  
DeleteContext |  Deletes a stored Context. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteContextAsync(DeleteContextRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteContextAsync(ContextName name) 
  * deleteContextAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteContextOperationCallable() 
  * deleteContextCallable() 

  
PurgeContexts |  Purges Contexts. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeContextsAsync(PurgeContextsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * purgeContextsAsync(MetadataStoreName parent) 
  * purgeContextsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeContextsOperationCallable() 
  * purgeContextsCallable() 

  
AddContextArtifactsAndExecutions |  Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addContextArtifactsAndExecutions(AddContextArtifactsAndExecutionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * addContextArtifactsAndExecutions(ContextName context, List<String> artifacts, List<String> executions) 
  * addContextArtifactsAndExecutions(String context, List<String> artifacts, List<String> executions) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addContextArtifactsAndExecutionsCallable() 

  
AddContextChildren |  Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addContextChildren(AddContextChildrenRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * addContextChildren(ContextName context, List<String> childContexts) 
  * addContextChildren(String context, List<String> childContexts) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addContextChildrenCallable() 

  
RemoveContextChildren |  Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeContextChildren(RemoveContextChildrenRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * removeContextChildren(ContextName context, List<String> childContexts) 
  * removeContextChildren(String context, List<String> childContexts) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeContextChildrenCallable() 

  
QueryContextLineageSubgraph |  Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryContextLineageSubgraph(QueryContextLineageSubgraphRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryContextLineageSubgraph(ContextName context) 
  * queryContextLineageSubgraph(String context) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryContextLineageSubgraphCallable() 

  
CreateExecution |  Creates an Execution associated with a MetadataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExecution(CreateExecutionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createExecution(MetadataStoreName parent, Execution execution, String executionId) 
  * createExecution(String parent, Execution execution, String executionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExecutionCallable() 

  
GetExecution |  Retrieves a specific Execution. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExecution(GetExecutionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExecution(ExecutionName name) 
  * getExecution(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExecutionCallable() 

  
ListExecutions |  Lists Executions in the MetadataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExecutions(ListExecutionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExecutions(MetadataStoreName parent) 
  * listExecutions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExecutionsPagedCallable() 
  * listExecutionsCallable() 

  
UpdateExecution |  Updates a stored Execution. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExecution(UpdateExecutionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateExecution(Execution execution, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExecutionCallable() 

  
DeleteExecution |  Deletes an Execution. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExecutionAsync(DeleteExecutionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteExecutionAsync(ExecutionName name) 
  * deleteExecutionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExecutionOperationCallable() 
  * deleteExecutionCallable() 

  
PurgeExecutions |  Purges Executions. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeExecutionsAsync(PurgeExecutionsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * purgeExecutionsAsync(MetadataStoreName parent) 
  * purgeExecutionsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeExecutionsOperationCallable() 
  * purgeExecutionsCallable() 

  
AddExecutionEvents |  Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addExecutionEvents(AddExecutionEventsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * addExecutionEvents(ExecutionName execution, List<Event> events) 
  * addExecutionEvents(String execution, List<Event> events) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addExecutionEventsCallable() 

  
QueryExecutionInputsAndOutputs |  Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryExecutionInputsAndOutputs(QueryExecutionInputsAndOutputsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryExecutionInputsAndOutputs(ExecutionName execution) 
  * queryExecutionInputsAndOutputs(String execution) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryExecutionInputsAndOutputsCallable() 

  
CreateMetadataSchema |  Creates a MetadataSchema. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMetadataSchema(CreateMetadataSchemaRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createMetadataSchema(MetadataStoreName parent, MetadataSchema metadataSchema, String metadataSchemaId) 
  * createMetadataSchema(String parent, MetadataSchema metadataSchema, String metadataSchemaId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMetadataSchemaCallable() 

  
GetMetadataSchema |  Retrieves a specific MetadataSchema. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMetadataSchema(GetMetadataSchemaRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMetadataSchema(MetadataSchemaName name) 
  * getMetadataSchema(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMetadataSchemaCallable() 

  
ListMetadataSchemas |  Lists MetadataSchemas. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMetadataSchemas(ListMetadataSchemasRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMetadataSchemas(MetadataStoreName parent) 
  * listMetadataSchemas(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMetadataSchemasPagedCallable() 
  * listMetadataSchemasCallable() 

  
QueryArtifactLineageSubgraph |  Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryArtifactLineageSubgraph(QueryArtifactLineageSubgraphRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryArtifactLineageSubgraph(ArtifactName artifact) 
  * queryArtifactLineageSubgraph(String artifact) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryArtifactLineageSubgraphCallable() 

  
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

This class can be customized by passing in a custom instance of MetadataServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MetadataServiceSettings metadataServiceSettings =
         MetadataServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MetadataServiceClient metadataServiceClient =
         MetadataServiceClient.create(metadataServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MetadataServiceSettings metadataServiceSettings =
         MetadataServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     MetadataServiceClient metadataServiceClient =
         MetadataServiceClient.create(metadataServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MetadataServiceClient

## Static Methods 

### create()
    
    
    public static final MetadataServiceClient create()

Constructs an instance of MetadataServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MetadataServiceSettings settings)
    
    
    public static final MetadataServiceClient create(MetadataServiceSettings settings)

Constructs an instance of MetadataServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MetadataServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MetadataServiceStub stub)
    
    
    public static final MetadataServiceClient create(MetadataServiceStub stub)

Constructs an instance of MetadataServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(MetadataServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MetadataServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.MetadataServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient)` |   
  
## Constructors 

### MetadataServiceClient(MetadataServiceSettings settings)
    
    
    protected MetadataServiceClient(MetadataServiceSettings settings)

Constructs an instance of MetadataServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MetadataServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceSettings)`  
  
  
### MetadataServiceClient(MetadataServiceStub stub)
    
    
    protected MetadataServiceClient(MetadataServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MetadataServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.MetadataServiceStub)`  
  
  
## Methods 

### addContextArtifactsAndExecutions(@Nullable ContextName context, List<String> artifacts, List<String> executions)
    
    
    public final AddContextArtifactsAndExecutionsResponse addContextArtifactsAndExecutions(@Nullable ContextName context, List<String> artifacts, List<String> executions)

Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ContextName context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]");
       List<String> artifacts = new ArrayList<>();
       List<String> executions = new ArrayList<>();
       AddContextArtifactsAndExecutionsResponse response =
           metadataServiceClient.addContextArtifactsAndExecutions(context, artifacts, executions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ContextName`  
Required. The resource name of the Context that the Artifacts and Executions belong to. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
`artifacts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the Artifacts to attribute to the Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`  
`executions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the Executions to associate with the Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsResponse)` |   
  
### addContextArtifactsAndExecutions(AddContextArtifactsAndExecutionsRequest request)
    
    
    public final AddContextArtifactsAndExecutionsResponse addContextArtifactsAndExecutions(AddContextArtifactsAndExecutionsRequest request)

Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       AddContextArtifactsAndExecutionsRequest request =
           AddContextArtifactsAndExecutionsRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .addAllArtifacts(new ArrayList<String>())
               .addAllExecutions(new ArrayList<String>())
               .build();
       AddContextArtifactsAndExecutionsResponse response =
           metadataServiceClient.addContextArtifactsAndExecutions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsResponse)` |   
  
### addContextArtifactsAndExecutions(String context, List<String> artifacts, List<String> executions)
    
    
    public final AddContextArtifactsAndExecutionsResponse addContextArtifactsAndExecutions(String context, List<String> artifacts, List<String> executions)

Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]").toString();
       List<String> artifacts = new ArrayList<>();
       List<String> executions = new ArrayList<>();
       AddContextArtifactsAndExecutionsResponse response =
           metadataServiceClient.addContextArtifactsAndExecutions(context, artifacts, executions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`context` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Context that the Artifacts and Executions belong to. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
`artifacts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the Artifacts to attribute to the Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`  
`executions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the Executions to associate with the Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsResponse)` |   
  
### addContextArtifactsAndExecutionsCallable()
    
    
    public final UnaryCallable<AddContextArtifactsAndExecutionsRequest,AddContextArtifactsAndExecutionsResponse> addContextArtifactsAndExecutionsCallable()

Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       AddContextArtifactsAndExecutionsRequest request =
           AddContextArtifactsAndExecutionsRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .addAllArtifacts(new ArrayList<String>())
               .addAllExecutions(new ArrayList<String>())
               .build();
       ApiFuture<AddContextArtifactsAndExecutionsResponse> future =
           metadataServiceClient.addContextArtifactsAndExecutionsCallable().futureCall(request);
       // Do something.
       AddContextArtifactsAndExecutionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsRequest),[AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsResponse)>` |   
  
### addContextChildren(@Nullable ContextName context, List<String> childContexts)
    
    
    public final AddContextChildrenResponse addContextChildren(@Nullable ContextName context, List<String> childContexts)

Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ContextName context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]");
       List<String> childContexts = new ArrayList<>();
       AddContextChildrenResponse response =
           metadataServiceClient.addContextChildren(context, childContexts);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ContextName`  
Required. The resource name of the parent Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
`childContexts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the child Contexts.  
**Returns**  
---  
**Type** | **Description**  
`[AddContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenResponse)` |   
  
### addContextChildren(AddContextChildrenRequest request)
    
    
    public final AddContextChildrenResponse addContextChildren(AddContextChildrenRequest request)

Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       AddContextChildrenRequest request =
           AddContextChildrenRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .addAllChildContexts(new ArrayList<String>())
               .build();
       AddContextChildrenResponse response = metadataServiceClient.addContextChildren(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AddContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenResponse)` |   
  
### addContextChildren(String context, List<String> childContexts)
    
    
    public final AddContextChildrenResponse addContextChildren(String context, List<String> childContexts)

Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]").toString();
       List<String> childContexts = new ArrayList<>();
       AddContextChildrenResponse response =
           metadataServiceClient.addContextChildren(context, childContexts);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`context` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
`childContexts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the child Contexts.  
**Returns**  
---  
**Type** | **Description**  
`[AddContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenResponse)` |   
  
### addContextChildrenCallable()
    
    
    public final UnaryCallable<AddContextChildrenRequest,AddContextChildrenResponse> addContextChildrenCallable()

Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       AddContextChildrenRequest request =
           AddContextChildrenRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .addAllChildContexts(new ArrayList<String>())
               .build();
       ApiFuture<AddContextChildrenResponse> future =
           metadataServiceClient.addContextChildrenCallable().futureCall(request);
       // Do something.
       AddContextChildrenResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenRequest),[AddContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenResponse)>` |   
  
### addExecutionEvents(@Nullable ExecutionName execution, List<Event> events)
    
    
    public final AddExecutionEventsResponse addExecutionEvents(@Nullable ExecutionName execution, List<Event> events)

Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ExecutionName execution =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]");
       List<Event> events = new ArrayList<>();
       AddExecutionEventsResponse response =
           metadataServiceClient.addExecutionEvents(execution, events);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`execution` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ExecutionName`  
Required. The resource name of the Execution that the Events connect Artifacts with. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
`events` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Event)>`  
The Events to create and add.  
**Returns**  
---  
**Type** | **Description**  
`[AddExecutionEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsResponse)` |   
  
### addExecutionEvents(AddExecutionEventsRequest request)
    
    
    public final AddExecutionEventsResponse addExecutionEvents(AddExecutionEventsRequest request)

Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       AddExecutionEventsRequest request =
           AddExecutionEventsRequest.newBuilder()
               .setExecution(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .addAllEvents(new ArrayList<Event>())
               .build();
       AddExecutionEventsResponse response = metadataServiceClient.addExecutionEvents(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddExecutionEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AddExecutionEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsResponse)` |   
  
### addExecutionEvents(String execution, List<Event> events)
    
    
    public final AddExecutionEventsResponse addExecutionEvents(String execution, List<Event> events)

Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String execution =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]").toString();
       List<Event> events = new ArrayList<>();
       AddExecutionEventsResponse response =
           metadataServiceClient.addExecutionEvents(execution, events);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`execution` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Execution that the Events connect Artifacts with. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
`events` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Event)>`  
The Events to create and add.  
**Returns**  
---  
**Type** | **Description**  
`[AddExecutionEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsResponse)` |   
  
### addExecutionEventsCallable()
    
    
    public final UnaryCallable<AddExecutionEventsRequest,AddExecutionEventsResponse> addExecutionEventsCallable()

Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       AddExecutionEventsRequest request =
           AddExecutionEventsRequest.newBuilder()
               .setExecution(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .addAllEvents(new ArrayList<Event>())
               .build();
       ApiFuture<AddExecutionEventsResponse> future =
           metadataServiceClient.addExecutionEventsCallable().futureCall(request);
       // Do something.
       AddExecutionEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddExecutionEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsRequest),[AddExecutionEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsResponse)>` |   
  
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

### createArtifact(@Nullable MetadataStoreName parent, Artifact artifact, String artifactId)
    
    
    public final Artifact createArtifact(@Nullable MetadataStoreName parent, Artifact artifact, String artifactId)

Creates an Artifact associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       Artifact artifact = Artifact.newBuilder().build();
       String artifactId = "artifactId240640653";
       Artifact response = metadataServiceClient.createArtifact(parent, artifact, artifactId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The resource name of the MetadataStore where the Artifact should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`artifact` | `[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)`  
Required. The Artifact to create.  
`artifactId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {artifact} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` If not provided, the Artifact's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Artifacts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Artifact.)  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### createArtifact(CreateArtifactRequest request)
    
    
    public final Artifact createArtifact(CreateArtifactRequest request)

Creates an Artifact associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateArtifactRequest request =
           CreateArtifactRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setArtifact(Artifact.newBuilder().build())
               .setArtifactId("artifactId240640653")
               .build();
       Artifact response = metadataServiceClient.createArtifact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateArtifactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### createArtifact(String parent, Artifact artifact, String artifactId)
    
    
    public final Artifact createArtifact(String parent, Artifact artifact, String artifactId)

Creates an Artifact associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       Artifact artifact = Artifact.newBuilder().build();
       String artifactId = "artifactId240640653";
       Artifact response = metadataServiceClient.createArtifact(parent, artifact, artifactId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MetadataStore where the Artifact should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`artifact` | `[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)`  
Required. The Artifact to create.  
`artifactId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {artifact} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` If not provided, the Artifact's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Artifacts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Artifact.)  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### createArtifactCallable()
    
    
    public final UnaryCallable<CreateArtifactRequest,Artifact> createArtifactCallable()

Creates an Artifact associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateArtifactRequest request =
           CreateArtifactRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setArtifact(Artifact.newBuilder().build())
               .setArtifactId("artifactId240640653")
               .build();
       ApiFuture<Artifact> future =
           metadataServiceClient.createArtifactCallable().futureCall(request);
       // Do something.
       Artifact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateArtifactRequest),[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)>` |   
  
### createContext(@Nullable MetadataStoreName parent, Context context, String contextId)
    
    
    public final Context createContext(@Nullable MetadataStoreName parent, Context context, String contextId)

Creates a Context associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       Context context = Context.newBuilder().build();
       String contextId = "contextId-406810838";
       Context response = metadataServiceClient.createContext(parent, context, contextId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The resource name of the MetadataStore where the Context should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`context` | `[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)`  
Required. The Context to create.  
`contextId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {context} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`. If not provided, the Context's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Contexts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Context.)  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### createContext(CreateContextRequest request)
    
    
    public final Context createContext(CreateContextRequest request)

Creates a Context associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateContextRequest request =
           CreateContextRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setContext(Context.newBuilder().build())
               .setContextId("contextId-406810838")
               .build();
       Context response = metadataServiceClient.createContext(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateContextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### createContext(String parent, Context context, String contextId)
    
    
    public final Context createContext(String parent, Context context, String contextId)

Creates a Context associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       Context context = Context.newBuilder().build();
       String contextId = "contextId-406810838";
       Context response = metadataServiceClient.createContext(parent, context, contextId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MetadataStore where the Context should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`context` | `[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)`  
Required. The Context to create.  
`contextId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {context} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`. If not provided, the Context's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Contexts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Context.)  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### createContextCallable()
    
    
    public final UnaryCallable<CreateContextRequest,Context> createContextCallable()

Creates a Context associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateContextRequest request =
           CreateContextRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setContext(Context.newBuilder().build())
               .setContextId("contextId-406810838")
               .build();
       ApiFuture<Context> future = metadataServiceClient.createContextCallable().futureCall(request);
       // Do something.
       Context response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateContextRequest),[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)>` |   
  
### createExecution(@Nullable MetadataStoreName parent, Execution execution, String executionId)
    
    
    public final Execution createExecution(@Nullable MetadataStoreName parent, Execution execution, String executionId)

Creates an Execution associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       Execution execution = Execution.newBuilder().build();
       String executionId = "executionId-454906285";
       Execution response = metadataServiceClient.createExecution(parent, execution, executionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The resource name of the MetadataStore where the Execution should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`execution` | `[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)`  
Required. The Execution to create.  
`executionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.)  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### createExecution(CreateExecutionRequest request)
    
    
    public final Execution createExecution(CreateExecutionRequest request)

Creates an Execution associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateExecutionRequest request =
           CreateExecutionRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setExecution(Execution.newBuilder().build())
               .setExecutionId("executionId-454906285")
               .build();
       Execution response = metadataServiceClient.createExecution(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateExecutionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### createExecution(String parent, Execution execution, String executionId)
    
    
    public final Execution createExecution(String parent, Execution execution, String executionId)

Creates an Execution associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       Execution execution = Execution.newBuilder().build();
       String executionId = "executionId-454906285";
       Execution response = metadataServiceClient.createExecution(parent, execution, executionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MetadataStore where the Execution should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`execution` | `[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)`  
Required. The Execution to create.  
`executionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.)  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### createExecutionCallable()
    
    
    public final UnaryCallable<CreateExecutionRequest,Execution> createExecutionCallable()

Creates an Execution associated with a MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateExecutionRequest request =
           CreateExecutionRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setExecution(Execution.newBuilder().build())
               .setExecutionId("executionId-454906285")
               .build();
       ApiFuture<Execution> future =
           metadataServiceClient.createExecutionCallable().futureCall(request);
       // Do something.
       Execution response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateExecutionRequest),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)>` |   
  
### createMetadataSchema(@Nullable MetadataStoreName parent, MetadataSchema metadataSchema, String metadataSchemaId)
    
    
    public final MetadataSchema createMetadataSchema(@Nullable MetadataStoreName parent, MetadataSchema metadataSchema, String metadataSchemaId)

Creates a MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       MetadataSchema metadataSchema = MetadataSchema.newBuilder().build();
       String metadataSchemaId = "metadataSchemaId1549245163";
       MetadataSchema response =
           metadataServiceClient.createMetadataSchema(parent, metadataSchema, metadataSchemaId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The resource name of the MetadataStore where the MetadataSchema should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`metadataSchema` | `[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)`  
Required. The MetadataSchema to create.  
`metadataSchemaId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {metadata_schema} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataSchemas in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataSchema.)  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)` |   
  
### createMetadataSchema(CreateMetadataSchemaRequest request)
    
    
    public final MetadataSchema createMetadataSchema(CreateMetadataSchemaRequest request)

Creates a MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateMetadataSchemaRequest request =
           CreateMetadataSchemaRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setMetadataSchema(MetadataSchema.newBuilder().build())
               .setMetadataSchemaId("metadataSchemaId1549245163")
               .build();
       MetadataSchema response = metadataServiceClient.createMetadataSchema(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)` |   
  
### createMetadataSchema(String parent, MetadataSchema metadataSchema, String metadataSchemaId)
    
    
    public final MetadataSchema createMetadataSchema(String parent, MetadataSchema metadataSchema, String metadataSchemaId)

Creates a MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       MetadataSchema metadataSchema = MetadataSchema.newBuilder().build();
       String metadataSchemaId = "metadataSchemaId1549245163";
       MetadataSchema response =
           metadataServiceClient.createMetadataSchema(parent, metadataSchema, metadataSchemaId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MetadataStore where the MetadataSchema should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`metadataSchema` | `[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)`  
Required. The MetadataSchema to create.  
`metadataSchemaId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {metadata_schema} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataSchemas in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataSchema.)  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)` |   
  
### createMetadataSchemaCallable()
    
    
    public final UnaryCallable<CreateMetadataSchemaRequest,MetadataSchema> createMetadataSchemaCallable()

Creates a MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateMetadataSchemaRequest request =
           CreateMetadataSchemaRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setMetadataSchema(MetadataSchema.newBuilder().build())
               .setMetadataSchemaId("metadataSchemaId1549245163")
               .build();
       ApiFuture<MetadataSchema> future =
           metadataServiceClient.createMetadataSchemaCallable().futureCall(request);
       // Do something.
       MetadataSchema response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataSchemaRequest),[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)>` |   
  
### createMetadataStoreAsync(@Nullable LocationName parent, MetadataStore metadataStore, String metadataStoreId)
    
    
    public final OperationFuture<MetadataStore,CreateMetadataStoreOperationMetadata> createMetadataStoreAsync(@Nullable LocationName parent, MetadataStore metadataStore, String metadataStoreId)

Initializes a MetadataStore, including allocation of resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       MetadataStore metadataStore = MetadataStore.newBuilder().build();
       String metadataStoreId = "metadataStoreId-1811789907";
       MetadataStore response =
           metadataServiceClient
               .createMetadataStoreAsync(parent, metadataStore, metadataStoreId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location where the MetadataStore should be created. Format: `projects/{project}/locations/{location}/`  
`metadataStore` | `[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore)`  
Required. The MetadataStore to create.  
`metadataStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore),[CreateMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreOperationMetadata)>` |   
  
### createMetadataStoreAsync(CreateMetadataStoreRequest request)
    
    
    public final OperationFuture<MetadataStore,CreateMetadataStoreOperationMetadata> createMetadataStoreAsync(CreateMetadataStoreRequest request)

Initializes a MetadataStore, including allocation of resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateMetadataStoreRequest request =
           CreateMetadataStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataStore(MetadataStore.newBuilder().build())
               .setMetadataStoreId("metadataStoreId-1811789907")
               .build();
       MetadataStore response = metadataServiceClient.createMetadataStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore),[CreateMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreOperationMetadata)>` |   
  
### createMetadataStoreAsync(String parent, MetadataStore metadataStore, String metadataStoreId)
    
    
    public final OperationFuture<MetadataStore,CreateMetadataStoreOperationMetadata> createMetadataStoreAsync(String parent, MetadataStore metadataStore, String metadataStoreId)

Initializes a MetadataStore, including allocation of resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       MetadataStore metadataStore = MetadataStore.newBuilder().build();
       String metadataStoreId = "metadataStoreId-1811789907";
       MetadataStore response =
           metadataServiceClient
               .createMetadataStoreAsync(parent, metadataStore, metadataStoreId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location where the MetadataStore should be created. Format: `projects/{project}/locations/{location}/`  
`metadataStore` | `[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore)`  
Required. The MetadataStore to create.  
`metadataStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.)  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore),[CreateMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreOperationMetadata)>` |   
  
### createMetadataStoreCallable()
    
    
    public final UnaryCallable<CreateMetadataStoreRequest,Operation> createMetadataStoreCallable()

Initializes a MetadataStore, including allocation of resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateMetadataStoreRequest request =
           CreateMetadataStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataStore(MetadataStore.newBuilder().build())
               .setMetadataStoreId("metadataStoreId-1811789907")
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.createMetadataStoreCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMetadataStoreOperationCallable()
    
    
    public final OperationCallable<CreateMetadataStoreRequest,MetadataStore,CreateMetadataStoreOperationMetadata> createMetadataStoreOperationCallable()

Initializes a MetadataStore, including allocation of resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       CreateMetadataStoreRequest request =
           CreateMetadataStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataStore(MetadataStore.newBuilder().build())
               .setMetadataStoreId("metadataStoreId-1811789907")
               .build();
       OperationFuture<MetadataStore, CreateMetadataStoreOperationMetadata> future =
           metadataServiceClient.createMetadataStoreOperationCallable().futureCall(request);
       // Do something.
       MetadataStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreRequest),[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore),[CreateMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreOperationMetadata)>` |   
  
### deleteArtifactAsync(@Nullable ArtifactName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteArtifactAsync(@Nullable ArtifactName name)

Deletes an Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ArtifactName name =
           ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]");
       metadataServiceClient.deleteArtifactAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ArtifactName`  
Required. The resource name of the Artifact to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteArtifactAsync(DeleteArtifactRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteArtifactAsync(DeleteArtifactRequest request)

Deletes an Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteArtifactRequest request =
           DeleteArtifactRequest.newBuilder()
               .setName(
                   ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       metadataServiceClient.deleteArtifactAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteArtifactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteArtifactAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteArtifactAsync(String name)

Deletes an Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name =
           ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]").toString();
       metadataServiceClient.deleteArtifactAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Artifact to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteArtifactCallable()
    
    
    public final UnaryCallable<DeleteArtifactRequest,Operation> deleteArtifactCallable()

Deletes an Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteArtifactRequest request =
           DeleteArtifactRequest.newBuilder()
               .setName(
                   ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.deleteArtifactCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteArtifactRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteArtifactOperationCallable()
    
    
    public final OperationCallable<DeleteArtifactRequest,Empty,DeleteOperationMetadata> deleteArtifactOperationCallable()

Deletes an Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteArtifactRequest request =
           DeleteArtifactRequest.newBuilder()
               .setName(
                   ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           metadataServiceClient.deleteArtifactOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteArtifactRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteContextAsync(@Nullable ContextName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteContextAsync(@Nullable ContextName name)

Deletes a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ContextName name = ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]");
       metadataServiceClient.deleteContextAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ContextName`  
Required. The resource name of the Context to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteContextAsync(DeleteContextRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteContextAsync(DeleteContextRequest request)

Deletes a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteContextRequest request =
           DeleteContextRequest.newBuilder()
               .setName(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       metadataServiceClient.deleteContextAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteContextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteContextAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteContextAsync(String name)

Deletes a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]").toString();
       metadataServiceClient.deleteContextAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Context to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteContextCallable()
    
    
    public final UnaryCallable<DeleteContextRequest,Operation> deleteContextCallable()

Deletes a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteContextRequest request =
           DeleteContextRequest.newBuilder()
               .setName(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.deleteContextCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteContextRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteContextOperationCallable()
    
    
    public final OperationCallable<DeleteContextRequest,Empty,DeleteOperationMetadata> deleteContextOperationCallable()

Deletes a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteContextRequest request =
           DeleteContextRequest.newBuilder()
               .setName(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           metadataServiceClient.deleteContextOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteContextRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteExecutionAsync(@Nullable ExecutionName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteExecutionAsync(@Nullable ExecutionName name)

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ExecutionName name =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]");
       metadataServiceClient.deleteExecutionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ExecutionName`  
Required. The resource name of the Execution to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteExecutionAsync(DeleteExecutionRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteExecutionAsync(DeleteExecutionRequest request)

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteExecutionRequest request =
           DeleteExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       metadataServiceClient.deleteExecutionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteExecutionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteExecutionAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteExecutionAsync(String name)

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]").toString();
       metadataServiceClient.deleteExecutionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Execution to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteExecutionCallable()
    
    
    public final UnaryCallable<DeleteExecutionRequest,Operation> deleteExecutionCallable()

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteExecutionRequest request =
           DeleteExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.deleteExecutionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteExecutionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExecutionOperationCallable()
    
    
    public final OperationCallable<DeleteExecutionRequest,Empty,DeleteOperationMetadata> deleteExecutionOperationCallable()

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteExecutionRequest request =
           DeleteExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           metadataServiceClient.deleteExecutionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteExecutionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteMetadataStoreAsync(@Nullable MetadataStoreName name)
    
    
    public final OperationFuture<Empty,DeleteMetadataStoreOperationMetadata> deleteMetadataStoreAsync(@Nullable MetadataStoreName name)

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName name = MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       metadataServiceClient.deleteMetadataStoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The resource name of the MetadataStore to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreOperationMetadata)>` |   
  
### deleteMetadataStoreAsync(DeleteMetadataStoreRequest request)
    
    
    public final OperationFuture<Empty,DeleteMetadataStoreOperationMetadata> deleteMetadataStoreAsync(DeleteMetadataStoreRequest request)

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteMetadataStoreRequest request =
           DeleteMetadataStoreRequest.newBuilder()
               .setName(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setForce(true)
               .build();
       metadataServiceClient.deleteMetadataStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreOperationMetadata)>` |   
  
### deleteMetadataStoreAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteMetadataStoreOperationMetadata> deleteMetadataStoreAsync(String name)

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name = MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       metadataServiceClient.deleteMetadataStoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MetadataStore to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreOperationMetadata)>` |   
  
### deleteMetadataStoreCallable()
    
    
    public final UnaryCallable<DeleteMetadataStoreRequest,Operation> deleteMetadataStoreCallable()

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteMetadataStoreRequest request =
           DeleteMetadataStoreRequest.newBuilder()
               .setName(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.deleteMetadataStoreCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMetadataStoreOperationCallable()
    
    
    public final OperationCallable<DeleteMetadataStoreRequest,Empty,DeleteMetadataStoreOperationMetadata> deleteMetadataStoreOperationCallable()

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       DeleteMetadataStoreRequest request =
           DeleteMetadataStoreRequest.newBuilder()
               .setName(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteMetadataStoreOperationMetadata> future =
           metadataServiceClient.deleteMetadataStoreOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteMetadataStoreOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreOperationMetadata)>` |   
  
### getArtifact(@Nullable ArtifactName name)
    
    
    public final Artifact getArtifact(@Nullable ArtifactName name)

Retrieves a specific Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ArtifactName name =
           ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]");
       Artifact response = metadataServiceClient.getArtifact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ArtifactName`  
Required. The resource name of the Artifact to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### getArtifact(GetArtifactRequest request)
    
    
    public final Artifact getArtifact(GetArtifactRequest request)

Retrieves a specific Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetArtifactRequest request =
           GetArtifactRequest.newBuilder()
               .setName(
                   ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]")
                       .toString())
               .build();
       Artifact response = metadataServiceClient.getArtifact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetArtifactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### getArtifact(String name)
    
    
    public final Artifact getArtifact(String name)

Retrieves a specific Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name =
           ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]").toString();
       Artifact response = metadataServiceClient.getArtifact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Artifact to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### getArtifactCallable()
    
    
    public final UnaryCallable<GetArtifactRequest,Artifact> getArtifactCallable()

Retrieves a specific Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetArtifactRequest request =
           GetArtifactRequest.newBuilder()
               .setName(
                   ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]")
                       .toString())
               .build();
       ApiFuture<Artifact> future = metadataServiceClient.getArtifactCallable().futureCall(request);
       // Do something.
       Artifact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetArtifactRequest),[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)>` |   
  
### getContext(@Nullable ContextName name)
    
    
    public final Context getContext(@Nullable ContextName name)

Retrieves a specific Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ContextName name = ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]");
       Context response = metadataServiceClient.getContext(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ContextName`  
Required. The resource name of the Context to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### getContext(GetContextRequest request)
    
    
    public final Context getContext(GetContextRequest request)

Retrieves a specific Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetContextRequest request =
           GetContextRequest.newBuilder()
               .setName(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .build();
       Context response = metadataServiceClient.getContext(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetContextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### getContext(String name)
    
    
    public final Context getContext(String name)

Retrieves a specific Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]").toString();
       Context response = metadataServiceClient.getContext(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Context to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### getContextCallable()
    
    
    public final UnaryCallable<GetContextRequest,Context> getContextCallable()

Retrieves a specific Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetContextRequest request =
           GetContextRequest.newBuilder()
               .setName(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .build();
       ApiFuture<Context> future = metadataServiceClient.getContextCallable().futureCall(request);
       // Do something.
       Context response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetContextRequest),[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)>` |   
  
### getExecution(@Nullable ExecutionName name)
    
    
    public final Execution getExecution(@Nullable ExecutionName name)

Retrieves a specific Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ExecutionName name =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]");
       Execution response = metadataServiceClient.getExecution(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ExecutionName`  
Required. The resource name of the Execution to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### getExecution(GetExecutionRequest request)
    
    
    public final Execution getExecution(GetExecutionRequest request)

Retrieves a specific Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetExecutionRequest request =
           GetExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .build();
       Execution response = metadataServiceClient.getExecution(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetExecutionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### getExecution(String name)
    
    
    public final Execution getExecution(String name)

Retrieves a specific Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]").toString();
       Execution response = metadataServiceClient.getExecution(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Execution to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### getExecutionCallable()
    
    
    public final UnaryCallable<GetExecutionRequest,Execution> getExecutionCallable()

Retrieves a specific Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetExecutionRequest request =
           GetExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .build();
       ApiFuture<Execution> future =
           metadataServiceClient.getExecutionCallable().futureCall(request);
       // Do something.
       Execution response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetExecutionRequest),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = metadataServiceClient.getIamPolicy(request);
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
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = metadataServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = metadataServiceClient.getLocation(request);
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
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = metadataServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMetadataSchema(@Nullable MetadataSchemaName name)
    
    
    public final MetadataSchema getMetadataSchema(@Nullable MetadataSchemaName name)

Retrieves a specific MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataSchemaName name =
           MetadataSchemaName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[METADATA_SCHEMA]");
       MetadataSchema response = metadataServiceClient.getMetadataSchema(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataSchemaName`  
Required. The resource name of the MetadataSchema to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)` |   
  
### getMetadataSchema(GetMetadataSchemaRequest request)
    
    
    public final MetadataSchema getMetadataSchema(GetMetadataSchemaRequest request)

Retrieves a specific MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetMetadataSchemaRequest request =
           GetMetadataSchemaRequest.newBuilder()
               .setName(
                   MetadataSchemaName.of(
                           "[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[METADATA_SCHEMA]")
                       .toString())
               .build();
       MetadataSchema response = metadataServiceClient.getMetadataSchema(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetMetadataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)` |   
  
### getMetadataSchema(String name)
    
    
    public final MetadataSchema getMetadataSchema(String name)

Retrieves a specific MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name =
           MetadataSchemaName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[METADATA_SCHEMA]")
               .toString();
       MetadataSchema response = metadataServiceClient.getMetadataSchema(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MetadataSchema to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)` |   
  
### getMetadataSchemaCallable()
    
    
    public final UnaryCallable<GetMetadataSchemaRequest,MetadataSchema> getMetadataSchemaCallable()

Retrieves a specific MetadataSchema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetMetadataSchemaRequest request =
           GetMetadataSchemaRequest.newBuilder()
               .setName(
                   MetadataSchemaName.of(
                           "[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[METADATA_SCHEMA]")
                       .toString())
               .build();
       ApiFuture<MetadataSchema> future =
           metadataServiceClient.getMetadataSchemaCallable().futureCall(request);
       // Do something.
       MetadataSchema response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetMetadataSchemaRequest),[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)>` |   
  
### getMetadataStore(@Nullable MetadataStoreName name)
    
    
    public final MetadataStore getMetadataStore(@Nullable MetadataStoreName name)

Retrieves a specific MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName name = MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       MetadataStore response = metadataServiceClient.getMetadataStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The resource name of the MetadataStore to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore)` |   
  
### getMetadataStore(GetMetadataStoreRequest request)
    
    
    public final MetadataStore getMetadataStore(GetMetadataStoreRequest request)

Retrieves a specific MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetMetadataStoreRequest request =
           GetMetadataStoreRequest.newBuilder()
               .setName(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .build();
       MetadataStore response = metadataServiceClient.getMetadataStore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetMetadataStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore)` |   
  
### getMetadataStore(String name)
    
    
    public final MetadataStore getMetadataStore(String name)

Retrieves a specific MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String name = MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       MetadataStore response = metadataServiceClient.getMetadataStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MetadataStore to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore)` |   
  
### getMetadataStoreCallable()
    
    
    public final UnaryCallable<GetMetadataStoreRequest,MetadataStore> getMetadataStoreCallable()

Retrieves a specific MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       GetMetadataStoreRequest request =
           GetMetadataStoreRequest.newBuilder()
               .setName(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .build();
       ApiFuture<MetadataStore> future =
           metadataServiceClient.getMetadataStoreCallable().futureCall(request);
       // Do something.
       MetadataStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetMetadataStoreRequest),[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable MetadataServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataServiceSettings` |   
  
### getStub()
    
    
    public MetadataServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.MetadataServiceStub)` |   
  
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
  
### listArtifacts(@Nullable MetadataStoreName parent)
    
    
    public final MetadataServiceClient.ListArtifactsPagedResponse listArtifacts(@Nullable MetadataStoreName parent)

Lists Artifacts in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       for (Artifact element : metadataServiceClient.listArtifacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The MetadataStore whose Artifacts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListArtifactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListArtifactsPagedResponse)` |   
  
### listArtifacts(ListArtifactsRequest request)
    
    
    public final MetadataServiceClient.ListArtifactsPagedResponse listArtifacts(ListArtifactsRequest request)

Lists Artifacts in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListArtifactsRequest request =
           ListArtifactsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Artifact element : metadataServiceClient.listArtifacts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListArtifactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListArtifactsPagedResponse)` |   
  
### listArtifacts(String parent)
    
    
    public final MetadataServiceClient.ListArtifactsPagedResponse listArtifacts(String parent)

Lists Artifacts in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       for (Artifact element : metadataServiceClient.listArtifacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The MetadataStore whose Artifacts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListArtifactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListArtifactsPagedResponse)` |   
  
### listArtifactsCallable()
    
    
    public final UnaryCallable<ListArtifactsRequest,ListArtifactsResponse> listArtifactsCallable()

Lists Artifacts in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListArtifactsRequest request =
           ListArtifactsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListArtifactsResponse response =
             metadataServiceClient.listArtifactsCallable().call(request);
         for (Artifact element : response.getArtifactsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListArtifactsRequest),[ListArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListArtifactsResponse)>` |   
  
### listArtifactsPagedCallable()
    
    
    public final UnaryCallable<ListArtifactsRequest,MetadataServiceClient.ListArtifactsPagedResponse> listArtifactsPagedCallable()

Lists Artifacts in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListArtifactsRequest request =
           ListArtifactsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Artifact> future =
           metadataServiceClient.listArtifactsPagedCallable().futureCall(request);
       // Do something.
       for (Artifact element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListArtifactsRequest),[ListArtifactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListArtifactsPagedResponse)>` |   
  
### listContexts(@Nullable MetadataStoreName parent)
    
    
    public final MetadataServiceClient.ListContextsPagedResponse listContexts(@Nullable MetadataStoreName parent)

Lists Contexts on the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       for (Context element : metadataServiceClient.listContexts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The MetadataStore whose Contexts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListContextsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListContextsPagedResponse)` |   
  
### listContexts(ListContextsRequest request)
    
    
    public final MetadataServiceClient.ListContextsPagedResponse listContexts(ListContextsRequest request)

Lists Contexts on the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListContextsRequest request =
           ListContextsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Context element : metadataServiceClient.listContexts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListContextsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListContextsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListContextsPagedResponse)` |   
  
### listContexts(String parent)
    
    
    public final MetadataServiceClient.ListContextsPagedResponse listContexts(String parent)

Lists Contexts on the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       for (Context element : metadataServiceClient.listContexts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The MetadataStore whose Contexts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListContextsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListContextsPagedResponse)` |   
  
### listContextsCallable()
    
    
    public final UnaryCallable<ListContextsRequest,ListContextsResponse> listContextsCallable()

Lists Contexts on the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListContextsRequest request =
           ListContextsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListContextsResponse response = metadataServiceClient.listContextsCallable().call(request);
         for (Context element : response.getContextsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListContextsRequest),[ListContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListContextsResponse)>` |   
  
### listContextsPagedCallable()
    
    
    public final UnaryCallable<ListContextsRequest,MetadataServiceClient.ListContextsPagedResponse> listContextsPagedCallable()

Lists Contexts on the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListContextsRequest request =
           ListContextsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Context> future =
           metadataServiceClient.listContextsPagedCallable().futureCall(request);
       // Do something.
       for (Context element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListContextsRequest),[ListContextsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListContextsPagedResponse)>` |   
  
### listExecutions(@Nullable MetadataStoreName parent)
    
    
    public final MetadataServiceClient.ListExecutionsPagedResponse listExecutions(@Nullable MetadataStoreName parent)

Lists Executions in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       for (Execution element : metadataServiceClient.listExecutions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The MetadataStore whose Executions should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListExecutionsPagedResponse)` |   
  
### listExecutions(ListExecutionsRequest request)
    
    
    public final MetadataServiceClient.ListExecutionsPagedResponse listExecutions(ListExecutionsRequest request)

Lists Executions in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListExecutionsRequest request =
           ListExecutionsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Execution element : metadataServiceClient.listExecutions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListExecutionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListExecutionsPagedResponse)` |   
  
### listExecutions(String parent)
    
    
    public final MetadataServiceClient.ListExecutionsPagedResponse listExecutions(String parent)

Lists Executions in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       for (Execution element : metadataServiceClient.listExecutions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The MetadataStore whose Executions should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListExecutionsPagedResponse)` |   
  
### listExecutionsCallable()
    
    
    public final UnaryCallable<ListExecutionsRequest,ListExecutionsResponse> listExecutionsCallable()

Lists Executions in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListExecutionsRequest request =
           ListExecutionsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListExecutionsResponse response =
             metadataServiceClient.listExecutionsCallable().call(request);
         for (Execution element : response.getExecutionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListExecutionsRequest),[ListExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListExecutionsResponse)>` |   
  
### listExecutionsPagedCallable()
    
    
    public final UnaryCallable<ListExecutionsRequest,MetadataServiceClient.ListExecutionsPagedResponse> listExecutionsPagedCallable()

Lists Executions in the MetadataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListExecutionsRequest request =
           ListExecutionsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Execution> future =
           metadataServiceClient.listExecutionsPagedCallable().futureCall(request);
       // Do something.
       for (Execution element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListExecutionsRequest),[ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListExecutionsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final MetadataServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : metadataServiceClient.listLocations(request).iterateAll()) {
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
`[MetadataServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             metadataServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,MetadataServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           metadataServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListLocationsPagedResponse)>` |   
  
### listMetadataSchemas(@Nullable MetadataStoreName parent)
    
    
    public final MetadataServiceClient.ListMetadataSchemasPagedResponse listMetadataSchemas(@Nullable MetadataStoreName parent)

Lists MetadataSchemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       for (MetadataSchema element :
           metadataServiceClient.listMetadataSchemas(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The MetadataStore whose MetadataSchemas should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListMetadataSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataSchemasPagedResponse)` |   
  
### listMetadataSchemas(ListMetadataSchemasRequest request)
    
    
    public final MetadataServiceClient.ListMetadataSchemasPagedResponse listMetadataSchemas(ListMetadataSchemasRequest request)

Lists MetadataSchemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListMetadataSchemasRequest request =
           ListMetadataSchemasRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (MetadataSchema element :
           metadataServiceClient.listMetadataSchemas(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetadataSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataSchemasRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListMetadataSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataSchemasPagedResponse)` |   
  
### listMetadataSchemas(String parent)
    
    
    public final MetadataServiceClient.ListMetadataSchemasPagedResponse listMetadataSchemas(String parent)

Lists MetadataSchemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       for (MetadataSchema element :
           metadataServiceClient.listMetadataSchemas(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The MetadataStore whose MetadataSchemas should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListMetadataSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataSchemasPagedResponse)` |   
  
### listMetadataSchemasCallable()
    
    
    public final UnaryCallable<ListMetadataSchemasRequest,ListMetadataSchemasResponse> listMetadataSchemasCallable()

Lists MetadataSchemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListMetadataSchemasRequest request =
           ListMetadataSchemasRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListMetadataSchemasResponse response =
             metadataServiceClient.listMetadataSchemasCallable().call(request);
         for (MetadataSchema element : response.getMetadataSchemasList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataSchemasRequest),[ListMetadataSchemasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataSchemasResponse)>` |   
  
### listMetadataSchemasPagedCallable()
    
    
    public final UnaryCallable<ListMetadataSchemasRequest,MetadataServiceClient.ListMetadataSchemasPagedResponse> listMetadataSchemasPagedCallable()

Lists MetadataSchemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListMetadataSchemasRequest request =
           ListMetadataSchemasRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<MetadataSchema> future =
           metadataServiceClient.listMetadataSchemasPagedCallable().futureCall(request);
       // Do something.
       for (MetadataSchema element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataSchemasRequest),[ListMetadataSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataSchemasPagedResponse)>` |   
  
### listMetadataStores(@Nullable LocationName parent)
    
    
    public final MetadataServiceClient.ListMetadataStoresPagedResponse listMetadataStores(@Nullable LocationName parent)

Lists MetadataStores for a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (MetadataStore element : metadataServiceClient.listMetadataStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The Location whose MetadataStores should be listed. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListMetadataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataStoresPagedResponse)` |   
  
### listMetadataStores(ListMetadataStoresRequest request)
    
    
    public final MetadataServiceClient.ListMetadataStoresPagedResponse listMetadataStores(ListMetadataStoresRequest request)

Lists MetadataStores for a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListMetadataStoresRequest request =
           ListMetadataStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (MetadataStore element : metadataServiceClient.listMetadataStores(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetadataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataStoresRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListMetadataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataStoresPagedResponse)` |   
  
### listMetadataStores(String parent)
    
    
    public final MetadataServiceClient.ListMetadataStoresPagedResponse listMetadataStores(String parent)

Lists MetadataStores for a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (MetadataStore element : metadataServiceClient.listMetadataStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Location whose MetadataStores should be listed. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceClient.ListMetadataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataStoresPagedResponse)` |   
  
### listMetadataStoresCallable()
    
    
    public final UnaryCallable<ListMetadataStoresRequest,ListMetadataStoresResponse> listMetadataStoresCallable()

Lists MetadataStores for a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListMetadataStoresRequest request =
           ListMetadataStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMetadataStoresResponse response =
             metadataServiceClient.listMetadataStoresCallable().call(request);
         for (MetadataStore element : response.getMetadataStoresList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataStoresRequest),[ListMetadataStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataStoresResponse)>` |   
  
### listMetadataStoresPagedCallable()
    
    
    public final UnaryCallable<ListMetadataStoresRequest,MetadataServiceClient.ListMetadataStoresPagedResponse> listMetadataStoresPagedCallable()

Lists MetadataStores for a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ListMetadataStoresRequest request =
           ListMetadataStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<MetadataStore> future =
           metadataServiceClient.listMetadataStoresPagedCallable().futureCall(request);
       // Do something.
       for (MetadataStore element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataStoresRequest),[ListMetadataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceClient.ListMetadataStoresPagedResponse)>` |   
  
### purgeArtifactsAsync(@Nullable MetadataStoreName parent)
    
    
    public final OperationFuture<PurgeArtifactsResponse,PurgeArtifactsMetadata> purgeArtifactsAsync(@Nullable MetadataStoreName parent)

Purges Artifacts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       PurgeArtifactsResponse response = metadataServiceClient.purgeArtifactsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The metadata store to purge Artifacts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsResponse),[PurgeArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsMetadata)>` |   
  
### purgeArtifactsAsync(PurgeArtifactsRequest request)
    
    
    public final OperationFuture<PurgeArtifactsResponse,PurgeArtifactsMetadata> purgeArtifactsAsync(PurgeArtifactsRequest request)

Purges Artifacts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeArtifactsRequest request =
           PurgeArtifactsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       PurgeArtifactsResponse response = metadataServiceClient.purgeArtifactsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsResponse),[PurgeArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsMetadata)>` |   
  
### purgeArtifactsAsync(String parent)
    
    
    public final OperationFuture<PurgeArtifactsResponse,PurgeArtifactsMetadata> purgeArtifactsAsync(String parent)

Purges Artifacts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       PurgeArtifactsResponse response = metadataServiceClient.purgeArtifactsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The metadata store to purge Artifacts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsResponse),[PurgeArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsMetadata)>` |   
  
### purgeArtifactsCallable()
    
    
    public final UnaryCallable<PurgeArtifactsRequest,Operation> purgeArtifactsCallable()

Purges Artifacts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeArtifactsRequest request =
           PurgeArtifactsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.purgeArtifactsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeArtifactsOperationCallable()
    
    
    public final OperationCallable<PurgeArtifactsRequest,PurgeArtifactsResponse,PurgeArtifactsMetadata> purgeArtifactsOperationCallable()

Purges Artifacts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeArtifactsRequest request =
           PurgeArtifactsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       OperationFuture<PurgeArtifactsResponse, PurgeArtifactsMetadata> future =
           metadataServiceClient.purgeArtifactsOperationCallable().futureCall(request);
       // Do something.
       PurgeArtifactsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsRequest),[PurgeArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsResponse),[PurgeArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsMetadata)>` |   
  
### purgeContextsAsync(@Nullable MetadataStoreName parent)
    
    
    public final OperationFuture<PurgeContextsResponse,PurgeContextsMetadata> purgeContextsAsync(@Nullable MetadataStoreName parent)

Purges Contexts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       PurgeContextsResponse response = metadataServiceClient.purgeContextsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The metadata store to purge Contexts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsResponse),[PurgeContextsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsMetadata)>` |   
  
### purgeContextsAsync(PurgeContextsRequest request)
    
    
    public final OperationFuture<PurgeContextsResponse,PurgeContextsMetadata> purgeContextsAsync(PurgeContextsRequest request)

Purges Contexts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeContextsRequest request =
           PurgeContextsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       PurgeContextsResponse response = metadataServiceClient.purgeContextsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsResponse),[PurgeContextsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsMetadata)>` |   
  
### purgeContextsAsync(String parent)
    
    
    public final OperationFuture<PurgeContextsResponse,PurgeContextsMetadata> purgeContextsAsync(String parent)

Purges Contexts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       PurgeContextsResponse response = metadataServiceClient.purgeContextsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The metadata store to purge Contexts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsResponse),[PurgeContextsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsMetadata)>` |   
  
### purgeContextsCallable()
    
    
    public final UnaryCallable<PurgeContextsRequest,Operation> purgeContextsCallable()

Purges Contexts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeContextsRequest request =
           PurgeContextsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.purgeContextsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeContextsOperationCallable()
    
    
    public final OperationCallable<PurgeContextsRequest,PurgeContextsResponse,PurgeContextsMetadata> purgeContextsOperationCallable()

Purges Contexts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeContextsRequest request =
           PurgeContextsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       OperationFuture<PurgeContextsResponse, PurgeContextsMetadata> future =
           metadataServiceClient.purgeContextsOperationCallable().futureCall(request);
       // Do something.
       PurgeContextsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsRequest),[PurgeContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsResponse),[PurgeContextsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsMetadata)>` |   
  
### purgeExecutionsAsync(@Nullable MetadataStoreName parent)
    
    
    public final OperationFuture<PurgeExecutionsResponse,PurgeExecutionsMetadata> purgeExecutionsAsync(@Nullable MetadataStoreName parent)

Purges Executions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       MetadataStoreName parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]");
       PurgeExecutionsResponse response = metadataServiceClient.purgeExecutionsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.MetadataStoreName`  
Required. The metadata store to purge Executions from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsResponse),[PurgeExecutionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsMetadata)>` |   
  
### purgeExecutionsAsync(PurgeExecutionsRequest request)
    
    
    public final OperationFuture<PurgeExecutionsResponse,PurgeExecutionsMetadata> purgeExecutionsAsync(PurgeExecutionsRequest request)

Purges Executions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeExecutionsRequest request =
           PurgeExecutionsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       PurgeExecutionsResponse response = metadataServiceClient.purgeExecutionsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsResponse),[PurgeExecutionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsMetadata)>` |   
  
### purgeExecutionsAsync(String parent)
    
    
    public final OperationFuture<PurgeExecutionsResponse,PurgeExecutionsMetadata> purgeExecutionsAsync(String parent)

Purges Executions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String parent =
           MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString();
       PurgeExecutionsResponse response = metadataServiceClient.purgeExecutionsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The metadata store to purge Executions from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsResponse),[PurgeExecutionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsMetadata)>` |   
  
### purgeExecutionsCallable()
    
    
    public final UnaryCallable<PurgeExecutionsRequest,Operation> purgeExecutionsCallable()

Purges Executions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeExecutionsRequest request =
           PurgeExecutionsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           metadataServiceClient.purgeExecutionsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeExecutionsOperationCallable()
    
    
    public final OperationCallable<PurgeExecutionsRequest,PurgeExecutionsResponse,PurgeExecutionsMetadata> purgeExecutionsOperationCallable()

Purges Executions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       PurgeExecutionsRequest request =
           PurgeExecutionsRequest.newBuilder()
               .setParent(
                   MetadataStoreName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       OperationFuture<PurgeExecutionsResponse, PurgeExecutionsMetadata> future =
           metadataServiceClient.purgeExecutionsOperationCallable().futureCall(request);
       // Do something.
       PurgeExecutionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsRequest),[PurgeExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsResponse),[PurgeExecutionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsMetadata)>` |   
  
### queryArtifactLineageSubgraph(@Nullable ArtifactName artifact)
    
    
    public final LineageSubgraph queryArtifactLineageSubgraph(@Nullable ArtifactName artifact)

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ArtifactName artifact =
           ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]");
       LineageSubgraph response = metadataServiceClient.queryArtifactLineageSubgraph(artifact);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`artifact` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ArtifactName`  
Required. The resource name of the Artifact whose Lineage needs to be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryArtifactLineageSubgraph(QueryArtifactLineageSubgraphRequest request)
    
    
    public final LineageSubgraph queryArtifactLineageSubgraph(QueryArtifactLineageSubgraphRequest request)

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       QueryArtifactLineageSubgraphRequest request =
           QueryArtifactLineageSubgraphRequest.newBuilder()
               .setArtifact(
                   ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]")
                       .toString())
               .setMaxHops(407750469)
               .setFilter("filter-1274492040")
               .build();
       LineageSubgraph response = metadataServiceClient.queryArtifactLineageSubgraph(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryArtifactLineageSubgraphRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryArtifactLineageSubgraph(String artifact)
    
    
    public final LineageSubgraph queryArtifactLineageSubgraph(String artifact)

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String artifact =
           ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]").toString();
       LineageSubgraph response = metadataServiceClient.queryArtifactLineageSubgraph(artifact);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`artifact` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Artifact whose Lineage needs to be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryArtifactLineageSubgraphCallable()
    
    
    public final UnaryCallable<QueryArtifactLineageSubgraphRequest,LineageSubgraph> queryArtifactLineageSubgraphCallable()

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       QueryArtifactLineageSubgraphRequest request =
           QueryArtifactLineageSubgraphRequest.newBuilder()
               .setArtifact(
                   ArtifactName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[ARTIFACT]")
                       .toString())
               .setMaxHops(407750469)
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<LineageSubgraph> future =
           metadataServiceClient.queryArtifactLineageSubgraphCallable().futureCall(request);
       // Do something.
       LineageSubgraph response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryArtifactLineageSubgraphRequest),[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)>` |   
  
### queryContextLineageSubgraph(@Nullable ContextName context)
    
    
    public final LineageSubgraph queryContextLineageSubgraph(@Nullable ContextName context)

Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ContextName context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]");
       LineageSubgraph response = metadataServiceClient.queryContextLineageSubgraph(context);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ContextName`  
Required. The resource name of the Context whose Artifacts and Executions should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}` The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryContextLineageSubgraph(QueryContextLineageSubgraphRequest request)
    
    
    public final LineageSubgraph queryContextLineageSubgraph(QueryContextLineageSubgraphRequest request)

Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       QueryContextLineageSubgraphRequest request =
           QueryContextLineageSubgraphRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .build();
       LineageSubgraph response = metadataServiceClient.queryContextLineageSubgraph(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryContextLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryContextLineageSubgraphRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryContextLineageSubgraph(String context)
    
    
    public final LineageSubgraph queryContextLineageSubgraph(String context)

Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]").toString();
       LineageSubgraph response = metadataServiceClient.queryContextLineageSubgraph(context);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`context` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Context whose Artifacts and Executions should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}` The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryContextLineageSubgraphCallable()
    
    
    public final UnaryCallable<QueryContextLineageSubgraphRequest,LineageSubgraph> queryContextLineageSubgraphCallable()

Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       QueryContextLineageSubgraphRequest request =
           QueryContextLineageSubgraphRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .build();
       ApiFuture<LineageSubgraph> future =
           metadataServiceClient.queryContextLineageSubgraphCallable().futureCall(request);
       // Do something.
       LineageSubgraph response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryContextLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryContextLineageSubgraphRequest),[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)>` |   
  
### queryExecutionInputsAndOutputs(@Nullable ExecutionName execution)
    
    
    public final LineageSubgraph queryExecutionInputsAndOutputs(@Nullable ExecutionName execution)

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ExecutionName execution =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]");
       LineageSubgraph response = metadataServiceClient.queryExecutionInputsAndOutputs(execution);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`execution` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ExecutionName`  
Required. The resource name of the Execution whose input and output Artifacts should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryExecutionInputsAndOutputs(QueryExecutionInputsAndOutputsRequest request)
    
    
    public final LineageSubgraph queryExecutionInputsAndOutputs(QueryExecutionInputsAndOutputsRequest request)

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       QueryExecutionInputsAndOutputsRequest request =
           QueryExecutionInputsAndOutputsRequest.newBuilder()
               .setExecution(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .build();
       LineageSubgraph response = metadataServiceClient.queryExecutionInputsAndOutputs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryExecutionInputsAndOutputsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryExecutionInputsAndOutputs(String execution)
    
    
    public final LineageSubgraph queryExecutionInputsAndOutputs(String execution)

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String execution =
           ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]").toString();
       LineageSubgraph response = metadataServiceClient.queryExecutionInputsAndOutputs(execution);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`execution` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Execution whose input and output Artifacts should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)` |   
  
### queryExecutionInputsAndOutputsCallable()
    
    
    public final UnaryCallable<QueryExecutionInputsAndOutputsRequest,LineageSubgraph> queryExecutionInputsAndOutputsCallable()

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       QueryExecutionInputsAndOutputsRequest request =
           QueryExecutionInputsAndOutputsRequest.newBuilder()
               .setExecution(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[EXECUTION]")
                       .toString())
               .build();
       ApiFuture<LineageSubgraph> future =
           metadataServiceClient.queryExecutionInputsAndOutputsCallable().futureCall(request);
       // Do something.
       LineageSubgraph response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryExecutionInputsAndOutputsRequest),[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)>` |   
  
### removeContextChildren(@Nullable ContextName context, List<String> childContexts)
    
    
    public final RemoveContextChildrenResponse removeContextChildren(@Nullable ContextName context, List<String> childContexts)

Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       ContextName context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]");
       List<String> childContexts = new ArrayList<>();
       RemoveContextChildrenResponse response =
           metadataServiceClient.removeContextChildren(context, childContexts);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ContextName`  
Required. The resource name of the parent Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
`childContexts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the child Contexts.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenResponse)` |   
  
### removeContextChildren(RemoveContextChildrenRequest request)
    
    
    public final RemoveContextChildrenResponse removeContextChildren(RemoveContextChildrenRequest request)

Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       RemoveContextChildrenRequest request =
           RemoveContextChildrenRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .addAllChildContexts(new ArrayList<String>())
               .build();
       RemoveContextChildrenResponse response = metadataServiceClient.removeContextChildren(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenResponse)` |   
  
### removeContextChildren(String context, List<String> childContexts)
    
    
    public final RemoveContextChildrenResponse removeContextChildren(String context, List<String> childContexts)

Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       String context =
           ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]").toString();
       List<String> childContexts = new ArrayList<>();
       RemoveContextChildrenResponse response =
           metadataServiceClient.removeContextChildren(context, childContexts);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`context` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent Context. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
`childContexts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resource names of the child Contexts.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenResponse)` |   
  
### removeContextChildrenCallable()
    
    
    public final UnaryCallable<RemoveContextChildrenRequest,RemoveContextChildrenResponse> removeContextChildrenCallable()

Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       RemoveContextChildrenRequest request =
           RemoveContextChildrenRequest.newBuilder()
               .setContext(
                   ContextName.of("[PROJECT]", "[LOCATION]", "[METADATA_STORE]", "[CONTEXT]")
                       .toString())
               .addAllChildContexts(new ArrayList<String>())
               .build();
       ApiFuture<RemoveContextChildrenResponse> future =
           metadataServiceClient.removeContextChildrenCallable().futureCall(request);
       // Do something.
       RemoveContextChildrenResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenRequest),[RemoveContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenResponse)>` |   
  
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
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = metadataServiceClient.setIamPolicy(request);
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
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = metadataServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = metadataServiceClient.testIamPermissions(request);
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
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           metadataServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateArtifact(Artifact artifact, FieldMask updateMask)
    
    
    public final Artifact updateArtifact(Artifact artifact, FieldMask updateMask)

Updates a stored Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       Artifact artifact = Artifact.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Artifact response = metadataServiceClient.updateArtifact(artifact, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`artifact` | `[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)`  
Required. The Artifact containing updates. The Artifact's Artifact.name field is used to identify the Artifact to be updated. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. A FieldMask indicating which fields should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### updateArtifact(UpdateArtifactRequest request)
    
    
    public final Artifact updateArtifact(UpdateArtifactRequest request)

Updates a stored Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       UpdateArtifactRequest request =
           UpdateArtifactRequest.newBuilder()
               .setArtifact(Artifact.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       Artifact response = metadataServiceClient.updateArtifact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateArtifactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)` |   
  
### updateArtifactCallable()
    
    
    public final UnaryCallable<UpdateArtifactRequest,Artifact> updateArtifactCallable()

Updates a stored Artifact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       UpdateArtifactRequest request =
           UpdateArtifactRequest.newBuilder()
               .setArtifact(Artifact.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Artifact> future =
           metadataServiceClient.updateArtifactCallable().futureCall(request);
       // Do something.
       Artifact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateArtifactRequest),[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)>` |   
  
### updateContext(Context context, FieldMask updateMask)
    
    
    public final Context updateContext(Context context, FieldMask updateMask)

Updates a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       Context context = Context.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Context response = metadataServiceClient.updateContext(context, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`context` | `[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)`  
Required. The Context containing updates. The Context's Context.name field is used to identify the Context to be updated. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. A FieldMask indicating which fields should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### updateContext(UpdateContextRequest request)
    
    
    public final Context updateContext(UpdateContextRequest request)

Updates a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       UpdateContextRequest request =
           UpdateContextRequest.newBuilder()
               .setContext(Context.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       Context response = metadataServiceClient.updateContext(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateContextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)` |   
  
### updateContextCallable()
    
    
    public final UnaryCallable<UpdateContextRequest,Context> updateContextCallable()

Updates a stored Context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       UpdateContextRequest request =
           UpdateContextRequest.newBuilder()
               .setContext(Context.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Context> future = metadataServiceClient.updateContextCallable().futureCall(request);
       // Do something.
       Context response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateContextRequest),[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)>` |   
  
### updateExecution(Execution execution, FieldMask updateMask)
    
    
    public final Execution updateExecution(Execution execution, FieldMask updateMask)

Updates a stored Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       Execution execution = Execution.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Execution response = metadataServiceClient.updateExecution(execution, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`execution` | `[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)`  
Required. The Execution containing updates. The Execution's Execution.name field is used to identify the Execution to be updated. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. A FieldMask indicating which fields should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### updateExecution(UpdateExecutionRequest request)
    
    
    public final Execution updateExecution(UpdateExecutionRequest request)

Updates a stored Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       UpdateExecutionRequest request =
           UpdateExecutionRequest.newBuilder()
               .setExecution(Execution.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       Execution response = metadataServiceClient.updateExecution(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExecutionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)` |   
  
### updateExecutionCallable()
    
    
    public final UnaryCallable<UpdateExecutionRequest,Execution> updateExecutionCallable()

Updates a stored Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetadataServiceClient metadataServiceClient = MetadataServiceClient.create()) {
       UpdateExecutionRequest request =
           UpdateExecutionRequest.newBuilder()
               .setExecution(Execution.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Execution> future =
           metadataServiceClient.updateExecutionCallable().futureCall(request);
       // Do something.
       Execution response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExecutionRequest),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
