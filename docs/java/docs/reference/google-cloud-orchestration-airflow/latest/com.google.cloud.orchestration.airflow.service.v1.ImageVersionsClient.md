---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient
title: Class ImageVersionsClient (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:57.450071+00:00
---

# Class ImageVersionsClient (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ImageVersionsClient (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-orchestration-airflow/google-cloud-orchestration-airflow/src/main/java/com/google/cloud/orchestration/airflow/service/v1/ImageVersionsClient.java)| [Product Reference](https://cloud.google.com/composer/docs)| [REST Documentation](https://cloud.google.com/composer/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/composer/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Readonly service to query available ImageVersions.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageVersionsClient imageVersionsClient = ImageVersionsClient.create()) {
       String parent = "parent-995424086";
       for (ImageVersion element : imageVersionsClient.listImageVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

Note: close() needs to be called on the ImageVersionsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListImageVersions |  List ImageVersions for provided location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listImageVersions(ListImageVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listImageVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listImageVersionsPagedCallable() 
  * listImageVersionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ImageVersionsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ImageVersionsSettings imageVersionsSettings =
         ImageVersionsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ImageVersionsClient imageVersionsClient = ImageVersionsClient.create(imageVersionsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ImageVersionsSettings imageVersionsSettings =
         ImageVersionsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ImageVersionsClient imageVersionsClient = ImageVersionsClient.create(imageVersionsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ImageVersionsSettings imageVersionsSettings =
         ImageVersionsSettings.newHttpJsonBuilder().build();
     ImageVersionsClient imageVersionsClient = ImageVersionsClient.create(imageVersionsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ImageVersionsClient

## Static Methods 

### create()
    
    
    public static final ImageVersionsClient create()

Constructs an instance of ImageVersionsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ImageVersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ImageVersionsSettings settings)
    
    
    public static final ImageVersionsClient create(ImageVersionsSettings settings)

Constructs an instance of ImageVersionsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ImageVersionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImageVersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ImageVersionsStub stub)
    
    
    public static final ImageVersionsClient create(ImageVersionsStub stub)

Constructs an instance of ImageVersionsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ImageVersionsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ImageVersionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.stub.ImageVersionsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImageVersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient)` |   
  
## Constructors 

### ImageVersionsClient(ImageVersionsSettings settings)
    
    
    protected ImageVersionsClient(ImageVersionsSettings settings)

Constructs an instance of ImageVersionsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ImageVersionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsSettings)`  
  
  
### ImageVersionsClient(ImageVersionsStub stub)
    
    
    protected ImageVersionsClient(ImageVersionsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ImageVersionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.stub.ImageVersionsStub)`  
  
  
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

### getSettings()
    
    
    public final @Nullable ImageVersionsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.ImageVersionsSettings` |   
  
### getStub()
    
    
    public ImageVersionsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ImageVersionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.stub.ImageVersionsStub)` |   
  
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
  
### listImageVersions(ListImageVersionsRequest request)
    
    
    public final ImageVersionsClient.ListImageVersionsPagedResponse listImageVersions(ListImageVersionsRequest request)

List ImageVersions for provided location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageVersionsClient imageVersionsClient = ImageVersionsClient.create()) {
       ListImageVersionsRequest request =
           ListImageVersionsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setIncludePastReleases(true)
               .build();
       for (ImageVersion element : imageVersionsClient.listImageVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListImageVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListImageVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ImageVersionsClient.ListImageVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient.ListImageVersionsPagedResponse)` |   
  
### listImageVersions(String parent)
    
    
    public final ImageVersionsClient.ListImageVersionsPagedResponse listImageVersions(String parent)

List ImageVersions for provided location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageVersionsClient imageVersionsClient = ImageVersionsClient.create()) {
       String parent = "parent-995424086";
       for (ImageVersion element : imageVersionsClient.listImageVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
List ImageVersions in the given project and location, in the form: "projects/{projectId}/locations/{locationId}"  
**Returns**  
---  
**Type** | **Description**  
`[ImageVersionsClient.ListImageVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient.ListImageVersionsPagedResponse)` |   
  
### listImageVersionsCallable()
    
    
    public final UnaryCallable<ListImageVersionsRequest,ListImageVersionsResponse> listImageVersionsCallable()

List ImageVersions for provided location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageVersionsClient imageVersionsClient = ImageVersionsClient.create()) {
       ListImageVersionsRequest request =
           ListImageVersionsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setIncludePastReleases(true)
               .build();
       while (true) {
         ListImageVersionsResponse response =
             imageVersionsClient.listImageVersionsCallable().call(request);
         for (ImageVersion element : response.getImageVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImageVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListImageVersionsRequest),[ListImageVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListImageVersionsResponse)>` |   
  
### listImageVersionsPagedCallable()
    
    
    public final UnaryCallable<ListImageVersionsRequest,ImageVersionsClient.ListImageVersionsPagedResponse> listImageVersionsPagedCallable()

List ImageVersions for provided location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageVersionsClient imageVersionsClient = ImageVersionsClient.create()) {
       ListImageVersionsRequest request =
           ListImageVersionsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setIncludePastReleases(true)
               .build();
       ApiFuture<ImageVersion> future =
           imageVersionsClient.listImageVersionsPagedCallable().futureCall(request);
       // Do something.
       for (ImageVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImageVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListImageVersionsRequest),[ListImageVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ImageVersionsClient.ListImageVersionsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
