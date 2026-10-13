---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient
title: Class TaxonomyCategoryServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:06.468686+00:00
---

# Class TaxonomyCategoryServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TaxonomyCategoryServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/TaxonomyCategoryServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `TaxonomyCategory` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       TaxonomyCategoryName name = TaxonomyCategoryName.of("[NETWORK_CODE]", "[TAXONOMY_CATEGORY]");
       TaxonomyCategory response = taxonomyCategoryServiceClient.getTaxonomyCategory(name);
     }
     

Note: close() needs to be called on the TaxonomyCategoryServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetTaxonomyCategory |  Retrieves a `TaxonomyCategory` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTaxonomyCategory(GetTaxonomyCategoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTaxonomyCategory(TaxonomyCategoryName name) 
  * getTaxonomyCategory(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTaxonomyCategoryCallable() 

  
ListTaxonomyCategories |  Lists `TaxonomyCategory` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTaxonomyCategories(ListTaxonomyCategoriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTaxonomyCategories(NetworkName parent) 
  * listTaxonomyCategories(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTaxonomyCategoriesPagedCallable() 
  * listTaxonomyCategoriesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TaxonomyCategoryServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TaxonomyCategoryServiceSettings taxonomyCategoryServiceSettings =
         TaxonomyCategoryServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create(taxonomyCategoryServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TaxonomyCategoryServiceSettings taxonomyCategoryServiceSettings =
         TaxonomyCategoryServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create(taxonomyCategoryServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TaxonomyCategoryServiceClient

## Static Methods 

### create()
    
    
    public static final TaxonomyCategoryServiceClient create()

Constructs an instance of TaxonomyCategoryServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategoryServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TaxonomyCategoryServiceSettings settings)
    
    
    public static final TaxonomyCategoryServiceClient create(TaxonomyCategoryServiceSettings settings)

Constructs an instance of TaxonomyCategoryServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TaxonomyCategoryServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategoryServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TaxonomyCategoryServiceStub stub)
    
    
    public static final TaxonomyCategoryServiceClient create(TaxonomyCategoryServiceStub stub)

Constructs an instance of TaxonomyCategoryServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(TaxonomyCategoryServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TaxonomyCategoryServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TaxonomyCategoryServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategoryServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient)` |   
  
## Constructors 

### TaxonomyCategoryServiceClient(TaxonomyCategoryServiceSettings settings)
    
    
    protected TaxonomyCategoryServiceClient(TaxonomyCategoryServiceSettings settings)

Constructs an instance of TaxonomyCategoryServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TaxonomyCategoryServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceSettings)`  
  
  
### TaxonomyCategoryServiceClient(TaxonomyCategoryServiceStub stub)
    
    
    protected TaxonomyCategoryServiceClient(TaxonomyCategoryServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TaxonomyCategoryServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TaxonomyCategoryServiceStub)`  
  
  
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
    
    
    public final @Nullable TaxonomyCategoryServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.TaxonomyCategoryServiceSettings` |   
  
### getStub()
    
    
    public TaxonomyCategoryServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategoryServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TaxonomyCategoryServiceStub)` |   
  
### getTaxonomyCategory(@Nullable TaxonomyCategoryName name)
    
    
    public final TaxonomyCategory getTaxonomyCategory(@Nullable TaxonomyCategoryName name)

Retrieves a `TaxonomyCategory` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       TaxonomyCategoryName name = TaxonomyCategoryName.of("[NETWORK_CODE]", "[TAXONOMY_CATEGORY]");
       TaxonomyCategory response = taxonomyCategoryServiceClient.getTaxonomyCategory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.TaxonomyCategoryName`  
Required. The resource name of the TaxonomyCategory. Format: `networks/{network_code}/taxonomyCategories/{taxonomy_category_id}`  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategory](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategory)` |   
  
### getTaxonomyCategory(GetTaxonomyCategoryRequest request)
    
    
    public final TaxonomyCategory getTaxonomyCategory(GetTaxonomyCategoryRequest request)

Retrieves a `TaxonomyCategory` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       GetTaxonomyCategoryRequest request =
           GetTaxonomyCategoryRequest.newBuilder()
               .setName(TaxonomyCategoryName.of("[NETWORK_CODE]", "[TAXONOMY_CATEGORY]").toString())
               .build();
       TaxonomyCategory response = taxonomyCategoryServiceClient.getTaxonomyCategory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTaxonomyCategoryRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetTaxonomyCategoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategory](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategory)` |   
  
### getTaxonomyCategory(String name)
    
    
    public final TaxonomyCategory getTaxonomyCategory(String name)

Retrieves a `TaxonomyCategory` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       String name = TaxonomyCategoryName.of("[NETWORK_CODE]", "[TAXONOMY_CATEGORY]").toString();
       TaxonomyCategory response = taxonomyCategoryServiceClient.getTaxonomyCategory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TaxonomyCategory. Format: `networks/{network_code}/taxonomyCategories/{taxonomy_category_id}`  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategory](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategory)` |   
  
### getTaxonomyCategoryCallable()
    
    
    public final UnaryCallable<GetTaxonomyCategoryRequest,TaxonomyCategory> getTaxonomyCategoryCallable()

Retrieves a `TaxonomyCategory` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       GetTaxonomyCategoryRequest request =
           GetTaxonomyCategoryRequest.newBuilder()
               .setName(TaxonomyCategoryName.of("[NETWORK_CODE]", "[TAXONOMY_CATEGORY]").toString())
               .build();
       ApiFuture<TaxonomyCategory> future =
           taxonomyCategoryServiceClient.getTaxonomyCategoryCallable().futureCall(request);
       // Do something.
       TaxonomyCategory response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTaxonomyCategoryRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetTaxonomyCategoryRequest),[TaxonomyCategory](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategory)>` |   
  
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
  
### listTaxonomyCategories(@Nullable NetworkName parent)
    
    
    public final TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse listTaxonomyCategories(@Nullable NetworkName parent)

Lists `TaxonomyCategory` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (TaxonomyCategory element :
           taxonomyCategoryServiceClient.listTaxonomyCategories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of TaxonomyCategories. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse)` |   
  
### listTaxonomyCategories(ListTaxonomyCategoriesRequest request)
    
    
    public final TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse listTaxonomyCategories(ListTaxonomyCategoriesRequest request)

Lists `TaxonomyCategory` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       ListTaxonomyCategoriesRequest request =
           ListTaxonomyCategoriesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (TaxonomyCategory element :
           taxonomyCategoryServiceClient.listTaxonomyCategories(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTaxonomyCategoriesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTaxonomyCategoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse)` |   
  
### listTaxonomyCategories(String parent)
    
    
    public final TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse listTaxonomyCategories(String parent)

Lists `TaxonomyCategory` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (TaxonomyCategory element :
           taxonomyCategoryServiceClient.listTaxonomyCategories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of TaxonomyCategories. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse)` |   
  
### listTaxonomyCategoriesCallable()
    
    
    public final UnaryCallable<ListTaxonomyCategoriesRequest,ListTaxonomyCategoriesResponse> listTaxonomyCategoriesCallable()

Lists `TaxonomyCategory` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       ListTaxonomyCategoriesRequest request =
           ListTaxonomyCategoriesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListTaxonomyCategoriesResponse response =
             taxonomyCategoryServiceClient.listTaxonomyCategoriesCallable().call(request);
         for (TaxonomyCategory element : response.getTaxonomyCategoriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTaxonomyCategoriesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTaxonomyCategoriesRequest),[ListTaxonomyCategoriesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTaxonomyCategoriesResponse)>` |   
  
### listTaxonomyCategoriesPagedCallable()
    
    
    public final UnaryCallable<ListTaxonomyCategoriesRequest,TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse> listTaxonomyCategoriesPagedCallable()

Lists `TaxonomyCategory` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TaxonomyCategoryServiceClient taxonomyCategoryServiceClient =
         TaxonomyCategoryServiceClient.create()) {
       ListTaxonomyCategoriesRequest request =
           ListTaxonomyCategoriesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<TaxonomyCategory> future =
           taxonomyCategoryServiceClient.listTaxonomyCategoriesPagedCallable().futureCall(request);
       // Do something.
       for (TaxonomyCategory element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTaxonomyCategoriesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTaxonomyCategoriesRequest),[ListTaxonomyCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TaxonomyCategoryServiceClient.ListTaxonomyCategoriesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
