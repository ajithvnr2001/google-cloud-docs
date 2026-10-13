---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient
title: Class EngineServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:41.868594+00:00
---

# Class EngineServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EngineServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/EngineServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing Engine configuration.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       Engine engine = Engine.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Engine response = engineServiceClient.updateEngine(engine, updateMask);
     }
     

Note: close() needs to be called on the EngineServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateEngine |  Creates a Engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEngineAsync(CreateEngineRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEngineAsync(CollectionName parent, Engine engine, String engineId) 
  * createEngineAsync(String parent, Engine engine, String engineId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEngineOperationCallable() 
  * createEngineCallable() 

  
DeleteEngine |  Deletes a Engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEngineAsync(DeleteEngineRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEngineAsync(EngineName name) 
  * deleteEngineAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEngineOperationCallable() 
  * deleteEngineCallable() 

  
UpdateEngine |  Updates an Engine |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEngine(UpdateEngineRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEngine(Engine engine, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEngineCallable() 

  
GetEngine |  Gets a Engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEngine(GetEngineRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEngine(EngineName name) 
  * getEngine(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEngineCallable() 

  
ListEngines |  Lists all the Engines associated with the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEngines(ListEnginesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEngines(CollectionName parent) 
  * listEngines(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEnginesPagedCallable() 
  * listEnginesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of EngineServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EngineServiceSettings engineServiceSettings =
         EngineServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EngineServiceClient engineServiceClient = EngineServiceClient.create(engineServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EngineServiceSettings engineServiceSettings =
         EngineServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     EngineServiceClient engineServiceClient = EngineServiceClient.create(engineServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EngineServiceSettings engineServiceSettings =
         EngineServiceSettings.newHttpJsonBuilder().build();
     EngineServiceClient engineServiceClient = EngineServiceClient.create(engineServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EngineServiceClient

## Static Methods 

### create()
    
    
    public static final EngineServiceClient create()

Constructs an instance of EngineServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EngineServiceSettings settings)
    
    
    public static final EngineServiceClient create(EngineServiceSettings settings)

Constructs an instance of EngineServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EngineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EngineServiceStub stub)
    
    
    public static final EngineServiceClient create(EngineServiceStub stub)

Constructs an instance of EngineServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(EngineServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.EngineServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient)` |   
  
## Constructors 

### EngineServiceClient(EngineServiceSettings settings)
    
    
    protected EngineServiceClient(EngineServiceSettings settings)

Constructs an instance of EngineServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EngineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceSettings)`  
  
  
### EngineServiceClient(EngineServiceStub stub)
    
    
    protected EngineServiceClient(EngineServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.EngineServiceStub)`  
  
  
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

### createEngineAsync(@Nullable CollectionName parent, Engine engine, String engineId)
    
    
    public final OperationFuture<Engine,CreateEngineMetadata> createEngineAsync(@Nullable CollectionName parent, Engine engine, String engineId)

Creates a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       Engine engine = Engine.newBuilder().build();
       String engineId = "engineId1820490493";
       Engine response = engineServiceClient.createEngineAsync(parent, engine, engineId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CollectionName`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)`  
Required. The Engine to create.  
`engineId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Engine, which will become the final component of the Engine's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine),[CreateEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateEngineMetadata)>` |   
  
### createEngineAsync(CreateEngineRequest request)
    
    
    public final OperationFuture<Engine,CreateEngineMetadata> createEngineAsync(CreateEngineRequest request)

Creates a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       CreateEngineRequest request =
           CreateEngineRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setEngine(Engine.newBuilder().build())
               .setEngineId("engineId1820490493")
               .build();
       Engine response = engineServiceClient.createEngineAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine),[CreateEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateEngineMetadata)>` |   
  
### createEngineAsync(String parent, Engine engine, String engineId)
    
    
    public final OperationFuture<Engine,CreateEngineMetadata> createEngineAsync(String parent, Engine engine, String engineId)

Creates a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       Engine engine = Engine.newBuilder().build();
       String engineId = "engineId1820490493";
       Engine response = engineServiceClient.createEngineAsync(parent, engine, engineId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)`  
Required. The Engine to create.  
`engineId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Engine, which will become the final component of the Engine's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine),[CreateEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateEngineMetadata)>` |   
  
### createEngineCallable()
    
    
    public final UnaryCallable<CreateEngineRequest,Operation> createEngineCallable()

Creates a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       CreateEngineRequest request =
           CreateEngineRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setEngine(Engine.newBuilder().build())
               .setEngineId("engineId1820490493")
               .build();
       ApiFuture<Operation> future = engineServiceClient.createEngineCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateEngineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEngineOperationCallable()
    
    
    public final OperationCallable<CreateEngineRequest,Engine,CreateEngineMetadata> createEngineOperationCallable()

Creates a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       CreateEngineRequest request =
           CreateEngineRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setEngine(Engine.newBuilder().build())
               .setEngineId("engineId1820490493")
               .build();
       OperationFuture<Engine, CreateEngineMetadata> future =
           engineServiceClient.createEngineOperationCallable().futureCall(request);
       // Do something.
       Engine response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateEngineRequest),[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine),[CreateEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateEngineMetadata)>` |   
  
### deleteEngineAsync(@Nullable EngineName name)
    
    
    public final OperationFuture<Empty,DeleteEngineMetadata> deleteEngineAsync(@Nullable EngineName name)

Deletes a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       EngineName name = EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
       engineServiceClient.deleteEngineAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.EngineName`  
Required. Full resource name of Engine, such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the Engine, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Engine to delete does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteEngineMetadata)>` |   
  
### deleteEngineAsync(DeleteEngineRequest request)
    
    
    public final OperationFuture<Empty,DeleteEngineMetadata> deleteEngineAsync(DeleteEngineRequest request)

Deletes a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       DeleteEngineRequest request =
           DeleteEngineRequest.newBuilder()
               .setName(
                   EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]").toString())
               .build();
       engineServiceClient.deleteEngineAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteEngineMetadata)>` |   
  
### deleteEngineAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteEngineMetadata> deleteEngineAsync(String name)

Deletes a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       String name = EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]").toString();
       engineServiceClient.deleteEngineAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Engine, such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the Engine, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Engine to delete does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteEngineMetadata)>` |   
  
### deleteEngineCallable()
    
    
    public final UnaryCallable<DeleteEngineRequest,Operation> deleteEngineCallable()

Deletes a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       DeleteEngineRequest request =
           DeleteEngineRequest.newBuilder()
               .setName(
                   EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]").toString())
               .build();
       ApiFuture<Operation> future = engineServiceClient.deleteEngineCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteEngineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEngineOperationCallable()
    
    
    public final OperationCallable<DeleteEngineRequest,Empty,DeleteEngineMetadata> deleteEngineOperationCallable()

Deletes a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       DeleteEngineRequest request =
           DeleteEngineRequest.newBuilder()
               .setName(
                   EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]").toString())
               .build();
       OperationFuture<Empty, DeleteEngineMetadata> future =
           engineServiceClient.deleteEngineOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteEngineRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteEngineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteEngineMetadata)>` |   
  
### getEngine(@Nullable EngineName name)
    
    
    public final Engine getEngine(@Nullable EngineName name)

Gets a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       EngineName name = EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
       Engine response = engineServiceClient.getEngine(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.EngineName`  
Required. Full resource name of Engine, such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)` |   
  
### getEngine(GetEngineRequest request)
    
    
    public final Engine getEngine(GetEngineRequest request)

Gets a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       GetEngineRequest request =
           GetEngineRequest.newBuilder()
               .setName(
                   EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]").toString())
               .build();
       Engine response = engineServiceClient.getEngine(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)` |   
  
### getEngine(String name)
    
    
    public final Engine getEngine(String name)

Gets a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       String name = EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]").toString();
       Engine response = engineServiceClient.getEngine(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Engine, such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)` |   
  
### getEngineCallable()
    
    
    public final UnaryCallable<GetEngineRequest,Engine> getEngineCallable()

Gets a Engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       GetEngineRequest request =
           GetEngineRequest.newBuilder()
               .setName(
                   EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]").toString())
               .build();
       ApiFuture<Engine> future = engineServiceClient.getEngineCallable().futureCall(request);
       // Do something.
       Engine response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetEngineRequest),[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable EngineServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.EngineServiceSettings` |   
  
### getStub()
    
    
    public EngineServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.EngineServiceStub)` |   
  
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
  
### listEngines(@Nullable CollectionName parent)
    
    
    public final EngineServiceClient.ListEnginesPagedResponse listEngines(@Nullable CollectionName parent)

Lists all the Engines associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       for (Engine element : engineServiceClient.listEngines(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CollectionName`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EngineServiceClient.ListEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient.ListEnginesPagedResponse)` |   
  
### listEngines(ListEnginesRequest request)
    
    
    public final EngineServiceClient.ListEnginesPagedResponse listEngines(ListEnginesRequest request)

Lists all the Engines associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       ListEnginesRequest request =
           ListEnginesRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Engine element : engineServiceClient.listEngines(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEnginesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListEnginesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EngineServiceClient.ListEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient.ListEnginesPagedResponse)` |   
  
### listEngines(String parent)
    
    
    public final EngineServiceClient.ListEnginesPagedResponse listEngines(String parent)

Lists all the Engines associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       for (Engine element : engineServiceClient.listEngines(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EngineServiceClient.ListEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient.ListEnginesPagedResponse)` |   
  
### listEnginesCallable()
    
    
    public final UnaryCallable<ListEnginesRequest,ListEnginesResponse> listEnginesCallable()

Lists all the Engines associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       ListEnginesRequest request =
           ListEnginesRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListEnginesResponse response = engineServiceClient.listEnginesCallable().call(request);
         for (Engine element : response.getEnginesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnginesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListEnginesRequest),[ListEnginesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListEnginesResponse)>` |   
  
### listEnginesPagedCallable()
    
    
    public final UnaryCallable<ListEnginesRequest,EngineServiceClient.ListEnginesPagedResponse> listEnginesPagedCallable()

Lists all the Engines associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       ListEnginesRequest request =
           ListEnginesRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Engine> future = engineServiceClient.listEnginesPagedCallable().futureCall(request);
       // Do something.
       for (Engine element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnginesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListEnginesRequest),[ListEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EngineServiceClient.ListEnginesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateEngine(Engine engine, FieldMask updateMask)
    
    
    public final Engine updateEngine(Engine engine, FieldMask updateMask)

Updates an Engine

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       Engine engine = Engine.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Engine response = engineServiceClient.updateEngine(engine, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`engine` | `[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)`  
Required. The Engine to update. If the caller does not have permission to update the Engine, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Engine to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided Engine to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)` |   
  
### updateEngine(UpdateEngineRequest request)
    
    
    public final Engine updateEngine(UpdateEngineRequest request)

Updates an Engine

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       UpdateEngineRequest request =
           UpdateEngineRequest.newBuilder()
               .setEngine(Engine.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Engine response = engineServiceClient.updateEngine(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)` |   
  
### updateEngineCallable()
    
    
    public final UnaryCallable<UpdateEngineRequest,Engine> updateEngineCallable()

Updates an Engine

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EngineServiceClient engineServiceClient = EngineServiceClient.create()) {
       UpdateEngineRequest request =
           UpdateEngineRequest.newBuilder()
               .setEngine(Engine.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Engine> future = engineServiceClient.updateEngineCallable().futureCall(request);
       // Do something.
       Engine response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateEngineRequest),[Engine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Engine)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
