---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient
title: Class AppConnectorsServiceClient (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:08.678828+00:00
---

# Class AppConnectorsServiceClient (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AppConnectorsServiceClient (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-beyondcorp-appconnectors/google-cloud-beyondcorp-appconnectors/src/main/java/com/google/cloud/beyondcorp/appconnectors/v1/AppConnectorsServiceClient.java)| [Product Reference](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/cloud.google.com/beyondcorp-enterprise)  
---|---  
  
Service Description: API Overview:

The `beyondcorp.googleapis.com` service implements the Google Cloud BeyondCorp API.

Data Model:

The AppConnectorsService exposes the following resource:

  * AppConnectors, named as follows: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}`. 



The AppConnectorsService provides methods to manage (create/read/update/delete) BeyondCorp AppConnectors.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       AppConnectorName name = AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]");
       AppConnector response = appConnectorsServiceClient.getAppConnector(name);
     }
     

Note: close() needs to be called on the AppConnectorsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListAppConnectors |  Lists AppConnectors in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAppConnectors(ListAppConnectorsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAppConnectors(LocationName parent) 
  * listAppConnectors(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAppConnectorsPagedCallable() 
  * listAppConnectorsCallable() 

  
GetAppConnector |  Gets details of a single AppConnector. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAppConnector(GetAppConnectorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAppConnector(AppConnectorName name) 
  * getAppConnector(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAppConnectorCallable() 

  
CreateAppConnector |  Creates a new AppConnector in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAppConnectorAsync(CreateAppConnectorRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAppConnectorAsync(LocationName parent, AppConnector appConnector, String appConnectorId) 
  * createAppConnectorAsync(String parent, AppConnector appConnector, String appConnectorId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAppConnectorOperationCallable() 
  * createAppConnectorCallable() 

  
UpdateAppConnector |  Updates the parameters of a single AppConnector. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAppConnectorAsync(UpdateAppConnectorRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAppConnectorAsync(AppConnector appConnector, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAppConnectorOperationCallable() 
  * updateAppConnectorCallable() 

  
DeleteAppConnector |  Deletes a single AppConnector. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAppConnectorAsync(DeleteAppConnectorRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAppConnectorAsync(AppConnectorName name) 
  * deleteAppConnectorAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAppConnectorOperationCallable() 
  * deleteAppConnectorCallable() 

  
ReportStatus |  Report status for a given connector. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reportStatusAsync(ReportStatusRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * reportStatusAsync(AppConnectorName appConnector, ResourceInfo resourceInfo) 
  * reportStatusAsync(String appConnector, ResourceInfo resourceInfo) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reportStatusOperationCallable() 
  * reportStatusCallable() 

  
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

This class can be customized by passing in a custom instance of AppConnectorsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AppConnectorsServiceSettings appConnectorsServiceSettings =
         AppConnectorsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create(appConnectorsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AppConnectorsServiceSettings appConnectorsServiceSettings =
         AppConnectorsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create(appConnectorsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AppConnectorsServiceClient

## Static Methods 

### create()
    
    
    public static final AppConnectorsServiceClient create()

Constructs an instance of AppConnectorsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AppConnectorsServiceSettings settings)
    
    
    public static final AppConnectorsServiceClient create(AppConnectorsServiceSettings settings)

Constructs an instance of AppConnectorsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AppConnectorsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AppConnectorsServiceStub stub)
    
    
    public static final AppConnectorsServiceClient create(AppConnectorsServiceStub stub)

Constructs an instance of AppConnectorsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AppConnectorsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AppConnectorsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.stub.AppConnectorsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient)` |   
  
## Constructors 

### AppConnectorsServiceClient(AppConnectorsServiceSettings settings)
    
    
    protected AppConnectorsServiceClient(AppConnectorsServiceSettings settings)

Constructs an instance of AppConnectorsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AppConnectorsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceSettings)`  
  
  
### AppConnectorsServiceClient(AppConnectorsServiceStub stub)
    
    
    protected AppConnectorsServiceClient(AppConnectorsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AppConnectorsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.stub.AppConnectorsServiceStub)`  
  
  
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

### createAppConnectorAsync(@Nullable LocationName parent, AppConnector appConnector, String appConnectorId)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> createAppConnectorAsync(@Nullable LocationName parent, AppConnector appConnector, String appConnectorId)

Creates a new AppConnector in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AppConnector appConnector = AppConnector.newBuilder().build();
       String appConnectorId = "appConnectorId374103399";
       AppConnector response =
           appConnectorsServiceClient
               .createAppConnectorAsync(parent, appConnector, appConnectorId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.appconnectors.v1.LocationName`  
Required. The resource project name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`  
`appConnector` | `[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)`  
Required. A BeyondCorp AppConnector resource.  
`appConnectorId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User-settable AppConnector resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### createAppConnectorAsync(CreateAppConnectorRequest request)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> createAppConnectorAsync(CreateAppConnectorRequest request)

Creates a new AppConnector in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       CreateAppConnectorRequest request =
           CreateAppConnectorRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAppConnectorId("appConnectorId374103399")
               .setAppConnector(AppConnector.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       AppConnector response = appConnectorsServiceClient.createAppConnectorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.CreateAppConnectorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### createAppConnectorAsync(String parent, AppConnector appConnector, String appConnectorId)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> createAppConnectorAsync(String parent, AppConnector appConnector, String appConnectorId)

Creates a new AppConnector in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AppConnector appConnector = AppConnector.newBuilder().build();
       String appConnectorId = "appConnectorId374103399";
       AppConnector response =
           appConnectorsServiceClient
               .createAppConnectorAsync(parent, appConnector, appConnectorId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource project name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`  
`appConnector` | `[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)`  
Required. A BeyondCorp AppConnector resource.  
`appConnectorId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User-settable AppConnector resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### createAppConnectorCallable()
    
    
    public final UnaryCallable<CreateAppConnectorRequest,Operation> createAppConnectorCallable()

Creates a new AppConnector in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       CreateAppConnectorRequest request =
           CreateAppConnectorRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAppConnectorId("appConnectorId374103399")
               .setAppConnector(AppConnector.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           appConnectorsServiceClient.createAppConnectorCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.CreateAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAppConnectorOperationCallable()
    
    
    public final OperationCallable<CreateAppConnectorRequest,AppConnector,AppConnectorOperationMetadata> createAppConnectorOperationCallable()

Creates a new AppConnector in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       CreateAppConnectorRequest request =
           CreateAppConnectorRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAppConnectorId("appConnectorId374103399")
               .setAppConnector(AppConnector.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<AppConnector, AppConnectorOperationMetadata> future =
           appConnectorsServiceClient.createAppConnectorOperationCallable().futureCall(request);
       // Do something.
       AppConnector response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.CreateAppConnectorRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### deleteAppConnectorAsync(@Nullable AppConnectorName name)
    
    
    public final OperationFuture<Empty,AppConnectorOperationMetadata> deleteAppConnectorAsync(@Nullable AppConnectorName name)

Deletes a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       AppConnectorName name = AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]");
       appConnectorsServiceClient.deleteAppConnectorAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorName`  
Required. BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### deleteAppConnectorAsync(DeleteAppConnectorRequest request)
    
    
    public final OperationFuture<Empty,AppConnectorOperationMetadata> deleteAppConnectorAsync(DeleteAppConnectorRequest request)

Deletes a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       DeleteAppConnectorRequest request =
           DeleteAppConnectorRequest.newBuilder()
               .setName(AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       appConnectorsServiceClient.deleteAppConnectorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.DeleteAppConnectorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### deleteAppConnectorAsync(String name)
    
    
    public final OperationFuture<Empty,AppConnectorOperationMetadata> deleteAppConnectorAsync(String name)

Deletes a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       String name = AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString();
       appConnectorsServiceClient.deleteAppConnectorAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### deleteAppConnectorCallable()
    
    
    public final UnaryCallable<DeleteAppConnectorRequest,Operation> deleteAppConnectorCallable()

Deletes a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       DeleteAppConnectorRequest request =
           DeleteAppConnectorRequest.newBuilder()
               .setName(AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           appConnectorsServiceClient.deleteAppConnectorCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.DeleteAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAppConnectorOperationCallable()
    
    
    public final OperationCallable<DeleteAppConnectorRequest,Empty,AppConnectorOperationMetadata> deleteAppConnectorOperationCallable()

Deletes a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       DeleteAppConnectorRequest request =
           DeleteAppConnectorRequest.newBuilder()
               .setName(AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Empty, AppConnectorOperationMetadata> future =
           appConnectorsServiceClient.deleteAppConnectorOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.DeleteAppConnectorRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### getAppConnector(@Nullable AppConnectorName name)
    
    
    public final AppConnector getAppConnector(@Nullable AppConnectorName name)

Gets details of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       AppConnectorName name = AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]");
       AppConnector response = appConnectorsServiceClient.getAppConnector(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorName`  
Required. BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)` |   
  
### getAppConnector(GetAppConnectorRequest request)
    
    
    public final AppConnector getAppConnector(GetAppConnectorRequest request)

Gets details of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       GetAppConnectorRequest request =
           GetAppConnectorRequest.newBuilder()
               .setName(AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .build();
       AppConnector response = appConnectorsServiceClient.getAppConnector(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.GetAppConnectorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)` |   
  
### getAppConnector(String name)
    
    
    public final AppConnector getAppConnector(String name)

Gets details of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       String name = AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString();
       AppConnector response = appConnectorsServiceClient.getAppConnector(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)` |   
  
### getAppConnectorCallable()
    
    
    public final UnaryCallable<GetAppConnectorRequest,AppConnector> getAppConnectorCallable()

Gets details of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       GetAppConnectorRequest request =
           GetAppConnectorRequest.newBuilder()
               .setName(AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .build();
       ApiFuture<AppConnector> future =
           appConnectorsServiceClient.getAppConnectorCallable().futureCall(request);
       // Do something.
       AppConnector response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.GetAppConnectorRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = appConnectorsServiceClient.getIamPolicy(request);
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
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           appConnectorsServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = appConnectorsServiceClient.getLocation(request);
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
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           appConnectorsServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable AppConnectorsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceSettings` |   
  
### getStub()
    
    
    public AppConnectorsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.stub.AppConnectorsServiceStub)` |   
  
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
  
### listAppConnectors(@Nullable LocationName parent)
    
    
    public final AppConnectorsServiceClient.ListAppConnectorsPagedResponse listAppConnectors(@Nullable LocationName parent)

Lists AppConnectors in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AppConnector element :
           appConnectorsServiceClient.listAppConnectors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.appconnectors.v1.LocationName`  
Required. The resource name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceClient.ListAppConnectorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListAppConnectorsPagedResponse)` |   
  
### listAppConnectors(ListAppConnectorsRequest request)
    
    
    public final AppConnectorsServiceClient.ListAppConnectorsPagedResponse listAppConnectors(ListAppConnectorsRequest request)

Lists AppConnectors in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ListAppConnectorsRequest request =
           ListAppConnectorsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AppConnector element :
           appConnectorsServiceClient.listAppConnectors(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAppConnectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceClient.ListAppConnectorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListAppConnectorsPagedResponse)` |   
  
### listAppConnectors(String parent)
    
    
    public final AppConnectorsServiceClient.ListAppConnectorsPagedResponse listAppConnectors(String parent)

Lists AppConnectors in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AppConnector element :
           appConnectorsServiceClient.listAppConnectors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AppConnectorsServiceClient.ListAppConnectorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListAppConnectorsPagedResponse)` |   
  
### listAppConnectorsCallable()
    
    
    public final UnaryCallable<ListAppConnectorsRequest,ListAppConnectorsResponse> listAppConnectorsCallable()

Lists AppConnectors in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ListAppConnectorsRequest request =
           ListAppConnectorsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAppConnectorsResponse response =
             appConnectorsServiceClient.listAppConnectorsCallable().call(request);
         for (AppConnector element : response.getAppConnectorsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppConnectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsRequest),[ListAppConnectorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsResponse)>` |   
  
### listAppConnectorsPagedCallable()
    
    
    public final UnaryCallable<ListAppConnectorsRequest,AppConnectorsServiceClient.ListAppConnectorsPagedResponse> listAppConnectorsPagedCallable()

Lists AppConnectors in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ListAppConnectorsRequest request =
           ListAppConnectorsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AppConnector> future =
           appConnectorsServiceClient.listAppConnectorsPagedCallable().futureCall(request);
       // Do something.
       for (AppConnector element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppConnectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsRequest),[ListAppConnectorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListAppConnectorsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final AppConnectorsServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : appConnectorsServiceClient.listLocations(request).iterateAll()) {
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
`[AppConnectorsServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             appConnectorsServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,AppConnectorsServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           appConnectorsServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListLocationsPagedResponse)>` |   
  
### reportStatusAsync(@Nullable AppConnectorName appConnector, ResourceInfo resourceInfo)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> reportStatusAsync(@Nullable AppConnectorName appConnector, ResourceInfo resourceInfo)

Report status for a given connector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       AppConnectorName appConnector =
           AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]");
       ResourceInfo resourceInfo = ResourceInfo.newBuilder().build();
       AppConnector response =
           appConnectorsServiceClient.reportStatusAsync(appConnector, resourceInfo).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`appConnector` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorName`  
Required. BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector}`  
`resourceInfo` | `[ResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfo)`  
Required. Resource info of the connector.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### reportStatusAsync(ReportStatusRequest request)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> reportStatusAsync(ReportStatusRequest request)

Report status for a given connector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ReportStatusRequest request =
           ReportStatusRequest.newBuilder()
               .setAppConnector(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setResourceInfo(ResourceInfo.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       AppConnector response = appConnectorsServiceClient.reportStatusAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReportStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ReportStatusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### reportStatusAsync(String appConnector, ResourceInfo resourceInfo)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> reportStatusAsync(String appConnector, ResourceInfo resourceInfo)

Report status for a given connector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       String appConnector =
           AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString();
       ResourceInfo resourceInfo = ResourceInfo.newBuilder().build();
       AppConnector response =
           appConnectorsServiceClient.reportStatusAsync(appConnector, resourceInfo).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`appConnector` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector}`  
`resourceInfo` | `[ResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfo)`  
Required. Resource info of the connector.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### reportStatusCallable()
    
    
    public final UnaryCallable<ReportStatusRequest,Operation> reportStatusCallable()

Report status for a given connector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ReportStatusRequest request =
           ReportStatusRequest.newBuilder()
               .setAppConnector(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setResourceInfo(ResourceInfo.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           appConnectorsServiceClient.reportStatusCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReportStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ReportStatusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### reportStatusOperationCallable()
    
    
    public final OperationCallable<ReportStatusRequest,AppConnector,AppConnectorOperationMetadata> reportStatusOperationCallable()

Report status for a given connector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       ReportStatusRequest request =
           ReportStatusRequest.newBuilder()
               .setAppConnector(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setResourceInfo(ResourceInfo.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<AppConnector, AppConnectorOperationMetadata> future =
           appConnectorsServiceClient.reportStatusOperationCallable().futureCall(request);
       // Do something.
       AppConnector response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ReportStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ReportStatusRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
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
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = appConnectorsServiceClient.setIamPolicy(request);
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
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           appConnectorsServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = appConnectorsServiceClient.testIamPermissions(request);
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
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AppConnectorName.of("[PROJECT]", "[LOCATION]", "[APP_CONNECTOR]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           appConnectorsServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAppConnectorAsync(AppConnector appConnector, FieldMask updateMask)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> updateAppConnectorAsync(AppConnector appConnector, FieldMask updateMask)

Updates the parameters of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       AppConnector appConnector = AppConnector.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AppConnector response =
           appConnectorsServiceClient.updateAppConnectorAsync(appConnector, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`appConnector` | `[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)`  
Required. AppConnector message with updated fields. Only supported fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.AppConnector]: 

  * `labels`
  * `display_name`

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### updateAppConnectorAsync(UpdateAppConnectorRequest request)
    
    
    public final OperationFuture<AppConnector,AppConnectorOperationMetadata> updateAppConnectorAsync(UpdateAppConnectorRequest request)

Updates the parameters of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       UpdateAppConnectorRequest request =
           UpdateAppConnectorRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAppConnector(AppConnector.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       AppConnector response = appConnectorsServiceClient.updateAppConnectorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.UpdateAppConnectorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### updateAppConnectorCallable()
    
    
    public final UnaryCallable<UpdateAppConnectorRequest,Operation> updateAppConnectorCallable()

Updates the parameters of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       UpdateAppConnectorRequest request =
           UpdateAppConnectorRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAppConnector(AppConnector.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           appConnectorsServiceClient.updateAppConnectorCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.UpdateAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAppConnectorOperationCallable()
    
    
    public final OperationCallable<UpdateAppConnectorRequest,AppConnector,AppConnectorOperationMetadata> updateAppConnectorOperationCallable()

Updates the parameters of a single AppConnector.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AppConnectorsServiceClient appConnectorsServiceClient =
         AppConnectorsServiceClient.create()) {
       UpdateAppConnectorRequest request =
           UpdateAppConnectorRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAppConnector(AppConnector.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<AppConnector, AppConnectorOperationMetadata> future =
           appConnectorsServiceClient.updateAppConnectorOperationCallable().futureCall(request);
       // Do something.
       AppConnector response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.UpdateAppConnectorRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
