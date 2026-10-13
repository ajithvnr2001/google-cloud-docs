---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient
title: Class VideoIntelligenceServiceClient (2.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:58:02.519756+00:00
---

# Class VideoIntelligenceServiceClient (2.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VideoIntelligenceServiceClient (2.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.98.0 (latest)  2.94.0  2.93.0  2.92.0  2.90.0  2.87.0  2.86.0  2.84.0  2.82.0  2.81.0  2.79.0  2.77.0  2.75.0  2.74.0  2.73.0  2.72.0  2.71.0  2.69.0  2.67.0  2.66.0  2.63.0  2.62.0  2.61.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.13  2.1.0  2.0.27 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-video-intelligence/google-cloud-video-intelligence/src/main/java/com/google/cloud/videointelligence/v1/VideoIntelligenceServiceClient.java)| [Product Reference](https://cloud.google.com/video-intelligence/docs/)| [REST Documentation](https://cloud.google.com/video-intelligence/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/video-intelligence/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service that implements the Video Intelligence API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create()) {
       String inputUri = "inputUri470706498";
       List<Feature> features = new ArrayList<>();
       AnnotateVideoResponse response =
           videoIntelligenceServiceClient.annotateVideoAsync(inputUri, features).get();
     }
     

Note: close() needs to be called on the VideoIntelligenceServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AnnotateVideo |  Performs asynchronous video annotation. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `AnnotateVideoProgress` (progress). `Operation.response` contains `AnnotateVideoResponse` (results). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * annotateVideoAsync(AnnotateVideoRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * annotateVideoAsync(String inputUri, List<Feature> features) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * annotateVideoOperationCallable() 
  * annotateVideoCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of VideoIntelligenceServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VideoIntelligenceServiceSettings videoIntelligenceServiceSettings =
         VideoIntelligenceServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create(videoIntelligenceServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VideoIntelligenceServiceSettings videoIntelligenceServiceSettings =
         VideoIntelligenceServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create(videoIntelligenceServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VideoIntelligenceServiceSettings videoIntelligenceServiceSettings =
         VideoIntelligenceServiceSettings.newHttpJsonBuilder().build();
     VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create(videoIntelligenceServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VideoIntelligenceServiceClient

## Static Methods 

### create()
    
    
    public static final VideoIntelligenceServiceClient create()

Constructs an instance of VideoIntelligenceServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VideoIntelligenceServiceSettings settings)
    
    
    public static final VideoIntelligenceServiceClient create(VideoIntelligenceServiceSettings settings)

Constructs an instance of VideoIntelligenceServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VideoIntelligenceServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VideoIntelligenceServiceStub stub)
    
    
    public static final VideoIntelligenceServiceClient create(VideoIntelligenceServiceStub stub)

Constructs an instance of VideoIntelligenceServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(VideoIntelligenceServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VideoIntelligenceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.stub.VideoIntelligenceServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient)` |   
  
## Constructors 

### VideoIntelligenceServiceClient(VideoIntelligenceServiceSettings settings)
    
    
    protected VideoIntelligenceServiceClient(VideoIntelligenceServiceSettings settings)

Constructs an instance of VideoIntelligenceServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VideoIntelligenceServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceSettings)`  
  
  
### VideoIntelligenceServiceClient(VideoIntelligenceServiceStub stub)
    
    
    protected VideoIntelligenceServiceClient(VideoIntelligenceServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VideoIntelligenceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.stub.VideoIntelligenceServiceStub)`  
  
  
## Methods 

### annotateVideoAsync(AnnotateVideoRequest request)
    
    
    public final OperationFuture<AnnotateVideoResponse,AnnotateVideoProgress> annotateVideoAsync(AnnotateVideoRequest request)

Performs asynchronous video annotation. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `AnnotateVideoProgress` (progress). `Operation.response` contains `AnnotateVideoResponse` (results).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create()) {
       AnnotateVideoRequest request =
           AnnotateVideoRequest.newBuilder()
               .setInputUri("inputUri470706498")
               .setInputContent(ByteString.EMPTY)
               .addAllFeatures(new ArrayList<Feature>())
               .setVideoContext(VideoContext.newBuilder().build())
               .setOutputUri("outputUri-2119300949")
               .setLocationId("locationId1541836720")
               .build();
       AnnotateVideoResponse response =
           videoIntelligenceServiceClient.annotateVideoAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse),[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress)>` |   
  
### annotateVideoAsync(String inputUri, List<Feature> features)
    
    
    public final OperationFuture<AnnotateVideoResponse,AnnotateVideoProgress> annotateVideoAsync(String inputUri, List<Feature> features)

Performs asynchronous video annotation. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `AnnotateVideoProgress` (progress). `Operation.response` contains `AnnotateVideoResponse` (results).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create()) {
       String inputUri = "inputUri470706498";
       List<Feature> features = new ArrayList<>();
       AnnotateVideoResponse response =
           videoIntelligenceServiceClient.annotateVideoAsync(inputUri, features).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`inputUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Input video location. Currently, only [Cloud Storage](https://cloud.google.com/storage/) URIs are supported. URIs must be specified in the following format: `gs://bucket-id/object-id` (other URI formats return google.rpc.Code.INVALID_ARGUMENT). For more information, see [Request URIs](https://cloud.google.com/storage/docs/request-endpoints). To identify multiple videos, a video URI may include wildcards in the `object-id`. Supported wildcards: '*' to match 0 or more characters; '?' to match 1 character. If unset, the input video should be embedded in the request as `input_content`. If set, `input_content` must be unset.  
`features` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature)>`  
Required. Requested video annotation features.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse),[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress)>` |   
  
### annotateVideoCallable()
    
    
    public final UnaryCallable<AnnotateVideoRequest,Operation> annotateVideoCallable()

Performs asynchronous video annotation. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `AnnotateVideoProgress` (progress). `Operation.response` contains `AnnotateVideoResponse` (results).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create()) {
       AnnotateVideoRequest request =
           AnnotateVideoRequest.newBuilder()
               .setInputUri("inputUri470706498")
               .setInputContent(ByteString.EMPTY)
               .addAllFeatures(new ArrayList<Feature>())
               .setVideoContext(VideoContext.newBuilder().build())
               .setOutputUri("outputUri-2119300949")
               .setLocationId("locationId1541836720")
               .build();
       ApiFuture<Operation> future =
           videoIntelligenceServiceClient.annotateVideoCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### annotateVideoOperationCallable()
    
    
    public final OperationCallable<AnnotateVideoRequest,AnnotateVideoResponse,AnnotateVideoProgress> annotateVideoOperationCallable()

Performs asynchronous video annotation. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `AnnotateVideoProgress` (progress). `Operation.response` contains `AnnotateVideoResponse` (results).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoIntelligenceServiceClient videoIntelligenceServiceClient =
         VideoIntelligenceServiceClient.create()) {
       AnnotateVideoRequest request =
           AnnotateVideoRequest.newBuilder()
               .setInputUri("inputUri470706498")
               .setInputContent(ByteString.EMPTY)
               .addAllFeatures(new ArrayList<Feature>())
               .setVideoContext(VideoContext.newBuilder().build())
               .setOutputUri("outputUri-2119300949")
               .setLocationId("locationId1541836720")
               .build();
       OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
           videoIntelligenceServiceClient.annotateVideoOperationCallable().futureCall(request);
       // Do something.
       AnnotateVideoResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest),[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse),[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress)>` |   
  
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

### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable VideoIntelligenceServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.videointelligence.v1.VideoIntelligenceServiceSettings` |   
  
### getStub()
    
    
    public VideoIntelligenceServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[VideoIntelligenceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.stub.VideoIntelligenceServiceStub)` |   
  
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
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
