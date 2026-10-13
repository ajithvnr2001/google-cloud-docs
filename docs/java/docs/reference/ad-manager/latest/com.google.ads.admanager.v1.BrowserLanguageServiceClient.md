---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient
title: Class BrowserLanguageServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:28.859543+00:00
---

# Class BrowserLanguageServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BrowserLanguageServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/BrowserLanguageServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `BrowserLanguage` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       BrowserLanguageName name = BrowserLanguageName.of("[NETWORK_CODE]", "[BROWSER_LANGUAGE]");
       BrowserLanguage response = browserLanguageServiceClient.getBrowserLanguage(name);
     }
     

Note: close() needs to be called on the BrowserLanguageServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetBrowserLanguage |  Retrieves a `BrowserLanguage` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBrowserLanguage(GetBrowserLanguageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBrowserLanguage(BrowserLanguageName name) 
  * getBrowserLanguage(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBrowserLanguageCallable() 

  
ListBrowserLanguages |  Lists `BrowserLanguage` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBrowserLanguages(ListBrowserLanguagesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBrowserLanguages(NetworkName parent) 
  * listBrowserLanguages(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBrowserLanguagesPagedCallable() 
  * listBrowserLanguagesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BrowserLanguageServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BrowserLanguageServiceSettings browserLanguageServiceSettings =
         BrowserLanguageServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create(browserLanguageServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BrowserLanguageServiceSettings browserLanguageServiceSettings =
         BrowserLanguageServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create(browserLanguageServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BrowserLanguageServiceClient

## Static Methods 

### create()
    
    
    public static final BrowserLanguageServiceClient create()

Constructs an instance of BrowserLanguageServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BrowserLanguageServiceSettings settings)
    
    
    public static final BrowserLanguageServiceClient create(BrowserLanguageServiceSettings settings)

Constructs an instance of BrowserLanguageServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BrowserLanguageServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BrowserLanguageServiceStub stub)
    
    
    public static final BrowserLanguageServiceClient create(BrowserLanguageServiceStub stub)

Constructs an instance of BrowserLanguageServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(BrowserLanguageServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BrowserLanguageServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BrowserLanguageServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient)` |   
  
## Constructors 

### BrowserLanguageServiceClient(BrowserLanguageServiceSettings settings)
    
    
    protected BrowserLanguageServiceClient(BrowserLanguageServiceSettings settings)

Constructs an instance of BrowserLanguageServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BrowserLanguageServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceSettings)`  
  
  
### BrowserLanguageServiceClient(BrowserLanguageServiceStub stub)
    
    
    protected BrowserLanguageServiceClient(BrowserLanguageServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BrowserLanguageServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BrowserLanguageServiceStub)`  
  
  
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

### getBrowserLanguage(@Nullable BrowserLanguageName name)
    
    
    public final BrowserLanguage getBrowserLanguage(@Nullable BrowserLanguageName name)

Retrieves a `BrowserLanguage` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       BrowserLanguageName name = BrowserLanguageName.of("[NETWORK_CODE]", "[BROWSER_LANGUAGE]");
       BrowserLanguage response = browserLanguageServiceClient.getBrowserLanguage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.BrowserLanguageName`  
Required. The resource name of the BrowserLanguage. Format: `networks/{network_code}/browserLanguages/{browser_language_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguage](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguage)` |   
  
### getBrowserLanguage(GetBrowserLanguageRequest request)
    
    
    public final BrowserLanguage getBrowserLanguage(GetBrowserLanguageRequest request)

Retrieves a `BrowserLanguage` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       GetBrowserLanguageRequest request =
           GetBrowserLanguageRequest.newBuilder()
               .setName(BrowserLanguageName.of("[NETWORK_CODE]", "[BROWSER_LANGUAGE]").toString())
               .build();
       BrowserLanguage response = browserLanguageServiceClient.getBrowserLanguage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBrowserLanguageRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetBrowserLanguageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguage](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguage)` |   
  
### getBrowserLanguage(String name)
    
    
    public final BrowserLanguage getBrowserLanguage(String name)

Retrieves a `BrowserLanguage` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       String name = BrowserLanguageName.of("[NETWORK_CODE]", "[BROWSER_LANGUAGE]").toString();
       BrowserLanguage response = browserLanguageServiceClient.getBrowserLanguage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the BrowserLanguage. Format: `networks/{network_code}/browserLanguages/{browser_language_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguage](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguage)` |   
  
### getBrowserLanguageCallable()
    
    
    public final UnaryCallable<GetBrowserLanguageRequest,BrowserLanguage> getBrowserLanguageCallable()

Retrieves a `BrowserLanguage` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       GetBrowserLanguageRequest request =
           GetBrowserLanguageRequest.newBuilder()
               .setName(BrowserLanguageName.of("[NETWORK_CODE]", "[BROWSER_LANGUAGE]").toString())
               .build();
       ApiFuture<BrowserLanguage> future =
           browserLanguageServiceClient.getBrowserLanguageCallable().futureCall(request);
       // Do something.
       BrowserLanguage response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBrowserLanguageRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetBrowserLanguageRequest),[BrowserLanguage](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguage)>` |   
  
### getSettings()
    
    
    public final @Nullable BrowserLanguageServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.BrowserLanguageServiceSettings` |   
  
### getStub()
    
    
    public BrowserLanguageServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguageServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BrowserLanguageServiceStub)` |   
  
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
  
### listBrowserLanguages(@Nullable NetworkName parent)
    
    
    public final BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse listBrowserLanguages(@Nullable NetworkName parent)

Lists `BrowserLanguage` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (BrowserLanguage element :
           browserLanguageServiceClient.listBrowserLanguages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of BrowserLanguages. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse)` |   
  
### listBrowserLanguages(ListBrowserLanguagesRequest request)
    
    
    public final BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse listBrowserLanguages(ListBrowserLanguagesRequest request)

Lists `BrowserLanguage` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       ListBrowserLanguagesRequest request =
           ListBrowserLanguagesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (BrowserLanguage element :
           browserLanguageServiceClient.listBrowserLanguages(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBrowserLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowserLanguagesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse)` |   
  
### listBrowserLanguages(String parent)
    
    
    public final BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse listBrowserLanguages(String parent)

Lists `BrowserLanguage` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (BrowserLanguage element :
           browserLanguageServiceClient.listBrowserLanguages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of BrowserLanguages. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse)` |   
  
### listBrowserLanguagesCallable()
    
    
    public final UnaryCallable<ListBrowserLanguagesRequest,ListBrowserLanguagesResponse> listBrowserLanguagesCallable()

Lists `BrowserLanguage` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       ListBrowserLanguagesRequest request =
           ListBrowserLanguagesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListBrowserLanguagesResponse response =
             browserLanguageServiceClient.listBrowserLanguagesCallable().call(request);
         for (BrowserLanguage element : response.getBrowserLanguagesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBrowserLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowserLanguagesRequest),[ListBrowserLanguagesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowserLanguagesResponse)>` |   
  
### listBrowserLanguagesPagedCallable()
    
    
    public final UnaryCallable<ListBrowserLanguagesRequest,BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse> listBrowserLanguagesPagedCallable()

Lists `BrowserLanguage` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BrowserLanguageServiceClient browserLanguageServiceClient =
         BrowserLanguageServiceClient.create()) {
       ListBrowserLanguagesRequest request =
           ListBrowserLanguagesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<BrowserLanguage> future =
           browserLanguageServiceClient.listBrowserLanguagesPagedCallable().futureCall(request);
       // Do something.
       for (BrowserLanguage element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBrowserLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBrowserLanguagesRequest),[ListBrowserLanguagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BrowserLanguageServiceClient.ListBrowserLanguagesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
