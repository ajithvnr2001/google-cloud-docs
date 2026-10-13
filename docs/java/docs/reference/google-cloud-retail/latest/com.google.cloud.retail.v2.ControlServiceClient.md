---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient
title: Class ControlServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:19.485548+00:00
---

# Class ControlServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ControlServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/ControlServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for modifying Control.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       Control control = Control.newBuilder().build();
       String controlId = "controlId-395080872";
       Control response = controlServiceClient.createControl(parent, control, controlId);
     }
     

Note: close() needs to be called on the ControlServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateControl |  Creates a Control.  If the Control to create already exists, an ALREADY_EXISTS error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createControl(CreateControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createControl(CatalogName parent, Control control, String controlId) 
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

  
UpdateControl |  Updates a Control.  Control cannot be set to a different oneof field, if so an INVALID_ARGUMENT is returned. If the Control to update does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

  
ListControls |  Lists all Controls by their parent Catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listControls(ListControlsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listControls(CatalogName parent) 
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
`[ControlServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient)` |   
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
`settings` | `[ControlServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient)` |   
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
`stub` | `[ControlServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ControlServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient)` |   
  
## Constructors 

### ControlServiceClient(ControlServiceSettings settings)
    
    
    protected ControlServiceClient(ControlServiceSettings settings)

Constructs an instance of ControlServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ControlServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceSettings)`  
  
  
### ControlServiceClient(ControlServiceStub stub)
    
    
    protected ControlServiceClient(ControlServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ControlServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ControlServiceStub)`  
  
  
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

### createControl(@Nullable CatalogName parent, Control control, String controlId)
    
    
    public final Control createControl(@Nullable CatalogName parent, Control control, String controlId)

Creates a Control.

If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       Control control = Control.newBuilder().build();
       String controlId = "controlId-395080872";
       Control response = controlServiceClient.createControl(parent, control, controlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. Full resource name of parent catalog. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
`control` | `[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)`  
Required. The Control to create.  
`controlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Control, which will become the final component of the Control's resource name. This value should be 4-63 characters, and valid characters are /a-z-_/.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
### createControl(CreateControlRequest request)
    
    
    public final Control createControl(CreateControlRequest request)

Creates a Control.

If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       CreateControlRequest request =
           CreateControlRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setControl(Control.newBuilder().build())
               .setControlId("controlId-395080872")
               .build();
       Control response = controlServiceClient.createControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
### createControl(String parent, Control control, String controlId)
    
    
    public final Control createControl(String parent, Control control, String controlId)

Creates a Control.

If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       Control control = Control.newBuilder().build();
       String controlId = "controlId-395080872";
       Control response = controlServiceClient.createControl(parent, control, controlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of parent catalog. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
`control` | `[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)`  
Required. The Control to create.  
`controlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Control, which will become the final component of the Control's resource name. This value should be 4-63 characters, and valid characters are /a-z-_/.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
### createControlCallable()
    
    
    public final UnaryCallable<CreateControlRequest,Control> createControlCallable()

Creates a Control.

If the Control to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       CreateControlRequest request =
           CreateControlRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateControlRequest),[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)>` |   
  
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
       ControlName name = ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]");
       controlServiceClient.deleteControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ControlName`  
Required. The resource name of the Control to delete. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/controls/{control_id}`  
  
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
                   ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]").toString())
               .build();
       controlServiceClient.deleteControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteControlRequest)`  
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
       String name = ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]").toString();
       controlServiceClient.deleteControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Control to delete. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/controls/{control_id}`  
  
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
                   ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]").toString())
               .build();
       ApiFuture<Empty> future = controlServiceClient.deleteControlCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteControlRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
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
       ControlName name = ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]");
       Control response = controlServiceClient.getControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ControlName`  
Required. The resource name of the Control to get. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/controls/{control_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
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
                   ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]").toString())
               .build();
       Control response = controlServiceClient.getControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
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
       String name = ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]").toString();
       Control response = controlServiceClient.getControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Control to get. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/controls/{control_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
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
                   ControlName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[CONTROL]").toString())
               .build();
       ApiFuture<Control> future = controlServiceClient.getControlCallable().futureCall(request);
       // Do something.
       Control response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetControlRequest),[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)>` |   
  
### getSettings()
    
    
    public final @Nullable ControlServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ControlServiceSettings` |   
  
### getStub()
    
    
    public ControlServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ControlServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ControlServiceStub)` |   
  
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
  
### listControls(@Nullable CatalogName parent)
    
    
    public final ControlServiceClient.ListControlsPagedResponse listControls(@Nullable CatalogName parent)

Lists all Controls by their parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       for (Control element : controlServiceClient.listControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. The catalog resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient.ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient.ListControlsPagedResponse)` |   
  
### listControls(ListControlsRequest request)
    
    
    public final ControlServiceClient.ListControlsPagedResponse listControls(ListControlsRequest request)

Lists all Controls by their parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ListControlsRequest request =
           ListControlsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
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
`request` | `[ListControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListControlsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient.ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient.ListControlsPagedResponse)` |   
  
### listControls(String parent)
    
    
    public final ControlServiceClient.ListControlsPagedResponse listControls(String parent)

Lists all Controls by their parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       for (Control element : controlServiceClient.listControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The catalog resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ControlServiceClient.ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient.ListControlsPagedResponse)` |   
  
### listControlsCallable()
    
    
    public final UnaryCallable<ListControlsRequest,ListControlsResponse> listControlsCallable()

Lists all Controls by their parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ListControlsRequest request =
           ListControlsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListControlsRequest),[ListControlsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListControlsResponse)>` |   
  
### listControlsPagedCallable()
    
    
    public final UnaryCallable<ListControlsRequest,ControlServiceClient.ListControlsPagedResponse> listControlsPagedCallable()

Lists all Controls by their parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ControlServiceClient controlServiceClient = ControlServiceClient.create()) {
       ListControlsRequest request =
           ListControlsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListControlsRequest),[ListControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ControlServiceClient.ListControlsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateControl(Control control, FieldMask updateMask)
    
    
    public final Control updateControl(Control control, FieldMask updateMask)

Updates a Control.

Control cannot be set to a different oneof field, if so an INVALID_ARGUMENT is returned. If the Control to update does not exist, a NOT_FOUND error is returned.

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
`control` | `[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)`  
Required. The Control to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided Control to update. The following are NOT supported: 

  * Control.name

If not set or empty, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
### updateControl(UpdateControlRequest request)
    
    
    public final Control updateControl(UpdateControlRequest request)

Updates a Control.

Control cannot be set to a different oneof field, if so an INVALID_ARGUMENT is returned. If the Control to update does not exist, a NOT_FOUND error is returned.

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
`request` | `[UpdateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)` |   
  
### updateControlCallable()
    
    
    public final UnaryCallable<UpdateControlRequest,Control> updateControlCallable()

Updates a Control.

Control cannot be set to a different oneof field, if so an INVALID_ARGUMENT is returned. If the Control to update does not exist, a NOT_FOUND error is returned.

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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateControlRequest),[Control](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Control)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
