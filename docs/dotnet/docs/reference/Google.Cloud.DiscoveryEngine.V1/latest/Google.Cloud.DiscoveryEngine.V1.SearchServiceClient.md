---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient
title: Discovery Engine v1 API - Class SearchServiceClient (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:47.135118+00:00
---

# Discovery Engine v1 API - Class SearchServiceClient (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class SearchServiceClient (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public abstract class SearchServiceClient

Reference documentation and code samples for the Discovery Engine v1 API class SearchServiceClient.

SearchService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[SearchServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClientImpl)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Remarks

Service for search.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the SearchService service, which is a host of "discoveryengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default SearchService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default SearchService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/discoveryengine.assist.readwrite>
  * <https://www.googleapis.com/auth/discoveryengine.readwrite>
  * <https://www.googleapis.com/auth/discoveryengine.serving.readwrite>



### GrpcClient
    
    
    public virtual SearchService.SearchServiceClient GrpcClient { get; }

The underlying gRPC SearchService client

**Property Value**  
---  
**Type** | **Description**  
`[SearchService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchService)[SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchService.SearchServiceClient)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static SearchServiceClient Create()

Synchronously creates a [SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SearchServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient)` | The created [SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<SearchServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SearchServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient)` | The task representing the created [SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient).  
  
### Search(SearchRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchResponse, SearchResponse.Types.SearchResult> Search(SearchRequest request, CallSettings callSettings = null)

Performs a search.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult)` | A pageable sequence of [SearchResponse.Types.SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult) resources.  
**Example**
    
    
    // Create client
    SearchServiceClient searchServiceClient = SearchServiceClient.Create();
    // Initialize request argument(s)
    SearchRequest request = new SearchRequest
    {
        ServingConfigAsServingConfigName = ServingConfigName.FromProjectLocationDataStoreServingConfig("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"),
        BranchAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Query = "",
        Offset = 0,
        Filter = "",
        OrderBy = "",
        FacetSpecs =
        {
            new SearchRequest.Types.FacetSpec(),
        },
        BoostSpec = new SearchRequest.Types.BoostSpec(),
        Params = { { "", new Value() }, },
        QueryExpansionSpec = new SearchRequest.Types.QueryExpansionSpec(),
        SpellCorrectionSpec = new SearchRequest.Types.SpellCorrectionSpec(),
        UserPseudoId = "",
        ImageQuery = new SearchRequest.Types.ImageQuery(),
        SafeSearch = false,
        UserInfo = new UserInfo(),
        UserLabels = { { "", "" }, },
        ContentSearchSpec = new SearchRequest.Types.ContentSearchSpec(),
        RankingExpression = "",
        NaturalLanguageQueryUnderstandingSpec = new SearchRequest.Types.NaturalLanguageQueryUnderstandingSpec(),
        CanonicalFilter = "",
        SearchAsYouTypeSpec = new SearchRequest.Types.SearchAsYouTypeSpec(),
        DataStoreSpecs =
        {
            new SearchRequest.Types.DataStoreSpec(),
        },
        LanguageCode = "",
        DisplaySpec = new SearchRequest.Types.DisplaySpec(),
        CrowdingSpecs =
        {
            new SearchRequest.Types.CrowdingSpec(),
        },
        SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"),
        SessionSpec = new SearchRequest.Types.SessionSpec(),
        RelevanceThreshold = SearchRequest.Types.RelevanceThreshold.Unspecified,
        OneBoxPageSize = 0,
        RelevanceScoreSpec = new SearchRequest.Types.RelevanceScoreSpec(),
        RankingExpressionBackend = SearchRequest.Types.RankingExpressionBackend.Unspecified,
        SearchAddonSpec = new SearchRequest.Types.SearchAddonSpec(),
        PageCategories = { "", },
        CustomRankingParams = new SearchRequest.Types.CustomRankingParams(),
        NumResultsPerDataStore = 0,
        Entity = "",
        RelevanceFilterSpec = new SearchRequest.Types.RelevanceFilterSpec(),
    };
    // Make the request
    PagedEnumerable<SearchResponse, SearchResponse.Types.SearchResult> response = searchServiceClient.Search(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SearchResponse.Types.SearchResult item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SearchResponse.Types.SearchResult item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SearchResponse.Types.SearchResult> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SearchResponse.Types.SearchResult item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchAsync(SearchRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchResponse, SearchResponse.Types.SearchResult> SearchAsync(SearchRequest request, CallSettings callSettings = null)

Performs a search.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult)` | A pageable asynchronous sequence of [SearchResponse.Types.SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult) resources.  
**Example**
    
    
    // Create client
    SearchServiceClient searchServiceClient = await SearchServiceClient.CreateAsync();
    // Initialize request argument(s)
    SearchRequest request = new SearchRequest
    {
        ServingConfigAsServingConfigName = ServingConfigName.FromProjectLocationDataStoreServingConfig("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"),
        BranchAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Query = "",
        Offset = 0,
        Filter = "",
        OrderBy = "",
        FacetSpecs =
        {
            new SearchRequest.Types.FacetSpec(),
        },
        BoostSpec = new SearchRequest.Types.BoostSpec(),
        Params = { { "", new Value() }, },
        QueryExpansionSpec = new SearchRequest.Types.QueryExpansionSpec(),
        SpellCorrectionSpec = new SearchRequest.Types.SpellCorrectionSpec(),
        UserPseudoId = "",
        ImageQuery = new SearchRequest.Types.ImageQuery(),
        SafeSearch = false,
        UserInfo = new UserInfo(),
        UserLabels = { { "", "" }, },
        ContentSearchSpec = new SearchRequest.Types.ContentSearchSpec(),
        RankingExpression = "",
        NaturalLanguageQueryUnderstandingSpec = new SearchRequest.Types.NaturalLanguageQueryUnderstandingSpec(),
        CanonicalFilter = "",
        SearchAsYouTypeSpec = new SearchRequest.Types.SearchAsYouTypeSpec(),
        DataStoreSpecs =
        {
            new SearchRequest.Types.DataStoreSpec(),
        },
        LanguageCode = "",
        DisplaySpec = new SearchRequest.Types.DisplaySpec(),
        CrowdingSpecs =
        {
            new SearchRequest.Types.CrowdingSpec(),
        },
        SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"),
        SessionSpec = new SearchRequest.Types.SessionSpec(),
        RelevanceThreshold = SearchRequest.Types.RelevanceThreshold.Unspecified,
        OneBoxPageSize = 0,
        RelevanceScoreSpec = new SearchRequest.Types.RelevanceScoreSpec(),
        RankingExpressionBackend = SearchRequest.Types.RankingExpressionBackend.Unspecified,
        SearchAddonSpec = new SearchRequest.Types.SearchAddonSpec(),
        PageCategories = { "", },
        CustomRankingParams = new SearchRequest.Types.CustomRankingParams(),
        NumResultsPerDataStore = 0,
        Entity = "",
        RelevanceFilterSpec = new SearchRequest.Types.RelevanceFilterSpec(),
    };
    // Make the request
    PagedAsyncEnumerable<SearchResponse, SearchResponse.Types.SearchResult> response = searchServiceClient.SearchAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SearchResponse.Types.SearchResult item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SearchResponse.Types.SearchResult item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SearchResponse.Types.SearchResult> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SearchResponse.Types.SearchResult item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchLite(SearchRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchResponse, SearchResponse.Types.SearchResult> SearchLite(SearchRequest request, CallSettings callSettings = null)

Performs a search. Similar to the [SearchService.Search][google.cloud.discoveryengine.v1.SearchService.Search] method, but a lite version that allows API key for authentication, where OAuth and IAM checks are not required.

Only public website search is supported by this method. If data stores and engines not associated with public website search are specified, a `FAILED_PRECONDITION` error is returned.

This method can be used for easy onboarding without having to implement an authentication backend. However, it is strongly recommended to use [SearchService.Search][google.cloud.discoveryengine.v1.SearchService.Search] instead with required OAuth and IAM checks to provide better data security.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult)` | A pageable sequence of [SearchResponse.Types.SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult) resources.  
**Example**
    
    
    // Create client
    SearchServiceClient searchServiceClient = SearchServiceClient.Create();
    // Initialize request argument(s)
    SearchRequest request = new SearchRequest
    {
        ServingConfigAsServingConfigName = ServingConfigName.FromProjectLocationDataStoreServingConfig("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"),
        BranchAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Query = "",
        Offset = 0,
        Filter = "",
        OrderBy = "",
        FacetSpecs =
        {
            new SearchRequest.Types.FacetSpec(),
        },
        BoostSpec = new SearchRequest.Types.BoostSpec(),
        Params = { { "", new Value() }, },
        QueryExpansionSpec = new SearchRequest.Types.QueryExpansionSpec(),
        SpellCorrectionSpec = new SearchRequest.Types.SpellCorrectionSpec(),
        UserPseudoId = "",
        ImageQuery = new SearchRequest.Types.ImageQuery(),
        SafeSearch = false,
        UserInfo = new UserInfo(),
        UserLabels = { { "", "" }, },
        ContentSearchSpec = new SearchRequest.Types.ContentSearchSpec(),
        RankingExpression = "",
        NaturalLanguageQueryUnderstandingSpec = new SearchRequest.Types.NaturalLanguageQueryUnderstandingSpec(),
        CanonicalFilter = "",
        SearchAsYouTypeSpec = new SearchRequest.Types.SearchAsYouTypeSpec(),
        DataStoreSpecs =
        {
            new SearchRequest.Types.DataStoreSpec(),
        },
        LanguageCode = "",
        DisplaySpec = new SearchRequest.Types.DisplaySpec(),
        CrowdingSpecs =
        {
            new SearchRequest.Types.CrowdingSpec(),
        },
        SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"),
        SessionSpec = new SearchRequest.Types.SessionSpec(),
        RelevanceThreshold = SearchRequest.Types.RelevanceThreshold.Unspecified,
        OneBoxPageSize = 0,
        RelevanceScoreSpec = new SearchRequest.Types.RelevanceScoreSpec(),
        RankingExpressionBackend = SearchRequest.Types.RankingExpressionBackend.Unspecified,
        SearchAddonSpec = new SearchRequest.Types.SearchAddonSpec(),
        PageCategories = { "", },
        CustomRankingParams = new SearchRequest.Types.CustomRankingParams(),
        NumResultsPerDataStore = 0,
        Entity = "",
        RelevanceFilterSpec = new SearchRequest.Types.RelevanceFilterSpec(),
    };
    // Make the request
    PagedEnumerable<SearchResponse, SearchResponse.Types.SearchResult> response = searchServiceClient.SearchLite(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SearchResponse.Types.SearchResult item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SearchResponse.Types.SearchResult item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SearchResponse.Types.SearchResult> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SearchResponse.Types.SearchResult item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchLiteAsync(SearchRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchResponse, SearchResponse.Types.SearchResult> SearchLiteAsync(SearchRequest request, CallSettings callSettings = null)

Performs a search. Similar to the [SearchService.Search][google.cloud.discoveryengine.v1.SearchService.Search] method, but a lite version that allows API key for authentication, where OAuth and IAM checks are not required.

Only public website search is supported by this method. If data stores and engines not associated with public website search are specified, a `FAILED_PRECONDITION` error is returned.

This method can be used for easy onboarding without having to implement an authentication backend. However, it is strongly recommended to use [SearchService.Search][google.cloud.discoveryengine.v1.SearchService.Search] instead with required OAuth and IAM checks to provide better data security.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult)` | A pageable asynchronous sequence of [SearchResponse.Types.SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult) resources.  
**Example**
    
    
    // Create client
    SearchServiceClient searchServiceClient = await SearchServiceClient.CreateAsync();
    // Initialize request argument(s)
    SearchRequest request = new SearchRequest
    {
        ServingConfigAsServingConfigName = ServingConfigName.FromProjectLocationDataStoreServingConfig("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"),
        BranchAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Query = "",
        Offset = 0,
        Filter = "",
        OrderBy = "",
        FacetSpecs =
        {
            new SearchRequest.Types.FacetSpec(),
        },
        BoostSpec = new SearchRequest.Types.BoostSpec(),
        Params = { { "", new Value() }, },
        QueryExpansionSpec = new SearchRequest.Types.QueryExpansionSpec(),
        SpellCorrectionSpec = new SearchRequest.Types.SpellCorrectionSpec(),
        UserPseudoId = "",
        ImageQuery = new SearchRequest.Types.ImageQuery(),
        SafeSearch = false,
        UserInfo = new UserInfo(),
        UserLabels = { { "", "" }, },
        ContentSearchSpec = new SearchRequest.Types.ContentSearchSpec(),
        RankingExpression = "",
        NaturalLanguageQueryUnderstandingSpec = new SearchRequest.Types.NaturalLanguageQueryUnderstandingSpec(),
        CanonicalFilter = "",
        SearchAsYouTypeSpec = new SearchRequest.Types.SearchAsYouTypeSpec(),
        DataStoreSpecs =
        {
            new SearchRequest.Types.DataStoreSpec(),
        },
        LanguageCode = "",
        DisplaySpec = new SearchRequest.Types.DisplaySpec(),
        CrowdingSpecs =
        {
            new SearchRequest.Types.CrowdingSpec(),
        },
        SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"),
        SessionSpec = new SearchRequest.Types.SessionSpec(),
        RelevanceThreshold = SearchRequest.Types.RelevanceThreshold.Unspecified,
        OneBoxPageSize = 0,
        RelevanceScoreSpec = new SearchRequest.Types.RelevanceScoreSpec(),
        RankingExpressionBackend = SearchRequest.Types.RankingExpressionBackend.Unspecified,
        SearchAddonSpec = new SearchRequest.Types.SearchAddonSpec(),
        PageCategories = { "", },
        CustomRankingParams = new SearchRequest.Types.CustomRankingParams(),
        NumResultsPerDataStore = 0,
        Entity = "",
        RelevanceFilterSpec = new SearchRequest.Types.RelevanceFilterSpec(),
    };
    // Make the request
    PagedAsyncEnumerable<SearchResponse, SearchResponse.Types.SearchResult> response = searchServiceClient.SearchLiteAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SearchResponse.Types.SearchResult item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SearchResponse.Types.SearchResult item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SearchResponse.Types.SearchResult> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SearchResponse.Types.SearchResult item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
