---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient
title: Class PreviewFeaturesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:23.469701+00:00
---

# Class PreviewFeaturesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PreviewFeaturesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/PreviewFeaturesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The PreviewFeatures API.

This client uses PreviewFeatures version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       String project = "project-309310695";
       String previewFeature = "previewFeature-712516082";
       PreviewFeature response = previewFeaturesClient.get(project, previewFeature);
     }
     

Note: close() needs to be called on the PreviewFeaturesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Returns the details of the given PreviewFeature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetPreviewFeatureRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String previewFeature) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Returns the details of the given PreviewFeature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListPreviewFeaturesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Update |  Patches the given PreviewFeature. This method is used to enable or disable a PreviewFeature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdatePreviewFeatureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String previewFeature, PreviewFeature previewFeatureResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PreviewFeaturesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PreviewFeaturesSettings previewFeaturesSettings =
         PreviewFeaturesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PreviewFeaturesClient previewFeaturesClient =
         PreviewFeaturesClient.create(previewFeaturesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PreviewFeaturesSettings previewFeaturesSettings =
         PreviewFeaturesSettings.newBuilder().setEndpoint(myEndpoint).build();
     PreviewFeaturesClient previewFeaturesClient =
         PreviewFeaturesClient.create(previewFeaturesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PreviewFeaturesClient

## Static Methods 

### create()
    
    
    public static final PreviewFeaturesClient create()

Constructs an instance of PreviewFeaturesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PreviewFeaturesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PreviewFeaturesSettings settings)
    
    
    public static final PreviewFeaturesClient create(PreviewFeaturesSettings settings)

Constructs an instance of PreviewFeaturesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PreviewFeaturesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PreviewFeaturesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PreviewFeaturesStub stub)
    
    
    public static final PreviewFeaturesClient create(PreviewFeaturesStub stub)

Constructs an instance of PreviewFeaturesClient, using the given stub for making calls. This is for advanced usage - prefer using create(PreviewFeaturesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PreviewFeaturesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PreviewFeaturesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PreviewFeaturesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient)` |   
  
## Constructors 

### PreviewFeaturesClient(PreviewFeaturesSettings settings)
    
    
    protected PreviewFeaturesClient(PreviewFeaturesSettings settings)

Constructs an instance of PreviewFeaturesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PreviewFeaturesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesSettings)`  
  
  
### PreviewFeaturesClient(PreviewFeaturesStub stub)
    
    
    protected PreviewFeaturesClient(PreviewFeaturesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PreviewFeaturesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PreviewFeaturesStub)`  
  
  
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

### get(GetPreviewFeatureRequest request)
    
    
    public final PreviewFeature get(GetPreviewFeatureRequest request)

Returns the details of the given PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       GetPreviewFeatureRequest request =
           GetPreviewFeatureRequest.newBuilder()
               .setPreviewFeature("previewFeature-712516082")
               .setProject("project-309310695")
               .build();
       PreviewFeature response = previewFeaturesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPreviewFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPreviewFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PreviewFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeature)` |   
  
### get(String project, String previewFeature)
    
    
    public final PreviewFeature get(String project, String previewFeature)

Returns the details of the given PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       String project = "project-309310695";
       String previewFeature = "previewFeature-712516082";
       PreviewFeature response = previewFeaturesClient.get(project, previewFeature);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`previewFeature` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PreviewFeature for this request.  
**Returns**  
---  
**Type** | **Description**  
`[PreviewFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeature)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetPreviewFeatureRequest,PreviewFeature> getCallable()

Returns the details of the given PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       GetPreviewFeatureRequest request =
           GetPreviewFeatureRequest.newBuilder()
               .setPreviewFeature("previewFeature-712516082")
               .setProject("project-309310695")
               .build();
       ApiFuture<PreviewFeature> future = previewFeaturesClient.getCallable().futureCall(request);
       // Do something.
       PreviewFeature response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPreviewFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPreviewFeatureRequest),[PreviewFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeature)>` |   
  
### getSettings()
    
    
    public final @Nullable PreviewFeaturesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.PreviewFeaturesSettings` |   
  
### getStub()
    
    
    public PreviewFeaturesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PreviewFeaturesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PreviewFeaturesStub)` |   
  
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
  
### list(ListPreviewFeaturesRequest request)
    
    
    public final PreviewFeaturesClient.ListPagedResponse list(ListPreviewFeaturesRequest request)

Returns the details of the given PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       ListPreviewFeaturesRequest request =
           ListPreviewFeaturesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (PreviewFeature element : previewFeaturesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPreviewFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPreviewFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PreviewFeaturesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final PreviewFeaturesClient.ListPagedResponse list(String project)

Returns the details of the given PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       String project = "project-309310695";
       for (PreviewFeature element : previewFeaturesClient.list(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[PreviewFeaturesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListPreviewFeaturesRequest,PreviewFeatureList> listCallable()

Returns the details of the given PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       ListPreviewFeaturesRequest request =
           ListPreviewFeaturesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         PreviewFeatureList response = previewFeaturesClient.listCallable().call(request);
         for (PreviewFeature element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPreviewFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPreviewFeaturesRequest),[PreviewFeatureList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeatureList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListPreviewFeaturesRequest,PreviewFeaturesClient.ListPagedResponse> listPagedCallable()

Returns the details of the given PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       ListPreviewFeaturesRequest request =
           ListPreviewFeaturesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<PreviewFeature> future =
           previewFeaturesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (PreviewFeature element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPreviewFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPreviewFeaturesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeaturesClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAsync(UpdatePreviewFeatureRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdatePreviewFeatureRequest request)

Patches the given PreviewFeature. This method is used to enable or disable a PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       UpdatePreviewFeatureRequest request =
           UpdatePreviewFeatureRequest.newBuilder()
               .setPreviewFeature("previewFeature-712516082")
               .setPreviewFeatureResource(PreviewFeature.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = previewFeaturesClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePreviewFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePreviewFeatureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String previewFeature, PreviewFeature previewFeatureResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String previewFeature, PreviewFeature previewFeatureResource)

Patches the given PreviewFeature. This method is used to enable or disable a PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       String project = "project-309310695";
       String previewFeature = "previewFeature-712516082";
       PreviewFeature previewFeatureResource = PreviewFeature.newBuilder().build();
       Operation response =
           previewFeaturesClient.updateAsync(project, previewFeature, previewFeatureResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`previewFeature` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PreviewFeature for this request.  
`previewFeatureResource` | `[PreviewFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeature)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdatePreviewFeatureRequest,Operation> updateCallable()

Patches the given PreviewFeature. This method is used to enable or disable a PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       UpdatePreviewFeatureRequest request =
           UpdatePreviewFeatureRequest.newBuilder()
               .setPreviewFeature("previewFeature-712516082")
               .setPreviewFeatureResource(PreviewFeature.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = previewFeaturesClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePreviewFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePreviewFeatureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdatePreviewFeatureRequest,Operation,Operation> updateOperationCallable()

Patches the given PreviewFeature. This method is used to enable or disable a PreviewFeature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PreviewFeaturesClient previewFeaturesClient = PreviewFeaturesClient.create()) {
       UpdatePreviewFeatureRequest request =
           UpdatePreviewFeatureRequest.newBuilder()
               .setPreviewFeature("previewFeature-712516082")
               .setPreviewFeatureResource(PreviewFeature.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           previewFeaturesClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePreviewFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePreviewFeatureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
