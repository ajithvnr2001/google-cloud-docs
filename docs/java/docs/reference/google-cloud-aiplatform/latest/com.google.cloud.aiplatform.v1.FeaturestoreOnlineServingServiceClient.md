---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient
title: Class FeaturestoreOnlineServingServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:56.580445+00:00
---

# Class FeaturestoreOnlineServingServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FeaturestoreOnlineServingServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/FeaturestoreOnlineServingServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for serving online feature values.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       EntityTypeName entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       ReadFeatureValuesResponse response =
           featurestoreOnlineServingServiceClient.readFeatureValues(entityType);
     }
     

Note: close() needs to be called on the FeaturestoreOnlineServingServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ReadFeatureValues |  Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * readFeatureValues(ReadFeatureValuesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * readFeatureValues(EntityTypeName entityType) 
  * readFeatureValues(String entityType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readFeatureValuesCallable() 

  
StreamingReadFeatureValues |  Reads Feature values for multiple entities. Depending on their size, data for different entities may be broken up across multiple responses. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamingReadFeatureValuesCallable() 

  
WriteFeatureValues |  Writes Feature values of one or more entities of an EntityType.  The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * writeFeatureValues(WriteFeatureValuesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * writeFeatureValues(EntityTypeName entityType, List<WriteFeatureValuesPayload> payloads) 
  * writeFeatureValues(String entityType, List<WriteFeatureValuesPayload> payloads) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * writeFeatureValuesCallable() 

  
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

This class can be customized by passing in a custom instance of FeaturestoreOnlineServingServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeaturestoreOnlineServingServiceSettings featurestoreOnlineServingServiceSettings =
         FeaturestoreOnlineServingServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create(featurestoreOnlineServingServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FeaturestoreOnlineServingServiceSettings featurestoreOnlineServingServiceSettings =
         FeaturestoreOnlineServingServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create(featurestoreOnlineServingServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FeaturestoreOnlineServingServiceClient

## Static Methods 

### create()
    
    
    public static final FeaturestoreOnlineServingServiceClient create()

Constructs an instance of FeaturestoreOnlineServingServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeaturestoreOnlineServingServiceSettings settings)
    
    
    public static final FeaturestoreOnlineServingServiceClient create(FeaturestoreOnlineServingServiceSettings settings)

Constructs an instance of FeaturestoreOnlineServingServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeaturestoreOnlineServingServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FeaturestoreOnlineServingServiceStub stub)
    
    
    public static final FeaturestoreOnlineServingServiceClient create(FeaturestoreOnlineServingServiceStub stub)

Constructs an instance of FeaturestoreOnlineServingServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(FeaturestoreOnlineServingServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeaturestoreOnlineServingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeaturestoreOnlineServingServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient)` |   
  
## Constructors 

### FeaturestoreOnlineServingServiceClient(FeaturestoreOnlineServingServiceSettings settings)
    
    
    protected FeaturestoreOnlineServingServiceClient(FeaturestoreOnlineServingServiceSettings settings)

Constructs an instance of FeaturestoreOnlineServingServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FeaturestoreOnlineServingServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceSettings)`  
  
  
### FeaturestoreOnlineServingServiceClient(FeaturestoreOnlineServingServiceStub stub)
    
    
    protected FeaturestoreOnlineServingServiceClient(FeaturestoreOnlineServingServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FeaturestoreOnlineServingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeaturestoreOnlineServingServiceStub)`  
  
  
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

### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = featurestoreOnlineServingServiceClient.getIamPolicy(request);
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
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           featurestoreOnlineServingServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = featurestoreOnlineServingServiceClient.getLocation(request);
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
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           featurestoreOnlineServingServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable FeaturestoreOnlineServingServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceSettings` |   
  
### getStub()
    
    
    public FeaturestoreOnlineServingServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FeaturestoreOnlineServingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.FeaturestoreOnlineServingServiceStub)` |   
  
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
    
    
    public final FeaturestoreOnlineServingServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element :
           featurestoreOnlineServingServiceClient.listLocations(request).iterateAll()) {
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
`[FeaturestoreOnlineServingServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             featurestoreOnlineServingServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,FeaturestoreOnlineServingServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           featurestoreOnlineServingServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient.ListLocationsPagedResponse)>` |   
  
### readFeatureValues(@Nullable EntityTypeName entityType)
    
    
    public final ReadFeatureValuesResponse readFeatureValues(@Nullable EntityTypeName entityType)

Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       EntityTypeName entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       ReadFeatureValuesResponse response =
           featurestoreOnlineServingServiceClient.readFeatureValues(entityType);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType for the entity being read. Value format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be `user`.  
**Returns**  
---  
**Type** | **Description**  
`[ReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesResponse)` |   
  
### readFeatureValues(ReadFeatureValuesRequest request)
    
    
    public final ReadFeatureValuesResponse readFeatureValues(ReadFeatureValuesRequest request)

Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       ReadFeatureValuesRequest request =
           ReadFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setEntityId("entityId-2102099874")
               .setFeatureSelector(FeatureSelector.newBuilder().build())
               .build();
       ReadFeatureValuesResponse response =
           featurestoreOnlineServingServiceClient.readFeatureValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesResponse)` |   
  
### readFeatureValues(String entityType)
    
    
    public final ReadFeatureValuesResponse readFeatureValues(String entityType)

Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       String entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       ReadFeatureValuesResponse response =
           featurestoreOnlineServingServiceClient.readFeatureValues(entityType);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entityType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType for the entity being read. Value format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be `user`.  
**Returns**  
---  
**Type** | **Description**  
`[ReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesResponse)` |   
  
### readFeatureValuesCallable()
    
    
    public final UnaryCallable<ReadFeatureValuesRequest,ReadFeatureValuesResponse> readFeatureValuesCallable()

Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       ReadFeatureValuesRequest request =
           ReadFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .setEntityId("entityId-2102099874")
               .setFeatureSelector(FeatureSelector.newBuilder().build())
               .build();
       ApiFuture<ReadFeatureValuesResponse> future =
           featurestoreOnlineServingServiceClient.readFeatureValuesCallable().futureCall(request);
       // Do something.
       ReadFeatureValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesRequest),[ReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesResponse)>` |   
  
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
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = featurestoreOnlineServingServiceClient.setIamPolicy(request);
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
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           featurestoreOnlineServingServiceClient.setIamPolicyCallable().futureCall(request);
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

### streamingReadFeatureValuesCallable()
    
    
    public final ServerStreamingCallable<StreamingReadFeatureValuesRequest,ReadFeatureValuesResponse> streamingReadFeatureValuesCallable()

Reads Feature values for multiple entities. Depending on their size, data for different entities may be broken up across multiple responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       StreamingReadFeatureValuesRequest request =
           StreamingReadFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllEntityIds(new ArrayList<String>())
               .setFeatureSelector(FeatureSelector.newBuilder().build())
               .build();
       ServerStream<ReadFeatureValuesResponse> stream =
           featurestoreOnlineServingServiceClient.streamingReadFeatureValuesCallable().call(request);
       for (ReadFeatureValuesResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[StreamingReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StreamingReadFeatureValuesRequest),[ReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesResponse)>` |   
  
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
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           featurestoreOnlineServingServiceClient.testIamPermissions(request);
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
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           featurestoreOnlineServingServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### writeFeatureValues(@Nullable EntityTypeName entityType, List<WriteFeatureValuesPayload> payloads)
    
    
    public final WriteFeatureValuesResponse writeFeatureValues(@Nullable EntityTypeName entityType, List<WriteFeatureValuesPayload> payloads)

Writes Feature values of one or more entities of an EntityType.

The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       EntityTypeName entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
       List<WriteFeatureValuesPayload> payloads = new ArrayList<>();
       WriteFeatureValuesResponse response =
           featurestoreOnlineServingServiceClient.writeFeatureValues(entityType, payloads);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entityType` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EntityTypeName`  
Required. The resource name of the EntityType for the entities being written. Value format: `projects/{project}/locations/{location}/featurestores/ {featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be `user`.  
`payloads` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[WriteFeatureValuesPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesPayload)>`  
Required. The entities to be written. Up to 100,000 feature values can be written across all `payloads`.  
**Returns**  
---  
**Type** | **Description**  
`[WriteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesResponse)` |   
  
### writeFeatureValues(WriteFeatureValuesRequest request)
    
    
    public final WriteFeatureValuesResponse writeFeatureValues(WriteFeatureValuesRequest request)

Writes Feature values of one or more entities of an EntityType.

The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       WriteFeatureValuesRequest request =
           WriteFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllPayloads(new ArrayList<WriteFeatureValuesPayload>())
               .build();
       WriteFeatureValuesResponse response =
           featurestoreOnlineServingServiceClient.writeFeatureValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesResponse)` |   
  
### writeFeatureValues(String entityType, List<WriteFeatureValuesPayload> payloads)
    
    
    public final WriteFeatureValuesResponse writeFeatureValues(String entityType, List<WriteFeatureValuesPayload> payloads)

Writes Feature values of one or more entities of an EntityType.

The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       String entityType =
           EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
               .toString();
       List<WriteFeatureValuesPayload> payloads = new ArrayList<>();
       WriteFeatureValuesResponse response =
           featurestoreOnlineServingServiceClient.writeFeatureValues(entityType, payloads);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entityType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntityType for the entities being written. Value format: `projects/{project}/locations/{location}/featurestores/ {featurestore}/entityTypes/{entityType}`. For example, for a machine learning model predicting user clicks on a website, an EntityType ID could be `user`.  
`payloads` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[WriteFeatureValuesPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesPayload)>`  
Required. The entities to be written. Up to 100,000 feature values can be written across all `payloads`.  
**Returns**  
---  
**Type** | **Description**  
`[WriteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesResponse)` |   
  
### writeFeatureValuesCallable()
    
    
    public final UnaryCallable<WriteFeatureValuesRequest,WriteFeatureValuesResponse> writeFeatureValuesCallable()

Writes Feature values of one or more entities of an EntityType.

The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FeaturestoreOnlineServingServiceClient featurestoreOnlineServingServiceClient =
         FeaturestoreOnlineServingServiceClient.create()) {
       WriteFeatureValuesRequest request =
           WriteFeatureValuesRequest.newBuilder()
               .setEntityType(
                   EntityTypeName.of("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]")
                       .toString())
               .addAllPayloads(new ArrayList<WriteFeatureValuesPayload>())
               .build();
       ApiFuture<WriteFeatureValuesResponse> future =
           featurestoreOnlineServingServiceClient.writeFeatureValuesCallable().futureCall(request);
       // Do something.
       WriteFeatureValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WriteFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesRequest),[WriteFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteFeatureValuesResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
