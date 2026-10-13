---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient
title: Class ControlServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:27.803594+00:00
---

# Class ControlServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ControlServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/ControlServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       Control control = Control.newBuilder().build();
       String controlId = "controlId-395080872";
       Control response = controlServiceClient.createControl(parent, control, controlId);
     }
     

Note: close() needs to be called on the ControlServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateControl |  Creates a Control.  By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createControl(CreateControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createControl(DataStoreName parent, Control control, String controlId) 
  * createControl(EngineName parent, Control control, String controlId) 
  * createControl(String parent, Control control, String controlId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createControlCallable() 

  
DeleteControl |  Deletes a Control.  If the Control to delete does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteControl(DeleteControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteControl(ControlName name) 
  * deleteControl(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteControlCallable() 

  
UpdateControl |  Updates a Control.  Control action type cannot be changed. If the Control to update does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateControl(UpdateControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateControl(Control control, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateControlCallable() 

  
GetControl |  Gets a Control. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getControl(GetControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getControl(ControlName name) 
  * getControl(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getControlCallable() 

  
ListControls |  Lists all Controls by their parent DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listControls(ListControlsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listControls(DataStoreName parent) 
  * listControls(EngineName parent) 
  * listControls(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listControlsPagedCallable() 
  * listControlsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ControlServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ControlServiceSettings controlServiceSettings =
         ControlServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ControlServiceClient controlServiceClient = ControlServiceClient.create(controlServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ControlServiceSettings controlServiceSettings =
         ControlServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ControlServiceClient controlServiceClient = ControlServiceClient.create(controlServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ControlServiceSettings controlServiceSettings =
         ControlServiceSettings.newHttpJsonBuilder().build();
     ControlServiceClient controlServiceClient = ControlServiceClient.create(controlServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ControlServiceClient

## Static Methods 

### create()
    
    
    public static final ControlServiceClient create()

Constructs an instance of ControlServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ControlServiceSettings settings)
    
    
    public static final ControlServiceClient create(ControlServiceSettings settings)

Constructs an instance of ControlServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ControlServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ControlServiceStub stub)
    
    
    public static final ControlServiceClient create(ControlServiceStub stub)

Constructs an instance of ControlServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ControlServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ControlServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.ControlServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient)` |   
  
## Constructors 

### ControlServiceClient(ControlServiceSettings settings)
    
    
    protected ControlServiceClient(ControlServiceSettings settings)

Constructs an instance of ControlServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ControlServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceSettings)`  
  
  
### ControlServiceClient(ControlServiceStub stub)
    
    
    protected ControlServiceClient(ControlServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ControlServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.ControlServiceStub)`  
  
  
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

### createControl(@Nullable DataStoreName parent, Control control, String controlId)
    
    
    public final Control createControl(@Nullable DataStoreName parent, Control control, String controlId)

Creates a Control.

By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       Control control = Control.newBuilder().build();
       String controlId = "controlId-395080872";
       Control response = controlServiceClient.createControl(parent, control, controlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`control` | `[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)`  
Required. The Control to create.  
`controlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Control, which will become the final component of the Control's resource name. This value must be within 1-63 characters. Valid characters are /a-z-_/.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### createControl(@Nullable EngineName parent, Control control, String controlId)
    
    
    public final Control createControl(@Nullable EngineName parent, Control control, String controlId)

Creates a Control.

By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       EngineName parent = EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
       Control control = Control.newBuilder().build();
       String controlId = "controlId-395080872";
       Control response = controlServiceClient.createControl(parent, control, controlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.EngineName`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`control` | `[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)`  
Required. The Control to create.  
`controlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Control, which will become the final component of the Control's resource name. This value must be within 1-63 characters. Valid characters are /a-z-_/.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### createControl(CreateControlRequest request)
    
    
    public final Control createControl(CreateControlRequest request)

Creates a Control.

By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       CreateControlRequest request =
           CreateControlRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setControl(Control.newBuilder().build())
               .setControlId("controlId-395080872")
               .build();
       Control response = controlServiceClient.createControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### createControl(String parent, Control control, String controlId)
    
    
    public final Control createControl(String parent, Control control, String controlId)

Creates a Control.

By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       Control control = Control.newBuilder().build();
       String controlId = "controlId-395080872";
       Control response = controlServiceClient.createControl(parent, control, controlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`control` | `[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)`  
Required. The Control to create.  
`controlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Control, which will become the final component of the Control's resource name. This value must be within 1-63 characters. Valid characters are /a-z-_/.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### createControlCallable()
    
    
    public final UnaryCallable<CreateControlRequest,Control> createControlCallable()

Creates a Control.

By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       CreateControlRequest request =
           CreateControlRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setControl(Control.newBuilder().build())
               .setControlId("controlId-395080872")
               .build();
       ApiFuture<Control> future = controlServiceClient.createControlCallable().futureCall(request);
       // Do something.
       Control response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateControlRequest),[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)>` |   
  
### deleteControl(@Nullable ControlName name)
    
    
    public final void deleteControl(@Nullable ControlName name)

Deletes a Control.

If the Control to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ControlName name =
           ControlName.ofProjectLocationDataStoreControlName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]");
       controlServiceClient.deleteControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.ControlName`  
Required. The resource name of the Control to delete. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/controls/{control_id}`  
  
### deleteControl(DeleteControlRequest request)
    
    
    public final void deleteControl(DeleteControlRequest request)

Deletes a Control.

If the Control to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       DeleteControlRequest request =
           DeleteControlRequest.newBuilder()
               .setName(
                   ControlName.ofProjectLocationDataStoreControlName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]")
                       .toString())
               .build();
       controlServiceClient.deleteControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteControlRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteControl(String name)
    
    
    public final void deleteControl(String name)

Deletes a Control.

If the Control to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       String name =
           ControlName.ofProjectLocationDataStoreControlName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]")
               .toString();
       controlServiceClient.deleteControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Control to delete. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/controls/{control_id}`  
  
### deleteControlCallable()
    
    
    public final UnaryCallable<DeleteControlRequest,Empty> deleteControlCallable()

Deletes a Control.

If the Control to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       DeleteControlRequest request =
           DeleteControlRequest.newBuilder()
               .setName(
                   ControlName.ofProjectLocationDataStoreControlName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]")
                       .toString())
               .build();
       ApiFuture<Empty> future = controlServiceClient.deleteControlCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteControlRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getControl(@Nullable ControlName name)
    
    
    public final Control getControl(@Nullable ControlName name)

Gets a Control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ControlName name =
           ControlName.ofProjectLocationDataStoreControlName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]");
       Control response = controlServiceClient.getControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.ControlName`  
Required. The resource name of the Control to get. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/controls/{control_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### getControl(GetControlRequest request)
    
    
    public final Control getControl(GetControlRequest request)

Gets a Control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       GetControlRequest request =
           GetControlRequest.newBuilder()
               .setName(
                   ControlName.ofProjectLocationDataStoreControlName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]")
                       .toString())
               .build();
       Control response = controlServiceClient.getControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### getControl(String name)
    
    
    public final Control getControl(String name)

Gets a Control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       String name =
           ControlName.ofProjectLocationDataStoreControlName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]")
               .toString();
       Control response = controlServiceClient.getControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Control to get. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/controls/{control_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### getControlCallable()
    
    
    public final UnaryCallable<GetControlRequest,Control> getControlCallable()

Gets a Control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       GetControlRequest request =
           GetControlRequest.newBuilder()
               .setName(
                   ControlName.ofProjectLocationDataStoreControlName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONTROL]")
                       .toString())
               .build();
       ApiFuture<Control> future = controlServiceClient.getControlCallable().futureCall(request);
       // Do something.
       Control response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetControlRequest),[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)>` |   
  
### getSettings()
    
    
    public final @Nullable ControlServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.ControlServiceSettings` |   
  
### getStub()
    
    
    public ControlServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ControlServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.ControlServiceStub)` |   
  
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
  
### listControls(@Nullable DataStoreName parent)
    
    
    public final ControlServiceClient.ListControlsPagedResponse listControls(@Nullable DataStoreName parent)

Lists all Controls by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       for (Control element : controlServiceClient.listControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient.ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient.ListControlsPagedResponse)` |   
  
### listControls(@Nullable EngineName parent)
    
    
    public final ControlServiceClient.ListControlsPagedResponse listControls(@Nullable EngineName parent)

Lists all Controls by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       EngineName parent = EngineName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
       for (Control element : controlServiceClient.listControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.EngineName`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient.ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient.ListControlsPagedResponse)` |   
  
### listControls(ListControlsRequest request)
    
    
    public final ControlServiceClient.ListControlsPagedResponse listControls(ListControlsRequest request)

Lists all Controls by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ListControlsRequest request =
           ListControlsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Control element : controlServiceClient.listControls(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListControlsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient.ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient.ListControlsPagedResponse)` |   
  
### listControls(String parent)
    
    
    public final ControlServiceClient.ListControlsPagedResponse listControls(String parent)

Lists all Controls by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       for (Control element : controlServiceClient.listControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient.ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient.ListControlsPagedResponse)` |   
  
### listControlsCallable()
    
    
    public final UnaryCallable<ListControlsRequest,ListControlsResponse> listControlsCallable()

Lists all Controls by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ListControlsRequest request =
           ListControlsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListControlsResponse response = controlServiceClient.listControlsCallable().call(request);
         for (Control element : response.getControlsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListControlsRequest),[ListControlsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListControlsResponse)>` |   
  
### listControlsPagedCallable()
    
    
    public final UnaryCallable<ListControlsRequest,ControlServiceClient.ListControlsPagedResponse> listControlsPagedCallable()

Lists all Controls by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ListControlsRequest request =
           ListControlsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Control> future =
           controlServiceClient.listControlsPagedCallable().futureCall(request);
       // Do something.
       for (Control element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListControlsRequest),[ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ControlServiceClient.ListControlsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateControl(Control control, FieldMask updateMask)
    
    
    public final Control updateControl(Control control, FieldMask updateMask)

Updates a Control.

Control action type cannot be changed. If the Control to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       Control control = Control.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Control response = controlServiceClient.updateControl(control, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`control` | `[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)`  
Required. The Control to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Indicates which fields in the provided Control to update. The following are NOT supported: 

  * Control.name
  * Control.solution_type

If not set or empty, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### updateControl(UpdateControlRequest request)
    
    
    public final Control updateControl(UpdateControlRequest request)

Updates a Control.

Control action type cannot be changed. If the Control to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       UpdateControlRequest request =
           UpdateControlRequest.newBuilder()
               .setControl(Control.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Control response = controlServiceClient.updateControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)` |   
  
### updateControlCallable()
    
    
    public final UnaryCallable<UpdateControlRequest,Control> updateControlCallable()

Updates a Control.

Control action type cannot be changed. If the Control to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       UpdateControlRequest request =
           UpdateControlRequest.newBuilder()
               .setControl(Control.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Control> future = controlServiceClient.updateControlCallable().futureCall(request);
       // Do something.
       Control response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateControlRequest),[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Control)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
