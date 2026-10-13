---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient
title: Class SipTrunksClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:48.522092+00:00
---

# Class SipTrunksClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SipTrunksClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/SipTrunksClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing SipTrunks.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SipTrunk sipTrunk = SipTrunk.newBuilder().build();
       SipTrunk response = sipTrunksClient.createSipTrunk(parent, sipTrunk);
     }
     

Note: close() needs to be called on the SipTrunksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateSipTrunk |  Creates a SipTrunk for a specified location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSipTrunk(CreateSipTrunkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSipTrunk(LocationName parent, SipTrunk sipTrunk) 
  * createSipTrunk(String parent, SipTrunk sipTrunk) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSipTrunkCallable() 

  
DeleteSipTrunk |  Deletes a specified SipTrunk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSipTrunk(DeleteSipTrunkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSipTrunk(SipTrunkName name) 
  * deleteSipTrunk(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSipTrunkCallable() 

  
ListSipTrunks |  Returns a list of SipTrunks in the specified location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSipTrunks(ListSipTrunksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSipTrunks(LocationName parent) 
  * listSipTrunks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSipTrunksPagedCallable() 
  * listSipTrunksCallable() 

  
GetSipTrunk |  Retrieves the specified SipTrunk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSipTrunk(GetSipTrunkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSipTrunk(SipTrunkName name) 
  * getSipTrunk(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSipTrunkCallable() 

  
UpdateSipTrunk |  Updates the specified SipTrunk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSipTrunk(UpdateSipTrunkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSipTrunk(SipTrunk sipTrunk, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSipTrunkCallable() 

  
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

This class can be customized by passing in a custom instance of SipTrunksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SipTrunksSettings sipTrunksSettings =
         SipTrunksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SipTrunksClient sipTrunksClient = SipTrunksClient.create(sipTrunksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SipTrunksSettings sipTrunksSettings =
         SipTrunksSettings.newBuilder().setEndpoint(myEndpoint).build();
     SipTrunksClient sipTrunksClient = SipTrunksClient.create(sipTrunksSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SipTrunksSettings sipTrunksSettings = SipTrunksSettings.newHttpJsonBuilder().build();
     SipTrunksClient sipTrunksClient = SipTrunksClient.create(sipTrunksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SipTrunksClient

## Static Methods 

### create()
    
    
    public static final SipTrunksClient create()

Constructs an instance of SipTrunksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SipTrunksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SipTrunksSettings settings)
    
    
    public static final SipTrunksClient create(SipTrunksSettings settings)

Constructs an instance of SipTrunksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SipTrunksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SipTrunksStub stub)
    
    
    public static final SipTrunksClient create(SipTrunksStub stub)

Constructs an instance of SipTrunksClient, using the given stub for making calls. This is for advanced usage - prefer using create(SipTrunksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SipTrunksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.SipTrunksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient)` |   
  
## Constructors 

### SipTrunksClient(SipTrunksSettings settings)
    
    
    protected SipTrunksClient(SipTrunksSettings settings)

Constructs an instance of SipTrunksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SipTrunksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksSettings)`  
  
  
### SipTrunksClient(SipTrunksStub stub)
    
    
    protected SipTrunksClient(SipTrunksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SipTrunksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.SipTrunksStub)`  
  
  
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

### createSipTrunk(@Nullable LocationName parent, SipTrunk sipTrunk)
    
    
    public final SipTrunk createSipTrunk(@Nullable LocationName parent, SipTrunk sipTrunk)

Creates a SipTrunk for a specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SipTrunk sipTrunk = SipTrunk.newBuilder().build();
       SipTrunk response = sipTrunksClient.createSipTrunk(parent, sipTrunk);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The location to create a SIP trunk for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`sipTrunk` | `[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)`  
Required. The SIP trunk to create.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### createSipTrunk(CreateSipTrunkRequest request)
    
    
    public final SipTrunk createSipTrunk(CreateSipTrunkRequest request)

Creates a SipTrunk for a specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       CreateSipTrunkRequest request =
           CreateSipTrunkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSipTrunk(SipTrunk.newBuilder().build())
               .build();
       SipTrunk response = sipTrunksClient.createSipTrunk(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateSipTrunkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### createSipTrunk(String parent, SipTrunk sipTrunk)
    
    
    public final SipTrunk createSipTrunk(String parent, SipTrunk sipTrunk)

Creates a SipTrunk for a specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       SipTrunk sipTrunk = SipTrunk.newBuilder().build();
       SipTrunk response = sipTrunksClient.createSipTrunk(parent, sipTrunk);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location to create a SIP trunk for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`sipTrunk` | `[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)`  
Required. The SIP trunk to create.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### createSipTrunkCallable()
    
    
    public final UnaryCallable<CreateSipTrunkRequest,SipTrunk> createSipTrunkCallable()

Creates a SipTrunk for a specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       CreateSipTrunkRequest request =
           CreateSipTrunkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSipTrunk(SipTrunk.newBuilder().build())
               .build();
       ApiFuture<SipTrunk> future = sipTrunksClient.createSipTrunkCallable().futureCall(request);
       // Do something.
       SipTrunk response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateSipTrunkRequest),[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)>` |   
  
### deleteSipTrunk(@Nullable SipTrunkName name)
    
    
    public final void deleteSipTrunk(@Nullable SipTrunkName name)

Deletes a specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       SipTrunkName name = SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]");
       sipTrunksClient.deleteSipTrunk(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SipTrunkName`  
Required. The name of the SIP trunk to delete. Format: `projects/<Project ID>/locations/<Location ID>/sipTrunks/<SipTrunk ID>`.  
  
### deleteSipTrunk(DeleteSipTrunkRequest request)
    
    
    public final void deleteSipTrunk(DeleteSipTrunkRequest request)

Deletes a specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       DeleteSipTrunkRequest request =
           DeleteSipTrunkRequest.newBuilder()
               .setName(SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]").toString())
               .build();
       sipTrunksClient.deleteSipTrunk(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteSipTrunkRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSipTrunk(String name)
    
    
    public final void deleteSipTrunk(String name)

Deletes a specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       String name = SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]").toString();
       sipTrunksClient.deleteSipTrunk(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the SIP trunk to delete. Format: `projects/<Project ID>/locations/<Location ID>/sipTrunks/<SipTrunk ID>`.  
  
### deleteSipTrunkCallable()
    
    
    public final UnaryCallable<DeleteSipTrunkRequest,Empty> deleteSipTrunkCallable()

Deletes a specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       DeleteSipTrunkRequest request =
           DeleteSipTrunkRequest.newBuilder()
               .setName(SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]").toString())
               .build();
       ApiFuture<Empty> future = sipTrunksClient.deleteSipTrunkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteSipTrunkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = sipTrunksClient.getLocation(request);
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
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = sipTrunksClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable SipTrunksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SipTrunksSettings` |   
  
### getSipTrunk(@Nullable SipTrunkName name)
    
    
    public final SipTrunk getSipTrunk(@Nullable SipTrunkName name)

Retrieves the specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       SipTrunkName name = SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]");
       SipTrunk response = sipTrunksClient.getSipTrunk(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SipTrunkName`  
Required. The name of the SIP trunk to delete. Format: `projects/<Project ID>/locations/<Location ID>/sipTrunks/<SipTrunk ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### getSipTrunk(GetSipTrunkRequest request)
    
    
    public final SipTrunk getSipTrunk(GetSipTrunkRequest request)

Retrieves the specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       GetSipTrunkRequest request =
           GetSipTrunkRequest.newBuilder()
               .setName(SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]").toString())
               .build();
       SipTrunk response = sipTrunksClient.getSipTrunk(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetSipTrunkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### getSipTrunk(String name)
    
    
    public final SipTrunk getSipTrunk(String name)

Retrieves the specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       String name = SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]").toString();
       SipTrunk response = sipTrunksClient.getSipTrunk(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the SIP trunk to delete. Format: `projects/<Project ID>/locations/<Location ID>/sipTrunks/<SipTrunk ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### getSipTrunkCallable()
    
    
    public final UnaryCallable<GetSipTrunkRequest,SipTrunk> getSipTrunkCallable()

Retrieves the specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       GetSipTrunkRequest request =
           GetSipTrunkRequest.newBuilder()
               .setName(SipTrunkName.of("[PROJECT]", "[LOCATION]", "[SIPTRUNK]").toString())
               .build();
       ApiFuture<SipTrunk> future = sipTrunksClient.getSipTrunkCallable().futureCall(request);
       // Do something.
       SipTrunk response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetSipTrunkRequest),[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)>` |   
  
### getStub()
    
    
    public SipTrunksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SipTrunksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.SipTrunksStub)` |   
  
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
    
    
    public final SipTrunksClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : sipTrunksClient.listLocations(request).iterateAll()) {
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
`[SipTrunksClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient.ListLocationsPagedResponse)` |   
  
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
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = sipTrunksClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SipTrunksClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = sipTrunksClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient.ListLocationsPagedResponse)>` |   
  
### listSipTrunks(@Nullable LocationName parent)
    
    
    public final SipTrunksClient.ListSipTrunksPagedResponse listSipTrunks(@Nullable LocationName parent)

Returns a list of SipTrunks in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SipTrunk element : sipTrunksClient.listSipTrunks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The location to list SIP trunks from. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunksClient.ListSipTrunksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient.ListSipTrunksPagedResponse)` |   
  
### listSipTrunks(ListSipTrunksRequest request)
    
    
    public final SipTrunksClient.ListSipTrunksPagedResponse listSipTrunks(ListSipTrunksRequest request)

Returns a list of SipTrunks in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       ListSipTrunksRequest request =
           ListSipTrunksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SipTrunk element : sipTrunksClient.listSipTrunks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSipTrunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSipTrunksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunksClient.ListSipTrunksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient.ListSipTrunksPagedResponse)` |   
  
### listSipTrunks(String parent)
    
    
    public final SipTrunksClient.ListSipTrunksPagedResponse listSipTrunks(String parent)

Returns a list of SipTrunks in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SipTrunk element : sipTrunksClient.listSipTrunks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location to list SIP trunks from. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunksClient.ListSipTrunksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient.ListSipTrunksPagedResponse)` |   
  
### listSipTrunksCallable()
    
    
    public final UnaryCallable<ListSipTrunksRequest,ListSipTrunksResponse> listSipTrunksCallable()

Returns a list of SipTrunks in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       ListSipTrunksRequest request =
           ListSipTrunksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSipTrunksResponse response = sipTrunksClient.listSipTrunksCallable().call(request);
         for (SipTrunk element : response.getSipTrunksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSipTrunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSipTrunksRequest),[ListSipTrunksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSipTrunksResponse)>` |   
  
### listSipTrunksPagedCallable()
    
    
    public final UnaryCallable<ListSipTrunksRequest,SipTrunksClient.ListSipTrunksPagedResponse> listSipTrunksPagedCallable()

Returns a list of SipTrunks in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       ListSipTrunksRequest request =
           ListSipTrunksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SipTrunk> future = sipTrunksClient.listSipTrunksPagedCallable().futureCall(request);
       // Do something.
       for (SipTrunk element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSipTrunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSipTrunksRequest),[ListSipTrunksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunksClient.ListSipTrunksPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSipTrunk(SipTrunk sipTrunk, FieldMask updateMask)
    
    
    public final SipTrunk updateSipTrunk(SipTrunk sipTrunk, FieldMask updateMask)

Updates the specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       SipTrunk sipTrunk = SipTrunk.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SipTrunk response = sipTrunksClient.updateSipTrunk(sipTrunk, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`sipTrunk` | `[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)`  
Required. The SipTrunk to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### updateSipTrunk(UpdateSipTrunkRequest request)
    
    
    public final SipTrunk updateSipTrunk(UpdateSipTrunkRequest request)

Updates the specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       UpdateSipTrunkRequest request =
           UpdateSipTrunkRequest.newBuilder()
               .setSipTrunk(SipTrunk.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SipTrunk response = sipTrunksClient.updateSipTrunk(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateSipTrunkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)` |   
  
### updateSipTrunkCallable()
    
    
    public final UnaryCallable<UpdateSipTrunkRequest,SipTrunk> updateSipTrunkCallable()

Updates the specified SipTrunk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SipTrunksClient sipTrunksClient = SipTrunksClient.create()) {
       UpdateSipTrunkRequest request =
           UpdateSipTrunkRequest.newBuilder()
               .setSipTrunk(SipTrunk.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SipTrunk> future = sipTrunksClient.updateSipTrunkCallable().futureCall(request);
       // Do something.
       SipTrunk response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSipTrunkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateSipTrunkRequest),[SipTrunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SipTrunk)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
