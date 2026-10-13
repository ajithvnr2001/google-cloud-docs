---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient
title: Class AudienceSegmentServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:27.513858+00:00
---

# Class AudienceSegmentServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AudienceSegmentServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/AudienceSegmentServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `AudienceSegment` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       AudienceSegmentName name = AudienceSegmentName.of("[NETWORK_CODE]", "[AUDIENCE_SEGMENT]");
       AudienceSegment response = audienceSegmentServiceClient.getAudienceSegment(name);
     }
     

Note: close() needs to be called on the AudienceSegmentServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetAudienceSegment |  Retrieves an `AudienceSegment` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAudienceSegment(GetAudienceSegmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAudienceSegment(AudienceSegmentName name) 
  * getAudienceSegment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAudienceSegmentCallable() 

  
ListAudienceSegments |  Lists `AudienceSegment` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAudienceSegments(ListAudienceSegmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAudienceSegments(NetworkName parent) 
  * listAudienceSegments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAudienceSegmentsPagedCallable() 
  * listAudienceSegmentsCallable() 

  
CreateAudienceSegment |  Creates an `AudienceSegment` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAudienceSegment(CreateAudienceSegmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAudienceSegment(NetworkName parent, AudienceSegment audienceSegment) 
  * createAudienceSegment(String parent, AudienceSegment audienceSegment) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAudienceSegmentCallable() 

  
BatchCreateAudienceSegments |  Creates `AudienceSegment` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateAudienceSegments(NetworkName parent, List<CreateAudienceSegmentRequest> requests) 
  * batchCreateAudienceSegments(String parent, List<CreateAudienceSegmentRequest> requests) 
  * batchCreateAudienceSegments(BatchCreateAudienceSegmentsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateAudienceSegmentsCallable() 

  
BatchActivateAudienceSegments |  Activates `AudienceSegment` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateAudienceSegments(BatchActivateAudienceSegmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateAudienceSegments(NetworkName parent, List<String> names) 
  * batchActivateAudienceSegments(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateAudienceSegmentsCallable() 

  
BatchDeactivateAudienceSegments |  Deactivates `AudienceSegment` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateAudienceSegments(BatchDeactivateAudienceSegmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateAudienceSegments(NetworkName parent, List<String> names) 
  * batchDeactivateAudienceSegments(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateAudienceSegmentsCallable() 

  
BatchApproveAudienceSegments |  Approves `AudienceSegment` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchApproveAudienceSegments(BatchApproveAudienceSegmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchApproveAudienceSegments(NetworkName parent, List<String> names) 
  * batchApproveAudienceSegments(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchApproveAudienceSegmentsCallable() 

  
BatchRejectAudienceSegments |  Rejects `AudienceSegment` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRejectAudienceSegments(BatchRejectAudienceSegmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchRejectAudienceSegments(NetworkName parent, List<String> names) 
  * batchRejectAudienceSegments(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRejectAudienceSegmentsCallable() 

  
BatchPopulateAudienceSegments |  Populates `AudienceSegment` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchPopulateAudienceSegments(BatchPopulateAudienceSegmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchPopulateAudienceSegments(NetworkName parent, List<String> names) 
  * batchPopulateAudienceSegments(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchPopulateAudienceSegmentsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AudienceSegmentServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AudienceSegmentServiceSettings audienceSegmentServiceSettings =
         AudienceSegmentServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create(audienceSegmentServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AudienceSegmentServiceSettings audienceSegmentServiceSettings =
         AudienceSegmentServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create(audienceSegmentServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AudienceSegmentServiceClient

## Static Methods 

### create()
    
    
    public static final AudienceSegmentServiceClient create()

Constructs an instance of AudienceSegmentServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AudienceSegmentServiceSettings settings)
    
    
    public static final AudienceSegmentServiceClient create(AudienceSegmentServiceSettings settings)

Constructs an instance of AudienceSegmentServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AudienceSegmentServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AudienceSegmentServiceStub stub)
    
    
    public static final AudienceSegmentServiceClient create(AudienceSegmentServiceStub stub)

Constructs an instance of AudienceSegmentServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AudienceSegmentServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AudienceSegmentServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AudienceSegmentServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient)` |   
  
## Constructors 

### AudienceSegmentServiceClient(AudienceSegmentServiceSettings settings)
    
    
    protected AudienceSegmentServiceClient(AudienceSegmentServiceSettings settings)

Constructs an instance of AudienceSegmentServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AudienceSegmentServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceSettings)`  
  
  
### AudienceSegmentServiceClient(AudienceSegmentServiceStub stub)
    
    
    protected AudienceSegmentServiceClient(AudienceSegmentServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AudienceSegmentServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AudienceSegmentServiceStub)`  
  
  
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
  
### batchActivateAudienceSegments(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateAudienceSegmentsResponse batchActivateAudienceSegments(@Nullable NetworkName parent, List<String> names)

Activates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchActivateAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAudienceSegmentsResponse)` |   
  
### batchActivateAudienceSegments(BatchActivateAudienceSegmentsRequest request)
    
    
    public final BatchActivateAudienceSegmentsResponse batchActivateAudienceSegments(BatchActivateAudienceSegmentsRequest request)

Activates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchActivateAudienceSegmentsRequest request =
           BatchActivateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchActivateAudienceSegments(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAudienceSegmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAudienceSegmentsResponse)` |   
  
### batchActivateAudienceSegments(String parent, List<String> names)
    
    
    public final BatchActivateAudienceSegmentsResponse batchActivateAudienceSegments(String parent, List<String> names)

Activates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchActivateAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAudienceSegmentsResponse)` |   
  
### batchActivateAudienceSegmentsCallable()
    
    
    public final UnaryCallable<BatchActivateAudienceSegmentsRequest,BatchActivateAudienceSegmentsResponse> batchActivateAudienceSegmentsCallable()

Activates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchActivateAudienceSegmentsRequest request =
           BatchActivateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateAudienceSegmentsResponse> future =
           audienceSegmentServiceClient.batchActivateAudienceSegmentsCallable().futureCall(request);
       // Do something.
       BatchActivateAudienceSegmentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAudienceSegmentsRequest),[BatchActivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAudienceSegmentsResponse)>` |   
  
### batchApproveAudienceSegments(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchApproveAudienceSegmentsResponse batchApproveAudienceSegments(@Nullable NetworkName parent, List<String> names)

Approves `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchApproveAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchApproveAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAudienceSegmentsResponse)` |   
  
### batchApproveAudienceSegments(BatchApproveAudienceSegmentsRequest request)
    
    
    public final BatchApproveAudienceSegmentsResponse batchApproveAudienceSegments(BatchApproveAudienceSegmentsRequest request)

Approves `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchApproveAudienceSegmentsRequest request =
           BatchApproveAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchApproveAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchApproveAudienceSegments(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchApproveAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAudienceSegmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAudienceSegmentsResponse)` |   
  
### batchApproveAudienceSegments(String parent, List<String> names)
    
    
    public final BatchApproveAudienceSegmentsResponse batchApproveAudienceSegments(String parent, List<String> names)

Approves `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchApproveAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchApproveAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchApproveAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAudienceSegmentsResponse)` |   
  
### batchApproveAudienceSegmentsCallable()
    
    
    public final UnaryCallable<BatchApproveAudienceSegmentsRequest,BatchApproveAudienceSegmentsResponse> batchApproveAudienceSegmentsCallable()

Approves `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchApproveAudienceSegmentsRequest request =
           BatchApproveAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchApproveAudienceSegmentsResponse> future =
           audienceSegmentServiceClient.batchApproveAudienceSegmentsCallable().futureCall(request);
       // Do something.
       BatchApproveAudienceSegmentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchApproveAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAudienceSegmentsRequest),[BatchApproveAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAudienceSegmentsResponse)>` |   
  
### batchCreateAudienceSegments(@Nullable NetworkName parent, List<CreateAudienceSegmentRequest> requests)
    
    
    public final BatchCreateAudienceSegmentsResponse batchCreateAudienceSegments(@Nullable NetworkName parent, List<CreateAudienceSegmentRequest> requests)

Creates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateAudienceSegmentRequest> requests = new ArrayList<>();
       BatchCreateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchCreateAudienceSegments(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `AudienceSegments` will be created. Format: `networks/{network_code}` The parent field in the CreateAudienceSegmentRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAudienceSegmentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAudienceSegmentRequest)>`  
Required. The `AudienceSegment` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAudienceSegmentsResponse)` |   
  
### batchCreateAudienceSegments(BatchCreateAudienceSegmentsRequest request)
    
    
    public final BatchCreateAudienceSegmentsResponse batchCreateAudienceSegments(BatchCreateAudienceSegmentsRequest request)

Creates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchCreateAudienceSegmentsRequest request =
           BatchCreateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAudienceSegmentRequest>())
               .build();
       BatchCreateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchCreateAudienceSegments(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAudienceSegmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAudienceSegmentsResponse)` |   
  
### batchCreateAudienceSegments(String parent, List<CreateAudienceSegmentRequest> requests)
    
    
    public final BatchCreateAudienceSegmentsResponse batchCreateAudienceSegments(String parent, List<CreateAudienceSegmentRequest> requests)

Creates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateAudienceSegmentRequest> requests = new ArrayList<>();
       BatchCreateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchCreateAudienceSegments(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `AudienceSegments` will be created. Format: `networks/{network_code}` The parent field in the CreateAudienceSegmentRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAudienceSegmentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAudienceSegmentRequest)>`  
Required. The `AudienceSegment` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAudienceSegmentsResponse)` |   
  
### batchCreateAudienceSegmentsCallable()
    
    
    public final UnaryCallable<BatchCreateAudienceSegmentsRequest,BatchCreateAudienceSegmentsResponse> batchCreateAudienceSegmentsCallable()

Creates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchCreateAudienceSegmentsRequest request =
           BatchCreateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAudienceSegmentRequest>())
               .build();
       ApiFuture<BatchCreateAudienceSegmentsResponse> future =
           audienceSegmentServiceClient.batchCreateAudienceSegmentsCallable().futureCall(request);
       // Do something.
       BatchCreateAudienceSegmentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAudienceSegmentsRequest),[BatchCreateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAudienceSegmentsResponse)>` |   
  
### batchDeactivateAudienceSegments(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateAudienceSegmentsResponse batchDeactivateAudienceSegments(@Nullable NetworkName parent, List<String> names)

Deactivates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchDeactivateAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAudienceSegmentsResponse)` |   
  
### batchDeactivateAudienceSegments(BatchDeactivateAudienceSegmentsRequest request)
    
    
    public final BatchDeactivateAudienceSegmentsResponse batchDeactivateAudienceSegments(BatchDeactivateAudienceSegmentsRequest request)

Deactivates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchDeactivateAudienceSegmentsRequest request =
           BatchDeactivateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchDeactivateAudienceSegments(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAudienceSegmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAudienceSegmentsResponse)` |   
  
### batchDeactivateAudienceSegments(String parent, List<String> names)
    
    
    public final BatchDeactivateAudienceSegmentsResponse batchDeactivateAudienceSegments(String parent, List<String> names)

Deactivates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchDeactivateAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAudienceSegmentsResponse)` |   
  
### batchDeactivateAudienceSegmentsCallable()
    
    
    public final UnaryCallable<BatchDeactivateAudienceSegmentsRequest,BatchDeactivateAudienceSegmentsResponse> batchDeactivateAudienceSegmentsCallable()

Deactivates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchDeactivateAudienceSegmentsRequest request =
           BatchDeactivateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateAudienceSegmentsResponse> future =
           audienceSegmentServiceClient
               .batchDeactivateAudienceSegmentsCallable()
               .futureCall(request);
       // Do something.
       BatchDeactivateAudienceSegmentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAudienceSegmentsRequest),[BatchDeactivateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAudienceSegmentsResponse)>` |   
  
### batchPopulateAudienceSegments(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchPopulateAudienceSegmentsResponse batchPopulateAudienceSegments(@Nullable NetworkName parent, List<String> names)

Populates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchPopulateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchPopulateAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPopulateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPopulateAudienceSegmentsResponse)` |   
  
### batchPopulateAudienceSegments(BatchPopulateAudienceSegmentsRequest request)
    
    
    public final BatchPopulateAudienceSegmentsResponse batchPopulateAudienceSegments(BatchPopulateAudienceSegmentsRequest request)

Populates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchPopulateAudienceSegmentsRequest request =
           BatchPopulateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchPopulateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchPopulateAudienceSegments(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchPopulateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPopulateAudienceSegmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPopulateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPopulateAudienceSegmentsResponse)` |   
  
### batchPopulateAudienceSegments(String parent, List<String> names)
    
    
    public final BatchPopulateAudienceSegmentsResponse batchPopulateAudienceSegments(String parent, List<String> names)

Populates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchPopulateAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchPopulateAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPopulateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPopulateAudienceSegmentsResponse)` |   
  
### batchPopulateAudienceSegmentsCallable()
    
    
    public final UnaryCallable<BatchPopulateAudienceSegmentsRequest,BatchPopulateAudienceSegmentsResponse> batchPopulateAudienceSegmentsCallable()

Populates `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchPopulateAudienceSegmentsRequest request =
           BatchPopulateAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchPopulateAudienceSegmentsResponse> future =
           audienceSegmentServiceClient.batchPopulateAudienceSegmentsCallable().futureCall(request);
       // Do something.
       BatchPopulateAudienceSegmentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchPopulateAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPopulateAudienceSegmentsRequest),[BatchPopulateAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPopulateAudienceSegmentsResponse)>` |   
  
### batchRejectAudienceSegments(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchRejectAudienceSegmentsResponse batchRejectAudienceSegments(@Nullable NetworkName parent, List<String> names)

Rejects `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchRejectAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchRejectAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRejectAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectAudienceSegmentsResponse)` |   
  
### batchRejectAudienceSegments(BatchRejectAudienceSegmentsRequest request)
    
    
    public final BatchRejectAudienceSegmentsResponse batchRejectAudienceSegments(BatchRejectAudienceSegmentsRequest request)

Rejects `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchRejectAudienceSegmentsRequest request =
           BatchRejectAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchRejectAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchRejectAudienceSegments(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRejectAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectAudienceSegmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRejectAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectAudienceSegmentsResponse)` |   
  
### batchRejectAudienceSegments(String parent, List<String> names)
    
    
    public final BatchRejectAudienceSegmentsResponse batchRejectAudienceSegments(String parent, List<String> names)

Rejects `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchRejectAudienceSegmentsResponse response =
           audienceSegmentServiceClient.batchRejectAudienceSegments(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AudienceSegments. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRejectAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectAudienceSegmentsResponse)` |   
  
### batchRejectAudienceSegmentsCallable()
    
    
    public final UnaryCallable<BatchRejectAudienceSegmentsRequest,BatchRejectAudienceSegmentsResponse> batchRejectAudienceSegmentsCallable()

Rejects `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       BatchRejectAudienceSegmentsRequest request =
           BatchRejectAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchRejectAudienceSegmentsResponse> future =
           audienceSegmentServiceClient.batchRejectAudienceSegmentsCallable().futureCall(request);
       // Do something.
       BatchRejectAudienceSegmentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRejectAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectAudienceSegmentsRequest),[BatchRejectAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectAudienceSegmentsResponse)>` |   
  
### close()
    
    
    public final void close()

### createAudienceSegment(@Nullable NetworkName parent, AudienceSegment audienceSegment)
    
    
    public final AudienceSegment createAudienceSegment(@Nullable NetworkName parent, AudienceSegment audienceSegment)

Creates an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       AudienceSegment audienceSegment = AudienceSegment.newBuilder().build();
       AudienceSegment response =
           audienceSegmentServiceClient.createAudienceSegment(parent, audienceSegment);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `AudienceSegment` will be created. Format: `networks/{network_code}`  
`audienceSegment` | `[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)`  
Required. The `AudienceSegment` to create. Only first-party segments can be created.  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)` |   
  
### createAudienceSegment(CreateAudienceSegmentRequest request)
    
    
    public final AudienceSegment createAudienceSegment(CreateAudienceSegmentRequest request)

Creates an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       CreateAudienceSegmentRequest request =
           CreateAudienceSegmentRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAudienceSegment(AudienceSegment.newBuilder().build())
               .build();
       AudienceSegment response = audienceSegmentServiceClient.createAudienceSegment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAudienceSegmentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAudienceSegmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)` |   
  
### createAudienceSegment(String parent, AudienceSegment audienceSegment)
    
    
    public final AudienceSegment createAudienceSegment(String parent, AudienceSegment audienceSegment)

Creates an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       AudienceSegment audienceSegment = AudienceSegment.newBuilder().build();
       AudienceSegment response =
           audienceSegmentServiceClient.createAudienceSegment(parent, audienceSegment);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `AudienceSegment` will be created. Format: `networks/{network_code}`  
`audienceSegment` | `[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)`  
Required. The `AudienceSegment` to create. Only first-party segments can be created.  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)` |   
  
### createAudienceSegmentCallable()
    
    
    public final UnaryCallable<CreateAudienceSegmentRequest,AudienceSegment> createAudienceSegmentCallable()

Creates an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       CreateAudienceSegmentRequest request =
           CreateAudienceSegmentRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAudienceSegment(AudienceSegment.newBuilder().build())
               .build();
       ApiFuture<AudienceSegment> future =
           audienceSegmentServiceClient.createAudienceSegmentCallable().futureCall(request);
       // Do something.
       AudienceSegment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAudienceSegmentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAudienceSegmentRequest),[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)>` |   
  
### getAudienceSegment(@Nullable AudienceSegmentName name)
    
    
    public final AudienceSegment getAudienceSegment(@Nullable AudienceSegmentName name)

Retrieves an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       AudienceSegmentName name = AudienceSegmentName.of("[NETWORK_CODE]", "[AUDIENCE_SEGMENT]");
       AudienceSegment response = audienceSegmentServiceClient.getAudienceSegment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AudienceSegmentName`  
Required. The resource name of the AudienceSegment. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)` |   
  
### getAudienceSegment(GetAudienceSegmentRequest request)
    
    
    public final AudienceSegment getAudienceSegment(GetAudienceSegmentRequest request)

Retrieves an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       GetAudienceSegmentRequest request =
           GetAudienceSegmentRequest.newBuilder()
               .setName(AudienceSegmentName.of("[NETWORK_CODE]", "[AUDIENCE_SEGMENT]").toString())
               .build();
       AudienceSegment response = audienceSegmentServiceClient.getAudienceSegment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAudienceSegmentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAudienceSegmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)` |   
  
### getAudienceSegment(String name)
    
    
    public final AudienceSegment getAudienceSegment(String name)

Retrieves an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String name = AudienceSegmentName.of("[NETWORK_CODE]", "[AUDIENCE_SEGMENT]").toString();
       AudienceSegment response = audienceSegmentServiceClient.getAudienceSegment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AudienceSegment. Format: `networks/{network_code}/audienceSegments/{audience_segment_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)` |   
  
### getAudienceSegmentCallable()
    
    
    public final UnaryCallable<GetAudienceSegmentRequest,AudienceSegment> getAudienceSegmentCallable()

Retrieves an `AudienceSegment` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       GetAudienceSegmentRequest request =
           GetAudienceSegmentRequest.newBuilder()
               .setName(AudienceSegmentName.of("[NETWORK_CODE]", "[AUDIENCE_SEGMENT]").toString())
               .build();
       ApiFuture<AudienceSegment> future =
           audienceSegmentServiceClient.getAudienceSegmentCallable().futureCall(request);
       // Do something.
       AudienceSegment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAudienceSegmentRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAudienceSegmentRequest),[AudienceSegment](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegment)>` |   
  
### getSettings()
    
    
    public final @Nullable AudienceSegmentServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AudienceSegmentServiceSettings` |   
  
### getStub()
    
    
    public AudienceSegmentServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AudienceSegmentServiceStub)` |   
  
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
  
### listAudienceSegments(@Nullable NetworkName parent)
    
    
    public final AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse listAudienceSegments(@Nullable NetworkName parent)

Lists `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (AudienceSegment element :
           audienceSegmentServiceClient.listAudienceSegments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent publisher network associated with these audience segments. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse)` |   
  
### listAudienceSegments(ListAudienceSegmentsRequest request)
    
    
    public final AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse listAudienceSegments(ListAudienceSegmentsRequest request)

Lists `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       ListAudienceSegmentsRequest request =
           ListAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (AudienceSegment element :
           audienceSegmentServiceClient.listAudienceSegments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAudienceSegmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse)` |   
  
### listAudienceSegments(String parent)
    
    
    public final AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse listAudienceSegments(String parent)

Lists `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (AudienceSegment element :
           audienceSegmentServiceClient.listAudienceSegments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent publisher network associated with these audience segments. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse)` |   
  
### listAudienceSegmentsCallable()
    
    
    public final UnaryCallable<ListAudienceSegmentsRequest,ListAudienceSegmentsResponse> listAudienceSegmentsCallable()

Lists `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       ListAudienceSegmentsRequest request =
           ListAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListAudienceSegmentsResponse response =
             audienceSegmentServiceClient.listAudienceSegmentsCallable().call(request);
         for (AudienceSegment element : response.getAudienceSegmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAudienceSegmentsRequest),[ListAudienceSegmentsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAudienceSegmentsResponse)>` |   
  
### listAudienceSegmentsPagedCallable()
    
    
    public final UnaryCallable<ListAudienceSegmentsRequest,AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse> listAudienceSegmentsPagedCallable()

Lists `AudienceSegment` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AudienceSegmentServiceClient audienceSegmentServiceClient =
         AudienceSegmentServiceClient.create()) {
       ListAudienceSegmentsRequest request =
           ListAudienceSegmentsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<AudienceSegment> future =
           audienceSegmentServiceClient.listAudienceSegmentsPagedCallable().futureCall(request);
       // Do something.
       for (AudienceSegment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAudienceSegmentsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAudienceSegmentsRequest),[ListAudienceSegmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudienceSegmentServiceClient.ListAudienceSegmentsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
