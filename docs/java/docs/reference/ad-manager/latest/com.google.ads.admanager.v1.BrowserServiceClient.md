---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient
title: Class BrowserServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:31.147521+00:00
---

# Class BrowserServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BrowserServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/BrowserServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Browser` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       BrowserName name = BrowserName.of("[NETWORK_CODE]", "[BROWSER]");
       Browser response = browserServiceClient.getBrowser(name);
     }
     

Note: close() needs to be called on the BrowserServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetBrowser |  Retrieves a `Browser` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBrowser(GetBrowserRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBrowser(BrowserName name) 
  * getBrowser(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBrowserCallable() 

  
ListBrowsers |  Lists `Browser` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBrowsers(ListBrowsersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBrowsers(NetworkName parent) 
  * listBrowsers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBrowsersPagedCallable() 
  * listBrowsersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BrowserServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BrowserServiceSettings browserServiceSettings =
         BrowserServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BrowserServiceClient browserServiceClient = BrowserServiceClient.create(browserServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BrowserServiceSettings browserServiceSettings =
         BrowserServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     BrowserServiceClient browserServiceClient = BrowserServiceClient.create(browserServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BrowserServiceClient

## Static Methods 

### create()
    
    
    public static final BrowserServiceClient create()

Constructs an instance of BrowserServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BrowserServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BrowserServiceSettings settings)
    
    
    public static final BrowserServiceClient create(BrowserServiceSettings settings)

Constructs an instance of BrowserServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BrowserServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BrowserServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BrowserServiceStub stub)
    
    
    public static final BrowserServiceClient create(BrowserServiceStub stub)

Constructs an instance of BrowserServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(BrowserServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BrowserServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BrowserServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BrowserServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient)` |   
  
## Constructors 

### BrowserServiceClient(BrowserServiceSettings settings)
    
    
    protected BrowserServiceClient(BrowserServiceSettings settings)

Constructs an instance of BrowserServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BrowserServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceSettings)`  
  
  
### BrowserServiceClient(BrowserServiceStub stub)
    
    
    protected BrowserServiceClient(BrowserServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BrowserServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BrowserServiceStub)`  
  
  
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

### getBrowser(@Nullable BrowserName name)
    
    
    public final Browser getBrowser(@Nullable BrowserName name)

Retrieves a `Browser` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       BrowserName name = BrowserName.of("[NETWORK_CODE]", "[BROWSER]");
       Browser response = browserServiceClient.getBrowser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.BrowserName`  
Required. The resource name of the Browser. Format: `networks/{network_code}/browsers/{browser_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Browser](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Browser)` |   
  
### getBrowser(GetBrowserRequest request)
    
    
    public final Browser getBrowser(GetBrowserRequest request)

Retrieves a `Browser` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       GetBrowserRequest request =
           GetBrowserRequest.newBuilder()
               .setName(BrowserName.of("[NETWORK_CODE]", "[BROWSER]").toString())
               .build();
       Browser response = browserServiceClient.getBrowser(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBrowserRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetBrowserRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Browser](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Browser)` |   
  
### getBrowser(String name)
    
    
    public final Browser getBrowser(String name)

Retrieves a `Browser` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       String name = BrowserName.of("[NETWORK_CODE]", "[BROWSER]").toString();
       Browser response = browserServiceClient.getBrowser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Browser. Format: `networks/{network_code}/browsers/{browser_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Browser](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Browser)` |   
  
### getBrowserCallable()
    
    
    public final UnaryCallable<GetBrowserRequest,Browser> getBrowserCallable()

Retrieves a `Browser` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       GetBrowserRequest request =
           GetBrowserRequest.newBuilder()
               .setName(BrowserName.of("[NETWORK_CODE]", "[BROWSER]").toString())
               .build();
       ApiFuture<Browser> future = browserServiceClient.getBrowserCallable().futureCall(request);
       // Do something.
       Browser response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBrowserRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetBrowserRequest),[Browser](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Browser)>` |   
  
### getSettings()
    
    
    public final @Nullable BrowserServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.BrowserServiceSettings` |   
  
### getStub()
    
    
    public BrowserServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BrowserServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BrowserServiceStub)` |   
  
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
  
### listBrowsers(@Nullable NetworkName parent)
    
    
    public final BrowserServiceClient.ListBrowsersPagedResponse listBrowsers(@Nullable NetworkName parent)

Lists `Browser` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Browser element : browserServiceClient.listBrowsers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Browsers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[BrowserServiceClient.ListBrowsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient.ListBrowsersPagedResponse)` |   
  
### listBrowsers(ListBrowsersRequest request)
    
    
    public final BrowserServiceClient.ListBrowsersPagedResponse listBrowsers(ListBrowsersRequest request)

Lists `Browser` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       ListBrowsersRequest request =
           ListBrowsersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Browser element : browserServiceClient.listBrowsers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBrowsersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowsersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BrowserServiceClient.ListBrowsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient.ListBrowsersPagedResponse)` |   
  
### listBrowsers(String parent)
    
    
    public final BrowserServiceClient.ListBrowsersPagedResponse listBrowsers(String parent)

Lists `Browser` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Browser element : browserServiceClient.listBrowsers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Browsers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[BrowserServiceClient.ListBrowsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient.ListBrowsersPagedResponse)` |   
  
### listBrowsersCallable()
    
    
    public final UnaryCallable<ListBrowsersRequest,ListBrowsersResponse> listBrowsersCallable()

Lists `Browser` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       ListBrowsersRequest request =
           ListBrowsersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListBrowsersResponse response = browserServiceClient.listBrowsersCallable().call(request);
         for (Browser element : response.getBrowsersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBrowsersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowsersRequest),[ListBrowsersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowsersResponse)>` |   
  
### listBrowsersPagedCallable()
    
    
    public final UnaryCallable<ListBrowsersRequest,BrowserServiceClient.ListBrowsersPagedResponse> listBrowsersPagedCallable()

Lists `Browser` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserServiceClient browserServiceClient = BrowserServiceClient.create()) {
       ListBrowsersRequest request =
           ListBrowsersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Browser> future =
           browserServiceClient.listBrowsersPagedCallable().futureCall(request);
       // Do something.
       for (Browser element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBrowsersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowsersRequest),[ListBrowsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserServiceClient.ListBrowsersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
