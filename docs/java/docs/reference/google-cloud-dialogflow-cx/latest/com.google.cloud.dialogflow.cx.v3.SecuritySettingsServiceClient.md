---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient
title: Class SecuritySettingsServiceClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:34:08.135776+00:00
---

# Class SecuritySettingsServiceClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecuritySettingsServiceClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/SecuritySettingsServiceClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing security settings for Dialogflow.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SecuritySettings securitySettings = SecuritySettings.newBuilder().build();
       SecuritySettings response =
           securitySettingsServiceClient.createSecuritySettings(parent, securitySettings);
     }
     

Note: close() needs to be called on the SecuritySettingsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateSecuritySettings |  Create security settings in the specified location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSecuritySettings(CreateSecuritySettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSecuritySettings(LocationName parent, SecuritySettings securitySettings) 
  * createSecuritySettings(String parent, SecuritySettings securitySettings) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSecuritySettingsCallable() 

  
GetSecuritySettings |  Retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSecuritySettings(GetSecuritySettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSecuritySettings(SecuritySettingsName name) 
  * getSecuritySettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSecuritySettingsCallable() 

  
UpdateSecuritySettings |  Updates the specified SecuritySettings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSecuritySettings(UpdateSecuritySettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSecuritySettings(SecuritySettings securitySettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSecuritySettingsCallable() 

  
ListSecuritySettings |  Returns the list of all security settings in the specified location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSecuritySettings(ListSecuritySettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSecuritySettings(LocationName parent) 
  * listSecuritySettings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSecuritySettingsPagedCallable() 
  * listSecuritySettingsCallable() 

  
DeleteSecuritySettings |  Deletes the specified SecuritySettings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSecuritySettings(DeleteSecuritySettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSecuritySettings(SecuritySettingsName name) 
  * deleteSecuritySettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSecuritySettingsCallable() 

  
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

This class can be customized by passing in a custom instance of SecuritySettingsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecuritySettingsServiceSettings securitySettingsServiceSettings =
         SecuritySettingsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create(securitySettingsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecuritySettingsServiceSettings securitySettingsServiceSettings =
         SecuritySettingsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create(securitySettingsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecuritySettingsServiceSettings securitySettingsServiceSettings =
         SecuritySettingsServiceSettings.newHttpJsonBuilder().build();
     SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create(securitySettingsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SecuritySettingsServiceClient

## Static Methods 

### create()
    
    
    public static final SecuritySettingsServiceClient create()

Constructs an instance of SecuritySettingsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SecuritySettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecuritySettingsServiceSettings settings)
    
    
    public static final SecuritySettingsServiceClient create(SecuritySettingsServiceSettings settings)

Constructs an instance of SecuritySettingsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecuritySettingsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecuritySettingsServiceStub stub)
    
    
    public static final SecuritySettingsServiceClient create(SecuritySettingsServiceStub stub)

Constructs an instance of SecuritySettingsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SecuritySettingsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecuritySettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.SecuritySettingsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient)` |   
  
## Constructors 

### SecuritySettingsServiceClient(SecuritySettingsServiceSettings settings)
    
    
    protected SecuritySettingsServiceClient(SecuritySettingsServiceSettings settings)

Constructs an instance of SecuritySettingsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecuritySettingsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceSettings)`  
  
  
### SecuritySettingsServiceClient(SecuritySettingsServiceStub stub)
    
    
    protected SecuritySettingsServiceClient(SecuritySettingsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecuritySettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.SecuritySettingsServiceStub)`  
  
  
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

### createSecuritySettings(@Nullable LocationName parent, SecuritySettings securitySettings)
    
    
    public final SecuritySettings createSecuritySettings(@Nullable LocationName parent, SecuritySettings securitySettings)

Create security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SecuritySettings securitySettings = SecuritySettings.newBuilder().build();
       SecuritySettings response =
           securitySettingsServiceClient.createSecuritySettings(parent, securitySettings);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.LocationName`  
Required. The location to create an SecuritySettings for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`securitySettings` | `[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)`  
Required. The security settings to create.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### createSecuritySettings(CreateSecuritySettingsRequest request)
    
    
    public final SecuritySettings createSecuritySettings(CreateSecuritySettingsRequest request)

Create security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       CreateSecuritySettingsRequest request =
           CreateSecuritySettingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSecuritySettings(SecuritySettings.newBuilder().build())
               .build();
       SecuritySettings response = securitySettingsServiceClient.createSecuritySettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### createSecuritySettings(String parent, SecuritySettings securitySettings)
    
    
    public final SecuritySettings createSecuritySettings(String parent, SecuritySettings securitySettings)

Create security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       SecuritySettings securitySettings = SecuritySettings.newBuilder().build();
       SecuritySettings response =
           securitySettingsServiceClient.createSecuritySettings(parent, securitySettings);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location to create an SecuritySettings for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`securitySettings` | `[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)`  
Required. The security settings to create.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### createSecuritySettingsCallable()
    
    
    public final UnaryCallable<CreateSecuritySettingsRequest,SecuritySettings> createSecuritySettingsCallable()

Create security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       CreateSecuritySettingsRequest request =
           CreateSecuritySettingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSecuritySettings(SecuritySettings.newBuilder().build())
               .build();
       ApiFuture<SecuritySettings> future =
           securitySettingsServiceClient.createSecuritySettingsCallable().futureCall(request);
       // Do something.
       SecuritySettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateSecuritySettingsRequest),[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)>` |   
  
### deleteSecuritySettings(@Nullable SecuritySettingsName name)
    
    
    public final void deleteSecuritySettings(@Nullable SecuritySettingsName name)

Deletes the specified SecuritySettings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       SecuritySettingsName name =
           SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]");
       securitySettingsServiceClient.deleteSecuritySettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.SecuritySettingsName`  
Required. The name of the SecuritySettings to delete. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`.  
  
### deleteSecuritySettings(DeleteSecuritySettingsRequest request)
    
    
    public final void deleteSecuritySettings(DeleteSecuritySettingsRequest request)

Deletes the specified SecuritySettings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       DeleteSecuritySettingsRequest request =
           DeleteSecuritySettingsRequest.newBuilder()
               .setName(
                   SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]")
                       .toString())
               .build();
       securitySettingsServiceClient.deleteSecuritySettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSecuritySettings(String name)
    
    
    public final void deleteSecuritySettings(String name)

Deletes the specified SecuritySettings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       String name =
           SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]").toString();
       securitySettingsServiceClient.deleteSecuritySettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the SecuritySettings to delete. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`.  
  
### deleteSecuritySettingsCallable()
    
    
    public final UnaryCallable<DeleteSecuritySettingsRequest,Empty> deleteSecuritySettingsCallable()

Deletes the specified SecuritySettings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       DeleteSecuritySettingsRequest request =
           DeleteSecuritySettingsRequest.newBuilder()
               .setName(
                   SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           securitySettingsServiceClient.deleteSecuritySettingsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteSecuritySettingsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = securitySettingsServiceClient.getLocation(request);
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
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           securitySettingsServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSecuritySettings(@Nullable SecuritySettingsName name)
    
    
    public final SecuritySettings getSecuritySettings(@Nullable SecuritySettingsName name)

Retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       SecuritySettingsName name =
           SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]");
       SecuritySettings response = securitySettingsServiceClient.getSecuritySettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.SecuritySettingsName`  
Required. Resource name of the settings. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<securitysettingsID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### getSecuritySettings(GetSecuritySettingsRequest request)
    
    
    public final SecuritySettings getSecuritySettings(GetSecuritySettingsRequest request)

Retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       GetSecuritySettingsRequest request =
           GetSecuritySettingsRequest.newBuilder()
               .setName(
                   SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]")
                       .toString())
               .build();
       SecuritySettings response = securitySettingsServiceClient.getSecuritySettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### getSecuritySettings(String name)
    
    
    public final SecuritySettings getSecuritySettings(String name)

Retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       String name =
           SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]").toString();
       SecuritySettings response = securitySettingsServiceClient.getSecuritySettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the settings. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<securitysettingsID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### getSecuritySettingsCallable()
    
    
    public final UnaryCallable<GetSecuritySettingsRequest,SecuritySettings> getSecuritySettingsCallable()

Retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       GetSecuritySettingsRequest request =
           GetSecuritySettingsRequest.newBuilder()
               .setName(
                   SecuritySettingsName.of("[PROJECT]", "[LOCATION]", "[SECURITY_SETTINGS]")
                       .toString())
               .build();
       ApiFuture<SecuritySettings> future =
           securitySettingsServiceClient.getSecuritySettingsCallable().futureCall(request);
       // Do something.
       SecuritySettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetSecuritySettingsRequest),[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)>` |   
  
### getSettings()
    
    
    public final @Nullable SecuritySettingsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceSettings` |   
  
### getStub()
    
    
    public SecuritySettingsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SecuritySettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.SecuritySettingsServiceStub)` |   
  
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
    
    
    public final SecuritySettingsServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : securitySettingsServiceClient.listLocations(request).iterateAll()) {
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
`[SecuritySettingsServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             securitySettingsServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SecuritySettingsServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           securitySettingsServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient.ListLocationsPagedResponse)>` |   
  
### listSecuritySettings(@Nullable LocationName parent)
    
    
    public final SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse listSecuritySettings(@Nullable LocationName parent)

Returns the list of all security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SecuritySettings element :
           securitySettingsServiceClient.listSecuritySettings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.LocationName`  
Required. The location to list all security settings for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse)` |   
  
### listSecuritySettings(ListSecuritySettingsRequest request)
    
    
    public final SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse listSecuritySettings(ListSecuritySettingsRequest request)

Returns the list of all security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       ListSecuritySettingsRequest request =
           ListSecuritySettingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SecuritySettings element :
           securitySettingsServiceClient.listSecuritySettings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse)` |   
  
### listSecuritySettings(String parent)
    
    
    public final SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse listSecuritySettings(String parent)

Returns the list of all security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SecuritySettings element :
           securitySettingsServiceClient.listSecuritySettings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location to list all security settings for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse)` |   
  
### listSecuritySettingsCallable()
    
    
    public final UnaryCallable<ListSecuritySettingsRequest,ListSecuritySettingsResponse> listSecuritySettingsCallable()

Returns the list of all security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       ListSecuritySettingsRequest request =
           ListSecuritySettingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSecuritySettingsResponse response =
             securitySettingsServiceClient.listSecuritySettingsCallable().call(request);
         for (SecuritySettings element : response.getSecuritySettingsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListSecuritySettingsRequest),[ListSecuritySettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListSecuritySettingsResponse)>` |   
  
### listSecuritySettingsPagedCallable()
    
    
    public final UnaryCallable<ListSecuritySettingsRequest,SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse> listSecuritySettingsPagedCallable()

Returns the list of all security settings in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       ListSecuritySettingsRequest request =
           ListSecuritySettingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SecuritySettings> future =
           securitySettingsServiceClient.listSecuritySettingsPagedCallable().futureCall(request);
       // Do something.
       for (SecuritySettings element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListSecuritySettingsRequest),[ListSecuritySettingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient.ListSecuritySettingsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSecuritySettings(SecuritySettings securitySettings, FieldMask updateMask)
    
    
    public final SecuritySettings updateSecuritySettings(SecuritySettings securitySettings, FieldMask updateMask)

Updates the specified SecuritySettings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       SecuritySettings securitySettings = SecuritySettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SecuritySettings response =
           securitySettingsServiceClient.updateSecuritySettings(securitySettings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securitySettings` | `[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)`  
Required. [SecuritySettings] object that contains values for each of the fields to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### updateSecuritySettings(UpdateSecuritySettingsRequest request)
    
    
    public final SecuritySettings updateSecuritySettings(UpdateSecuritySettingsRequest request)

Updates the specified SecuritySettings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       UpdateSecuritySettingsRequest request =
           UpdateSecuritySettingsRequest.newBuilder()
               .setSecuritySettings(SecuritySettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SecuritySettings response = securitySettingsServiceClient.updateSecuritySettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)` |   
  
### updateSecuritySettingsCallable()
    
    
    public final UnaryCallable<UpdateSecuritySettingsRequest,SecuritySettings> updateSecuritySettingsCallable()

Updates the specified SecuritySettings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecuritySettingsServiceClient securitySettingsServiceClient =
         SecuritySettingsServiceClient.create()) {
       UpdateSecuritySettingsRequest request =
           UpdateSecuritySettingsRequest.newBuilder()
               .setSecuritySettings(SecuritySettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SecuritySettings> future =
           securitySettingsServiceClient.updateSecuritySettingsCallable().futureCall(request);
       // Do something.
       SecuritySettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateSecuritySettingsRequest),[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettings)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
