---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient
title: Class SearchServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:44.962535+00:00
---

# Class SearchServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SearchServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/SearchServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for search.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setBranch(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setImageQuery(SearchRequest.ImageQuery.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setOneBoxPageSize(1988477988)
               .addAllDataStoreSpecs(new ArrayList<SearchRequest.DataStoreSpec>())
               .setNumResultsPerDataStore(397658288)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .setUserInfo(UserInfo.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .putAllParams(new HashMap<String, Value>())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setUserPseudoId("userPseudoId-1155274652")
               .setContentSearchSpec(SearchRequest.ContentSearchSpec.newBuilder().build())
               .setRankingExpression("rankingExpression2110320494")
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setNaturalLanguageQueryUnderstandingSpec(
                   SearchRequest.NaturalLanguageQueryUnderstandingSpec.newBuilder().build())
               .setSearchAsYouTypeSpec(SearchRequest.SearchAsYouTypeSpec.newBuilder().build())
               .setDisplaySpec(SearchRequest.DisplaySpec.newBuilder().build())
               .addAllCrowdingSpecs(new ArrayList<SearchRequest.CrowdingSpec>())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSessionSpec(SearchRequest.SessionSpec.newBuilder().build())
               .setRelevanceFilterSpec(SearchRequest.RelevanceFilterSpec.newBuilder().build())
               .setRelevanceScoreSpec(SearchRequest.RelevanceScoreSpec.newBuilder().build())
               .setSearchAddonSpec(SearchRequest.SearchAddonSpec.newBuilder().build())
               .setCustomRankingParams(SearchRequest.CustomRankingParams.newBuilder().build())
               .setEntity("entity-1298275357")
               .build();
       for (SearchResponse.SearchResult element : searchServiceClient.search(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

Note: close() needs to be called on the SearchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Search |  Performs a search. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * search(SearchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchPagedCallable() 
  * searchCallable() 

  
SearchLite |  Performs a search. Similar to the SearchService.Search method, but a lite version that allows API key for authentication, where OAuth and IAM checks are not required.  Only public website search is supported by this method. If data stores and engines not associated with public website search are specified, a `FAILED_PRECONDITION` error is returned.  This method can be used for easy onboarding without having to implement an authentication backend. However, it is strongly recommended to use SearchService.Search instead with required OAuth and IAM checks to provide better data security. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchLite(SearchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchLitePagedCallable() 
  * searchLiteCallable() 

  
  
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
`[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient)` |   
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
`settings` | `[SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient)` |   
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
`stub` | `[SearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SearchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient)` |   
  
## Constructors 

### SearchServiceClient(SearchServiceSettings settings)
    
    
    protected SearchServiceClient(SearchServiceSettings settings)

Constructs an instance of SearchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings)`  
  
  
### SearchServiceClient(SearchServiceStub stub)
    
    
    protected SearchServiceClient(SearchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SearchServiceStub)`  
  
  
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
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SearchServiceSettings` |   
  
### getStub()
    
    
    public SearchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SearchServiceStub)` |   
  
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

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setBranch(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setImageQuery(SearchRequest.ImageQuery.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setOneBoxPageSize(1988477988)
               .addAllDataStoreSpecs(new ArrayList<SearchRequest.DataStoreSpec>())
               .setNumResultsPerDataStore(397658288)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .setUserInfo(UserInfo.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .putAllParams(new HashMap<String, Value>())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setUserPseudoId("userPseudoId-1155274652")
               .setContentSearchSpec(SearchRequest.ContentSearchSpec.newBuilder().build())
               .setRankingExpression("rankingExpression2110320494")
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setNaturalLanguageQueryUnderstandingSpec(
                   SearchRequest.NaturalLanguageQueryUnderstandingSpec.newBuilder().build())
               .setSearchAsYouTypeSpec(SearchRequest.SearchAsYouTypeSpec.newBuilder().build())
               .setDisplaySpec(SearchRequest.DisplaySpec.newBuilder().build())
               .addAllCrowdingSpecs(new ArrayList<SearchRequest.CrowdingSpec>())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSessionSpec(SearchRequest.SessionSpec.newBuilder().build())
               .setRelevanceFilterSpec(SearchRequest.RelevanceFilterSpec.newBuilder().build())
               .setRelevanceScoreSpec(SearchRequest.RelevanceScoreSpec.newBuilder().build())
               .setSearchAddonSpec(SearchRequest.SearchAddonSpec.newBuilder().build())
               .setCustomRankingParams(SearchRequest.CustomRankingParams.newBuilder().build())
               .setEntity("entity-1298275357")
               .build();
       for (SearchResponse.SearchResult element : searchServiceClient.search(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient.SearchPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.SearchPagedResponse)` |   
  
### searchCallable()
    
    
    public final UnaryCallable<SearchRequest,SearchResponse> searchCallable()

Performs a search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setBranch(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setImageQuery(SearchRequest.ImageQuery.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setOneBoxPageSize(1988477988)
               .addAllDataStoreSpecs(new ArrayList<SearchRequest.DataStoreSpec>())
               .setNumResultsPerDataStore(397658288)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .setUserInfo(UserInfo.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .putAllParams(new HashMap<String, Value>())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setUserPseudoId("userPseudoId-1155274652")
               .setContentSearchSpec(SearchRequest.ContentSearchSpec.newBuilder().build())
               .setRankingExpression("rankingExpression2110320494")
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setNaturalLanguageQueryUnderstandingSpec(
                   SearchRequest.NaturalLanguageQueryUnderstandingSpec.newBuilder().build())
               .setSearchAsYouTypeSpec(SearchRequest.SearchAsYouTypeSpec.newBuilder().build())
               .setDisplaySpec(SearchRequest.DisplaySpec.newBuilder().build())
               .addAllCrowdingSpecs(new ArrayList<SearchRequest.CrowdingSpec>())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSessionSpec(SearchRequest.SessionSpec.newBuilder().build())
               .setRelevanceFilterSpec(SearchRequest.RelevanceFilterSpec.newBuilder().build())
               .setRelevanceScoreSpec(SearchRequest.RelevanceScoreSpec.newBuilder().build())
               .setSearchAddonSpec(SearchRequest.SearchAddonSpec.newBuilder().build())
               .setCustomRankingParams(SearchRequest.CustomRankingParams.newBuilder().build())
               .setEntity("entity-1298275357")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest),[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse)>` |   
  
### searchLite(SearchRequest request)
    
    
    public final SearchServiceClient.SearchLitePagedResponse searchLite(SearchRequest request)

Performs a search. Similar to the SearchService.Search method, but a lite version that allows API key for authentication, where OAuth and IAM checks are not required.

Only public website search is supported by this method. If data stores and engines not associated with public website search are specified, a `FAILED_PRECONDITION` error is returned.

This method can be used for easy onboarding without having to implement an authentication backend. However, it is strongly recommended to use SearchService.Search instead with required OAuth and IAM checks to provide better data security.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setBranch(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setImageQuery(SearchRequest.ImageQuery.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setOneBoxPageSize(1988477988)
               .addAllDataStoreSpecs(new ArrayList<SearchRequest.DataStoreSpec>())
               .setNumResultsPerDataStore(397658288)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .setUserInfo(UserInfo.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .putAllParams(new HashMap<String, Value>())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setUserPseudoId("userPseudoId-1155274652")
               .setContentSearchSpec(SearchRequest.ContentSearchSpec.newBuilder().build())
               .setRankingExpression("rankingExpression2110320494")
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setNaturalLanguageQueryUnderstandingSpec(
                   SearchRequest.NaturalLanguageQueryUnderstandingSpec.newBuilder().build())
               .setSearchAsYouTypeSpec(SearchRequest.SearchAsYouTypeSpec.newBuilder().build())
               .setDisplaySpec(SearchRequest.DisplaySpec.newBuilder().build())
               .addAllCrowdingSpecs(new ArrayList<SearchRequest.CrowdingSpec>())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSessionSpec(SearchRequest.SessionSpec.newBuilder().build())
               .setRelevanceFilterSpec(SearchRequest.RelevanceFilterSpec.newBuilder().build())
               .setRelevanceScoreSpec(SearchRequest.RelevanceScoreSpec.newBuilder().build())
               .setSearchAddonSpec(SearchRequest.SearchAddonSpec.newBuilder().build())
               .setCustomRankingParams(SearchRequest.CustomRankingParams.newBuilder().build())
               .setEntity("entity-1298275357")
               .build();
       for (SearchResponse.SearchResult element :
           searchServiceClient.searchLite(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient.SearchLitePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.SearchLitePagedResponse)` |   
  
### searchLiteCallable()
    
    
    public final UnaryCallable<SearchRequest,SearchResponse> searchLiteCallable()

Performs a search. Similar to the SearchService.Search method, but a lite version that allows API key for authentication, where OAuth and IAM checks are not required.

Only public website search is supported by this method. If data stores and engines not associated with public website search are specified, a `FAILED_PRECONDITION` error is returned.

This method can be used for easy onboarding without having to implement an authentication backend. However, it is strongly recommended to use SearchService.Search instead with required OAuth and IAM checks to provide better data security.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setBranch(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setImageQuery(SearchRequest.ImageQuery.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setOneBoxPageSize(1988477988)
               .addAllDataStoreSpecs(new ArrayList<SearchRequest.DataStoreSpec>())
               .setNumResultsPerDataStore(397658288)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .setUserInfo(UserInfo.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .putAllParams(new HashMap<String, Value>())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setUserPseudoId("userPseudoId-1155274652")
               .setContentSearchSpec(SearchRequest.ContentSearchSpec.newBuilder().build())
               .setRankingExpression("rankingExpression2110320494")
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setNaturalLanguageQueryUnderstandingSpec(
                   SearchRequest.NaturalLanguageQueryUnderstandingSpec.newBuilder().build())
               .setSearchAsYouTypeSpec(SearchRequest.SearchAsYouTypeSpec.newBuilder().build())
               .setDisplaySpec(SearchRequest.DisplaySpec.newBuilder().build())
               .addAllCrowdingSpecs(new ArrayList<SearchRequest.CrowdingSpec>())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSessionSpec(SearchRequest.SessionSpec.newBuilder().build())
               .setRelevanceFilterSpec(SearchRequest.RelevanceFilterSpec.newBuilder().build())
               .setRelevanceScoreSpec(SearchRequest.RelevanceScoreSpec.newBuilder().build())
               .setSearchAddonSpec(SearchRequest.SearchAddonSpec.newBuilder().build())
               .setCustomRankingParams(SearchRequest.CustomRankingParams.newBuilder().build())
               .setEntity("entity-1298275357")
               .build();
       while (true) {
         SearchResponse response = searchServiceClient.searchLiteCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest),[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse)>` |   
  
### searchLitePagedCallable()
    
    
    public final UnaryCallable<SearchRequest,SearchServiceClient.SearchLitePagedResponse> searchLitePagedCallable()

Performs a search. Similar to the SearchService.Search method, but a lite version that allows API key for authentication, where OAuth and IAM checks are not required.

Only public website search is supported by this method. If data stores and engines not associated with public website search are specified, a `FAILED_PRECONDITION` error is returned.

This method can be used for easy onboarding without having to implement an authentication backend. However, it is strongly recommended to use SearchService.Search instead with required OAuth and IAM checks to provide better data security.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setBranch(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setImageQuery(SearchRequest.ImageQuery.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setOneBoxPageSize(1988477988)
               .addAllDataStoreSpecs(new ArrayList<SearchRequest.DataStoreSpec>())
               .setNumResultsPerDataStore(397658288)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .setUserInfo(UserInfo.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .putAllParams(new HashMap<String, Value>())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setUserPseudoId("userPseudoId-1155274652")
               .setContentSearchSpec(SearchRequest.ContentSearchSpec.newBuilder().build())
               .setRankingExpression("rankingExpression2110320494")
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setNaturalLanguageQueryUnderstandingSpec(
                   SearchRequest.NaturalLanguageQueryUnderstandingSpec.newBuilder().build())
               .setSearchAsYouTypeSpec(SearchRequest.SearchAsYouTypeSpec.newBuilder().build())
               .setDisplaySpec(SearchRequest.DisplaySpec.newBuilder().build())
               .addAllCrowdingSpecs(new ArrayList<SearchRequest.CrowdingSpec>())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSessionSpec(SearchRequest.SessionSpec.newBuilder().build())
               .setRelevanceFilterSpec(SearchRequest.RelevanceFilterSpec.newBuilder().build())
               .setRelevanceScoreSpec(SearchRequest.RelevanceScoreSpec.newBuilder().build())
               .setSearchAddonSpec(SearchRequest.SearchAddonSpec.newBuilder().build())
               .setCustomRankingParams(SearchRequest.CustomRankingParams.newBuilder().build())
               .setEntity("entity-1298275357")
               .build();
       ApiFuture<SearchResponse.SearchResult> future =
           searchServiceClient.searchLitePagedCallable().futureCall(request);
       // Do something.
       for (SearchResponse.SearchResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest),[SearchLitePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.SearchLitePagedResponse)>` |   
  
### searchPagedCallable()
    
    
    public final UnaryCallable<SearchRequest,SearchServiceClient.SearchPagedResponse> searchPagedCallable()

Performs a search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchServiceClient searchServiceClient = SearchServiceClient.create()) {
       SearchRequest request =
           SearchRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setBranch(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setImageQuery(SearchRequest.ImageQuery.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOffset(-1019779949)
               .setOneBoxPageSize(1988477988)
               .addAllDataStoreSpecs(new ArrayList<SearchRequest.DataStoreSpec>())
               .setNumResultsPerDataStore(397658288)
               .setFilter("filter-1274492040")
               .setCanonicalFilter("canonicalFilter-722283124")
               .setOrderBy("orderBy-1207110587")
               .setUserInfo(UserInfo.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .addAllFacetSpecs(new ArrayList<SearchRequest.FacetSpec>())
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .putAllParams(new HashMap<String, Value>())
               .setQueryExpansionSpec(SearchRequest.QueryExpansionSpec.newBuilder().build())
               .setSpellCorrectionSpec(SearchRequest.SpellCorrectionSpec.newBuilder().build())
               .setUserPseudoId("userPseudoId-1155274652")
               .setContentSearchSpec(SearchRequest.ContentSearchSpec.newBuilder().build())
               .setRankingExpression("rankingExpression2110320494")
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setNaturalLanguageQueryUnderstandingSpec(
                   SearchRequest.NaturalLanguageQueryUnderstandingSpec.newBuilder().build())
               .setSearchAsYouTypeSpec(SearchRequest.SearchAsYouTypeSpec.newBuilder().build())
               .setDisplaySpec(SearchRequest.DisplaySpec.newBuilder().build())
               .addAllCrowdingSpecs(new ArrayList<SearchRequest.CrowdingSpec>())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSessionSpec(SearchRequest.SessionSpec.newBuilder().build())
               .setRelevanceFilterSpec(SearchRequest.RelevanceFilterSpec.newBuilder().build())
               .setRelevanceScoreSpec(SearchRequest.RelevanceScoreSpec.newBuilder().build())
               .setSearchAddonSpec(SearchRequest.SearchAddonSpec.newBuilder().build())
               .setCustomRankingParams(SearchRequest.CustomRankingParams.newBuilder().build())
               .setEntity("entity-1298275357")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest),[SearchPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.SearchPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
