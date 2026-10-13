---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient
title: Class LineItemServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:48.304997+00:00
---

# Class LineItemServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LineItemServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/LineItemServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `LineItem` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       LineItemName name = LineItemName.of("[NETWORK_CODE]", "[LINE_ITEM]");
       LineItem response = lineItemServiceClient.getLineItem(name);
     }
     

Note: close() needs to be called on the LineItemServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetLineItem |  Retrieves a `LineItem` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLineItem(GetLineItemRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLineItem(LineItemName name) 
  * getLineItem(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLineItemCallable() 

  
ListLineItems |  Lists `LineItem` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLineItems(ListLineItemsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLineItems(NetworkName parent) 
  * listLineItems(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLineItemsPagedCallable() 
  * listLineItemsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LineItemServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LineItemServiceSettings lineItemServiceSettings =
         LineItemServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LineItemServiceClient lineItemServiceClient =
         LineItemServiceClient.create(lineItemServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LineItemServiceSettings lineItemServiceSettings =
         LineItemServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     LineItemServiceClient lineItemServiceClient =
         LineItemServiceClient.create(lineItemServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LineItemServiceClient

## Static Methods 

### create()
    
    
    public static final LineItemServiceClient create()

Constructs an instance of LineItemServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LineItemServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LineItemServiceSettings settings)
    
    
    public static final LineItemServiceClient create(LineItemServiceSettings settings)

Constructs an instance of LineItemServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LineItemServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineItemServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LineItemServiceStub stub)
    
    
    public static final LineItemServiceClient create(LineItemServiceStub stub)

Constructs an instance of LineItemServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(LineItemServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LineItemServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LineItemServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineItemServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient)` |   
  
## Constructors 

### LineItemServiceClient(LineItemServiceSettings settings)
    
    
    protected LineItemServiceClient(LineItemServiceSettings settings)

Constructs an instance of LineItemServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LineItemServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceSettings)`  
  
  
### LineItemServiceClient(LineItemServiceStub stub)
    
    
    protected LineItemServiceClient(LineItemServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LineItemServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LineItemServiceStub)`  
  
  
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

### getLineItem(@Nullable LineItemName name)
    
    
    public final LineItem getLineItem(@Nullable LineItemName name)

Retrieves a `LineItem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       LineItemName name = LineItemName.of("[NETWORK_CODE]", "[LINE_ITEM]");
       LineItem response = lineItemServiceClient.getLineItem(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LineItemName`  
Required. The resource name of the LineItem. Format: `networks/{network_code}/lineItems/{line_item_id}`  
**Returns**  
---  
**Type** | **Description**  
`[LineItem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItem)` |   
  
### getLineItem(GetLineItemRequest request)
    
    
    public final LineItem getLineItem(GetLineItemRequest request)

Retrieves a `LineItem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       GetLineItemRequest request =
           GetLineItemRequest.newBuilder()
               .setName(LineItemName.of("[NETWORK_CODE]", "[LINE_ITEM]").toString())
               .build();
       LineItem response = lineItemServiceClient.getLineItem(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLineItemRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLineItemRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LineItem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItem)` |   
  
### getLineItem(String name)
    
    
    public final LineItem getLineItem(String name)

Retrieves a `LineItem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       String name = LineItemName.of("[NETWORK_CODE]", "[LINE_ITEM]").toString();
       LineItem response = lineItemServiceClient.getLineItem(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the LineItem. Format: `networks/{network_code}/lineItems/{line_item_id}`  
**Returns**  
---  
**Type** | **Description**  
`[LineItem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItem)` |   
  
### getLineItemCallable()
    
    
    public final UnaryCallable<GetLineItemRequest,LineItem> getLineItemCallable()

Retrieves a `LineItem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       GetLineItemRequest request =
           GetLineItemRequest.newBuilder()
               .setName(LineItemName.of("[NETWORK_CODE]", "[LINE_ITEM]").toString())
               .build();
       ApiFuture<LineItem> future = lineItemServiceClient.getLineItemCallable().futureCall(request);
       // Do something.
       LineItem response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLineItemRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLineItemRequest),[LineItem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItem)>` |   
  
### getSettings()
    
    
    public final @Nullable LineItemServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LineItemServiceSettings` |   
  
### getStub()
    
    
    public LineItemServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LineItemServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LineItemServiceStub)` |   
  
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
  
### listLineItems(@Nullable NetworkName parent)
    
    
    public final LineItemServiceClient.ListLineItemsPagedResponse listLineItems(@Nullable NetworkName parent)

Lists `LineItem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (LineItem element : lineItemServiceClient.listLineItems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of LineItems. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LineItemServiceClient.ListLineItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient.ListLineItemsPagedResponse)` |   
  
### listLineItems(ListLineItemsRequest request)
    
    
    public final LineItemServiceClient.ListLineItemsPagedResponse listLineItems(ListLineItemsRequest request)

Lists `LineItem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       ListLineItemsRequest request =
           ListLineItemsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (LineItem element : lineItemServiceClient.listLineItems(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLineItemsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLineItemsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LineItemServiceClient.ListLineItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient.ListLineItemsPagedResponse)` |   
  
### listLineItems(String parent)
    
    
    public final LineItemServiceClient.ListLineItemsPagedResponse listLineItems(String parent)

Lists `LineItem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (LineItem element : lineItemServiceClient.listLineItems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of LineItems. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LineItemServiceClient.ListLineItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient.ListLineItemsPagedResponse)` |   
  
### listLineItemsCallable()
    
    
    public final UnaryCallable<ListLineItemsRequest,ListLineItemsResponse> listLineItemsCallable()

Lists `LineItem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       ListLineItemsRequest request =
           ListLineItemsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListLineItemsResponse response =
             lineItemServiceClient.listLineItemsCallable().call(request);
         for (LineItem element : response.getLineItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLineItemsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLineItemsRequest),[ListLineItemsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLineItemsResponse)>` |   
  
### listLineItemsPagedCallable()
    
    
    public final UnaryCallable<ListLineItemsRequest,LineItemServiceClient.ListLineItemsPagedResponse> listLineItemsPagedCallable()

Lists `LineItem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LineItemServiceClient lineItemServiceClient = LineItemServiceClient.create()) {
       ListLineItemsRequest request =
           ListLineItemsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<LineItem> future =
           lineItemServiceClient.listLineItemsPagedCallable().futureCall(request);
       // Do something.
       for (LineItem element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLineItemsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLineItemsRequest),[ListLineItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LineItemServiceClient.ListLineItemsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
