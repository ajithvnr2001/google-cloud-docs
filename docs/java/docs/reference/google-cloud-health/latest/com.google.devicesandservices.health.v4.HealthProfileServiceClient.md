---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient
title: Class HealthProfileServiceClient (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:59.376496+00:00
---

# Class HealthProfileServiceClient (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HealthProfileServiceClient (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-health/google-cloud-health/src/main/java/com/google/devicesandservices/health/v4/HealthProfileServiceClient.java)| [Product Reference](https://developers.google.com/health/api)| [RPC Documentation](https://developers.google.com/health/api/reference/rpc)  
---|---|---  
  
Service Description: Health Profile Service

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       ProfileName name = ProfileName.of("[USER]");
       Profile response = healthProfileServiceClient.getProfile(name);
     }
     

Note: close() needs to be called on the HealthProfileServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetProfile |  Returns user Profile details. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProfile(GetProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProfile(ProfileName name) 
  * getProfile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProfileCallable() 

  
UpdateProfile |  Updates the user's profile details. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateProfile(UpdateProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateProfile(Profile profile, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateProfileCallable() 

  
GetSettings |  Returns user settings details. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSettings(GetSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSettings(SettingsName name) 
  * getSettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSettingsCallable() 

  
UpdateSettings |  Updates the user's settings details. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSettings(UpdateSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSettings(Settings settings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSettingsCallable() 

  
GetIdentity |  Gets the user's identity.  It includes the legacy Fitbit user ID and the Google user ID and it can be used by migrating clients to map identifiers between the two systems. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIdentity(GetIdentityRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIdentity(IdentityName name) 
  * getIdentity(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIdentityCallable() 

  
GetIrnProfile |  Returns user's IRN Profile details. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIrnProfile(GetIrnProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIrnProfile(IrnProfileName name) 
  * getIrnProfile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIrnProfileCallable() 

  
GetPairedDevice |  Returns user's Device. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPairedDevice(GetPairedDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPairedDevice(PairedDeviceName name) 
  * getPairedDevice(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPairedDeviceCallable() 

  
ListPairedDevices |  Returns the user's list of paired 1P trackers and smartwatches. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPairedDevices(ListPairedDevicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPairedDevices(UserName parent) 
  * listPairedDevices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPairedDevicesPagedCallable() 
  * listPairedDevicesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of HealthProfileServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HealthProfileServiceSettings healthProfileServiceSettings =
         HealthProfileServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create(healthProfileServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HealthProfileServiceSettings healthProfileServiceSettings =
         HealthProfileServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create(healthProfileServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HealthProfileServiceSettings healthProfileServiceSettings =
         HealthProfileServiceSettings.newHttpJsonBuilder().build();
     HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create(healthProfileServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HealthProfileServiceClient

## Static Methods 

### create()
    
    
    public static final HealthProfileServiceClient create()

Constructs an instance of HealthProfileServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[HealthProfileServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HealthProfileServiceSettings settings)
    
    
    public static final HealthProfileServiceClient create(HealthProfileServiceSettings settings)

Constructs an instance of HealthProfileServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HealthProfileServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HealthProfileServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HealthProfileServiceStub stub)
    
    
    public static final HealthProfileServiceClient create(HealthProfileServiceStub stub)

Constructs an instance of HealthProfileServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(HealthProfileServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HealthProfileServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.HealthProfileServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HealthProfileServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient)` |   
  
## Constructors 

### HealthProfileServiceClient(HealthProfileServiceSettings settings)
    
    
    protected HealthProfileServiceClient(HealthProfileServiceSettings settings)

Constructs an instance of HealthProfileServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HealthProfileServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceSettings)`  
  
  
### HealthProfileServiceClient(HealthProfileServiceStub stub)
    
    
    protected HealthProfileServiceClient(HealthProfileServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HealthProfileServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.HealthProfileServiceStub)`  
  
  
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

### getIdentity(@Nullable IdentityName name)
    
    
    public final Identity getIdentity(@Nullable IdentityName name)

Gets the user's identity.

It includes the legacy Fitbit user ID and the Google user ID and it can be used by migrating clients to map identifiers between the two systems.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       IdentityName name = IdentityName.of("[USER]");
       Identity response = healthProfileServiceClient.getIdentity(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.IdentityName`  
Required. The resource name of the Identity. Format: `users/me/identity`  
**Returns**  
---  
**Type** | **Description**  
`[Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Identity)` |   
  
### getIdentity(GetIdentityRequest request)
    
    
    public final Identity getIdentity(GetIdentityRequest request)

Gets the user's identity.

It includes the legacy Fitbit user ID and the Google user ID and it can be used by migrating clients to map identifiers between the two systems.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetIdentityRequest request =
           GetIdentityRequest.newBuilder().setName(IdentityName.of("[USER]").toString()).build();
       Identity response = healthProfileServiceClient.getIdentity(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetIdentityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Identity)` |   
  
### getIdentity(String name)
    
    
    public final Identity getIdentity(String name)

Gets the user's identity.

It includes the legacy Fitbit user ID and the Google user ID and it can be used by migrating clients to map identifiers between the two systems.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       String name = IdentityName.of("[USER]").toString();
       Identity response = healthProfileServiceClient.getIdentity(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Identity. Format: `users/me/identity`  
**Returns**  
---  
**Type** | **Description**  
`[Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Identity)` |   
  
### getIdentityCallable()
    
    
    public final UnaryCallable<GetIdentityRequest,Identity> getIdentityCallable()

Gets the user's identity.

It includes the legacy Fitbit user ID and the Google user ID and it can be used by migrating clients to map identifiers between the two systems.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetIdentityRequest request =
           GetIdentityRequest.newBuilder().setName(IdentityName.of("[USER]").toString()).build();
       ApiFuture<Identity> future =
           healthProfileServiceClient.getIdentityCallable().futureCall(request);
       // Do something.
       Identity response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetIdentityRequest),[Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Identity)>` |   
  
### getIrnProfile(@Nullable IrnProfileName name)
    
    
    public final IrnProfile getIrnProfile(@Nullable IrnProfileName name)

Returns user's IRN Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       IrnProfileName name = IrnProfileName.of("[USER]");
       IrnProfile response = healthProfileServiceClient.getIrnProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.IrnProfileName`  
Required. The resource name of the IRN Profile. Format: `users/{user}/irnProfile` Example: `users/1234567890/irnProfile` or `users/me/irnProfile` The {user} ID is a system-generated Google Health API user ID, a string of 1-63 characters consisting of lowercase and uppercase letters, numbers, and hyphens. The literal `me` can also be used to refer to the authenticated user.  
**Returns**  
---  
**Type** | **Description**  
`[IrnProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrnProfile)` |   
  
### getIrnProfile(GetIrnProfileRequest request)
    
    
    public final IrnProfile getIrnProfile(GetIrnProfileRequest request)

Returns user's IRN Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetIrnProfileRequest request =
           GetIrnProfileRequest.newBuilder().setName(IrnProfileName.of("[USER]").toString()).build();
       IrnProfile response = healthProfileServiceClient.getIrnProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIrnProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetIrnProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IrnProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrnProfile)` |   
  
### getIrnProfile(String name)
    
    
    public final IrnProfile getIrnProfile(String name)

Returns user's IRN Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       String name = IrnProfileName.of("[USER]").toString();
       IrnProfile response = healthProfileServiceClient.getIrnProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the IRN Profile. Format: `users/{user}/irnProfile` Example: `users/1234567890/irnProfile` or `users/me/irnProfile` The {user} ID is a system-generated Google Health API user ID, a string of 1-63 characters consisting of lowercase and uppercase letters, numbers, and hyphens. The literal `me` can also be used to refer to the authenticated user.  
**Returns**  
---  
**Type** | **Description**  
`[IrnProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrnProfile)` |   
  
### getIrnProfileCallable()
    
    
    public final UnaryCallable<GetIrnProfileRequest,IrnProfile> getIrnProfileCallable()

Returns user's IRN Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetIrnProfileRequest request =
           GetIrnProfileRequest.newBuilder().setName(IrnProfileName.of("[USER]").toString()).build();
       ApiFuture<IrnProfile> future =
           healthProfileServiceClient.getIrnProfileCallable().futureCall(request);
       // Do something.
       IrnProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIrnProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetIrnProfileRequest),[IrnProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrnProfile)>` |   
  
### getPairedDevice(@Nullable PairedDeviceName name)
    
    
    public final PairedDevice getPairedDevice(@Nullable PairedDeviceName name)

Returns user's Device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       PairedDeviceName name = PairedDeviceName.of("[USER]", "[PAIRED_DEVICE]");
       PairedDevice response = healthProfileServiceClient.getPairedDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.PairedDeviceName`  
Required. The name of the device to retrieve. Format: users/{user}/devices/{device}  
**Returns**  
---  
**Type** | **Description**  
`[PairedDevice](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.PairedDevice)` |   
  
### getPairedDevice(GetPairedDeviceRequest request)
    
    
    public final PairedDevice getPairedDevice(GetPairedDeviceRequest request)

Returns user's Device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetPairedDeviceRequest request =
           GetPairedDeviceRequest.newBuilder()
               .setName(PairedDeviceName.of("[USER]", "[PAIRED_DEVICE]").toString())
               .build();
       PairedDevice response = healthProfileServiceClient.getPairedDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPairedDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetPairedDeviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PairedDevice](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.PairedDevice)` |   
  
### getPairedDevice(String name)
    
    
    public final PairedDevice getPairedDevice(String name)

Returns user's Device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       String name = PairedDeviceName.of("[USER]", "[PAIRED_DEVICE]").toString();
       PairedDevice response = healthProfileServiceClient.getPairedDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device to retrieve. Format: users/{user}/devices/{device}  
**Returns**  
---  
**Type** | **Description**  
`[PairedDevice](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.PairedDevice)` |   
  
### getPairedDeviceCallable()
    
    
    public final UnaryCallable<GetPairedDeviceRequest,PairedDevice> getPairedDeviceCallable()

Returns user's Device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetPairedDeviceRequest request =
           GetPairedDeviceRequest.newBuilder()
               .setName(PairedDeviceName.of("[USER]", "[PAIRED_DEVICE]").toString())
               .build();
       ApiFuture<PairedDevice> future =
           healthProfileServiceClient.getPairedDeviceCallable().futureCall(request);
       // Do something.
       PairedDevice response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPairedDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetPairedDeviceRequest),[PairedDevice](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.PairedDevice)>` |   
  
### getProfile(@Nullable ProfileName name)
    
    
    public final Profile getProfile(@Nullable ProfileName name)

Returns user Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       ProfileName name = ProfileName.of("[USER]");
       Profile response = healthProfileServiceClient.getProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.ProfileName`  
Required. The name of the Profile. Format: `users/me/profile`.  
**Returns**  
---  
**Type** | **Description**  
`[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)` |   
  
### getProfile(GetProfileRequest request)
    
    
    public final Profile getProfile(GetProfileRequest request)

Returns user Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetProfileRequest request =
           GetProfileRequest.newBuilder().setName(ProfileName.of("[USER]").toString()).build();
       Profile response = healthProfileServiceClient.getProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)` |   
  
### getProfile(String name)
    
    
    public final Profile getProfile(String name)

Returns user Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       String name = ProfileName.of("[USER]").toString();
       Profile response = healthProfileServiceClient.getProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Profile. Format: `users/me/profile`.  
**Returns**  
---  
**Type** | **Description**  
`[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)` |   
  
### getProfileCallable()
    
    
    public final UnaryCallable<GetProfileRequest,Profile> getProfileCallable()

Returns user Profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetProfileRequest request =
           GetProfileRequest.newBuilder().setName(ProfileName.of("[USER]").toString()).build();
       ApiFuture<Profile> future =
           healthProfileServiceClient.getProfileCallable().futureCall(request);
       // Do something.
       Profile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetProfileRequest),[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)>` |   
  
### getSettings()
    
    
    public final @Nullable HealthProfileServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.HealthProfileServiceSettings` |   
  
### getSettings(@Nullable SettingsName name)
    
    
    public final Settings getSettings(@Nullable SettingsName name)

Returns user settings details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       SettingsName name = SettingsName.of("[USER]");
       Settings response = healthProfileServiceClient.getSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.SettingsName`  
Required. The name of the Settings. Format: `users/me/settings`.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)` |   
  
### getSettings(GetSettingsRequest request)
    
    
    public final Settings getSettings(GetSettingsRequest request)

Returns user settings details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetSettingsRequest request =
           GetSettingsRequest.newBuilder().setName(SettingsName.of("[USER]").toString()).build();
       Settings response = healthProfileServiceClient.getSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)` |   
  
### getSettings(String name)
    
    
    public final Settings getSettings(String name)

Returns user settings details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       String name = SettingsName.of("[USER]").toString();
       Settings response = healthProfileServiceClient.getSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Settings. Format: `users/me/settings`.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)` |   
  
### getSettingsCallable()
    
    
    public final UnaryCallable<GetSettingsRequest,Settings> getSettingsCallable()

Returns user settings details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       GetSettingsRequest request =
           GetSettingsRequest.newBuilder().setName(SettingsName.of("[USER]").toString()).build();
       ApiFuture<Settings> future =
           healthProfileServiceClient.getSettingsCallable().futureCall(request);
       // Do something.
       Settings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)>` |   
  
### getStub()
    
    
    public HealthProfileServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[HealthProfileServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.HealthProfileServiceStub)` |   
  
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
  
### listPairedDevices(@Nullable UserName parent)
    
    
    public final HealthProfileServiceClient.ListPairedDevicesPagedResponse listPairedDevices(@Nullable UserName parent)

Returns the user's list of paired 1P trackers and smartwatches.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       UserName parent = UserName.of("[USER]");
       for (PairedDevice element :
           healthProfileServiceClient.listPairedDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.UserName`  
Required. The parent, which owns this collection of devices. Format: users/{user}  
**Returns**  
---  
**Type** | **Description**  
`[HealthProfileServiceClient.ListPairedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient.ListPairedDevicesPagedResponse)` |   
  
### listPairedDevices(ListPairedDevicesRequest request)
    
    
    public final HealthProfileServiceClient.ListPairedDevicesPagedResponse listPairedDevices(ListPairedDevicesRequest request)

Returns the user's list of paired 1P trackers and smartwatches.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       ListPairedDevicesRequest request =
           ListPairedDevicesRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (PairedDevice element :
           healthProfileServiceClient.listPairedDevices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPairedDevicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListPairedDevicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HealthProfileServiceClient.ListPairedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient.ListPairedDevicesPagedResponse)` |   
  
### listPairedDevices(String parent)
    
    
    public final HealthProfileServiceClient.ListPairedDevicesPagedResponse listPairedDevices(String parent)

Returns the user's list of paired 1P trackers and smartwatches.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       String parent = UserName.of("[USER]").toString();
       for (PairedDevice element :
           healthProfileServiceClient.listPairedDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of devices. Format: users/{user}  
**Returns**  
---  
**Type** | **Description**  
`[HealthProfileServiceClient.ListPairedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient.ListPairedDevicesPagedResponse)` |   
  
### listPairedDevicesCallable()
    
    
    public final UnaryCallable<ListPairedDevicesRequest,ListPairedDevicesResponse> listPairedDevicesCallable()

Returns the user's list of paired 1P trackers and smartwatches.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       ListPairedDevicesRequest request =
           ListPairedDevicesRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPairedDevicesResponse response =
             healthProfileServiceClient.listPairedDevicesCallable().call(request);
         for (PairedDevice element : response.getPairedDevicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPairedDevicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListPairedDevicesRequest),[ListPairedDevicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListPairedDevicesResponse)>` |   
  
### listPairedDevicesPagedCallable()
    
    
    public final UnaryCallable<ListPairedDevicesRequest,HealthProfileServiceClient.ListPairedDevicesPagedResponse> listPairedDevicesPagedCallable()

Returns the user's list of paired 1P trackers and smartwatches.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       ListPairedDevicesRequest request =
           ListPairedDevicesRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<PairedDevice> future =
           healthProfileServiceClient.listPairedDevicesPagedCallable().futureCall(request);
       // Do something.
       for (PairedDevice element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPairedDevicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListPairedDevicesRequest),[ListPairedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HealthProfileServiceClient.ListPairedDevicesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateProfile(Profile profile, FieldMask updateMask)
    
    
    public final Profile updateProfile(Profile profile, FieldMask updateMask)

Updates the user's profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       Profile profile = Profile.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Profile response = healthProfileServiceClient.updateProfile(profile, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`profile` | `[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)`  
Required. Profile details.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)` |   
  
### updateProfile(UpdateProfileRequest request)
    
    
    public final Profile updateProfile(UpdateProfileRequest request)

Updates the user's profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       UpdateProfileRequest request =
           UpdateProfileRequest.newBuilder()
               .setProfile(Profile.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Profile response = healthProfileServiceClient.updateProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)` |   
  
### updateProfileCallable()
    
    
    public final UnaryCallable<UpdateProfileRequest,Profile> updateProfileCallable()

Updates the user's profile details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       UpdateProfileRequest request =
           UpdateProfileRequest.newBuilder()
               .setProfile(Profile.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Profile> future =
           healthProfileServiceClient.updateProfileCallable().futureCall(request);
       // Do something.
       Profile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateProfileRequest),[Profile](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Profile)>` |   
  
### updateSettings(Settings settings, FieldMask updateMask)
    
    
    public final Settings updateSettings(Settings settings, FieldMask updateMask)

Updates the user's settings details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       Settings settings = Settings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Settings response = healthProfileServiceClient.updateSettings(settings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)`  
Required. Settings details  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)` |   
  
### updateSettings(UpdateSettingsRequest request)
    
    
    public final Settings updateSettings(UpdateSettingsRequest request)

Updates the user's settings details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       UpdateSettingsRequest request =
           UpdateSettingsRequest.newBuilder()
               .setSettings(Settings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Settings response = healthProfileServiceClient.updateSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)` |   
  
### updateSettingsCallable()
    
    
    public final UnaryCallable<UpdateSettingsRequest,Settings> updateSettingsCallable()

Updates the user's settings details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HealthProfileServiceClient healthProfileServiceClient =
         HealthProfileServiceClient.create()) {
       UpdateSettingsRequest request =
           UpdateSettingsRequest.newBuilder()
               .setSettings(Settings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Settings> future =
           healthProfileServiceClient.updateSettingsCallable().futureCall(request);
       // Do something.
       Settings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Settings)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
