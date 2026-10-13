---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyViewsClient
title: Class ImageFamilyViewsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:29.743442+00:00
---

# Class ImageFamilyViewsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyViewsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ImageFamilyViewsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ImageFamilyViewsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ImageFamilyViews API.

This client uses ImageFamilyViews version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageFamilyViewsClient imageFamilyViewsClient = ImageFamilyViewsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String family = "family-1281860764";
       ImageFamilyView response = imageFamilyViewsClient.get(project, zone, family);
     }
     

Note: close() needs to be called on the ImageFamilyViewsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Returns the latest image that is part of an image family, is not deprecated and is rolled out in the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetImageFamilyViewRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String family) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ImageFamilyViewsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ImageFamilyViewsSettings imageFamilyViewsSettings =
         ImageFamilyViewsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ImageFamilyViewsClient imageFamilyViewsClient =
         ImageFamilyViewsClient.create(imageFamilyViewsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ImageFamilyViewsSettings imageFamilyViewsSettings =
         ImageFamilyViewsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ImageFamilyViewsClient imageFamilyViewsClient =
         ImageFamilyViewsClient.create(imageFamilyViewsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ImageFamilyViewsClient

## Static Methods 

### create()
    
    
    public static final ImageFamilyViewsClient create()

Constructs an instance of ImageFamilyViewsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ImageFamilyViewsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyViewsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ImageFamilyViewsSettings settings)
    
    
    public static final ImageFamilyViewsClient create(ImageFamilyViewsSettings settings)

Constructs an instance of ImageFamilyViewsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ImageFamilyViewsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyViewsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImageFamilyViewsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyViewsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ImageFamilyViewsStub stub)
    
    
    public static final ImageFamilyViewsClient create(ImageFamilyViewsStub stub)

Constructs an instance of ImageFamilyViewsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ImageFamilyViewsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ImageFamilyViewsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ImageFamilyViewsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImageFamilyViewsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyViewsClient)` |   
  
## Constructors 

### ImageFamilyViewsClient(ImageFamilyViewsSettings settings)
    
    
    protected ImageFamilyViewsClient(ImageFamilyViewsSettings settings)

Constructs an instance of ImageFamilyViewsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ImageFamilyViewsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyViewsSettings)`  
  
  
### ImageFamilyViewsClient(ImageFamilyViewsStub stub)
    
    
    protected ImageFamilyViewsClient(ImageFamilyViewsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ImageFamilyViewsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ImageFamilyViewsStub)`  
  
  
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

### get(GetImageFamilyViewRequest request)
    
    
    public final ImageFamilyView get(GetImageFamilyViewRequest request)

Returns the latest image that is part of an image family, is not deprecated and is rolled out in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageFamilyViewsClient imageFamilyViewsClient = ImageFamilyViewsClient.create()) {
       GetImageFamilyViewRequest request =
           GetImageFamilyViewRequest.newBuilder()
               .setFamily("family-1281860764")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ImageFamilyView response = imageFamilyViewsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetImageFamilyViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetImageFamilyViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ImageFamilyView](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyView)` |   
  
### get(String project, String zone, String family)
    
    
    public final ImageFamilyView get(String project, String zone, String family)

Returns the latest image that is part of an image family, is not deprecated and is rolled out in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageFamilyViewsClient imageFamilyViewsClient = ImageFamilyViewsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String family = "family-1281860764";
       ImageFamilyView response = imageFamilyViewsClient.get(project, zone, family);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`family` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the image family to search for.  
**Returns**  
---  
**Type** | **Description**  
`[ImageFamilyView](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyView)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetImageFamilyViewRequest,ImageFamilyView> getCallable()

Returns the latest image that is part of an image family, is not deprecated and is rolled out in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ImageFamilyViewsClient imageFamilyViewsClient = ImageFamilyViewsClient.create()) {
       GetImageFamilyViewRequest request =
           GetImageFamilyViewRequest.newBuilder()
               .setFamily("family-1281860764")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<ImageFamilyView> future = imageFamilyViewsClient.getCallable().futureCall(request);
       // Do something.
       ImageFamilyView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetImageFamilyViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetImageFamilyViewRequest),[ImageFamilyView](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImageFamilyView)>` |   
  
### getSettings()
    
    
    public final @Nullable ImageFamilyViewsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ImageFamilyViewsSettings` |   
  
### getStub()
    
    
    public ImageFamilyViewsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ImageFamilyViewsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ImageFamilyViewsStub)` |   
  
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

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
