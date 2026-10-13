---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient
title: Class InternalRangeServiceClient (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:05.056445+00:00
---

# Class InternalRangeServiceClient (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InternalRangeServiceClient (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkconnectivity/google-cloud-networkconnectivity/src/main/java/com/google/cloud/networkconnectivity/v1/InternalRangeServiceClient.java)| [Product Reference](https://cloud.google.com/network-connectivity/docs)  
---|---  
  
Service Description: The CLH-based service for internal range resources used to perform IPAM operations within a VPC network.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       InternalRangeName name = InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]");
       InternalRange response = internalRangeServiceClient.getInternalRange(name);
     }
     

Note: close() needs to be called on the InternalRangeServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListInternalRanges |  Lists internal ranges in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInternalRanges(ListInternalRangesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInternalRanges(LocationName parent) 
  * listInternalRanges(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInternalRangesPagedCallable() 
  * listInternalRangesCallable() 

  
GetInternalRange |  Gets details of a single internal range. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInternalRange(GetInternalRangeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInternalRange(InternalRangeName name) 
  * getInternalRange(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInternalRangeCallable() 

  
CreateInternalRange |  Creates a new internal range in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInternalRangeAsync(CreateInternalRangeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInternalRangeAsync(LocationName parent, InternalRange internalRange, String internalRangeId) 
  * createInternalRangeAsync(String parent, InternalRange internalRange, String internalRangeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInternalRangeOperationCallable() 
  * createInternalRangeCallable() 

  
UpdateInternalRange |  Updates the parameters of a single internal range. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateInternalRangeAsync(UpdateInternalRangeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateInternalRangeAsync(InternalRange internalRange, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateInternalRangeOperationCallable() 
  * updateInternalRangeCallable() 

  
DeleteInternalRange |  Deletes a single internal range. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInternalRangeAsync(DeleteInternalRangeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInternalRangeAsync(InternalRangeName name) 
  * deleteInternalRangeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInternalRangeOperationCallable() 
  * deleteInternalRangeCallable() 

  
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

This class can be customized by passing in a custom instance of InternalRangeServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InternalRangeServiceSettings internalRangeServiceSettings =
         InternalRangeServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create(internalRangeServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InternalRangeServiceSettings internalRangeServiceSettings =
         InternalRangeServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create(internalRangeServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InternalRangeServiceClient

## Static Methods 

### create()
    
    
    public static final InternalRangeServiceClient create()

Constructs an instance of InternalRangeServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InternalRangeServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InternalRangeServiceSettings settings)
    
    
    public static final InternalRangeServiceClient create(InternalRangeServiceSettings settings)

Constructs an instance of InternalRangeServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InternalRangeServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InternalRangeServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InternalRangeServiceStub stub)
    
    
    public static final InternalRangeServiceClient create(InternalRangeServiceStub stub)

Constructs an instance of InternalRangeServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(InternalRangeServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InternalRangeServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.InternalRangeServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InternalRangeServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient)` |   
  
## Constructors 

### InternalRangeServiceClient(InternalRangeServiceSettings settings)
    
    
    protected InternalRangeServiceClient(InternalRangeServiceSettings settings)

Constructs an instance of InternalRangeServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InternalRangeServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceSettings)`  
  
  
### InternalRangeServiceClient(InternalRangeServiceStub stub)
    
    
    protected InternalRangeServiceClient(InternalRangeServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InternalRangeServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.InternalRangeServiceStub)`  
  
  
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

### createInternalRangeAsync(@Nullable LocationName parent, InternalRange internalRange, String internalRangeId)
    
    
    public final OperationFuture<InternalRange,OperationMetadata> createInternalRangeAsync(@Nullable LocationName parent, InternalRange internalRange, String internalRangeId)

Creates a new internal range in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       InternalRange internalRange = InternalRange.newBuilder().build();
       String internalRangeId = "internalRangeId-392750661";
       InternalRange response =
           internalRangeServiceClient
               .createInternalRangeAsync(parent, internalRange, internalRangeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name of the internal range.  
`internalRange` | `[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange)`  
Required. Initial values for a new internal range  
`internalRangeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/internalRanges/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createInternalRangeAsync(CreateInternalRangeRequest request)
    
    
    public final OperationFuture<InternalRange,OperationMetadata> createInternalRangeAsync(CreateInternalRangeRequest request)

Creates a new internal range in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       CreateInternalRangeRequest request =
           CreateInternalRangeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInternalRangeId("internalRangeId-392750661")
               .setInternalRange(InternalRange.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       InternalRange response = internalRangeServiceClient.createInternalRangeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateInternalRangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createInternalRangeAsync(String parent, InternalRange internalRange, String internalRangeId)
    
    
    public final OperationFuture<InternalRange,OperationMetadata> createInternalRangeAsync(String parent, InternalRange internalRange, String internalRangeId)

Creates a new internal range in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       InternalRange internalRange = InternalRange.newBuilder().build();
       String internalRangeId = "internalRangeId-392750661";
       InternalRange response =
           internalRangeServiceClient
               .createInternalRangeAsync(parent, internalRange, internalRangeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name of the internal range.  
`internalRange` | `[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange)`  
Required. Initial values for a new internal range  
`internalRangeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/internalRanges/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createInternalRangeCallable()
    
    
    public final UnaryCallable<CreateInternalRangeRequest,Operation> createInternalRangeCallable()

Creates a new internal range in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       CreateInternalRangeRequest request =
           CreateInternalRangeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInternalRangeId("internalRangeId-392750661")
               .setInternalRange(InternalRange.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           internalRangeServiceClient.createInternalRangeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateInternalRangeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInternalRangeOperationCallable()
    
    
    public final OperationCallable<CreateInternalRangeRequest,InternalRange,OperationMetadata> createInternalRangeOperationCallable()

Creates a new internal range in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       CreateInternalRangeRequest request =
           CreateInternalRangeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInternalRangeId("internalRangeId-392750661")
               .setInternalRange(InternalRange.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<InternalRange, OperationMetadata> future =
           internalRangeServiceClient.createInternalRangeOperationCallable().futureCall(request);
       // Do something.
       InternalRange response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateInternalRangeRequest),[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteInternalRangeAsync(@Nullable InternalRangeName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInternalRangeAsync(@Nullable InternalRangeName name)

Deletes a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       InternalRangeName name = InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]");
       internalRangeServiceClient.deleteInternalRangeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.InternalRangeName`  
Required. The name of the internal range to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteInternalRangeAsync(DeleteInternalRangeRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInternalRangeAsync(DeleteInternalRangeRequest request)

Deletes a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       DeleteInternalRangeRequest request =
           DeleteInternalRangeRequest.newBuilder()
               .setName(
                   InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]").toString())
               .setRequestId("requestId693933066")
               .build();
       internalRangeServiceClient.deleteInternalRangeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteInternalRangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteInternalRangeAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInternalRangeAsync(String name)

Deletes a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       String name = InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]").toString();
       internalRangeServiceClient.deleteInternalRangeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the internal range to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteInternalRangeCallable()
    
    
    public final UnaryCallable<DeleteInternalRangeRequest,Operation> deleteInternalRangeCallable()

Deletes a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       DeleteInternalRangeRequest request =
           DeleteInternalRangeRequest.newBuilder()
               .setName(
                   InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           internalRangeServiceClient.deleteInternalRangeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteInternalRangeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInternalRangeOperationCallable()
    
    
    public final OperationCallable<DeleteInternalRangeRequest,Empty,OperationMetadata> deleteInternalRangeOperationCallable()

Deletes a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       DeleteInternalRangeRequest request =
           DeleteInternalRangeRequest.newBuilder()
               .setName(
                   InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           internalRangeServiceClient.deleteInternalRangeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteInternalRangeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = internalRangeServiceClient.getIamPolicy(request);
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
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           internalRangeServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getInternalRange(@Nullable InternalRangeName name)
    
    
    public final InternalRange getInternalRange(@Nullable InternalRangeName name)

Gets details of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       InternalRangeName name = InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]");
       InternalRange response = internalRangeServiceClient.getInternalRange(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.InternalRangeName`  
Required. Name of the InternalRange to get.  
**Returns**  
---  
**Type** | **Description**  
`[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange)` |   
  
### getInternalRange(GetInternalRangeRequest request)
    
    
    public final InternalRange getInternalRange(GetInternalRangeRequest request)

Gets details of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       GetInternalRangeRequest request =
           GetInternalRangeRequest.newBuilder()
               .setName(
                   InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]").toString())
               .build();
       InternalRange response = internalRangeServiceClient.getInternalRange(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetInternalRangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange)` |   
  
### getInternalRange(String name)
    
    
    public final InternalRange getInternalRange(String name)

Gets details of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       String name = InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]").toString();
       InternalRange response = internalRangeServiceClient.getInternalRange(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the InternalRange to get.  
**Returns**  
---  
**Type** | **Description**  
`[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange)` |   
  
### getInternalRangeCallable()
    
    
    public final UnaryCallable<GetInternalRangeRequest,InternalRange> getInternalRangeCallable()

Gets details of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       GetInternalRangeRequest request =
           GetInternalRangeRequest.newBuilder()
               .setName(
                   InternalRangeName.of("[PROJECT]", "[LOCATION]", "[INTERNAL_RANGE]").toString())
               .build();
       ApiFuture<InternalRange> future =
           internalRangeServiceClient.getInternalRangeCallable().futureCall(request);
       // Do something.
       InternalRange response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetInternalRangeRequest),[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = internalRangeServiceClient.getLocation(request);
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
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           internalRangeServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable InternalRangeServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.InternalRangeServiceSettings` |   
  
### getStub()
    
    
    public InternalRangeServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InternalRangeServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.InternalRangeServiceStub)` |   
  
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
  
### listInternalRanges(@Nullable LocationName parent)
    
    
    public final InternalRangeServiceClient.ListInternalRangesPagedResponse listInternalRanges(@Nullable LocationName parent)

Lists internal ranges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (InternalRange element :
           internalRangeServiceClient.listInternalRanges(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[InternalRangeServiceClient.ListInternalRangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient.ListInternalRangesPagedResponse)` |   
  
### listInternalRanges(ListInternalRangesRequest request)
    
    
    public final InternalRangeServiceClient.ListInternalRangesPagedResponse listInternalRanges(ListInternalRangesRequest request)

Lists internal ranges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       ListInternalRangesRequest request =
           ListInternalRangesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (InternalRange element :
           internalRangeServiceClient.listInternalRanges(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInternalRangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListInternalRangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InternalRangeServiceClient.ListInternalRangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient.ListInternalRangesPagedResponse)` |   
  
### listInternalRanges(String parent)
    
    
    public final InternalRangeServiceClient.ListInternalRangesPagedResponse listInternalRanges(String parent)

Lists internal ranges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (InternalRange element :
           internalRangeServiceClient.listInternalRanges(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[InternalRangeServiceClient.ListInternalRangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient.ListInternalRangesPagedResponse)` |   
  
### listInternalRangesCallable()
    
    
    public final UnaryCallable<ListInternalRangesRequest,ListInternalRangesResponse> listInternalRangesCallable()

Lists internal ranges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       ListInternalRangesRequest request =
           ListInternalRangesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListInternalRangesResponse response =
             internalRangeServiceClient.listInternalRangesCallable().call(request);
         for (InternalRange element : response.getInternalRangesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInternalRangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListInternalRangesRequest),[ListInternalRangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListInternalRangesResponse)>` |   
  
### listInternalRangesPagedCallable()
    
    
    public final UnaryCallable<ListInternalRangesRequest,InternalRangeServiceClient.ListInternalRangesPagedResponse> listInternalRangesPagedCallable()

Lists internal ranges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       ListInternalRangesRequest request =
           ListInternalRangesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<InternalRange> future =
           internalRangeServiceClient.listInternalRangesPagedCallable().futureCall(request);
       // Do something.
       for (InternalRange element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInternalRangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListInternalRangesRequest),[ListInternalRangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient.ListInternalRangesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final InternalRangeServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : internalRangeServiceClient.listLocations(request).iterateAll()) {
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
`[InternalRangeServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             internalRangeServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,InternalRangeServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           internalRangeServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRangeServiceClient.ListLocationsPagedResponse)>` |   
  
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
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = internalRangeServiceClient.setIamPolicy(request);
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
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           internalRangeServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = internalRangeServiceClient.testIamPermissions(request);
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
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           internalRangeServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateInternalRangeAsync(InternalRange internalRange, FieldMask updateMask)
    
    
    public final OperationFuture<InternalRange,OperationMetadata> updateInternalRangeAsync(InternalRange internalRange, FieldMask updateMask)

Updates the parameters of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       InternalRange internalRange = InternalRange.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       InternalRange response =
           internalRangeServiceClient.updateInternalRangeAsync(internalRange, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`internalRange` | `[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange)`  
Required. New values to be patched into the resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the InternalRange resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateInternalRangeAsync(UpdateInternalRangeRequest request)
    
    
    public final OperationFuture<InternalRange,OperationMetadata> updateInternalRangeAsync(UpdateInternalRangeRequest request)

Updates the parameters of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       UpdateInternalRangeRequest request =
           UpdateInternalRangeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInternalRange(InternalRange.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       InternalRange response = internalRangeServiceClient.updateInternalRangeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateInternalRangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateInternalRangeCallable()
    
    
    public final UnaryCallable<UpdateInternalRangeRequest,Operation> updateInternalRangeCallable()

Updates the parameters of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       UpdateInternalRangeRequest request =
           UpdateInternalRangeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInternalRange(InternalRange.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           internalRangeServiceClient.updateInternalRangeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateInternalRangeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInternalRangeOperationCallable()
    
    
    public final OperationCallable<UpdateInternalRangeRequest,InternalRange,OperationMetadata> updateInternalRangeOperationCallable()

Updates the parameters of a single internal range.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InternalRangeServiceClient internalRangeServiceClient =
         InternalRangeServiceClient.create()) {
       UpdateInternalRangeRequest request =
           UpdateInternalRangeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInternalRange(InternalRange.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<InternalRange, OperationMetadata> future =
           internalRangeServiceClient.updateInternalRangeOperationCallable().futureCall(request);
       // Do something.
       InternalRange response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInternalRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateInternalRangeRequest),[InternalRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
