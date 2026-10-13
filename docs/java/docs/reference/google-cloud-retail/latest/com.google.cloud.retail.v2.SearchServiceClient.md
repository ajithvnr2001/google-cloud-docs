---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient
title: Class SearchServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:24.987445+00:00
---

# Class SearchServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SearchServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/SearchServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setPlacement("placement1792938725")
               .setBranch(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setQuery("query107944136")
               .setVisitorId("visitorId1880545833")
               .setUserInfo(UserInfo.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setDynamicFacetSpec(SearchRequest.DynamicFacetSpec.newBuilder().build())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .addAllVariantRollupKeys(new ArrayList<String>())
               .addAllPageCategories(new ArrayList<String>())
               .setPersonalizationSpec(SearchRequest.PersonalizationSpec.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setEntity("entity-1298275357")
               .setConversationalSearchSpec(
                   SearchRequest.ConversationalSearchSpec.newBuilder().build())
               .setTileNavigationSpec(SearchRequest.TileNavigationSpec.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setRegionCode("regionCode-1991004415")
               .setPlaceId("placeId-494224254")
               .putAllUserAttributes(new HashMap<String, StringList>())
               .build();
       for (SearchResponse.SearchResult element : searchServiceClient.search(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

Note: close() needs to be called on the SearchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Search |  Performs a search.  This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * search(SearchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchPagedCallable() 
  * searchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SearchServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SearchServiceSettings searchServiceSettings =
         SearchServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SearchServiceClient searchServiceClient = SearchServiceClient.create(searchServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SearchServiceSettings searchServiceSettings =
         SearchServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SearchServiceClient searchServiceClient = SearchServiceClient.create(searchServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SearchServiceSettings searchServiceSettings =
         SearchServiceSettings.newHttpJsonBuilder().build();
     SearchServiceClient searchServiceClient = SearchServiceClient.create(searchServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SearchServiceClient

## Static Methods 

### create()
    
    
    public static final SearchServiceClient create()

Constructs an instance of SearchServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SearchServiceSettings settings)
    
    
    public static final SearchServiceClient create(SearchServiceSettings settings)

Constructs an instance of SearchServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SearchServiceStub stub)
    
    
    public static final SearchServiceClient create(SearchServiceStub stub)

Constructs an instance of SearchServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SearchServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.SearchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient)` |   
  
## Constructors 

### SearchServiceClient(SearchServiceSettings settings)
    
    
    protected SearchServiceClient(SearchServiceSettings settings)

Constructs an instance of SearchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceSettings)`  
  
  
### SearchServiceClient(SearchServiceStub stub)
    
    
    protected SearchServiceClient(SearchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.SearchServiceStub)`  
  
  
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
    
    
    public final @Nullable SearchServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.SearchServiceSettings` |   
  
### getStub()
    
    
    public SearchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.SearchServiceStub)` |   
  
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
  
### search(SearchRequest request)
    
    
    public final SearchServiceClient.SearchPagedResponse search(SearchRequest request)

Performs a search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setPlacement("placement1792938725")
               .setBranch(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setQuery("query107944136")
               .setVisitorId("visitorId1880545833")
               .setUserInfo(UserInfo.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setDynamicFacetSpec(SearchRequest.DynamicFacetSpec.newBuilder().build())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .addAllVariantRollupKeys(new ArrayList<String>())
               .addAllPageCategories(new ArrayList<String>())
               .setPersonalizationSpec(SearchRequest.PersonalizationSpec.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setEntity("entity-1298275357")
               .setConversationalSearchSpec(
                   SearchRequest.ConversationalSearchSpec.newBuilder().build())
               .setTileNavigationSpec(SearchRequest.TileNavigationSpec.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setRegionCode("regionCode-1991004415")
               .setPlaceId("placeId-494224254")
               .putAllUserAttributes(new HashMap<String, StringList>())
               .build();
       for (SearchResponse.SearchResult element : searchServiceClient.search(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient.SearchPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.SearchPagedResponse)` |   
  
### searchCallable()
    
    
    public final UnaryCallable<SearchRequest,SearchResponse> searchCallable()

Performs a search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setPlacement("placement1792938725")
               .setBranch(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setQuery("query107944136")
               .setVisitorId("visitorId1880545833")
               .setUserInfo(UserInfo.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setDynamicFacetSpec(SearchRequest.DynamicFacetSpec.newBuilder().build())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .addAllVariantRollupKeys(new ArrayList<String>())
               .addAllPageCategories(new ArrayList<String>())
               .setPersonalizationSpec(SearchRequest.PersonalizationSpec.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setEntity("entity-1298275357")
               .setConversationalSearchSpec(
                   SearchRequest.ConversationalSearchSpec.newBuilder().build())
               .setTileNavigationSpec(SearchRequest.TileNavigationSpec.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setRegionCode("regionCode-1991004415")
               .setPlaceId("placeId-494224254")
               .putAllUserAttributes(new HashMap<String, StringList>())
               .build();
       while (true) {
         SearchResponse response = searchServiceClient.searchCallable().call(request);
         for (SearchResponse.SearchResult element : response.getResultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest),[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse)>` |   
  
### searchPagedCallable()
    
    
    public final UnaryCallable<SearchRequest,SearchServiceClient.SearchPagedResponse> searchPagedCallable()

Performs a search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setPlacement("placement1792938725")
               .setBranch(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setQuery("query107944136")
               .setVisitorId("visitorId1880545833")
               .setUserInfo(UserInfo.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setDynamicFacetSpec(SearchRequest.DynamicFacetSpec.newBuilder().build())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .addAllVariantRollupKeys(new ArrayList<String>())
               .addAllPageCategories(new ArrayList<String>())
               .setPersonalizationSpec(SearchRequest.PersonalizationSpec.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setEntity("entity-1298275357")
               .setConversationalSearchSpec(
                   SearchRequest.ConversationalSearchSpec.newBuilder().build())
               .setTileNavigationSpec(SearchRequest.TileNavigationSpec.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setRegionCode("regionCode-1991004415")
               .setPlaceId("placeId-494224254")
               .putAllUserAttributes(new HashMap<String, StringList>())
               .build();
       ApiFuture<SearchResponse.SearchResult> future =
           searchServiceClient.searchPagedCallable().futureCall(request);
       // Do something.
       for (SearchResponse.SearchResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest),[SearchPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.SearchPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
