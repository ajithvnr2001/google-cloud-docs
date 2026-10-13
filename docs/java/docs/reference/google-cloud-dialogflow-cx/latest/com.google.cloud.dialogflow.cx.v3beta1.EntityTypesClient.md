---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient
title: Class EntityTypesClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:07.269303+00:00
---

# Class EntityTypesClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EntityTypesClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3beta1/EntityTypesClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing EntityTypes.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       EntityTypeName name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
       EntityType response = entityTypesClient.getEntityType(name);
     }
     

Note: close() needs to be called on the EntityTypesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetEntityType |  Retrieves the specified entity type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntityType(GetEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEntityType(EntityTypeName name) 
  * getEntityType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntityTypeCallable() 

  
CreateEntityType |  Creates an entity type in the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntityType(CreateEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createEntityType(AgentName parent, EntityType entityType) 
  * createEntityType(String parent, EntityType entityType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntityTypeCallable() 

  
UpdateEntityType |  Updates the specified entity type.  Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEntityType(UpdateEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEntityType(EntityType entityType, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEntityTypeCallable() 

  
DeleteEntityType |  Deletes the specified entity type.  Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEntityType(DeleteEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteEntityType(EntityTypeName name) 
  * deleteEntityType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEntityTypeCallable() 

  
ListEntityTypes |  Returns the list of all entity types in the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntityTypes(ListEntityTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntityTypes(AgentName parent) 
  * listEntityTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntityTypesPagedCallable() 
  * listEntityTypesCallable() 

  
ExportEntityTypes |  Exports the selected entity types. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportEntityTypesAsync(ExportEntityTypesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportEntityTypesOperationCallable() 
  * exportEntityTypesCallable() 

  
ImportEntityTypes |  Imports the specified entitytypes into the agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importEntityTypesAsync(ImportEntityTypesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importEntityTypesOperationCallable() 
  * importEntityTypesCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of EntityTypesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EntityTypesSettings entityTypesSettings =
         EntityTypesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EntityTypesClient entityTypesClient = EntityTypesClient.create(entityTypesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EntityTypesSettings entityTypesSettings =
         EntityTypesSettings.newBuilder().setEndpoint(myEndpoint).build();
     EntityTypesClient entityTypesClient = EntityTypesClient.create(entityTypesSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EntityTypesSettings entityTypesSettings = EntityTypesSettings.newHttpJsonBuilder().build();
     EntityTypesClient entityTypesClient = EntityTypesClient.create(entityTypesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EntityTypesClient

## Static Methods 

### create()
    
    
    public static final EntityTypesClient create()

Constructs an instance of EntityTypesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EntityTypesSettings settings)
    
    
    public static final EntityTypesClient create(EntityTypesSettings settings)

Constructs an instance of EntityTypesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EntityTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EntityTypesStub stub)
    
    
    public static final EntityTypesClient create(EntityTypesStub stub)

Constructs an instance of EntityTypesClient, using the given stub for making calls. This is for advanced usage - prefer using create(EntityTypesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.stub.EntityTypesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient)` |   
  
## Constructors 

### EntityTypesClient(EntityTypesSettings settings)
    
    
    protected EntityTypesClient(EntityTypesSettings settings)

Constructs an instance of EntityTypesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EntityTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesSettings)`  
  
  
### EntityTypesClient(EntityTypesStub stub)
    
    
    protected EntityTypesClient(EntityTypesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.stub.EntityTypesStub)`  
  
  
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

### createEntityType(@Nullable AgentName parent, EntityType entityType)
    
    
    public final EntityType createEntityType(@Nullable AgentName parent, EntityType entityType)

Creates an entity type in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       EntityType entityType = EntityType.newBuilder().build();
       EntityType response = entityTypesClient.createEntityType(parent, entityType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3beta1.AgentName`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)`  
Required. The entity type to create.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### createEntityType(CreateEntityTypeRequest request)
    
    
    public final EntityType createEntityType(CreateEntityTypeRequest request)

Creates an entity type in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       CreateEntityTypeRequest request =
           CreateEntityTypeRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setEntityType(EntityType.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .build();
       EntityType response = entityTypesClient.createEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.CreateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### createEntityType(String parent, EntityType entityType)
    
    
    public final EntityType createEntityType(String parent, EntityType entityType)

Creates an entity type in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       EntityType entityType = EntityType.newBuilder().build();
       EntityType response = entityTypesClient.createEntityType(parent, entityType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)`  
Required. The entity type to create.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### createEntityTypeCallable()
    
    
    public final UnaryCallable<CreateEntityTypeRequest,EntityType> createEntityTypeCallable()

Creates an entity type in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       CreateEntityTypeRequest request =
           CreateEntityTypeRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setEntityType(EntityType.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<EntityType> future =
           entityTypesClient.createEntityTypeCallable().futureCall(request);
       // Do something.
       EntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.CreateEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)>` |   
  
### deleteEntityType(@Nullable EntityTypeName name)
    
    
    public final void deleteEntityType(@Nullable EntityTypeName name)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       EntityTypeName name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
       entityTypesClient.deleteEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3beta1.EntityTypeName`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
  
### deleteEntityType(DeleteEntityTypeRequest request)
    
    
    public final void deleteEntityType(DeleteEntityTypeRequest request)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       DeleteEntityTypeRequest request =
           DeleteEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]")
                       .toString())
               .setForce(true)
               .build();
       entityTypesClient.deleteEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.DeleteEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteEntityType(String name)
    
    
    public final void deleteEntityType(String name)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       String name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]").toString();
       entityTypesClient.deleteEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
  
### deleteEntityTypeCallable()
    
    
    public final UnaryCallable<DeleteEntityTypeRequest,Empty> deleteEntityTypeCallable()

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       DeleteEntityTypeRequest request =
           DeleteEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future = entityTypesClient.deleteEntityTypeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.DeleteEntityTypeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### exportEntityTypesAsync(ExportEntityTypesRequest request)
    
    
    public final OperationFuture<ExportEntityTypesResponse,ExportEntityTypesMetadata> exportEntityTypesAsync(ExportEntityTypesRequest request)

Exports the selected entity types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ExportEntityTypesRequest request =
           ExportEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .addAllEntityTypes(new ArrayList<String>())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ExportEntityTypesResponse response = entityTypesClient.exportEntityTypesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ExportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ExportEntityTypesResponse),[ExportEntityTypesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ExportEntityTypesMetadata)>` |   
  
### exportEntityTypesCallable()
    
    
    public final UnaryCallable<ExportEntityTypesRequest,Operation> exportEntityTypesCallable()

Exports the selected entity types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ExportEntityTypesRequest request =
           ExportEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .addAllEntityTypes(new ArrayList<String>())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<Operation> future =
           entityTypesClient.exportEntityTypesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ExportEntityTypesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportEntityTypesOperationCallable()
    
    
    public final OperationCallable<ExportEntityTypesRequest,ExportEntityTypesResponse,ExportEntityTypesMetadata> exportEntityTypesOperationCallable()

Exports the selected entity types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ExportEntityTypesRequest request =
           ExportEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .addAllEntityTypes(new ArrayList<String>())
               .setLanguageCode("languageCode-2092349083")
               .build();
       OperationFuture<ExportEntityTypesResponse, ExportEntityTypesMetadata> future =
           entityTypesClient.exportEntityTypesOperationCallable().futureCall(request);
       // Do something.
       ExportEntityTypesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ExportEntityTypesRequest),[ExportEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ExportEntityTypesResponse),[ExportEntityTypesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ExportEntityTypesMetadata)>` |   
  
### getEntityType(@Nullable EntityTypeName name)
    
    
    public final EntityType getEntityType(@Nullable EntityTypeName name)

Retrieves the specified entity type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       EntityTypeName name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
       EntityType response = entityTypesClient.getEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3beta1.EntityTypeName`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### getEntityType(GetEntityTypeRequest request)
    
    
    public final EntityType getEntityType(GetEntityTypeRequest request)

Retrieves the specified entity type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       GetEntityTypeRequest request =
           GetEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]")
                       .toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       EntityType response = entityTypesClient.getEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.GetEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### getEntityType(String name)
    
    
    public final EntityType getEntityType(String name)

Retrieves the specified entity type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       String name =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]").toString();
       EntityType response = entityTypesClient.getEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### getEntityTypeCallable()
    
    
    public final UnaryCallable<GetEntityTypeRequest,EntityType> getEntityTypeCallable()

Retrieves the specified entity type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       GetEntityTypeRequest request =
           GetEntityTypeRequest.newBuilder()
               .setName(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]")
                       .toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<EntityType> future = entityTypesClient.getEntityTypeCallable().futureCall(request);
       // Do something.
       EntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.GetEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = entityTypesClient.getLocation(request);
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
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = entityTypesClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable EntityTypesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3beta1.EntityTypesSettings` |   
  
### getStub()
    
    
    public EntityTypesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.stub.EntityTypesStub)` |   
  
### importEntityTypesAsync(ImportEntityTypesRequest request)
    
    
    public final OperationFuture<ImportEntityTypesResponse,ImportEntityTypesMetadata> importEntityTypesAsync(ImportEntityTypesRequest request)

Imports the specified entitytypes into the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ImportEntityTypesRequest request =
           ImportEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setTargetEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       ImportEntityTypesResponse response = entityTypesClient.importEntityTypesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportEntityTypesResponse),[ImportEntityTypesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportEntityTypesMetadata)>` |   
  
### importEntityTypesCallable()
    
    
    public final UnaryCallable<ImportEntityTypesRequest,Operation> importEntityTypesCallable()

Imports the specified entitytypes into the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ImportEntityTypesRequest request =
           ImportEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setTargetEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           entityTypesClient.importEntityTypesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportEntityTypesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importEntityTypesOperationCallable()
    
    
    public final OperationCallable<ImportEntityTypesRequest,ImportEntityTypesResponse,ImportEntityTypesMetadata> importEntityTypesOperationCallable()

Imports the specified entitytypes into the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ImportEntityTypesRequest request =
           ImportEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setTargetEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       OperationFuture<ImportEntityTypesResponse, ImportEntityTypesMetadata> future =
           entityTypesClient.importEntityTypesOperationCallable().futureCall(request);
       // Do something.
       ImportEntityTypesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportEntityTypesRequest),[ImportEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportEntityTypesResponse),[ImportEntityTypesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ImportEntityTypesMetadata)>` |   
  
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
  
### listEntityTypes(@Nullable AgentName parent)
    
    
    public final EntityTypesClient.ListEntityTypesPagedResponse listEntityTypes(@Nullable AgentName parent)

Returns the list of all entity types in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       for (EntityType element : entityTypesClient.listEntityTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3beta1.AgentName`  
Required. The agent to list all entity types for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesClient.ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient.ListEntityTypesPagedResponse)` |   
  
### listEntityTypes(ListEntityTypesRequest request)
    
    
    public final EntityTypesClient.ListEntityTypesPagedResponse listEntityTypes(ListEntityTypesRequest request)

Returns the list of all entity types in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ListEntityTypesRequest request =
           ListEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (EntityType element : entityTypesClient.listEntityTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ListEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesClient.ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient.ListEntityTypesPagedResponse)` |   
  
### listEntityTypes(String parent)
    
    
    public final EntityTypesClient.ListEntityTypesPagedResponse listEntityTypes(String parent)

Returns the list of all entity types in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       for (EntityType element : entityTypesClient.listEntityTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to list all entity types for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EntityTypesClient.ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient.ListEntityTypesPagedResponse)` |   
  
### listEntityTypesCallable()
    
    
    public final UnaryCallable<ListEntityTypesRequest,ListEntityTypesResponse> listEntityTypesCallable()

Returns the list of all entity types in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ListEntityTypesRequest request =
           ListEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEntityTypesResponse response =
             entityTypesClient.listEntityTypesCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ListEntityTypesRequest),[ListEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ListEntityTypesResponse)>` |   
  
### listEntityTypesPagedCallable()
    
    
    public final UnaryCallable<ListEntityTypesRequest,EntityTypesClient.ListEntityTypesPagedResponse> listEntityTypesPagedCallable()

Returns the list of all entity types in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ListEntityTypesRequest request =
           ListEntityTypesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<EntityType> future =
           entityTypesClient.listEntityTypesPagedCallable().futureCall(request);
       // Do something.
       for (EntityType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ListEntityTypesRequest),[ListEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient.ListEntityTypesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final EntityTypesClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : entityTypesClient.listLocations(request).iterateAll()) {
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
`[EntityTypesClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = entityTypesClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,EntityTypesClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           entityTypesClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateEntityType(EntityType entityType, FieldMask updateMask)
    
    
    public final EntityType updateEntityType(EntityType entityType, FieldMask updateMask)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       EntityType entityType = EntityType.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EntityType response = entityTypesClient.updateEntityType(entityType, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entityType` | `[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)`  
Required. The entity type to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask to control which fields get updated.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### updateEntityType(UpdateEntityTypeRequest request)
    
    
    public final EntityType updateEntityType(UpdateEntityTypeRequest request)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       UpdateEntityTypeRequest request =
           UpdateEntityTypeRequest.newBuilder()
               .setEntityType(EntityType.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       EntityType response = entityTypesClient.updateEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.UpdateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)` |   
  
### updateEntityTypeCallable()
    
    
    public final UnaryCallable<UpdateEntityTypeRequest,EntityType> updateEntityTypeCallable()

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntityTypesClient entityTypesClient = EntityTypesClient.create()) {
       UpdateEntityTypeRequest request =
           UpdateEntityTypeRequest.newBuilder()
               .setEntityType(EntityType.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<EntityType> future =
           entityTypesClient.updateEntityTypeCallable().futureCall(request);
       // Do something.
       EntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.UpdateEntityTypeRequest),[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityType)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
