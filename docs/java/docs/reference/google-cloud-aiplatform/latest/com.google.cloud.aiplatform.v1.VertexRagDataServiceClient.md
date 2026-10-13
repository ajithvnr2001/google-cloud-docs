---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient
title: Class VertexRagDataServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:38.723367+00:00
---

# Class VertexRagDataServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VertexRagDataServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/VertexRagDataServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for managing user data for RAG.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagCorpusName name = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]");
       RagCorpus response = vertexRagDataServiceClient.getRagCorpus(name);
     }
     

Note: close() needs to be called on the VertexRagDataServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateRagCorpus |  Creates a RagCorpus. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRagCorpusAsync(CreateRagCorpusRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createRagCorpusAsync(LocationName parent, RagCorpus ragCorpus) 
  * createRagCorpusAsync(String parent, RagCorpus ragCorpus) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRagCorpusOperationCallable() 
  * createRagCorpusCallable() 

  
UpdateRagCorpus |  Updates a RagCorpus. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRagCorpusAsync(UpdateRagCorpusRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateRagCorpusAsync(RagCorpus ragCorpus) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRagCorpusOperationCallable() 
  * updateRagCorpusCallable() 

  
GetRagCorpus |  Gets a RagCorpus. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRagCorpus(GetRagCorpusRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRagCorpus(RagCorpusName name) 
  * getRagCorpus(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRagCorpusCallable() 

  
ListRagCorpora |  Lists RagCorpora in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRagCorpora(ListRagCorporaRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRagCorpora(LocationName parent) 
  * listRagCorpora(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRagCorporaPagedCallable() 
  * listRagCorporaCallable() 

  
DeleteRagCorpus |  Deletes a RagCorpus. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRagCorpusAsync(DeleteRagCorpusRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRagCorpusAsync(RagCorpusName name) 
  * deleteRagCorpusAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRagCorpusOperationCallable() 
  * deleteRagCorpusCallable() 

  
UploadRagFile |  Upload a file into a RagCorpus. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * uploadRagFile(UploadRagFileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * uploadRagFile(RagCorpusName parent, RagFile ragFile, UploadRagFileConfig uploadRagFileConfig) 
  * uploadRagFile(String parent, RagFile ragFile, UploadRagFileConfig uploadRagFileConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * uploadRagFileCallable() 

  
ImportRagFiles |  Import files from Google Cloud Storage or Google Drive into a RagCorpus. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importRagFilesAsync(ImportRagFilesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importRagFilesAsync(RagCorpusName parent, ImportRagFilesConfig importRagFilesConfig) 
  * importRagFilesAsync(String parent, ImportRagFilesConfig importRagFilesConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importRagFilesOperationCallable() 
  * importRagFilesCallable() 

  
GetRagFile |  Gets a RagFile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRagFile(GetRagFileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRagFile(RagFileName name) 
  * getRagFile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRagFileCallable() 

  
ListRagFiles |  Lists RagFiles in a RagCorpus. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRagFiles(ListRagFilesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRagFiles(RagCorpusName parent) 
  * listRagFiles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRagFilesPagedCallable() 
  * listRagFilesCallable() 

  
DeleteRagFile |  Deletes a RagFile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRagFileAsync(DeleteRagFileRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRagFileAsync(RagFileName name) 
  * deleteRagFileAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRagFileOperationCallable() 
  * deleteRagFileCallable() 

  
UpdateRagEngineConfig |  Updates a RagEngineConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRagEngineConfigAsync(UpdateRagEngineConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateRagEngineConfigAsync(RagEngineConfig ragEngineConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRagEngineConfigOperationCallable() 
  * updateRagEngineConfigCallable() 

  
GetRagEngineConfig |  Gets a RagEngineConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRagEngineConfig(GetRagEngineConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRagEngineConfig(RagEngineConfigName name) 
  * getRagEngineConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRagEngineConfigCallable() 

  
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

This class can be customized by passing in a custom instance of VertexRagDataServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VertexRagDataServiceSettings vertexRagDataServiceSettings =
         VertexRagDataServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create(vertexRagDataServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VertexRagDataServiceSettings vertexRagDataServiceSettings =
         VertexRagDataServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create(vertexRagDataServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VertexRagDataServiceClient

## Static Methods 

### create()
    
    
    public static final VertexRagDataServiceClient create()

Constructs an instance of VertexRagDataServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VertexRagDataServiceSettings settings)
    
    
    public static final VertexRagDataServiceClient create(VertexRagDataServiceSettings settings)

Constructs an instance of VertexRagDataServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VertexRagDataServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VertexRagDataServiceStub stub)
    
    
    public static final VertexRagDataServiceClient create(VertexRagDataServiceStub stub)

Constructs an instance of VertexRagDataServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(VertexRagDataServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VertexRagDataServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VertexRagDataServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient)` |   
  
## Constructors 

### VertexRagDataServiceClient(VertexRagDataServiceSettings settings)
    
    
    protected VertexRagDataServiceClient(VertexRagDataServiceSettings settings)

Constructs an instance of VertexRagDataServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VertexRagDataServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceSettings)`  
  
  
### VertexRagDataServiceClient(VertexRagDataServiceStub stub)
    
    
    protected VertexRagDataServiceClient(VertexRagDataServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VertexRagDataServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VertexRagDataServiceStub)`  
  
  
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

### createRagCorpusAsync(@Nullable LocationName parent, RagCorpus ragCorpus)
    
    
    public final OperationFuture<RagCorpus,CreateRagCorpusOperationMetadata> createRagCorpusAsync(@Nullable LocationName parent, RagCorpus ragCorpus)

Creates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RagCorpus ragCorpus = RagCorpus.newBuilder().build();
       RagCorpus response = vertexRagDataServiceClient.createRagCorpusAsync(parent, ragCorpus).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the RagCorpus in. Format: `projects/{project}/locations/{location}`  
`ragCorpus` | `[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus)`  
Required. The RagCorpus to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus),[CreateRagCorpusOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateRagCorpusOperationMetadata)>` |   
  
### createRagCorpusAsync(CreateRagCorpusRequest request)
    
    
    public final OperationFuture<RagCorpus,CreateRagCorpusOperationMetadata> createRagCorpusAsync(CreateRagCorpusRequest request)

Creates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       CreateRagCorpusRequest request =
           CreateRagCorpusRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRagCorpus(RagCorpus.newBuilder().build())
               .build();
       RagCorpus response = vertexRagDataServiceClient.createRagCorpusAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateRagCorpusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus),[CreateRagCorpusOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateRagCorpusOperationMetadata)>` |   
  
### createRagCorpusAsync(String parent, RagCorpus ragCorpus)
    
    
    public final OperationFuture<RagCorpus,CreateRagCorpusOperationMetadata> createRagCorpusAsync(String parent, RagCorpus ragCorpus)

Creates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       RagCorpus ragCorpus = RagCorpus.newBuilder().build();
       RagCorpus response = vertexRagDataServiceClient.createRagCorpusAsync(parent, ragCorpus).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the RagCorpus in. Format: `projects/{project}/locations/{location}`  
`ragCorpus` | `[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus)`  
Required. The RagCorpus to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus),[CreateRagCorpusOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateRagCorpusOperationMetadata)>` |   
  
### createRagCorpusCallable()
    
    
    public final UnaryCallable<CreateRagCorpusRequest,Operation> createRagCorpusCallable()

Creates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       CreateRagCorpusRequest request =
           CreateRagCorpusRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRagCorpus(RagCorpus.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           vertexRagDataServiceClient.createRagCorpusCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateRagCorpusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRagCorpusOperationCallable()
    
    
    public final OperationCallable<CreateRagCorpusRequest,RagCorpus,CreateRagCorpusOperationMetadata> createRagCorpusOperationCallable()

Creates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       CreateRagCorpusRequest request =
           CreateRagCorpusRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRagCorpus(RagCorpus.newBuilder().build())
               .build();
       OperationFuture<RagCorpus, CreateRagCorpusOperationMetadata> future =
           vertexRagDataServiceClient.createRagCorpusOperationCallable().futureCall(request);
       // Do something.
       RagCorpus response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateRagCorpusRequest),[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus),[CreateRagCorpusOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateRagCorpusOperationMetadata)>` |   
  
### deleteRagCorpusAsync(@Nullable RagCorpusName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteRagCorpusAsync(@Nullable RagCorpusName name)

Deletes a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagCorpusName name = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]");
       vertexRagDataServiceClient.deleteRagCorpusAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagCorpusName`  
Required. The name of the RagCorpus resource to be deleted. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteRagCorpusAsync(DeleteRagCorpusRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteRagCorpusAsync(DeleteRagCorpusRequest request)

Deletes a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       DeleteRagCorpusRequest request =
           DeleteRagCorpusRequest.newBuilder()
               .setName(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setForce(true)
               .build();
       vertexRagDataServiceClient.deleteRagCorpusAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteRagCorpusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteRagCorpusAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteRagCorpusAsync(String name)

Deletes a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String name = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString();
       vertexRagDataServiceClient.deleteRagCorpusAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the RagCorpus resource to be deleted. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteRagCorpusCallable()
    
    
    public final UnaryCallable<DeleteRagCorpusRequest,Operation> deleteRagCorpusCallable()

Deletes a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       DeleteRagCorpusRequest request =
           DeleteRagCorpusRequest.newBuilder()
               .setName(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           vertexRagDataServiceClient.deleteRagCorpusCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteRagCorpusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRagCorpusOperationCallable()
    
    
    public final OperationCallable<DeleteRagCorpusRequest,Empty,DeleteOperationMetadata> deleteRagCorpusOperationCallable()

Deletes a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       DeleteRagCorpusRequest request =
           DeleteRagCorpusRequest.newBuilder()
               .setName(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           vertexRagDataServiceClient.deleteRagCorpusOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteRagCorpusRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteRagFileAsync(@Nullable RagFileName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteRagFileAsync(@Nullable RagFileName name)

Deletes a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagFileName name = RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]");
       vertexRagDataServiceClient.deleteRagFileAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagFileName`  
Required. The name of the RagFile resource to be deleted. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragFiles/{rag_file}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteRagFileAsync(DeleteRagFileRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteRagFileAsync(DeleteRagFileRequest request)

Deletes a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       DeleteRagFileRequest request =
           DeleteRagFileRequest.newBuilder()
               .setName(
                   RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]")
                       .toString())
               .build();
       vertexRagDataServiceClient.deleteRagFileAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRagFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteRagFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteRagFileAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteRagFileAsync(String name)

Deletes a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String name =
           RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]").toString();
       vertexRagDataServiceClient.deleteRagFileAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the RagFile resource to be deleted. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragFiles/{rag_file}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteRagFileCallable()
    
    
    public final UnaryCallable<DeleteRagFileRequest,Operation> deleteRagFileCallable()

Deletes a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       DeleteRagFileRequest request =
           DeleteRagFileRequest.newBuilder()
               .setName(
                   RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           vertexRagDataServiceClient.deleteRagFileCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRagFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteRagFileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRagFileOperationCallable()
    
    
    public final OperationCallable<DeleteRagFileRequest,Empty,DeleteOperationMetadata> deleteRagFileOperationCallable()

Deletes a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       DeleteRagFileRequest request =
           DeleteRagFileRequest.newBuilder()
               .setName(
                   RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           vertexRagDataServiceClient.deleteRagFileOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRagFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteRagFileRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = vertexRagDataServiceClient.getIamPolicy(request);
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
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           vertexRagDataServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = vertexRagDataServiceClient.getLocation(request);
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
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           vertexRagDataServiceClient.getLocationCallable().futureCall(request);
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
  
### getRagCorpus(@Nullable RagCorpusName name)
    
    
    public final RagCorpus getRagCorpus(@Nullable RagCorpusName name)

Gets a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagCorpusName name = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]");
       RagCorpus response = vertexRagDataServiceClient.getRagCorpus(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagCorpusName`  
Required. The name of the RagCorpus resource. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
**Returns**  
---  
**Type** | **Description**  
`[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus)` |   
  
### getRagCorpus(GetRagCorpusRequest request)
    
    
    public final RagCorpus getRagCorpus(GetRagCorpusRequest request)

Gets a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetRagCorpusRequest request =
           GetRagCorpusRequest.newBuilder()
               .setName(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .build();
       RagCorpus response = vertexRagDataServiceClient.getRagCorpus(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetRagCorpusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus)` |   
  
### getRagCorpus(String name)
    
    
    public final RagCorpus getRagCorpus(String name)

Gets a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String name = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString();
       RagCorpus response = vertexRagDataServiceClient.getRagCorpus(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the RagCorpus resource. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
**Returns**  
---  
**Type** | **Description**  
`[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus)` |   
  
### getRagCorpusCallable()
    
    
    public final UnaryCallable<GetRagCorpusRequest,RagCorpus> getRagCorpusCallable()

Gets a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetRagCorpusRequest request =
           GetRagCorpusRequest.newBuilder()
               .setName(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .build();
       ApiFuture<RagCorpus> future =
           vertexRagDataServiceClient.getRagCorpusCallable().futureCall(request);
       // Do something.
       RagCorpus response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetRagCorpusRequest),[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus)>` |   
  
### getRagEngineConfig(@Nullable RagEngineConfigName name)
    
    
    public final RagEngineConfig getRagEngineConfig(@Nullable RagEngineConfigName name)

Gets a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagEngineConfigName name = RagEngineConfigName.of("[PROJECT]", "[LOCATION]");
       RagEngineConfig response = vertexRagDataServiceClient.getRagEngineConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagEngineConfigName`  
Required. The name of the RagEngineConfig resource. Format: `projects/{project}/locations/{location}/ragEngineConfig`  
**Returns**  
---  
**Type** | **Description**  
`[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig)` |   
  
### getRagEngineConfig(GetRagEngineConfigRequest request)
    
    
    public final RagEngineConfig getRagEngineConfig(GetRagEngineConfigRequest request)

Gets a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetRagEngineConfigRequest request =
           GetRagEngineConfigRequest.newBuilder()
               .setName(RagEngineConfigName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       RagEngineConfig response = vertexRagDataServiceClient.getRagEngineConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRagEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetRagEngineConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig)` |   
  
### getRagEngineConfig(String name)
    
    
    public final RagEngineConfig getRagEngineConfig(String name)

Gets a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String name = RagEngineConfigName.of("[PROJECT]", "[LOCATION]").toString();
       RagEngineConfig response = vertexRagDataServiceClient.getRagEngineConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the RagEngineConfig resource. Format: `projects/{project}/locations/{location}/ragEngineConfig`  
**Returns**  
---  
**Type** | **Description**  
`[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig)` |   
  
### getRagEngineConfigCallable()
    
    
    public final UnaryCallable<GetRagEngineConfigRequest,RagEngineConfig> getRagEngineConfigCallable()

Gets a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetRagEngineConfigRequest request =
           GetRagEngineConfigRequest.newBuilder()
               .setName(RagEngineConfigName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<RagEngineConfig> future =
           vertexRagDataServiceClient.getRagEngineConfigCallable().futureCall(request);
       // Do something.
       RagEngineConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRagEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetRagEngineConfigRequest),[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig)>` |   
  
### getRagFile(@Nullable RagFileName name)
    
    
    public final RagFile getRagFile(@Nullable RagFileName name)

Gets a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagFileName name = RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]");
       RagFile response = vertexRagDataServiceClient.getRagFile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagFileName`  
Required. The name of the RagFile resource. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragFiles/{rag_file}`  
**Returns**  
---  
**Type** | **Description**  
`[RagFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagFile)` |   
  
### getRagFile(GetRagFileRequest request)
    
    
    public final RagFile getRagFile(GetRagFileRequest request)

Gets a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetRagFileRequest request =
           GetRagFileRequest.newBuilder()
               .setName(
                   RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]")
                       .toString())
               .build();
       RagFile response = vertexRagDataServiceClient.getRagFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRagFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetRagFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RagFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagFile)` |   
  
### getRagFile(String name)
    
    
    public final RagFile getRagFile(String name)

Gets a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String name =
           RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]").toString();
       RagFile response = vertexRagDataServiceClient.getRagFile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the RagFile resource. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragFiles/{rag_file}`  
**Returns**  
---  
**Type** | **Description**  
`[RagFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagFile)` |   
  
### getRagFileCallable()
    
    
    public final UnaryCallable<GetRagFileRequest,RagFile> getRagFileCallable()

Gets a RagFile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       GetRagFileRequest request =
           GetRagFileRequest.newBuilder()
               .setName(
                   RagFileName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]", "[RAG_FILE]")
                       .toString())
               .build();
       ApiFuture<RagFile> future =
           vertexRagDataServiceClient.getRagFileCallable().futureCall(request);
       // Do something.
       RagFile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRagFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetRagFileRequest),[RagFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagFile)>` |   
  
### getSettings()
    
    
    public final @Nullable VertexRagDataServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.VertexRagDataServiceSettings` |   
  
### getStub()
    
    
    public VertexRagDataServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VertexRagDataServiceStub)` |   
  
### importRagFilesAsync(@Nullable RagCorpusName parent, ImportRagFilesConfig importRagFilesConfig)
    
    
    public final OperationFuture<ImportRagFilesResponse,ImportRagFilesOperationMetadata> importRagFilesAsync(@Nullable RagCorpusName parent, ImportRagFilesConfig importRagFilesConfig)

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagCorpusName parent = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]");
       ImportRagFilesConfig importRagFilesConfig = ImportRagFilesConfig.newBuilder().build();
       ImportRagFilesResponse response =
           vertexRagDataServiceClient.importRagFilesAsync(parent, importRagFilesConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagCorpusName`  
Required. The name of the RagCorpus resource into which to import files. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
`importRagFilesConfig` | `[ImportRagFilesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesConfig)`  
Required. The config for the RagFiles to be synced and imported into the RagCorpus. VertexRagDataService.ImportRagFiles.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportRagFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesResponse),[ImportRagFilesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesOperationMetadata)>` |   
  
### importRagFilesAsync(ImportRagFilesRequest request)
    
    
    public final OperationFuture<ImportRagFilesResponse,ImportRagFilesOperationMetadata> importRagFilesAsync(ImportRagFilesRequest request)

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ImportRagFilesRequest request =
           ImportRagFilesRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setImportRagFilesConfig(ImportRagFilesConfig.newBuilder().build())
               .build();
       ImportRagFilesResponse response =
           vertexRagDataServiceClient.importRagFilesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportRagFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportRagFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesResponse),[ImportRagFilesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesOperationMetadata)>` |   
  
### importRagFilesAsync(String parent, ImportRagFilesConfig importRagFilesConfig)
    
    
    public final OperationFuture<ImportRagFilesResponse,ImportRagFilesOperationMetadata> importRagFilesAsync(String parent, ImportRagFilesConfig importRagFilesConfig)

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String parent = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString();
       ImportRagFilesConfig importRagFilesConfig = ImportRagFilesConfig.newBuilder().build();
       ImportRagFilesResponse response =
           vertexRagDataServiceClient.importRagFilesAsync(parent, importRagFilesConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the RagCorpus resource into which to import files. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
`importRagFilesConfig` | `[ImportRagFilesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesConfig)`  
Required. The config for the RagFiles to be synced and imported into the RagCorpus. VertexRagDataService.ImportRagFiles.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportRagFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesResponse),[ImportRagFilesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesOperationMetadata)>` |   
  
### importRagFilesCallable()
    
    
    public final UnaryCallable<ImportRagFilesRequest,Operation> importRagFilesCallable()

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ImportRagFilesRequest request =
           ImportRagFilesRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setImportRagFilesConfig(ImportRagFilesConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           vertexRagDataServiceClient.importRagFilesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportRagFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importRagFilesOperationCallable()
    
    
    public final OperationCallable<ImportRagFilesRequest,ImportRagFilesResponse,ImportRagFilesOperationMetadata> importRagFilesOperationCallable()

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ImportRagFilesRequest request =
           ImportRagFilesRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setImportRagFilesConfig(ImportRagFilesConfig.newBuilder().build())
               .build();
       OperationFuture<ImportRagFilesResponse, ImportRagFilesOperationMetadata> future =
           vertexRagDataServiceClient.importRagFilesOperationCallable().futureCall(request);
       // Do something.
       ImportRagFilesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportRagFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesRequest),[ImportRagFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesResponse),[ImportRagFilesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesOperationMetadata)>` |   
  
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
    
    
    public final VertexRagDataServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : vertexRagDataServiceClient.listLocations(request).iterateAll()) {
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
`[VertexRagDataServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             vertexRagDataServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,VertexRagDataServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           vertexRagDataServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListLocationsPagedResponse)>` |   
  
### listRagCorpora(@Nullable LocationName parent)
    
    
    public final VertexRagDataServiceClient.ListRagCorporaPagedResponse listRagCorpora(@Nullable LocationName parent)

Lists RagCorpora in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (RagCorpus element : vertexRagDataServiceClient.listRagCorpora(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to list the RagCorpora. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient.ListRagCorporaPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagCorporaPagedResponse)` |   
  
### listRagCorpora(ListRagCorporaRequest request)
    
    
    public final VertexRagDataServiceClient.ListRagCorporaPagedResponse listRagCorpora(ListRagCorporaRequest request)

Lists RagCorpora in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListRagCorporaRequest request =
           ListRagCorporaRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (RagCorpus element : vertexRagDataServiceClient.listRagCorpora(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRagCorporaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagCorporaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient.ListRagCorporaPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagCorporaPagedResponse)` |   
  
### listRagCorpora(String parent)
    
    
    public final VertexRagDataServiceClient.ListRagCorporaPagedResponse listRagCorpora(String parent)

Lists RagCorpora in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (RagCorpus element : vertexRagDataServiceClient.listRagCorpora(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to list the RagCorpora. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient.ListRagCorporaPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagCorporaPagedResponse)` |   
  
### listRagCorporaCallable()
    
    
    public final UnaryCallable<ListRagCorporaRequest,ListRagCorporaResponse> listRagCorporaCallable()

Lists RagCorpora in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListRagCorporaRequest request =
           ListRagCorporaRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListRagCorporaResponse response =
             vertexRagDataServiceClient.listRagCorporaCallable().call(request);
         for (RagCorpus element : response.getRagCorporaList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRagCorporaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagCorporaRequest),[ListRagCorporaResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagCorporaResponse)>` |   
  
### listRagCorporaPagedCallable()
    
    
    public final UnaryCallable<ListRagCorporaRequest,VertexRagDataServiceClient.ListRagCorporaPagedResponse> listRagCorporaPagedCallable()

Lists RagCorpora in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListRagCorporaRequest request =
           ListRagCorporaRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<RagCorpus> future =
           vertexRagDataServiceClient.listRagCorporaPagedCallable().futureCall(request);
       // Do something.
       for (RagCorpus element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRagCorporaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagCorporaRequest),[ListRagCorporaPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagCorporaPagedResponse)>` |   
  
### listRagFiles(@Nullable RagCorpusName parent)
    
    
    public final VertexRagDataServiceClient.ListRagFilesPagedResponse listRagFiles(@Nullable RagCorpusName parent)

Lists RagFiles in a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagCorpusName parent = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]");
       for (RagFile element : vertexRagDataServiceClient.listRagFiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagCorpusName`  
Required. The resource name of the RagCorpus from which to list the RagFiles. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient.ListRagFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagFilesPagedResponse)` |   
  
### listRagFiles(ListRagFilesRequest request)
    
    
    public final VertexRagDataServiceClient.ListRagFilesPagedResponse listRagFiles(ListRagFilesRequest request)

Lists RagFiles in a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListRagFilesRequest request =
           ListRagFilesRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (RagFile element : vertexRagDataServiceClient.listRagFiles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRagFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagFilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient.ListRagFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagFilesPagedResponse)` |   
  
### listRagFiles(String parent)
    
    
    public final VertexRagDataServiceClient.ListRagFilesPagedResponse listRagFiles(String parent)

Lists RagFiles in a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String parent = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString();
       for (RagFile element : vertexRagDataServiceClient.listRagFiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the RagCorpus from which to list the RagFiles. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataServiceClient.ListRagFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagFilesPagedResponse)` |   
  
### listRagFilesCallable()
    
    
    public final UnaryCallable<ListRagFilesRequest,ListRagFilesResponse> listRagFilesCallable()

Lists RagFiles in a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListRagFilesRequest request =
           ListRagFilesRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListRagFilesResponse response =
             vertexRagDataServiceClient.listRagFilesCallable().call(request);
         for (RagFile element : response.getRagFilesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRagFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagFilesRequest),[ListRagFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagFilesResponse)>` |   
  
### listRagFilesPagedCallable()
    
    
    public final UnaryCallable<ListRagFilesRequest,VertexRagDataServiceClient.ListRagFilesPagedResponse> listRagFilesPagedCallable()

Lists RagFiles in a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       ListRagFilesRequest request =
           ListRagFilesRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<RagFile> future =
           vertexRagDataServiceClient.listRagFilesPagedCallable().futureCall(request);
       // Do something.
       for (RagFile element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRagFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListRagFilesRequest),[ListRagFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VertexRagDataServiceClient.ListRagFilesPagedResponse)>` |   
  
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
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = vertexRagDataServiceClient.setIamPolicy(request);
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
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
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
           vertexRagDataServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = vertexRagDataServiceClient.testIamPermissions(request);
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
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           vertexRagDataServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateRagCorpusAsync(RagCorpus ragCorpus)
    
    
    public final OperationFuture<RagCorpus,UpdateRagCorpusOperationMetadata> updateRagCorpusAsync(RagCorpus ragCorpus)

Updates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagCorpus ragCorpus = RagCorpus.newBuilder().build();
       RagCorpus response = vertexRagDataServiceClient.updateRagCorpusAsync(ragCorpus).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`ragCorpus` | `[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus)`  
Required. The RagCorpus which replaces the resource on the server.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus),[UpdateRagCorpusOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagCorpusOperationMetadata)>` |   
  
### updateRagCorpusAsync(UpdateRagCorpusRequest request)
    
    
    public final OperationFuture<RagCorpus,UpdateRagCorpusOperationMetadata> updateRagCorpusAsync(UpdateRagCorpusRequest request)

Updates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UpdateRagCorpusRequest request =
           UpdateRagCorpusRequest.newBuilder().setRagCorpus(RagCorpus.newBuilder().build()).build();
       RagCorpus response = vertexRagDataServiceClient.updateRagCorpusAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagCorpusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus),[UpdateRagCorpusOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagCorpusOperationMetadata)>` |   
  
### updateRagCorpusCallable()
    
    
    public final UnaryCallable<UpdateRagCorpusRequest,Operation> updateRagCorpusCallable()

Updates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UpdateRagCorpusRequest request =
           UpdateRagCorpusRequest.newBuilder().setRagCorpus(RagCorpus.newBuilder().build()).build();
       ApiFuture<Operation> future =
           vertexRagDataServiceClient.updateRagCorpusCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagCorpusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRagCorpusOperationCallable()
    
    
    public final OperationCallable<UpdateRagCorpusRequest,RagCorpus,UpdateRagCorpusOperationMetadata> updateRagCorpusOperationCallable()

Updates a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UpdateRagCorpusRequest request =
           UpdateRagCorpusRequest.newBuilder().setRagCorpus(RagCorpus.newBuilder().build()).build();
       OperationFuture<RagCorpus, UpdateRagCorpusOperationMetadata> future =
           vertexRagDataServiceClient.updateRagCorpusOperationCallable().futureCall(request);
       // Do something.
       RagCorpus response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRagCorpusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagCorpusRequest),[RagCorpus](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagCorpus),[UpdateRagCorpusOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagCorpusOperationMetadata)>` |   
  
### updateRagEngineConfigAsync(RagEngineConfig ragEngineConfig)
    
    
    public final OperationFuture<RagEngineConfig,UpdateRagEngineConfigOperationMetadata> updateRagEngineConfigAsync(RagEngineConfig ragEngineConfig)

Updates a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagEngineConfig ragEngineConfig = RagEngineConfig.newBuilder().build();
       RagEngineConfig response =
           vertexRagDataServiceClient.updateRagEngineConfigAsync(ragEngineConfig).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`ragEngineConfig` | `[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig)`  
Required. The updated RagEngineConfig. NOTE: Downgrading your RagManagedDb's ComputeTier could temporarily increase request latencies until the operation is fully complete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig),[UpdateRagEngineConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagEngineConfigOperationMetadata)>` |   
  
### updateRagEngineConfigAsync(UpdateRagEngineConfigRequest request)
    
    
    public final OperationFuture<RagEngineConfig,UpdateRagEngineConfigOperationMetadata> updateRagEngineConfigAsync(UpdateRagEngineConfigRequest request)

Updates a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UpdateRagEngineConfigRequest request =
           UpdateRagEngineConfigRequest.newBuilder()
               .setRagEngineConfig(RagEngineConfig.newBuilder().build())
               .build();
       RagEngineConfig response =
           vertexRagDataServiceClient.updateRagEngineConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRagEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagEngineConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig),[UpdateRagEngineConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagEngineConfigOperationMetadata)>` |   
  
### updateRagEngineConfigCallable()
    
    
    public final UnaryCallable<UpdateRagEngineConfigRequest,Operation> updateRagEngineConfigCallable()

Updates a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UpdateRagEngineConfigRequest request =
           UpdateRagEngineConfigRequest.newBuilder()
               .setRagEngineConfig(RagEngineConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           vertexRagDataServiceClient.updateRagEngineConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRagEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagEngineConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRagEngineConfigOperationCallable()
    
    
    public final OperationCallable<UpdateRagEngineConfigRequest,RagEngineConfig,UpdateRagEngineConfigOperationMetadata> updateRagEngineConfigOperationCallable()

Updates a RagEngineConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UpdateRagEngineConfigRequest request =
           UpdateRagEngineConfigRequest.newBuilder()
               .setRagEngineConfig(RagEngineConfig.newBuilder().build())
               .build();
       OperationFuture<RagEngineConfig, UpdateRagEngineConfigOperationMetadata> future =
           vertexRagDataServiceClient.updateRagEngineConfigOperationCallable().futureCall(request);
       // Do something.
       RagEngineConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRagEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagEngineConfigRequest),[RagEngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagEngineConfig),[UpdateRagEngineConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateRagEngineConfigOperationMetadata)>` |   
  
### uploadRagFile(@Nullable RagCorpusName parent, RagFile ragFile, UploadRagFileConfig uploadRagFileConfig)
    
    
    public final UploadRagFileResponse uploadRagFile(@Nullable RagCorpusName parent, RagFile ragFile, UploadRagFileConfig uploadRagFileConfig)

Upload a file into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       RagCorpusName parent = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]");
       RagFile ragFile = RagFile.newBuilder().build();
       UploadRagFileConfig uploadRagFileConfig = UploadRagFileConfig.newBuilder().build();
       UploadRagFileResponse response =
           vertexRagDataServiceClient.uploadRagFile(parent, ragFile, uploadRagFileConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.RagCorpusName`  
Required. The name of the RagCorpus resource into which to upload the file. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
`ragFile` | `[RagFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagFile)`  
Required. The RagFile to upload.  
`uploadRagFileConfig` | `[UploadRagFileConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileConfig)`  
Required. The config for the RagFiles to be uploaded into the RagCorpus. VertexRagDataService.UploadRagFile.  
**Returns**  
---  
**Type** | **Description**  
`[UploadRagFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileResponse)` |   
  
### uploadRagFile(UploadRagFileRequest request)
    
    
    public final UploadRagFileResponse uploadRagFile(UploadRagFileRequest request)

Upload a file into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UploadRagFileRequest request =
           UploadRagFileRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setRagFile(RagFile.newBuilder().build())
               .setUploadRagFileConfig(UploadRagFileConfig.newBuilder().build())
               .build();
       UploadRagFileResponse response = vertexRagDataServiceClient.uploadRagFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UploadRagFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UploadRagFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileResponse)` |   
  
### uploadRagFile(String parent, RagFile ragFile, UploadRagFileConfig uploadRagFileConfig)
    
    
    public final UploadRagFileResponse uploadRagFile(String parent, RagFile ragFile, UploadRagFileConfig uploadRagFileConfig)

Upload a file into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       String parent = RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString();
       RagFile ragFile = RagFile.newBuilder().build();
       UploadRagFileConfig uploadRagFileConfig = UploadRagFileConfig.newBuilder().build();
       UploadRagFileResponse response =
           vertexRagDataServiceClient.uploadRagFile(parent, ragFile, uploadRagFileConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the RagCorpus resource into which to upload the file. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`  
`ragFile` | `[RagFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagFile)`  
Required. The RagFile to upload.  
`uploadRagFileConfig` | `[UploadRagFileConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileConfig)`  
Required. The config for the RagFiles to be uploaded into the RagCorpus. VertexRagDataService.UploadRagFile.  
**Returns**  
---  
**Type** | **Description**  
`[UploadRagFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileResponse)` |   
  
### uploadRagFileCallable()
    
    
    public final UnaryCallable<UploadRagFileRequest,UploadRagFileResponse> uploadRagFileCallable()

Upload a file into a RagCorpus.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VertexRagDataServiceClient vertexRagDataServiceClient =
         VertexRagDataServiceClient.create()) {
       UploadRagFileRequest request =
           UploadRagFileRequest.newBuilder()
               .setParent(RagCorpusName.of("[PROJECT]", "[LOCATION]", "[RAG_CORPUS]").toString())
               .setRagFile(RagFile.newBuilder().build())
               .setUploadRagFileConfig(UploadRagFileConfig.newBuilder().build())
               .build();
       ApiFuture<UploadRagFileResponse> future =
           vertexRagDataServiceClient.uploadRagFileCallable().futureCall(request);
       // Do something.
       UploadRagFileResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UploadRagFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileRequest),[UploadRagFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadRagFileResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
