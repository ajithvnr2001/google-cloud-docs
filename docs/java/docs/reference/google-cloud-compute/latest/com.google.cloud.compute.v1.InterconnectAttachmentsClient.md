---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient
title: Class InterconnectAttachmentsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:49.117241+00:00
---

# Class InterconnectAttachmentsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InterconnectAttachmentsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InterconnectAttachmentsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InterconnectAttachments API.

This client uses InterconnectAttachments version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String interconnectAttachment = "interconnectAttachment1869250641";
       InterconnectAttachment response =
           interconnectAttachmentsClient.get(project, region, interconnectAttachment);
     }
     

Note: close() needs to be called on the InterconnectAttachmentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of interconnect attachments.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListInterconnectAttachmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified interconnect attachment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInterconnectAttachmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String interconnectAttachment) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified interconnect attachment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInterconnectAttachmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String interconnectAttachment) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates an InterconnectAttachment in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInterconnectAttachmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, InterconnectAttachment interconnectAttachmentResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of interconnect attachments contained within the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInterconnectAttachmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified interconnect attachment with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchInterconnectAttachmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String interconnectAttachment, InterconnectAttachment interconnectAttachmentResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetLabels |  Sets the labels on an InterconnectAttachment. To learn more about labels, read the Labeling Resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsInterconnectAttachmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InterconnectAttachmentsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectAttachmentsSettings interconnectAttachmentsSettings =
         InterconnectAttachmentsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create(interconnectAttachmentsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectAttachmentsSettings interconnectAttachmentsSettings =
         InterconnectAttachmentsSettings.newBuilder().setEndpoint(myEndpoint).build();
     InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create(interconnectAttachmentsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InterconnectAttachmentsClient

## Static Methods 

### create()
    
    
    public static final InterconnectAttachmentsClient create()

Constructs an instance of InterconnectAttachmentsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectAttachmentsSettings settings)
    
    
    public static final InterconnectAttachmentsClient create(InterconnectAttachmentsSettings settings)

Constructs an instance of InterconnectAttachmentsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectAttachmentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectAttachmentsStub stub)
    
    
    public static final InterconnectAttachmentsClient create(InterconnectAttachmentsStub stub)

Constructs an instance of InterconnectAttachmentsClient, using the given stub for making calls. This is for advanced usage - prefer using create(InterconnectAttachmentsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectAttachmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectAttachmentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient)` |   
  
## Constructors 

### InterconnectAttachmentsClient(InterconnectAttachmentsSettings settings)
    
    
    protected InterconnectAttachmentsClient(InterconnectAttachmentsSettings settings)

Constructs an instance of InterconnectAttachmentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectAttachmentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsSettings)`  
  
  
### InterconnectAttachmentsClient(InterconnectAttachmentsStub stub)
    
    
    protected InterconnectAttachmentsClient(InterconnectAttachmentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectAttachmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectAttachmentsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListInterconnectAttachmentsRequest request)
    
    
    public final InterconnectAttachmentsClient.AggregatedListPagedResponse aggregatedList(AggregatedListInterconnectAttachmentsRequest request)

Retrieves an aggregated list of interconnect attachments.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       AggregatedListInterconnectAttachmentsRequest request =
           AggregatedListInterconnectAttachmentsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, InterconnectAttachmentsScopedList> element :
           interconnectAttachmentsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInterconnectAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final InterconnectAttachmentsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of interconnect attachments.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, InterconnectAttachmentsScopedList> element :
           interconnectAttachmentsClient.aggregatedList(project).iterateAll()) {
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
`[InterconnectAttachmentsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListInterconnectAttachmentsRequest,InterconnectAttachmentAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of interconnect attachments.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       AggregatedListInterconnectAttachmentsRequest request =
           AggregatedListInterconnectAttachmentsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         InterconnectAttachmentAggregatedList response =
             interconnectAttachmentsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, InterconnectAttachmentsScopedList> element :
             response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInterconnectAttachmentsRequest),[InterconnectAttachmentAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListInterconnectAttachmentsRequest,InterconnectAttachmentsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of interconnect attachments.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       AggregatedListInterconnectAttachmentsRequest request =
           AggregatedListInterconnectAttachmentsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, InterconnectAttachmentsScopedList>> future =
           interconnectAttachmentsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, InterconnectAttachmentsScopedList> element :
           future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInterconnectAttachmentsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteInterconnectAttachmentRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInterconnectAttachmentRequest request)

Deletes the specified interconnect attachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       DeleteInterconnectAttachmentRequest request =
           DeleteInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = interconnectAttachmentsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String interconnectAttachment)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String interconnectAttachment)

Deletes the specified interconnect attachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String interconnectAttachment = "interconnectAttachment1869250641";
       Operation response =
           interconnectAttachmentsClient.deleteAsync(project, region, interconnectAttachment).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`interconnectAttachment` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the interconnect attachment to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInterconnectAttachmentRequest,Operation> deleteCallable()

Deletes the specified interconnect attachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       DeleteInterconnectAttachmentRequest request =
           DeleteInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           interconnectAttachmentsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInterconnectAttachmentRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified interconnect attachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       DeleteInterconnectAttachmentRequest request =
           DeleteInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectAttachmentsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInterconnectAttachmentRequest request)
    
    
    public final InterconnectAttachment get(GetInterconnectAttachmentRequest request)

Returns the specified interconnect attachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       GetInterconnectAttachmentRequest request =
           GetInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       InterconnectAttachment response = interconnectAttachmentsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachment)` |   
  
### get(String project, String region, String interconnectAttachment)
    
    
    public final InterconnectAttachment get(String project, String region, String interconnectAttachment)

Returns the specified interconnect attachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String interconnectAttachment = "interconnectAttachment1869250641";
       InterconnectAttachment response =
           interconnectAttachmentsClient.get(project, region, interconnectAttachment);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`interconnectAttachment` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the interconnect attachment to return.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachment)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInterconnectAttachmentRequest,InterconnectAttachment> getCallable()

Returns the specified interconnect attachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       GetInterconnectAttachmentRequest request =
           GetInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InterconnectAttachment> future =
           interconnectAttachmentsClient.getCallable().futureCall(request);
       // Do something.
       InterconnectAttachment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectAttachmentRequest),[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachment)>` |   
  
### getSettings()
    
    
    public final @Nullable InterconnectAttachmentsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InterconnectAttachmentsSettings` |   
  
### getStub()
    
    
    public InterconnectAttachmentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectAttachmentsStub)` |   
  
### insertAsync(InsertInterconnectAttachmentRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInterconnectAttachmentRequest request)

Creates an InterconnectAttachment in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       InsertInterconnectAttachmentRequest request =
           InsertInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachmentResource(InterconnectAttachment.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Operation response = interconnectAttachmentsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, InterconnectAttachment interconnectAttachmentResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, InterconnectAttachment interconnectAttachmentResource)

Creates an InterconnectAttachment in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       InterconnectAttachment interconnectAttachmentResource =
           InterconnectAttachment.newBuilder().build();
       Operation response =
           interconnectAttachmentsClient
               .insertAsync(project, region, interconnectAttachmentResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`interconnectAttachmentResource` | `[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachment)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInterconnectAttachmentRequest,Operation> insertCallable()

Creates an InterconnectAttachment in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       InsertInterconnectAttachmentRequest request =
           InsertInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachmentResource(InterconnectAttachment.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           interconnectAttachmentsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInterconnectAttachmentRequest,Operation,Operation> insertOperationCallable()

Creates an InterconnectAttachment in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       InsertInterconnectAttachmentRequest request =
           InsertInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachmentResource(InterconnectAttachment.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectAttachmentsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInterconnectAttachmentsRequest request)
    
    
    public final InterconnectAttachmentsClient.ListPagedResponse list(ListInterconnectAttachmentsRequest request)

Retrieves the list of interconnect attachments contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       ListInterconnectAttachmentsRequest request =
           ListInterconnectAttachmentsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (InterconnectAttachment element :
           interconnectAttachmentsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final InterconnectAttachmentsClient.ListPagedResponse list(String project, String region)

Retrieves the list of interconnect attachments contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (InterconnectAttachment element :
           interconnectAttachmentsClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInterconnectAttachmentsRequest,InterconnectAttachmentList> listCallable()

Retrieves the list of interconnect attachments contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       ListInterconnectAttachmentsRequest request =
           ListInterconnectAttachmentsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         InterconnectAttachmentList response =
             interconnectAttachmentsClient.listCallable().call(request);
         for (InterconnectAttachment element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectAttachmentsRequest),[InterconnectAttachmentList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInterconnectAttachmentsRequest,InterconnectAttachmentsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of interconnect attachments contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       ListInterconnectAttachmentsRequest request =
           ListInterconnectAttachmentsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InterconnectAttachment> future =
           interconnectAttachmentsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InterconnectAttachment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectAttachmentsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentsClient.ListPagedResponse)>` |   
  
### patchAsync(PatchInterconnectAttachmentRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchInterconnectAttachmentRequest request)

Updates the specified interconnect attachment with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       PatchInterconnectAttachmentRequest request =
           PatchInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setInterconnectAttachmentResource(InterconnectAttachment.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = interconnectAttachmentsClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String interconnectAttachment, InterconnectAttachment interconnectAttachmentResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String interconnectAttachment, InterconnectAttachment interconnectAttachmentResource)

Updates the specified interconnect attachment with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String interconnectAttachment = "interconnectAttachment1869250641";
       InterconnectAttachment interconnectAttachmentResource =
           InterconnectAttachment.newBuilder().build();
       Operation response =
           interconnectAttachmentsClient
               .patchAsync(project, region, interconnectAttachment, interconnectAttachmentResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`interconnectAttachment` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the interconnect attachment to patch.  
`interconnectAttachmentResource` | `[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachment)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchInterconnectAttachmentRequest,Operation> patchCallable()

Updates the specified interconnect attachment with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       PatchInterconnectAttachmentRequest request =
           PatchInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setInterconnectAttachmentResource(InterconnectAttachment.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           interconnectAttachmentsClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchInterconnectAttachmentRequest,Operation,Operation> patchOperationCallable()

Updates the specified interconnect attachment with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       PatchInterconnectAttachmentRequest request =
           PatchInterconnectAttachmentRequest.newBuilder()
               .setInterconnectAttachment("interconnectAttachment1869250641")
               .setInterconnectAttachmentResource(InterconnectAttachment.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectAttachmentsClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(SetLabelsInterconnectAttachmentRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsInterconnectAttachmentRequest request)

Sets the labels on an InterconnectAttachment. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       SetLabelsInterconnectAttachmentRequest request =
           SetLabelsInterconnectAttachmentRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       Operation response = interconnectAttachmentsClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)

Sets the labels on an InterconnectAttachment. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetLabelsRequest regionSetLabelsRequestResource =
           RegionSetLabelsRequest.newBuilder().build();
       Operation response =
           interconnectAttachmentsClient
               .setLabelsAsync(project, region, resource, regionSetLabelsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`regionSetLabelsRequestResource` | `[RegionSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsInterconnectAttachmentRequest,Operation> setLabelsCallable()

Sets the labels on an InterconnectAttachment. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       SetLabelsInterconnectAttachmentRequest request =
           SetLabelsInterconnectAttachmentRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Operation> future =
           interconnectAttachmentsClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsInterconnectAttachmentRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on an InterconnectAttachment. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentsClient interconnectAttachmentsClient =
         InterconnectAttachmentsClient.create()) {
       SetLabelsInterconnectAttachmentRequest request =
           SetLabelsInterconnectAttachmentRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectAttachmentsClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
