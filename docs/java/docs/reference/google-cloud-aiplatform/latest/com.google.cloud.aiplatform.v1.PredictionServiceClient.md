---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient
title: Class PredictionServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:10.201129+00:00
---

# Class PredictionServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PredictionServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/PredictionServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for online predictions and explanations.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       EndpointName endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       List<Value> instances = new ArrayList<>();
       Value parameters = Value.newBuilder().setBoolValue(true).build();
       PredictResponse response = predictionServiceClient.predict(endpoint, instances, parameters);
     }
     

Note: close() needs to be called on the PredictionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Predict |  Perform an online prediction. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * predict(PredictRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * predict(EndpointName endpoint, List<Value> instances, Value parameters) 
  * predict(String endpoint, List<Value> instances, Value parameters) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * predictCallable() 

  
RawPredict |  Perform an online prediction with an arbitrary HTTP payload.  The response includes the following HTTP headers: 

  * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. 


  * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rawPredict(RawPredictRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * rawPredict(EndpointName endpoint, HttpBody httpBody) 
  * rawPredict(String endpoint, HttpBody httpBody) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rawPredictCallable() 

  
StreamRawPredict |  Perform a streaming online prediction with an arbitrary HTTP payload. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamRawPredictCallable() 

  
DirectPredict |  Perform an unary online prediction request to a gRPC model server for Vertex first-party products and frameworks. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * directPredict(DirectPredictRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * directPredictCallable() 

  
DirectRawPredict |  Perform an unary online prediction request to a gRPC model server for custom containers. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * directRawPredict(DirectRawPredictRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * directRawPredictCallable() 

  
StreamDirectPredict |  Perform a streaming online prediction request to a gRPC model server for Vertex first-party products and frameworks. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamDirectPredictCallable() 

  
StreamDirectRawPredict |  Perform a streaming online prediction request to a gRPC model server for custom containers. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamDirectRawPredictCallable() 

  
StreamingPredict |  Perform a streaming online prediction request for Vertex first-party products and frameworks. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamingPredictCallable() 

  
ServerStreamingPredict |  Perform a server-side streaming online prediction request for Vertex LLM streaming. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * serverStreamingPredictCallable() 

  
StreamingRawPredict |  Perform a streaming online prediction request through gRPC. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamingRawPredictCallable() 

  
Explain |  Perform an online explanation.  If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * explain(ExplainRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * explain(EndpointName endpoint, List<Value> instances, Value parameters, String deployedModelId) 
  * explain(String endpoint, List<Value> instances, Value parameters, String deployedModelId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * explainCallable() 

  
GenerateContent |  Generate content with multimodal inputs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateContent(GenerateContentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * generateContent(String model, List<Content> contents) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateContentCallable() 

  
StreamGenerateContent |  Generate content with multimodal inputs with streaming support. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamGenerateContentCallable() 

  
EmbedContent |  Embed content with multimodal inputs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * embedContent(EmbedContentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * embedContent(EndpointName model, Content content) 
  * embedContent(String model, Content content) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * embedContentCallable() 

  
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

This class can be customized by passing in a custom instance of PredictionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PredictionServiceSettings predictionServiceSettings =
         PredictionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PredictionServiceClient predictionServiceClient =
         PredictionServiceClient.create(predictionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PredictionServiceSettings predictionServiceSettings =
         PredictionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PredictionServiceClient predictionServiceClient =
         PredictionServiceClient.create(predictionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PredictionServiceClient

## Static Methods 

### create()
    
    
    public static final PredictionServiceClient create()

Constructs an instance of PredictionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PredictionServiceSettings settings)
    
    
    public static final PredictionServiceClient create(PredictionServiceSettings settings)

Constructs an instance of PredictionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PredictionServiceStub stub)
    
    
    public static final PredictionServiceClient create(PredictionServiceStub stub)

Constructs an instance of PredictionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PredictionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PredictionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PredictionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient)` |   
  
## Constructors 

### PredictionServiceClient(PredictionServiceSettings settings)
    
    
    protected PredictionServiceClient(PredictionServiceSettings settings)

Constructs an instance of PredictionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings)`  
  
  
### PredictionServiceClient(PredictionServiceStub stub)
    
    
    protected PredictionServiceClient(PredictionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PredictionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PredictionServiceStub)`  
  
  
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

### directPredict(DirectPredictRequest request)
    
    
    public final DirectPredictResponse directPredict(DirectPredictRequest request)

Perform an unary online prediction request to a gRPC model server for Vertex first-party products and frameworks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       DirectPredictRequest request =
           DirectPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInputs(new ArrayList<Tensor>())
               .setParameters(Tensor.newBuilder().build())
               .build();
       DirectPredictResponse response = predictionServiceClient.directPredict(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DirectPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectPredictRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DirectPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectPredictResponse)` |   
  
### directPredictCallable()
    
    
    public final UnaryCallable<DirectPredictRequest,DirectPredictResponse> directPredictCallable()

Perform an unary online prediction request to a gRPC model server for Vertex first-party products and frameworks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       DirectPredictRequest request =
           DirectPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInputs(new ArrayList<Tensor>())
               .setParameters(Tensor.newBuilder().build())
               .build();
       ApiFuture<DirectPredictResponse> future =
           predictionServiceClient.directPredictCallable().futureCall(request);
       // Do something.
       DirectPredictResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DirectPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectPredictRequest),[DirectPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectPredictResponse)>` |   
  
### directRawPredict(DirectRawPredictRequest request)
    
    
    public final DirectRawPredictResponse directRawPredict(DirectRawPredictRequest request)

Perform an unary online prediction request to a gRPC model server for custom containers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       DirectRawPredictRequest request =
           DirectRawPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setMethodName("methodName-723163380")
               .setInput(ByteString.EMPTY)
               .build();
       DirectRawPredictResponse response = predictionServiceClient.directRawPredict(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DirectRawPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectRawPredictRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DirectRawPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectRawPredictResponse)` |   
  
### directRawPredictCallable()
    
    
    public final UnaryCallable<DirectRawPredictRequest,DirectRawPredictResponse> directRawPredictCallable()

Perform an unary online prediction request to a gRPC model server for custom containers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       DirectRawPredictRequest request =
           DirectRawPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setMethodName("methodName-723163380")
               .setInput(ByteString.EMPTY)
               .build();
       ApiFuture<DirectRawPredictResponse> future =
           predictionServiceClient.directRawPredictCallable().futureCall(request);
       // Do something.
       DirectRawPredictResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DirectRawPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectRawPredictRequest),[DirectRawPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DirectRawPredictResponse)>` |   
  
### embedContent(@Nullable EndpointName model, Content content)
    
    
    public final EmbedContentResponse embedContent(@Nullable EndpointName model, Content content)

Embed content with multimodal inputs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       EndpointName model =
           EndpointName.ofProjectLocationPublisherModelName(
               "[PROJECT]", "[LOCATION]", "[PUBLISHER]", "[MODEL]");
       Content content = Content.newBuilder().build();
       EmbedContentResponse response = predictionServiceClient.embedContent(model, content);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`model` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the publisher model requested to serve the prediction. Format: `projects/{project}/locations/{location}/publishers/*/models/*`  
`content` | `[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Content)`  
Required. Input content to be embedded.  
**Returns**  
---  
**Type** | **Description**  
`[EmbedContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EmbedContentResponse)` |   
  
### embedContent(EmbedContentRequest request)
    
    
    public final EmbedContentResponse embedContent(EmbedContentRequest request)

Embed content with multimodal inputs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       EmbedContentRequest request =
           EmbedContentRequest.newBuilder()
               .setModel(
                   EndpointName.ofProjectLocationPublisherModelName(
                           "[PROJECT]", "[LOCATION]", "[PUBLISHER]", "[MODEL]")
                       .toString())
               .setContent(Content.newBuilder().build())
               .setTitle("title110371416")
               .setOutputDimensionality(-495931909)
               .setAutoTruncate(true)
               .setEmbedContentConfig(EmbedContentRequest.EmbedContentConfig.newBuilder().build())
               .build();
       EmbedContentResponse response = predictionServiceClient.embedContent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EmbedContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EmbedContentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EmbedContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EmbedContentResponse)` |   
  
### embedContent(String model, Content content)
    
    
    public final EmbedContentResponse embedContent(String model, Content content)

Embed content with multimodal inputs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       String model =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       Content content = Content.newBuilder().build();
       EmbedContentResponse response = predictionServiceClient.embedContent(model, content);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`model` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the publisher model requested to serve the prediction. Format: `projects/{project}/locations/{location}/publishers/*/models/*`  
`content` | `[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Content)`  
Required. Input content to be embedded.  
**Returns**  
---  
**Type** | **Description**  
`[EmbedContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EmbedContentResponse)` |   
  
### embedContentCallable()
    
    
    public final UnaryCallable<EmbedContentRequest,EmbedContentResponse> embedContentCallable()

Embed content with multimodal inputs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       EmbedContentRequest request =
           EmbedContentRequest.newBuilder()
               .setModel(
                   EndpointName.ofProjectLocationPublisherModelName(
                           "[PROJECT]", "[LOCATION]", "[PUBLISHER]", "[MODEL]")
                       .toString())
               .setContent(Content.newBuilder().build())
               .setTitle("title110371416")
               .setOutputDimensionality(-495931909)
               .setAutoTruncate(true)
               .setEmbedContentConfig(EmbedContentRequest.EmbedContentConfig.newBuilder().build())
               .build();
       ApiFuture<EmbedContentResponse> future =
           predictionServiceClient.embedContentCallable().futureCall(request);
       // Do something.
       EmbedContentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EmbedContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EmbedContentRequest),[EmbedContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EmbedContentResponse)>` |   
  
### explain(@Nullable EndpointName endpoint, List<Value> instances, Value parameters, String deployedModelId)
    
    
    public final ExplainResponse explain(@Nullable EndpointName endpoint, List<Value> instances, Value parameters, String deployedModelId)

Perform an online explanation.

If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       EndpointName endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       List<Value> instances = new ArrayList<>();
       Value parameters = Value.newBuilder().setBoolValue(true).build();
       String deployedModelId = "deployedModelId-1817547906";
       ExplainResponse response =
           predictionServiceClient.explain(endpoint, instances, parameters, deployedModelId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint requested to serve the explanation. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`instances` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>`  
Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.  
`parameters` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' Model's  PredictSchemata's parameters_schema_uri.  
`deployedModelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding Endpoint.traffic_split.  
**Returns**  
---  
**Type** | **Description**  
`[ExplainResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExplainResponse)` |   
  
### explain(ExplainRequest request)
    
    
    public final ExplainResponse explain(ExplainRequest request)

Perform an online explanation.

If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ExplainRequest request =
           ExplainRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInstances(new ArrayList<Value>())
               .setParameters(Value.newBuilder().setBoolValue(true).build())
               .setExplanationSpecOverride(ExplanationSpecOverride.newBuilder().build())
               .setDeployedModelId("deployedModelId-1817547906")
               .build();
       ExplainResponse response = predictionServiceClient.explain(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExplainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExplainRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExplainResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExplainResponse)` |   
  
### explain(String endpoint, List<Value> instances, Value parameters, String deployedModelId)
    
    
    public final ExplainResponse explain(String endpoint, List<Value> instances, Value parameters, String deployedModelId)

Perform an online explanation.

If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       String endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       List<Value> instances = new ArrayList<>();
       Value parameters = Value.newBuilder().setBoolValue(true).build();
       String deployedModelId = "deployedModelId-1817547906";
       ExplainResponse response =
           predictionServiceClient.explain(endpoint, instances, parameters, deployedModelId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint requested to serve the explanation. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`instances` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>`  
Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.  
`parameters` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' Model's  PredictSchemata's parameters_schema_uri.  
`deployedModelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding Endpoint.traffic_split.  
**Returns**  
---  
**Type** | **Description**  
`[ExplainResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExplainResponse)` |   
  
### explainCallable()
    
    
    public final UnaryCallable<ExplainRequest,ExplainResponse> explainCallable()

Perform an online explanation.

If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ExplainRequest request =
           ExplainRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInstances(new ArrayList<Value>())
               .setParameters(Value.newBuilder().setBoolValue(true).build())
               .setExplanationSpecOverride(ExplanationSpecOverride.newBuilder().build())
               .setDeployedModelId("deployedModelId-1817547906")
               .build();
       ApiFuture<ExplainResponse> future =
           predictionServiceClient.explainCallable().futureCall(request);
       // Do something.
       ExplainResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExplainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExplainRequest),[ExplainResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExplainResponse)>` |   
  
### generateContent(GenerateContentRequest request)
    
    
    public final GenerateContentResponse generateContent(GenerateContentRequest request)

Generate content with multimodal inputs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       GenerateContentRequest request =
           GenerateContentRequest.newBuilder()
               .setModel("model104069929")
               .addAllContents(new ArrayList<Content>())
               .setSystemInstruction(Content.newBuilder().build())
               .setCachedContent(
                   CachedContentName.of("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]").toString())
               .addAllTools(new ArrayList<Tool>())
               .setToolConfig(ToolConfig.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .addAllSafetySettings(new ArrayList<SafetySetting>())
               .setModelArmorConfig(ModelArmorConfig.newBuilder().build())
               .setGenerationConfig(GenerationConfig.newBuilder().build())
               .build();
       GenerateContentResponse response = predictionServiceClient.generateContent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenerateContentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenerateContentResponse)` |   
  
### generateContent(String model, List<Content> contents)
    
    
    public final GenerateContentResponse generateContent(String model, List<Content> contents)

Generate content with multimodal inputs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       String model = "model104069929";
       List<Content> contents = new ArrayList<>();
       GenerateContentResponse response = predictionServiceClient.generateContent(model, contents);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`model` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The fully qualified name of the publisher model or tuned model endpoint to use. Publisher model format: `projects/{project}/locations/{location}/publishers/*/models/*` Tuned model endpoint format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`contents` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Content)>`  
Required. The content of the current conversation with the model. For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history + latest request.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenerateContentResponse)` |   
  
### generateContentCallable()
    
    
    public final UnaryCallable<GenerateContentRequest,GenerateContentResponse> generateContentCallable()

Generate content with multimodal inputs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       GenerateContentRequest request =
           GenerateContentRequest.newBuilder()
               .setModel("model104069929")
               .addAllContents(new ArrayList<Content>())
               .setSystemInstruction(Content.newBuilder().build())
               .setCachedContent(
                   CachedContentName.of("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]").toString())
               .addAllTools(new ArrayList<Tool>())
               .setToolConfig(ToolConfig.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .addAllSafetySettings(new ArrayList<SafetySetting>())
               .setModelArmorConfig(ModelArmorConfig.newBuilder().build())
               .setGenerationConfig(GenerationConfig.newBuilder().build())
               .build();
       ApiFuture<GenerateContentResponse> future =
           predictionServiceClient.generateContentCallable().futureCall(request);
       // Do something.
       GenerateContentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenerateContentRequest),[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenerateContentResponse)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = predictionServiceClient.getIamPolicy(request);
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
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = predictionServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = predictionServiceClient.getLocation(request);
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
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           predictionServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable PredictionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PredictionServiceSettings` |   
  
### getStub()
    
    
    public PredictionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PredictionServiceStub)` |   
  
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
    
    
    public final PredictionServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : predictionServiceClient.listLocations(request).iterateAll()) {
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
`[PredictionServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             predictionServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,PredictionServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           predictionServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.ListLocationsPagedResponse)>` |   
  
### predict(@Nullable EndpointName endpoint, List<Value> instances, Value parameters)
    
    
    public final PredictResponse predict(@Nullable EndpointName endpoint, List<Value> instances, Value parameters)

Perform an online prediction.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       EndpointName endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       List<Value> instances = new ArrayList<>();
       Value parameters = Value.newBuilder().setBoolValue(true).build();
       PredictResponse response = predictionServiceClient.predict(endpoint, instances, parameters);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`instances` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>`  
Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.  
`parameters` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' Model's  PredictSchemata's parameters_schema_uri.  
**Returns**  
---  
**Type** | **Description**  
`[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse)` |   
  
### predict(PredictRequest request)
    
    
    public final PredictResponse predict(PredictRequest request)

Perform an online prediction.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       PredictRequest request =
           PredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInstances(new ArrayList<Value>())
               .setParameters(Value.newBuilder().setBoolValue(true).build())
               .putAllLabels(new HashMap<String, String>())
               .build();
       PredictResponse response = predictionServiceClient.predict(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse)` |   
  
### predict(String endpoint, List<Value> instances, Value parameters)
    
    
    public final PredictResponse predict(String endpoint, List<Value> instances, Value parameters)

Perform an online prediction.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       String endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       List<Value> instances = new ArrayList<>();
       Value parameters = Value.newBuilder().setBoolValue(true).build();
       PredictResponse response = predictionServiceClient.predict(endpoint, instances, parameters);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`instances` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>`  
Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.  
`parameters` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' Model's  PredictSchemata's parameters_schema_uri.  
**Returns**  
---  
**Type** | **Description**  
`[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse)` |   
  
### predictCallable()
    
    
    public final UnaryCallable<PredictRequest,PredictResponse> predictCallable()

Perform an online prediction.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       PredictRequest request =
           PredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInstances(new ArrayList<Value>())
               .setParameters(Value.newBuilder().setBoolValue(true).build())
               .putAllLabels(new HashMap<String, String>())
               .build();
       ApiFuture<PredictResponse> future =
           predictionServiceClient.predictCallable().futureCall(request);
       // Do something.
       PredictResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest),[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse)>` |   
  
### rawPredict(@Nullable EndpointName endpoint, HttpBody httpBody)
    
    
    public final HttpBody rawPredict(@Nullable EndpointName endpoint, HttpBody httpBody)

Perform an online prediction with an arbitrary HTTP payload.

The response includes the following HTTP headers:

  * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. 


  * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       EndpointName endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       HttpBody httpBody = HttpBody.newBuilder().build();
       HttpBody response = predictionServiceClient.rawPredict(endpoint, httpBody);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`httpBody` | `com.google.api.HttpBody`  
The prediction input. Supports HTTP headers and arbitrary data payload. A DeployedModel may have an upper limit on the number of instances it supports per request. When this limit it is exceeded for an AutoML model, the RawPredict method returns an error. When this limit is exceeded for a custom-trained model, the behavior varies depending on the model. You can specify the schema for each instance in the predict_schemata.instance_schema_uri field when you create a Model. This schema applies when you deploy the `Model` as a `DeployedModel` to an Endpoint and use the `RawPredict` method.  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.HttpBody` |   
  
### rawPredict(RawPredictRequest request)
    
    
    public final HttpBody rawPredict(RawPredictRequest request)

Perform an online prediction with an arbitrary HTTP payload.

The response includes the following HTTP headers:

  * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. 


  * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       RawPredictRequest request =
           RawPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setHttpBody(HttpBody.newBuilder().build())
               .build();
       HttpBody response = predictionServiceClient.rawPredict(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RawPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RawPredictRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.HttpBody` |   
  
### rawPredict(String endpoint, HttpBody httpBody)
    
    
    public final HttpBody rawPredict(String endpoint, HttpBody httpBody)

Perform an online prediction with an arbitrary HTTP payload.

The response includes the following HTTP headers:

  * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. 


  * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       String endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       HttpBody httpBody = HttpBody.newBuilder().build();
       HttpBody response = predictionServiceClient.rawPredict(endpoint, httpBody);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`httpBody` | `com.google.api.HttpBody`  
The prediction input. Supports HTTP headers and arbitrary data payload. A DeployedModel may have an upper limit on the number of instances it supports per request. When this limit it is exceeded for an AutoML model, the RawPredict method returns an error. When this limit is exceeded for a custom-trained model, the behavior varies depending on the model. You can specify the schema for each instance in the predict_schemata.instance_schema_uri field when you create a Model. This schema applies when you deploy the `Model` as a `DeployedModel` to an Endpoint and use the `RawPredict` method.  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.HttpBody` |   
  
### rawPredictCallable()
    
    
    public final UnaryCallable<RawPredictRequest,HttpBody> rawPredictCallable()

Perform an online prediction with an arbitrary HTTP payload.

The response includes the following HTTP headers:

  * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. 


  * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       RawPredictRequest request =
           RawPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setHttpBody(HttpBody.newBuilder().build())
               .build();
       ApiFuture<HttpBody> future = predictionServiceClient.rawPredictCallable().futureCall(request);
       // Do something.
       HttpBody response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RawPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RawPredictRequest),com.google.api.HttpBody>` |   
  
### serverStreamingPredictCallable()
    
    
    public final ServerStreamingCallable<StreamingPredictRequest,StreamingPredictResponse> serverStreamingPredictCallable()

Perform a server-side streaming online prediction request for Vertex LLM streaming.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       StreamingPredictRequest request =
           StreamingPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInputs(new ArrayList<Tensor>())
               .setParameters(Tensor.newBuilder().build())
               .build();
       ServerStream<StreamingPredictResponse> stream =
           predictionServiceClient.serverStreamingPredictCallable().call(request);
       for (StreamingPredictResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[StreamingPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamingPredictRequest),[StreamingPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamingPredictResponse)>` |   
  
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
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = predictionServiceClient.setIamPolicy(request);
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
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = predictionServiceClient.setIamPolicyCallable().futureCall(request);
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

### streamDirectPredictCallable()
    
    
    public final BidiStreamingCallable<StreamDirectPredictRequest,StreamDirectPredictResponse> streamDirectPredictCallable()

Perform a streaming online prediction request to a gRPC model server for Vertex first-party products and frameworks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       BidiStream<StreamDirectPredictRequest, StreamDirectPredictResponse> bidiStream =
           predictionServiceClient.streamDirectPredictCallable().call();
       StreamDirectPredictRequest request =
           StreamDirectPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInputs(new ArrayList<Tensor>())
               .setParameters(Tensor.newBuilder().build())
               .build();
       bidiStream.send(request);
       for (StreamDirectPredictResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamDirectPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamDirectPredictRequest),[StreamDirectPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamDirectPredictResponse)>` |   
  
### streamDirectRawPredictCallable()
    
    
    public final BidiStreamingCallable<StreamDirectRawPredictRequest,StreamDirectRawPredictResponse> streamDirectRawPredictCallable()

Perform a streaming online prediction request to a gRPC model server for custom containers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       BidiStream<StreamDirectRawPredictRequest, StreamDirectRawPredictResponse> bidiStream =
           predictionServiceClient.streamDirectRawPredictCallable().call();
       StreamDirectRawPredictRequest request =
           StreamDirectRawPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setMethodName("methodName-723163380")
               .setInput(ByteString.EMPTY)
               .build();
       bidiStream.send(request);
       for (StreamDirectRawPredictResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamDirectRawPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamDirectRawPredictRequest),[StreamDirectRawPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamDirectRawPredictResponse)>` |   
  
### streamGenerateContentCallable()
    
    
    public final ServerStreamingCallable<GenerateContentRequest,GenerateContentResponse> streamGenerateContentCallable()

Generate content with multimodal inputs with streaming support.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       GenerateContentRequest request =
           GenerateContentRequest.newBuilder()
               .setModel("model104069929")
               .addAllContents(new ArrayList<Content>())
               .setSystemInstruction(Content.newBuilder().build())
               .setCachedContent(
                   CachedContentName.of("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]").toString())
               .addAllTools(new ArrayList<Tool>())
               .setToolConfig(ToolConfig.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .addAllSafetySettings(new ArrayList<SafetySetting>())
               .setModelArmorConfig(ModelArmorConfig.newBuilder().build())
               .setGenerationConfig(GenerationConfig.newBuilder().build())
               .build();
       ServerStream<GenerateContentResponse> stream =
           predictionServiceClient.streamGenerateContentCallable().call(request);
       for (GenerateContentResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[GenerateContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenerateContentRequest),[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenerateContentResponse)>` |   
  
### streamRawPredictCallable()
    
    
    public final ServerStreamingCallable<StreamRawPredictRequest,HttpBody> streamRawPredictCallable()

Perform a streaming online prediction with an arbitrary HTTP payload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       StreamRawPredictRequest request =
           StreamRawPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setHttpBody(HttpBody.newBuilder().build())
               .build();
       ServerStream<HttpBody> stream =
           predictionServiceClient.streamRawPredictCallable().call(request);
       for (HttpBody response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[StreamRawPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamRawPredictRequest),com.google.api.HttpBody>` |   
  
### streamingPredictCallable()
    
    
    public final BidiStreamingCallable<StreamingPredictRequest,StreamingPredictResponse> streamingPredictCallable()

Perform a streaming online prediction request for Vertex first-party products and frameworks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       BidiStream<StreamingPredictRequest, StreamingPredictResponse> bidiStream =
           predictionServiceClient.streamingPredictCallable().call();
       StreamingPredictRequest request =
           StreamingPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllInputs(new ArrayList<Tensor>())
               .setParameters(Tensor.newBuilder().build())
               .build();
       bidiStream.send(request);
       for (StreamingPredictResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamingPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamingPredictRequest),[StreamingPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamingPredictResponse)>` |   
  
### streamingRawPredictCallable()
    
    
    public final BidiStreamingCallable<StreamingRawPredictRequest,StreamingRawPredictResponse> streamingRawPredictCallable()

Perform a streaming online prediction request through gRPC.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       BidiStream<StreamingRawPredictRequest, StreamingRawPredictResponse> bidiStream =
           predictionServiceClient.streamingRawPredictCallable().call();
       StreamingRawPredictRequest request =
           StreamingRawPredictRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setMethodName("methodName-723163380")
               .setInput(ByteString.EMPTY)
               .build();
       bidiStream.send(request);
       for (StreamingRawPredictResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamingRawPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamingRawPredictRequest),[StreamingRawPredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamingRawPredictResponse)>` |   
  
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
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = predictionServiceClient.testIamPermissions(request);
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
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           predictionServiceClient.testIamPermissionsCallable().futureCall(request);
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
