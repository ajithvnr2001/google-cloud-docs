---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient
title: Class ContentLabelServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:36.261283+00:00
---

# Class ContentLabelServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ContentLabelServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ContentLabelServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `ContentLabel` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       ContentLabelName name = ContentLabelName.of("[NETWORK_CODE]", "[CONTENT_LABEL]");
       ContentLabel response = contentLabelServiceClient.getContentLabel(name);
     }
     

Note: close() needs to be called on the ContentLabelServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetContentLabel |  Retrieves a `ContentLabel` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getContentLabel(GetContentLabelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getContentLabel(ContentLabelName name) 
  * getContentLabel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getContentLabelCallable() 

  
ListContentLabels |  Lists `ContentLabel` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listContentLabels(ListContentLabelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listContentLabels(NetworkName parent) 
  * listContentLabels(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listContentLabelsPagedCallable() 
  * listContentLabelsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ContentLabelServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ContentLabelServiceSettings contentLabelServiceSettings =
         ContentLabelServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ContentLabelServiceClient contentLabelServiceClient =
         ContentLabelServiceClient.create(contentLabelServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ContentLabelServiceSettings contentLabelServiceSettings =
         ContentLabelServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ContentLabelServiceClient contentLabelServiceClient =
         ContentLabelServiceClient.create(contentLabelServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ContentLabelServiceClient

## Static Methods 

### create()
    
    
    public static final ContentLabelServiceClient create()

Constructs an instance of ContentLabelServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ContentLabelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ContentLabelServiceSettings settings)
    
    
    public static final ContentLabelServiceClient create(ContentLabelServiceSettings settings)

Constructs an instance of ContentLabelServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ContentLabelServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ContentLabelServiceStub stub)
    
    
    public static final ContentLabelServiceClient create(ContentLabelServiceStub stub)

Constructs an instance of ContentLabelServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ContentLabelServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ContentLabelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentLabelServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient)` |   
  
## Constructors 

### ContentLabelServiceClient(ContentLabelServiceSettings settings)
    
    
    protected ContentLabelServiceClient(ContentLabelServiceSettings settings)

Constructs an instance of ContentLabelServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ContentLabelServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceSettings)`  
  
  
### ContentLabelServiceClient(ContentLabelServiceStub stub)
    
    
    protected ContentLabelServiceClient(ContentLabelServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ContentLabelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentLabelServiceStub)`  
  
  
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

### getContentLabel(@Nullable ContentLabelName name)
    
    
    public final ContentLabel getContentLabel(@Nullable ContentLabelName name)

Retrieves a `ContentLabel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       ContentLabelName name = ContentLabelName.of("[NETWORK_CODE]", "[CONTENT_LABEL]");
       ContentLabel response = contentLabelServiceClient.getContentLabel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ContentLabelName`  
Required. The resource name of the ContentLabel. Format: `networks/{network_code}/contentLabels/{content_label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabel)` |   
  
### getContentLabel(GetContentLabelRequest request)
    
    
    public final ContentLabel getContentLabel(GetContentLabelRequest request)

Retrieves a `ContentLabel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       GetContentLabelRequest request =
           GetContentLabelRequest.newBuilder()
               .setName(ContentLabelName.of("[NETWORK_CODE]", "[CONTENT_LABEL]").toString())
               .build();
       ContentLabel response = contentLabelServiceClient.getContentLabel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetContentLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetContentLabelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabel)` |   
  
### getContentLabel(String name)
    
    
    public final ContentLabel getContentLabel(String name)

Retrieves a `ContentLabel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       String name = ContentLabelName.of("[NETWORK_CODE]", "[CONTENT_LABEL]").toString();
       ContentLabel response = contentLabelServiceClient.getContentLabel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ContentLabel. Format: `networks/{network_code}/contentLabels/{content_label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabel)` |   
  
### getContentLabelCallable()
    
    
    public final UnaryCallable<GetContentLabelRequest,ContentLabel> getContentLabelCallable()

Retrieves a `ContentLabel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       GetContentLabelRequest request =
           GetContentLabelRequest.newBuilder()
               .setName(ContentLabelName.of("[NETWORK_CODE]", "[CONTENT_LABEL]").toString())
               .build();
       ApiFuture<ContentLabel> future =
           contentLabelServiceClient.getContentLabelCallable().futureCall(request);
       // Do something.
       ContentLabel response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetContentLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetContentLabelRequest),[ContentLabel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabel)>` |   
  
### getSettings()
    
    
    public final @Nullable ContentLabelServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ContentLabelServiceSettings` |   
  
### getStub()
    
    
    public ContentLabelServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ContentLabelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentLabelServiceStub)` |   
  
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
  
### listContentLabels(@Nullable NetworkName parent)
    
    
    public final ContentLabelServiceClient.ListContentLabelsPagedResponse listContentLabels(@Nullable NetworkName parent)

Lists `ContentLabel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (ContentLabel element :
           contentLabelServiceClient.listContentLabels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of ContentLabels. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabelServiceClient.ListContentLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient.ListContentLabelsPagedResponse)` |   
  
### listContentLabels(ListContentLabelsRequest request)
    
    
    public final ContentLabelServiceClient.ListContentLabelsPagedResponse listContentLabels(ListContentLabelsRequest request)

Lists `ContentLabel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       ListContentLabelsRequest request =
           ListContentLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (ContentLabel element :
           contentLabelServiceClient.listContentLabels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListContentLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentLabelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabelServiceClient.ListContentLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient.ListContentLabelsPagedResponse)` |   
  
### listContentLabels(String parent)
    
    
    public final ContentLabelServiceClient.ListContentLabelsPagedResponse listContentLabels(String parent)

Lists `ContentLabel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (ContentLabel element :
           contentLabelServiceClient.listContentLabels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of ContentLabels. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentLabelServiceClient.ListContentLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient.ListContentLabelsPagedResponse)` |   
  
### listContentLabelsCallable()
    
    
    public final UnaryCallable<ListContentLabelsRequest,ListContentLabelsResponse> listContentLabelsCallable()

Lists `ContentLabel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       ListContentLabelsRequest request =
           ListContentLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListContentLabelsResponse response =
             contentLabelServiceClient.listContentLabelsCallable().call(request);
         for (ContentLabel element : response.getContentLabelsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContentLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentLabelsRequest),[ListContentLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentLabelsResponse)>` |   
  
### listContentLabelsPagedCallable()
    
    
    public final UnaryCallable<ListContentLabelsRequest,ContentLabelServiceClient.ListContentLabelsPagedResponse> listContentLabelsPagedCallable()

Lists `ContentLabel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentLabelServiceClient contentLabelServiceClient = ContentLabelServiceClient.create()) {
       ListContentLabelsRequest request =
           ListContentLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<ContentLabel> future =
           contentLabelServiceClient.listContentLabelsPagedCallable().futureCall(request);
       // Do something.
       for (ContentLabel element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContentLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentLabelsRequest),[ListContentLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentLabelServiceClient.ListContentLabelsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
