---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceClient
title: Class VertexRagServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:40.425442+00:00
---

# Class VertexRagServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VertexRagServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/VertexRagServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for retrieving relevant contexts.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RagQuery query = RagQuery.newBuilder().build();
       RetrieveContextsResponse response = vertexRagServiceClient.retrieveContexts(parent, query);
     }
     

Note: close() needs to be called on the VertexRagServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
RetrieveContexts |  Retrieves relevant contexts for a query. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * retrieveContexts(RetrieveContextsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * retrieveContexts(LocationName parent, RagQuery query) 
  * retrieveContexts(String parent, RagQuery query) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * retrieveContextsCallable() 

  
AugmentPrompt |  Given an input prompt, it returns augmented prompt from vertex rag store to guide LLM towards generating grounded responses. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * augmentPrompt(AugmentPromptRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * augmentPrompt(LocationName parent, AugmentPromptRequest.Model model, VertexRagStore vertexRagStore) 
  * augmentPrompt(String parent, AugmentPromptRequest.Model model, VertexRagStore vertexRagStore) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * augmentPromptCallable() 

  
CorroborateContent |  Given an input text, it returns a score that evaluates the factuality of the text. It also extracts and returns claims from the text and provides supporting facts. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * corroborateContent(CorroborateContentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * corroborateContent(LocationName parent, Content content, List<Fact> facts) 
  * corroborateContent(String parent, Content content, List<Fact> facts) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * corroborateContentCallable() 

  
AskContexts |  Agentic Retrieval Ask API for RAG. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * askContexts(AskContextsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * askContexts(LocationName parent, RagQuery query) 
  * askContexts(String parent, RagQuery query) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * askContextsCallable() 

  
AsyncRetrieveContexts |  Asynchronous API to retrieves relevant contexts for a query. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * asyncRetrieveContextsAsync(AsyncRetrieveContextsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * asyncRetrieveContextsAsync(LocationName parent, RagQuery query) 
  * asyncRetrieveContextsAsync(String parent, RagQuery query) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * asyncRetrieveContextsOperationCallable() 
  * asyncRetrieveContextsCallable() 

  
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

This class can be customized by passing in a custom instance of VertexRagServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VertexRagServiceSettings vertexRagServiceSettings =
         VertexRagServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     VertexRagServiceClient vertexRagServiceClient =
         VertexRagServiceClient.create(vertexRagServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VertexRagServiceSettings vertexRagServiceSettings =
         VertexRagServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     VertexRagServiceClient vertexRagServiceClient =
         VertexRagServiceClient.create(vertexRagServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VertexRagServiceClient

## Static Methods 

### create()
    
    
    public static final VertexRagServiceClient create()

Constructs an instance of VertexRagServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[VertexRagServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VertexRagServiceSettings settings)
    
    
    public static final VertexRagServiceClient create(VertexRagServiceSettings settings)

Constructs an instance of VertexRagServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VertexRagServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VertexRagServiceStub stub)
    
    
    public static final VertexRagServiceClient create(VertexRagServiceStub stub)

Constructs an instance of VertexRagServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(VertexRagServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VertexRagServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VertexRagServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceClient)` |   
  
## Constructors 

### VertexRagServiceClient(VertexRagServiceSettings settings)
    
    
    protected VertexRagServiceClient(VertexRagServiceSettings settings)

Constructs an instance of VertexRagServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VertexRagServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceSettings)`  
  
  
### VertexRagServiceClient(VertexRagServiceStub stub)
    
    
    protected VertexRagServiceClient(VertexRagServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VertexRagServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VertexRagServiceStub)`  
  
  
## Methods 

### askContexts(@Nullable LocationName parent, RagQuery query)
    
    
    public final AskContextsResponse askContexts(@Nullable LocationName parent, RagQuery query)

Agentic Retrieval Ask API for RAG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RagQuery query = RagQuery.newBuilder().build();
       AskContextsResponse response = vertexRagServiceClient.askContexts(parent, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`query` | `[RagQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagQuery)`  
Required. Single RAG retrieve query.  
**Returns**  
---  
**Type** | **Description**  
`[AskContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AskContextsResponse)` |   
  
### askContexts(AskContextsRequest request)
    
    
    public final AskContextsResponse askContexts(AskContextsRequest request)

Agentic Retrieval Ask API for RAG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       AskContextsRequest request =
           AskContextsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery(RagQuery.newBuilder().build())
               .addAllTools(new ArrayList<Tool>())
               .build();
       AskContextsResponse response = vertexRagServiceClient.askContexts(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AskContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AskContextsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AskContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AskContextsResponse)` |   
  
### askContexts(String parent, RagQuery query)
    
    
    public final AskContextsResponse askContexts(String parent, RagQuery query)

Agentic Retrieval Ask API for RAG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       RagQuery query = RagQuery.newBuilder().build();
       AskContextsResponse response = vertexRagServiceClient.askContexts(parent, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`query` | `[RagQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagQuery)`  
Required. Single RAG retrieve query.  
**Returns**  
---  
**Type** | **Description**  
`[AskContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AskContextsResponse)` |   
  
### askContextsCallable()
    
    
    public final UnaryCallable<AskContextsRequest,AskContextsResponse> askContextsCallable()

Agentic Retrieval Ask API for RAG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       AskContextsRequest request =
           AskContextsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery(RagQuery.newBuilder().build())
               .addAllTools(new ArrayList<Tool>())
               .build();
       ApiFuture<AskContextsResponse> future =
           vertexRagServiceClient.askContextsCallable().futureCall(request);
       // Do something.
       AskContextsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AskContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AskContextsRequest),[AskContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AskContextsResponse)>` |   
  
### asyncRetrieveContextsAsync(@Nullable LocationName parent, RagQuery query)
    
    
    public final OperationFuture<AsyncRetrieveContextsResponse,AsyncRetrieveContextsOperationMetadata> asyncRetrieveContextsAsync(@Nullable LocationName parent, RagQuery query)

Asynchronous API to retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RagQuery query = RagQuery.newBuilder().build();
       AsyncRetrieveContextsResponse response =
           vertexRagServiceClient.asyncRetrieveContextsAsync(parent, query).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`query` | `[RagQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagQuery)`  
Required. Single RAG retrieve query.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AsyncRetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsResponse),[AsyncRetrieveContextsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsOperationMetadata)>` |   
  
### asyncRetrieveContextsAsync(AsyncRetrieveContextsRequest request)
    
    
    public final OperationFuture<AsyncRetrieveContextsResponse,AsyncRetrieveContextsOperationMetadata> asyncRetrieveContextsAsync(AsyncRetrieveContextsRequest request)

Asynchronous API to retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       AsyncRetrieveContextsRequest request =
           AsyncRetrieveContextsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery(RagQuery.newBuilder().build())
               .addAllTools(new ArrayList<Tool>())
               .build();
       AsyncRetrieveContextsResponse response =
           vertexRagServiceClient.asyncRetrieveContextsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AsyncRetrieveContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AsyncRetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsResponse),[AsyncRetrieveContextsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsOperationMetadata)>` |   
  
### asyncRetrieveContextsAsync(String parent, RagQuery query)
    
    
    public final OperationFuture<AsyncRetrieveContextsResponse,AsyncRetrieveContextsOperationMetadata> asyncRetrieveContextsAsync(String parent, RagQuery query)

Asynchronous API to retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       RagQuery query = RagQuery.newBuilder().build();
       AsyncRetrieveContextsResponse response =
           vertexRagServiceClient.asyncRetrieveContextsAsync(parent, query).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`query` | `[RagQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagQuery)`  
Required. Single RAG retrieve query.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AsyncRetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsResponse),[AsyncRetrieveContextsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsOperationMetadata)>` |   
  
### asyncRetrieveContextsCallable()
    
    
    public final UnaryCallable<AsyncRetrieveContextsRequest,Operation> asyncRetrieveContextsCallable()

Asynchronous API to retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       AsyncRetrieveContextsRequest request =
           AsyncRetrieveContextsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery(RagQuery.newBuilder().build())
               .addAllTools(new ArrayList<Tool>())
               .build();
       ApiFuture<Operation> future =
           vertexRagServiceClient.asyncRetrieveContextsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AsyncRetrieveContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### asyncRetrieveContextsOperationCallable()
    
    
    public final OperationCallable<AsyncRetrieveContextsRequest,AsyncRetrieveContextsResponse,AsyncRetrieveContextsOperationMetadata> asyncRetrieveContextsOperationCallable()

Asynchronous API to retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       AsyncRetrieveContextsRequest request =
           AsyncRetrieveContextsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery(RagQuery.newBuilder().build())
               .addAllTools(new ArrayList<Tool>())
               .build();
       OperationFuture<AsyncRetrieveContextsResponse, AsyncRetrieveContextsOperationMetadata>
           future =
               vertexRagServiceClient.asyncRetrieveContextsOperationCallable().futureCall(request);
       // Do something.
       AsyncRetrieveContextsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AsyncRetrieveContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsRequest),[AsyncRetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsResponse),[AsyncRetrieveContextsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AsyncRetrieveContextsOperationMetadata)>` |   
  
### augmentPrompt(@Nullable LocationName parent, AugmentPromptRequest.Model model, VertexRagStore vertexRagStore)
    
    
    public final AugmentPromptResponse augmentPrompt(@Nullable LocationName parent, AugmentPromptRequest.Model model, VertexRagStore vertexRagStore)

Given an input prompt, it returns augmented prompt from vertex rag store to guide LLM towards generating grounded responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AugmentPromptRequest.Model model = AugmentPromptRequest.Model.newBuilder().build();
       VertexRagStore vertexRagStore = VertexRagStore.newBuilder().build();
       AugmentPromptResponse response =
           vertexRagServiceClient.augmentPrompt(parent, model, vertexRagStore);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to augment prompt. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`model` | `[AugmentPromptRequest.Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptRequest.Model)`  
Optional. Metadata of the backend deployed model.  
`vertexRagStore` | `[VertexRagStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagStore)`  
Optional. Retrieves contexts from the Vertex RagStore.  
**Returns**  
---  
**Type** | **Description**  
`[AugmentPromptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptResponse)` |   
  
### augmentPrompt(AugmentPromptRequest request)
    
    
    public final AugmentPromptResponse augmentPrompt(AugmentPromptRequest request)

Given an input prompt, it returns augmented prompt from vertex rag store to guide LLM towards generating grounded responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       AugmentPromptRequest request =
           AugmentPromptRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllContents(new ArrayList<Content>())
               .setModel(AugmentPromptRequest.Model.newBuilder().build())
               .build();
       AugmentPromptResponse response = vertexRagServiceClient.augmentPrompt(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AugmentPromptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AugmentPromptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptResponse)` |   
  
### augmentPrompt(String parent, AugmentPromptRequest.Model model, VertexRagStore vertexRagStore)
    
    
    public final AugmentPromptResponse augmentPrompt(String parent, AugmentPromptRequest.Model model, VertexRagStore vertexRagStore)

Given an input prompt, it returns augmented prompt from vertex rag store to guide LLM towards generating grounded responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AugmentPromptRequest.Model model = AugmentPromptRequest.Model.newBuilder().build();
       VertexRagStore vertexRagStore = VertexRagStore.newBuilder().build();
       AugmentPromptResponse response =
           vertexRagServiceClient.augmentPrompt(parent, model, vertexRagStore);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to augment prompt. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`model` | `[AugmentPromptRequest.Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptRequest.Model)`  
Optional. Metadata of the backend deployed model.  
`vertexRagStore` | `[VertexRagStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagStore)`  
Optional. Retrieves contexts from the Vertex RagStore.  
**Returns**  
---  
**Type** | **Description**  
`[AugmentPromptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptResponse)` |   
  
### augmentPromptCallable()
    
    
    public final UnaryCallable<AugmentPromptRequest,AugmentPromptResponse> augmentPromptCallable()

Given an input prompt, it returns augmented prompt from vertex rag store to guide LLM towards generating grounded responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       AugmentPromptRequest request =
           AugmentPromptRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllContents(new ArrayList<Content>())
               .setModel(AugmentPromptRequest.Model.newBuilder().build())
               .build();
       ApiFuture<AugmentPromptResponse> future =
           vertexRagServiceClient.augmentPromptCallable().futureCall(request);
       // Do something.
       AugmentPromptResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AugmentPromptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptRequest),[AugmentPromptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AugmentPromptResponse)>` |   
  
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

### corroborateContent(@Nullable LocationName parent, Content content, List<Fact> facts)
    
    
    public final CorroborateContentResponse corroborateContent(@Nullable LocationName parent, Content content, List<Fact> facts)

Given an input text, it returns a score that evaluates the factuality of the text. It also extracts and returns claims from the text and provides supporting facts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Content content = Content.newBuilder().build();
       List<Fact> facts = new ArrayList<>();
       CorroborateContentResponse response =
           vertexRagServiceClient.corroborateContent(parent, content, facts);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to corroborate text. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`content` | `[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Content)`  
Optional. Input content to corroborate, only text format is supported for now.  
`facts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Fact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Fact)>`  
Optional. Facts used to generate the text can also be used to corroborate the text.  
**Returns**  
---  
**Type** | **Description**  
`[CorroborateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CorroborateContentResponse)` |   
  
### corroborateContent(CorroborateContentRequest request)
    
    
    public final CorroborateContentResponse corroborateContent(CorroborateContentRequest request)

Given an input text, it returns a score that evaluates the factuality of the text. It also extracts and returns claims from the text and provides supporting facts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       CorroborateContentRequest request =
           CorroborateContentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setContent(Content.newBuilder().build())
               .addAllFacts(new ArrayList<Fact>())
               .setParameters(CorroborateContentRequest.Parameters.newBuilder().build())
               .build();
       CorroborateContentResponse response = vertexRagServiceClient.corroborateContent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CorroborateContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CorroborateContentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CorroborateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CorroborateContentResponse)` |   
  
### corroborateContent(String parent, Content content, List<Fact> facts)
    
    
    public final CorroborateContentResponse corroborateContent(String parent, Content content, List<Fact> facts)

Given an input text, it returns a score that evaluates the factuality of the text. It also extracts and returns claims from the text and provides supporting facts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Content content = Content.newBuilder().build();
       List<Fact> facts = new ArrayList<>();
       CorroborateContentResponse response =
           vertexRagServiceClient.corroborateContent(parent, content, facts);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to corroborate text. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`content` | `[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Content)`  
Optional. Input content to corroborate, only text format is supported for now.  
`facts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Fact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Fact)>`  
Optional. Facts used to generate the text can also be used to corroborate the text.  
**Returns**  
---  
**Type** | **Description**  
`[CorroborateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CorroborateContentResponse)` |   
  
### corroborateContentCallable()
    
    
    public final UnaryCallable<CorroborateContentRequest,CorroborateContentResponse> corroborateContentCallable()

Given an input text, it returns a score that evaluates the factuality of the text. It also extracts and returns claims from the text and provides supporting facts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       CorroborateContentRequest request =
           CorroborateContentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setContent(Content.newBuilder().build())
               .addAllFacts(new ArrayList<Fact>())
               .setParameters(CorroborateContentRequest.Parameters.newBuilder().build())
               .build();
       ApiFuture<CorroborateContentResponse> future =
           vertexRagServiceClient.corroborateContentCallable().futureCall(request);
       // Do something.
       CorroborateContentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CorroborateContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CorroborateContentRequest),[CorroborateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CorroborateContentResponse)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = vertexRagServiceClient.getIamPolicy(request);
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
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = vertexRagServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = vertexRagServiceClient.getLocation(request);
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
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = vertexRagServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable VertexRagServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.VertexRagServiceSettings` |   
  
### getStub()
    
    
    public VertexRagServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[VertexRagServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VertexRagServiceStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final VertexRagServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : vertexRagServiceClient.listLocations(request).iterateAll()) {
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
`[VertexRagServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             vertexRagServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,VertexRagServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           vertexRagServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagServiceClient.ListLocationsPagedResponse)>` |   
  
### retrieveContexts(@Nullable LocationName parent, RagQuery query)
    
    
    public final RetrieveContextsResponse retrieveContexts(@Nullable LocationName parent, RagQuery query)

Retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RagQuery query = RagQuery.newBuilder().build();
       RetrieveContextsResponse response = vertexRagServiceClient.retrieveContexts(parent, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`query` | `[RagQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagQuery)`  
Required. Single RAG retrieve query.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrieveContextsResponse)` |   
  
### retrieveContexts(RetrieveContextsRequest request)
    
    
    public final RetrieveContextsResponse retrieveContexts(RetrieveContextsRequest request)

Retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       RetrieveContextsRequest request =
           RetrieveContextsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery(RagQuery.newBuilder().build())
               .build();
       RetrieveContextsResponse response = vertexRagServiceClient.retrieveContexts(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrieveContextsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrieveContextsResponse)` |   
  
### retrieveContexts(String parent, RagQuery query)
    
    
    public final RetrieveContextsResponse retrieveContexts(String parent, RagQuery query)

Retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       RagQuery query = RagQuery.newBuilder().build();
       RetrieveContextsResponse response = vertexRagServiceClient.retrieveContexts(parent, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.  
`query` | `[RagQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagQuery)`  
Required. Single RAG retrieve query.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrieveContextsResponse)` |   
  
### retrieveContextsCallable()
    
    
    public final UnaryCallable<RetrieveContextsRequest,RetrieveContextsResponse> retrieveContextsCallable()

Retrieves relevant contexts for a query.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       RetrieveContextsRequest request =
           RetrieveContextsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery(RagQuery.newBuilder().build())
               .build();
       ApiFuture<RetrieveContextsResponse> future =
           vertexRagServiceClient.retrieveContextsCallable().futureCall(request);
       // Do something.
       RetrieveContextsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RetrieveContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrieveContextsRequest),[RetrieveContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RetrieveContextsResponse)>` |   
  
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
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = vertexRagServiceClient.setIamPolicy(request);
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
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = vertexRagServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = vertexRagServiceClient.testIamPermissions(request);
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
     try (VertexRagServiceClient vertexRagServiceClient = VertexRagServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           vertexRagServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
