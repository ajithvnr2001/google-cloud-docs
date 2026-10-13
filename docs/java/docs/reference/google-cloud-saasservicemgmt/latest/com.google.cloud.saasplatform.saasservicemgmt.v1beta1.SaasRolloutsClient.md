---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient
title: Class SaasRolloutsClient (0.29.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:58.152568+00:00
---

# Class SaasRolloutsClient (0.29.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SaasRolloutsClient (0.29.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.0 (latest)  0.25.0  0.24.0  0.23.0  0.21.0  0.18.0  0.17.0  0.15.0  0.13.0  0.12.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-saasservicemgmt/google-cloud-saasservicemgmt/src/main/java/com/google/cloud/saasplatform/saasservicemgmt/v1beta1/SaasRolloutsClient.java)| [Product Reference](https://cloud.google.com/saas-runtime/docs/overview)| [RPC Documentation](https://cloud.google.com/saas-runtime/docs/apis)  
---|---|---  
  
Service Description: Manages the rollout of SaaS services.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       RolloutName name = RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]");
       Rollout response = saasRolloutsClient.getRollout(name);
     }
     

Note: close() needs to be called on the SaasRolloutsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListRollouts |  Retrieve a collection of rollouts. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRollouts(ListRolloutsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRollouts(LocationName parent) 
  * listRollouts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRolloutsPagedCallable() 
  * listRolloutsCallable() 

  
GetRollout |  Retrieve a single rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRollout(GetRolloutRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRollout(RolloutName name) 
  * getRollout(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRolloutCallable() 

  
CreateRollout |  Create a new rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRollout(CreateRolloutRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createRollout(LocationName parent, Rollout rollout, String rolloutId) 
  * createRollout(String parent, Rollout rollout, String rolloutId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRolloutCallable() 

  
UpdateRollout |  Update a single rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRollout(UpdateRolloutRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRollout(Rollout rollout, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRolloutCallable() 

  
DeleteRollout |  Delete a single rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRollout(DeleteRolloutRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteRollout(RolloutName name) 
  * deleteRollout(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRolloutCallable() 

  
ListRolloutKinds |  Retrieve a collection of rollout kinds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRolloutKinds(ListRolloutKindsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRolloutKinds(LocationName parent) 
  * listRolloutKinds(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRolloutKindsPagedCallable() 
  * listRolloutKindsCallable() 

  
GetRolloutKind |  Retrieve a single rollout kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRolloutKind(GetRolloutKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRolloutKind(RolloutKindName name) 
  * getRolloutKind(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRolloutKindCallable() 

  
CreateRolloutKind |  Create a new rollout kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRolloutKind(CreateRolloutKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createRolloutKind(LocationName parent, RolloutKind rolloutKind, String rolloutKindId) 
  * createRolloutKind(String parent, RolloutKind rolloutKind, String rolloutKindId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRolloutKindCallable() 

  
UpdateRolloutKind |  Update a single rollout kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRolloutKind(UpdateRolloutKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRolloutKind(RolloutKind rolloutKind, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRolloutKindCallable() 

  
DeleteRolloutKind |  Delete a single rollout kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRolloutKind(DeleteRolloutKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteRolloutKind(RolloutKindName name) 
  * deleteRolloutKind(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRolloutKindCallable() 

  
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

This class can be customized by passing in a custom instance of SaasRolloutsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SaasRolloutsSettings saasRolloutsSettings =
         SaasRolloutsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create(saasRolloutsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SaasRolloutsSettings saasRolloutsSettings =
         SaasRolloutsSettings.newBuilder().setEndpoint(myEndpoint).build();
     SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create(saasRolloutsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SaasRolloutsSettings saasRolloutsSettings = SaasRolloutsSettings.newHttpJsonBuilder().build();
     SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create(saasRolloutsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SaasRolloutsClient

## Static Methods 

### create()
    
    
    public static final SaasRolloutsClient create()

Constructs an instance of SaasRolloutsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SaasRolloutsSettings settings)
    
    
    public static final SaasRolloutsClient create(SaasRolloutsSettings settings)

Constructs an instance of SaasRolloutsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SaasRolloutsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SaasRolloutsStub stub)
    
    
    public static final SaasRolloutsClient create(SaasRolloutsStub stub)

Constructs an instance of SaasRolloutsClient, using the given stub for making calls. This is for advanced usage - prefer using create(SaasRolloutsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SaasRolloutsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasRolloutsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient)` |   
  
## Constructors 

### SaasRolloutsClient(SaasRolloutsSettings settings)
    
    
    protected SaasRolloutsClient(SaasRolloutsSettings settings)

Constructs an instance of SaasRolloutsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SaasRolloutsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsSettings)`  
  
  
### SaasRolloutsClient(SaasRolloutsStub stub)
    
    
    protected SaasRolloutsClient(SaasRolloutsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SaasRolloutsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasRolloutsStub)`  
  
  
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

### createRollout(@Nullable LocationName parent, Rollout rollout, String rolloutId)
    
    
    public final Rollout createRollout(@Nullable LocationName parent, Rollout rollout, String rolloutId)

Create a new rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Rollout rollout = Rollout.newBuilder().build();
       String rolloutId = "rolloutId551248556";
       Rollout response = saasRolloutsClient.createRollout(parent, rollout, rolloutId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the rollout.  
`rollout` | `[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)`  
Required. The desired state for the rollout.  
`rolloutId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new rollout.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### createRollout(CreateRolloutRequest request)
    
    
    public final Rollout createRollout(CreateRolloutRequest request)

Create a new rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       CreateRolloutRequest request =
           CreateRolloutRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRolloutId("rolloutId551248556")
               .setRollout(Rollout.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       Rollout response = saasRolloutsClient.createRollout(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### createRollout(String parent, Rollout rollout, String rolloutId)
    
    
    public final Rollout createRollout(String parent, Rollout rollout, String rolloutId)

Create a new rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Rollout rollout = Rollout.newBuilder().build();
       String rolloutId = "rolloutId551248556";
       Rollout response = saasRolloutsClient.createRollout(parent, rollout, rolloutId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the rollout.  
`rollout` | `[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)`  
Required. The desired state for the rollout.  
`rolloutId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new rollout.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### createRolloutCallable()
    
    
    public final UnaryCallable<CreateRolloutRequest,Rollout> createRolloutCallable()

Create a new rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       CreateRolloutRequest request =
           CreateRolloutRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRolloutId("rolloutId551248556")
               .setRollout(Rollout.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Rollout> future = saasRolloutsClient.createRolloutCallable().futureCall(request);
       // Do something.
       Rollout response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateRolloutRequest),[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)>` |   
  
### createRolloutKind(@Nullable LocationName parent, RolloutKind rolloutKind, String rolloutKindId)
    
    
    public final RolloutKind createRolloutKind(@Nullable LocationName parent, RolloutKind rolloutKind, String rolloutKindId)

Create a new rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RolloutKind rolloutKind = RolloutKind.newBuilder().build();
       String rolloutKindId = "rolloutKindId-1380592416";
       RolloutKind response =
           saasRolloutsClient.createRolloutKind(parent, rolloutKind, rolloutKindId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the rollout kind.  
`rolloutKind` | `[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)`  
Required. The desired state for the rollout kind.  
`rolloutKindId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new rollout kind.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### createRolloutKind(CreateRolloutKindRequest request)
    
    
    public final RolloutKind createRolloutKind(CreateRolloutKindRequest request)

Create a new rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       CreateRolloutKindRequest request =
           CreateRolloutKindRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRolloutKindId("rolloutKindId-1380592416")
               .setRolloutKind(RolloutKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       RolloutKind response = saasRolloutsClient.createRolloutKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateRolloutKindRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### createRolloutKind(String parent, RolloutKind rolloutKind, String rolloutKindId)
    
    
    public final RolloutKind createRolloutKind(String parent, RolloutKind rolloutKind, String rolloutKindId)

Create a new rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       RolloutKind rolloutKind = RolloutKind.newBuilder().build();
       String rolloutKindId = "rolloutKindId-1380592416";
       RolloutKind response =
           saasRolloutsClient.createRolloutKind(parent, rolloutKind, rolloutKindId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the rollout kind.  
`rolloutKind` | `[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)`  
Required. The desired state for the rollout kind.  
`rolloutKindId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new rollout kind.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### createRolloutKindCallable()
    
    
    public final UnaryCallable<CreateRolloutKindRequest,RolloutKind> createRolloutKindCallable()

Create a new rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       CreateRolloutKindRequest request =
           CreateRolloutKindRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRolloutKindId("rolloutKindId-1380592416")
               .setRolloutKind(RolloutKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<RolloutKind> future =
           saasRolloutsClient.createRolloutKindCallable().futureCall(request);
       // Do something.
       RolloutKind response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateRolloutKindRequest),[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)>` |   
  
### deleteRollout(@Nullable RolloutName name)
    
    
    public final void deleteRollout(@Nullable RolloutName name)

Delete a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       RolloutName name = RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]");
       saasRolloutsClient.deleteRollout(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutName`  
Required. The resource name of the resource within a service.  
  
### deleteRollout(DeleteRolloutRequest request)
    
    
    public final void deleteRollout(DeleteRolloutRequest request)

Delete a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       DeleteRolloutRequest request =
           DeleteRolloutRequest.newBuilder()
               .setName(RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasRolloutsClient.deleteRollout(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteRolloutRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteRollout(String name)
    
    
    public final void deleteRollout(String name)

Delete a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String name = RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]").toString();
       saasRolloutsClient.deleteRollout(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteRolloutCallable()
    
    
    public final UnaryCallable<DeleteRolloutRequest,Empty> deleteRolloutCallable()

Delete a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       DeleteRolloutRequest request =
           DeleteRolloutRequest.newBuilder()
               .setName(RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future = saasRolloutsClient.deleteRolloutCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteRolloutRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteRolloutKind(@Nullable RolloutKindName name)
    
    
    public final void deleteRolloutKind(@Nullable RolloutKindName name)

Delete a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       RolloutKindName name = RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]");
       saasRolloutsClient.deleteRolloutKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKindName`  
Required. The resource name of the resource within a service.  
  
### deleteRolloutKind(DeleteRolloutKindRequest request)
    
    
    public final void deleteRolloutKind(DeleteRolloutKindRequest request)

Delete a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       DeleteRolloutKindRequest request =
           DeleteRolloutKindRequest.newBuilder()
               .setName(
                   RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasRolloutsClient.deleteRolloutKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteRolloutKindRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteRolloutKind(String name)
    
    
    public final void deleteRolloutKind(String name)

Delete a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String name = RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]").toString();
       saasRolloutsClient.deleteRolloutKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteRolloutKindCallable()
    
    
    public final UnaryCallable<DeleteRolloutKindRequest,Empty> deleteRolloutKindCallable()

Delete a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       DeleteRolloutKindRequest request =
           DeleteRolloutKindRequest.newBuilder()
               .setName(
                   RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future = saasRolloutsClient.deleteRolloutKindCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteRolloutKindRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = saasRolloutsClient.getLocation(request);
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
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = saasRolloutsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getRollout(@Nullable RolloutName name)
    
    
    public final Rollout getRollout(@Nullable RolloutName name)

Retrieve a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       RolloutName name = RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]");
       Rollout response = saasRolloutsClient.getRollout(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### getRollout(GetRolloutRequest request)
    
    
    public final Rollout getRollout(GetRolloutRequest request)

Retrieve a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       GetRolloutRequest request =
           GetRolloutRequest.newBuilder()
               .setName(RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]").toString())
               .build();
       Rollout response = saasRolloutsClient.getRollout(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### getRollout(String name)
    
    
    public final Rollout getRollout(String name)

Retrieve a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String name = RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]").toString();
       Rollout response = saasRolloutsClient.getRollout(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### getRolloutCallable()
    
    
    public final UnaryCallable<GetRolloutRequest,Rollout> getRolloutCallable()

Retrieve a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       GetRolloutRequest request =
           GetRolloutRequest.newBuilder()
               .setName(RolloutName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_ID]").toString())
               .build();
       ApiFuture<Rollout> future = saasRolloutsClient.getRolloutCallable().futureCall(request);
       // Do something.
       Rollout response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetRolloutRequest),[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)>` |   
  
### getRolloutKind(@Nullable RolloutKindName name)
    
    
    public final RolloutKind getRolloutKind(@Nullable RolloutKindName name)

Retrieve a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       RolloutKindName name = RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]");
       RolloutKind response = saasRolloutsClient.getRolloutKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKindName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### getRolloutKind(GetRolloutKindRequest request)
    
    
    public final RolloutKind getRolloutKind(GetRolloutKindRequest request)

Retrieve a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       GetRolloutKindRequest request =
           GetRolloutKindRequest.newBuilder()
               .setName(
                   RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]").toString())
               .build();
       RolloutKind response = saasRolloutsClient.getRolloutKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetRolloutKindRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### getRolloutKind(String name)
    
    
    public final RolloutKind getRolloutKind(String name)

Retrieve a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String name = RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]").toString();
       RolloutKind response = saasRolloutsClient.getRolloutKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### getRolloutKindCallable()
    
    
    public final UnaryCallable<GetRolloutKindRequest,RolloutKind> getRolloutKindCallable()

Retrieve a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       GetRolloutKindRequest request =
           GetRolloutKindRequest.newBuilder()
               .setName(
                   RolloutKindName.of("[PROJECT]", "[LOCATION]", "[ROLLOUT_KIND_ID]").toString())
               .build();
       ApiFuture<RolloutKind> future =
           saasRolloutsClient.getRolloutKindCallable().futureCall(request);
       // Do something.
       RolloutKind response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetRolloutKindRequest),[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)>` |   
  
### getSettings()
    
    
    public final @Nullable SaasRolloutsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsSettings` |   
  
### getStub()
    
    
    public SaasRolloutsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasRolloutsStub)` |   
  
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
    
    
    public final SaasRolloutsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : saasRolloutsClient.listLocations(request).iterateAll()) {
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
`[SaasRolloutsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListLocationsPagedResponse)` |   
  
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
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = saasRolloutsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SaasRolloutsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           saasRolloutsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListLocationsPagedResponse)>` |   
  
### listRolloutKinds(@Nullable LocationName parent)
    
    
    public final SaasRolloutsClient.ListRolloutKindsPagedResponse listRolloutKinds(@Nullable LocationName parent)

Retrieve a collection of rollout kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (RolloutKind element : saasRolloutsClient.listRolloutKinds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the rollout kind.  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient.ListRolloutKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutKindsPagedResponse)` |   
  
### listRolloutKinds(ListRolloutKindsRequest request)
    
    
    public final SaasRolloutsClient.ListRolloutKindsPagedResponse listRolloutKinds(ListRolloutKindsRequest request)

Retrieve a collection of rollout kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListRolloutKindsRequest request =
           ListRolloutKindsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (RolloutKind element : saasRolloutsClient.listRolloutKinds(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRolloutKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutKindsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient.ListRolloutKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutKindsPagedResponse)` |   
  
### listRolloutKinds(String parent)
    
    
    public final SaasRolloutsClient.ListRolloutKindsPagedResponse listRolloutKinds(String parent)

Retrieve a collection of rollout kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (RolloutKind element : saasRolloutsClient.listRolloutKinds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the rollout kind.  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient.ListRolloutKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutKindsPagedResponse)` |   
  
### listRolloutKindsCallable()
    
    
    public final UnaryCallable<ListRolloutKindsRequest,ListRolloutKindsResponse> listRolloutKindsCallable()

Retrieve a collection of rollout kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListRolloutKindsRequest request =
           ListRolloutKindsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListRolloutKindsResponse response =
             saasRolloutsClient.listRolloutKindsCallable().call(request);
         for (RolloutKind element : response.getRolloutKindsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutKindsRequest),[ListRolloutKindsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutKindsResponse)>` |   
  
### listRolloutKindsPagedCallable()
    
    
    public final UnaryCallable<ListRolloutKindsRequest,SaasRolloutsClient.ListRolloutKindsPagedResponse> listRolloutKindsPagedCallable()

Retrieve a collection of rollout kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListRolloutKindsRequest request =
           ListRolloutKindsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<RolloutKind> future =
           saasRolloutsClient.listRolloutKindsPagedCallable().futureCall(request);
       // Do something.
       for (RolloutKind element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutKindsRequest),[ListRolloutKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutKindsPagedResponse)>` |   
  
### listRollouts(@Nullable LocationName parent)
    
    
    public final SaasRolloutsClient.ListRolloutsPagedResponse listRollouts(@Nullable LocationName parent)

Retrieve a collection of rollouts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Rollout element : saasRolloutsClient.listRollouts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the rollout.  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient.ListRolloutsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutsPagedResponse)` |   
  
### listRollouts(ListRolloutsRequest request)
    
    
    public final SaasRolloutsClient.ListRolloutsPagedResponse listRollouts(ListRolloutsRequest request)

Retrieve a collection of rollouts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListRolloutsRequest request =
           ListRolloutsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Rollout element : saasRolloutsClient.listRollouts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient.ListRolloutsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutsPagedResponse)` |   
  
### listRollouts(String parent)
    
    
    public final SaasRolloutsClient.ListRolloutsPagedResponse listRollouts(String parent)

Retrieve a collection of rollouts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Rollout element : saasRolloutsClient.listRollouts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the rollout.  
**Returns**  
---  
**Type** | **Description**  
`[SaasRolloutsClient.ListRolloutsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutsPagedResponse)` |   
  
### listRolloutsCallable()
    
    
    public final UnaryCallable<ListRolloutsRequest,ListRolloutsResponse> listRolloutsCallable()

Retrieve a collection of rollouts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListRolloutsRequest request =
           ListRolloutsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListRolloutsResponse response = saasRolloutsClient.listRolloutsCallable().call(request);
         for (Rollout element : response.getRolloutsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutsRequest),[ListRolloutsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutsResponse)>` |   
  
### listRolloutsPagedCallable()
    
    
    public final UnaryCallable<ListRolloutsRequest,SaasRolloutsClient.ListRolloutsPagedResponse> listRolloutsPagedCallable()

Retrieve a collection of rollouts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       ListRolloutsRequest request =
           ListRolloutsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Rollout> future =
           saasRolloutsClient.listRolloutsPagedCallable().futureCall(request);
       // Do something.
       for (Rollout element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutsRequest),[ListRolloutsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRolloutsClient.ListRolloutsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateRollout(Rollout rollout, FieldMask updateMask)
    
    
    public final Rollout updateRollout(Rollout rollout, FieldMask updateMask)

Update a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       Rollout rollout = Rollout.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Rollout response = saasRolloutsClient.updateRollout(rollout, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`rollout` | `[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)`  
Required. The desired state for the rollout.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Rollout resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Rollout will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### updateRollout(UpdateRolloutRequest request)
    
    
    public final Rollout updateRollout(UpdateRolloutRequest request)

Update a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       UpdateRolloutRequest request =
           UpdateRolloutRequest.newBuilder()
               .setRollout(Rollout.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Rollout response = saasRolloutsClient.updateRollout(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)` |   
  
### updateRolloutCallable()
    
    
    public final UnaryCallable<UpdateRolloutRequest,Rollout> updateRolloutCallable()

Update a single rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       UpdateRolloutRequest request =
           UpdateRolloutRequest.newBuilder()
               .setRollout(Rollout.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Rollout> future = saasRolloutsClient.updateRolloutCallable().futureCall(request);
       // Do something.
       Rollout response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateRolloutRequest),[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout)>` |   
  
### updateRolloutKind(RolloutKind rolloutKind, FieldMask updateMask)
    
    
    public final RolloutKind updateRolloutKind(RolloutKind rolloutKind, FieldMask updateMask)

Update a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       RolloutKind rolloutKind = RolloutKind.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       RolloutKind response = saasRolloutsClient.updateRolloutKind(rolloutKind, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`rolloutKind` | `[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)`  
Required. The desired state for the rollout kind.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the RolloutKind resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the RolloutKind will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### updateRolloutKind(UpdateRolloutKindRequest request)
    
    
    public final RolloutKind updateRolloutKind(UpdateRolloutKindRequest request)

Update a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       UpdateRolloutKindRequest request =
           UpdateRolloutKindRequest.newBuilder()
               .setRolloutKind(RolloutKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       RolloutKind response = saasRolloutsClient.updateRolloutKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateRolloutKindRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)` |   
  
### updateRolloutKindCallable()
    
    
    public final UnaryCallable<UpdateRolloutKindRequest,RolloutKind> updateRolloutKindCallable()

Update a single rollout kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasRolloutsClient saasRolloutsClient = SaasRolloutsClient.create()) {
       UpdateRolloutKindRequest request =
           UpdateRolloutKindRequest.newBuilder()
               .setRolloutKind(RolloutKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<RolloutKind> future =
           saasRolloutsClient.updateRolloutKindCallable().futureCall(request);
       // Do something.
       RolloutKind response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRolloutKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateRolloutKindRequest),[RolloutKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
