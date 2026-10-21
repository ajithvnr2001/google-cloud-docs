---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results/
title: Get search results \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:05.548507+00:00
---

# Get search results  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Get search results Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to preview search results using the Google Cloud console and get search results using the API.

**Note:** For information about getting search results for media apps, see [Get search results for media](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-media-search-results).

Also, instead of creating a [search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget) to add to your web page, you can make API calls and integrate those calls into your server or application. This page includes code samples for how to make search queries using the gRPC client libraries with a service account.

**Note:** Depending on the amount of data, it can take hours after data ingestion to generate a preview.

## Exact match with double quotation marks

You can enclose a search query in double quotation marks (`""`) for an _exact match_. Such a type of search is often called a _quoted_ search.

If you don't enclose the search query in double quotation marks, the search is said to be for a _partial match_. Such a type of search is also called an _unquoted_ search.

For example, when your search query is `"query": "\"Mary had a little lamb\""`, Agent Search looks for the phrase exactly as it is. It doesn't return search results that contain `Mary had lamb`, which has missing words; or `a little lamb had Mary`, which has the words in a different order.

You can combine exact match search with logical operators in different ways to narrow down the search results. For more information, see Search query scenarios.

## Logical operators

When searching over structured data and unstructured data with metadata, you can add logical operators within a search. You can add `OR` and `AND` to the search query between multiple terms or phrases. The `NOT` logical operator isn't supported

The way you connect your search terms determines the precision of the results:

AND
    Every term in the query must appear in the results. For example, searching for `jazz AND piano` shows results that contain both the words `jazz` and `piano`.
OR
    At least one of the queried terms must appear in the results. For example, searching for `rock OR pop` returns results that include either `rock`, `pop`, or both.

You can combine the different logical operators with each other or with exact match search in different ways to narrow down the search results.

## Search query scenarios

The following table gives some scenarios that you might encounter when using exact match or partial match search.

Scenario | Description | Example  
---|---|---  
**Partial match search without any logical operators** | When there are no double quotation marks around search terms and no logical operators between them, the search works as if there is an `AND` operator between the terms. The results might also contain other documents that Agent Search deems relevant to the query due to semantic search. | 
    
    
           "query": "Mary little lamb"
          

  
For this query, the most relevant documents in the response contain all of the terms `Mary`, `little`, and `lamb`. The response might also contain other documents that contain semantically relevant terms.  
**Exact match search without any logical operators** | When there are double quotation marks around multiple individual search terms or phrases and no logical operators between them, the search works as if there is an `AND` operator between the phrases. When you add double quotation marks to at least one search term in the query, semantic search is turned off for the whole query. | 
    
    
           "query": "\"Mary\" \"little lamb\""
          

  
For this query, the search yields results that contain both the phrases `Mary` and `little lamb`.  
**Exact and partial match search** | When you add double quotation marks to at least one search term in the query, semantic search is turned off for the whole query. If logical operators are specified, they're honoured as specified. If no logical operators are specified in the query, then the search works as if there is an `AND` operator between the phrases. | 
    
    
           "query": "Mary \"little lamb\""
          

  
For this query, the search works as if there is an `AND` operator between the phrases. Because the word `Mary` is unquoted, it isn't matched exactly.   
  
## Get search results for an app with website data

### Console

To use the Google Cloud console to preview search results for an app with website data, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to edit.

  3. Click **Preview**.

  4. Open the **Preview** page in the console.

  5. Optional: If you connected multiple data stores to your app but want results only from a specific data store, select the data store to get results from.

  6. Type a search query.

If you enabled autocomplete, a list of autocomplete suggestions appears below the search bar as you type.

  7. Press **Enter** to submit the query.

     * A list of search results appears below the search bar.
     * Each result contains a title, a snippet, and a URL.
     * Clicking a result opens that URL.
     * If Advanced LLM features are enabled for the app, a generated answer might also appear.



### REST

To use the API to get search results for an app with website data, use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:

**Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Get search results.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "pageSize": "PAGE_SIZE",
         "offset": "OFFSET",
         "orderBy": "ORDER_BY",
         "params": {"user_country_code": "USER_COUNTRY_CODE",
         "searchType": "SEARCH_TYPE"},
         "filter": "FILTER",
         "boostSpec": "BOOST_SPEC",
         "contentSearchSpec": {
            "searchResultMode": "RESULT_MODE"
          },
          "userPseudoId": "USER_PSEUDO_ID",
          "dataStoreSpecs": [{"DATA_STORE_SPEC"}]
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `QUERY`: the query text to search.
     * `PAGE_SIZE`: the number of results returned by the search. The maximum allowed page size depends on the data type. Page sizes above the maximum value are coerced to the maximum value.

       * Websites with basic indexing: Default `10`, Maximum `25`
       * Websites with advanced indexing: Default `25`, Maximum `50`
       * Other: Default `50`, Maximum `100`
     * `OFFSET`: the starting index of the results. The default value is 0.

For example, if the offset is 2, the page size is 10, and there are 15 results to return, results 2 through 12 are returned on the first page.

     * `ORDER_BY`: the order in which the results are arranged. The attribute to sort on must have a numerical interpretation—for example, `date`. For more information, see [Order web search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results).

     * `USER_COUNTRY_CODE`: the location of the user. This key-value pair is the only supported entry for the `params` map field. The default value is empty. For acceptable values, see [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes) in the Programmable Search Engine JSON API reference documentation.

     * `SEARCH_TYPE`: the type of search to be performed. The default value is 0 for document search. The other supported value is 1 for image search.

     * `FILTER`: a text field for filtering your search using a filter expression. The default value is an empty string. For more information about using the `filter` field, see [Filter website search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search).

     * `BOOST_SPEC`: optional. A specification to boost or bury documents. Values:

       * `BOOST`: a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). 
       * `CONDITION`: a text filter expression to select the documents to which boost is applied. The filter must evaluate to a boolean value. For examples of filter expressions, see [Filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) and [Syntax for advanced indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing). To learn about boost for structured search, see [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results).
     * `RESULT_MODE`: determines whether search results are returned as full documents or in chunks. To get chunks, the data store must have document chunking turned on. Accepted values are `documents` and `chunks`. When chunking is turned on for a data store, the default value is `chunks`. Otherwise, the default is `documents`. For information about document chunking, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents). This field is in Public preview; to use it, change `v1` to `v1alpha` in the curl command.

     * `USER_PSEUDO_ID`: a UTF-8 encoded string, which acts as a unique pseudonymized identifier that tracks the users. It can have a maximum length of 128 characters. Google strongly recommends using this field because it improves model performance and personalization quality. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Some important considerations are as follows:

       * This identifier doesn't change when the visitor signs in or out of a website.
       * This field must not be set to the same identifier for multiple users. Otherwise, using the same user ID for multiple users can combine event histories of different users and degrade model quality.
       * This field must not include personally identifiable information (PII).
       * For a given search or browse request, this field must map to the corresponding `userPseudoId` field in the user events.

For more information, see [`userPseudoId`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search#body.request_body.FIELDS.user_pseudo_id). 

     * `DATA_STORE_SPEC`: filters for a specific data store to search across. Use `dataStoreSpecs` if your search app is connected to multiple data stores but you want results from a specific data store. For more information, see [DataStoreSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/DataStoreSpec).




### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public sealed partial class GeneratedSearchServiceClientSnippets
    {
        /// <summary>Snippet for Search</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void SearchRequestObject()
        {
            // Create client
            SearchServiceClient searchServiceClient = SearchServiceClient.Create();
            // Initialize request argument(s)
            SearchRequest request = new SearchRequest
            {
                ServingConfigAsServingConfigName = [ServingConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html).[FromProjectLocationDataStoreServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html#Google_Cloud_DiscoveryEngine_V1Beta_ServingConfigName_FromProjectLocationDataStoreServingConfig_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"),
                BranchAsBranchName = [BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName.html).[FromProjectLocationDataStoreBranch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName.html#Google_Cloud_DiscoveryEngine_V1Beta_BranchName_FromProjectLocationDataStoreBranch_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
                Query = "",
                Offset = 0,
                Filter = "",
                OrderBy = "",
                FacetSpecs =
                {
                    new SearchRequest.Types.FacetSpec(),
                },
                BoostSpec = new SearchRequest.Types.BoostSpec(),
                Params = { { "", new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)() }, },
                QueryExpansionSpec = new SearchRequest.Types.QueryExpansionSpec(),
                SpellCorrectionSpec = new SearchRequest.Types.SpellCorrectionSpec(),
                UserPseudoId = "",
                ImageQuery = new SearchRequest.Types.ImageQuery(),
                SafeSearch = false,
                UserInfo = new [UserInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UserInfo.html)(),
                UserLabels = { { "", "" }, },
                EmbeddingSpec = new SearchRequest.Types.EmbeddingSpec(),
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
                RegionCode = "",
                DisplaySpec = new SearchRequest.Types.DisplaySpec(),
                CrowdingSpecs =
                {
                    new SearchRequest.Types.CrowdingSpec(),
                },
                SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"),
                SessionSpec = new SearchRequest.Types.SessionSpec(),
                RelevanceThreshold = SearchRequest.Types.RelevanceThreshold.[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest.Types.ReconciliationMode.html#Google_Cloud_DiscoveryEngine_V1Beta_ImportDocumentsRequest_Types_ReconciliationMode_Unspecified),
                PersonalizationSpec = new SearchRequest.Types.PersonalizationSpec(),
                OneBoxPageSize = 0,
                RelevanceScoreSpec = new SearchRequest.Types.RelevanceScoreSpec(),
                RankingExpressionBackend = SearchRequest.Types.RankingExpressionBackend.[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest.Types.ReconciliationMode.html#Google_Cloud_DiscoveryEngine_V1Beta_ImportDocumentsRequest_Types_ReconciliationMode_Unspecified),
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
            string nextPageToken = singlePage.[NextPageToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse.html#Google_Cloud_DiscoveryEngine_V1Beta_ListDocumentsResponse_NextPageToken);
        }
    }

### Java

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html);
    import com.google.cloud.discoveryengine.v1.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html);
    import com.google.cloud.discoveryengine.v1.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html);
    import com.google.cloud.discoveryengine.v1.[ServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class Search {
      public static void main() throws IOException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "PROJECT_ID";
        // Location of the data store. Options: "global", "us", "eu"
        String location = "global";
        // Collection containing the data store.
        String collectionId = "default_collection";
        // Data store ID.
        String dataStoreId = "DATA_STORE_ID";
        // Serving configuration. Options: "default_search"
        String servingConfigId = "default_search";
        // Search Query for the data store.
        String searchQuery = "Google";
        search(projectId, location, collectionId, dataStoreId, servingConfigId, searchQuery);
      }
    
      /** Performs a search on a given datastore. */
      public static void search(
          String projectId,
          String location,
          String collectionId,
          String dataStoreId,
          String servingConfigId,
          String searchQuery)
          throws IOException, ExecutionException {
        // For more information, refer to:
        // https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        String endpoint = (location.equals("global")) 
            ? String.format("discoveryengine.googleapis.com:443", location) 
            : String.format("%s-discoveryengine.googleapis.com:443", location);
        [SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html) settings =
            [SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `searchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html) searchServiceClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html).create(settings)) {
          [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html) request =
              [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html).newBuilder()
                  .setServingConfig(
                      [ServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html).[formatProjectLocationCollectionDataStoreServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html#com_google_cloud_discoveryengine_v1_ServingConfigName_formatProjectLocationCollectionDataStoreServingConfigName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                          projectId, location, collectionId, dataStoreId, servingConfigId))
                  .setQuery(searchQuery)
                  .setPageSize(10)
                  .build();
          [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html) response = searchServiceClient.search(request).getPage().getResponse();
          for ([SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html).SearchResult element : response.[getResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html#com_google_cloud_discoveryengine_v1_SearchResponse_getResultsList__)()) {
            System.out.println("Response content: " + element);
          }
        }
      }
    }

### Node.js

For more information, see the [Agent Search Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_LOCATION';              // Options: 'global', 'us', 'eu'
    // const collectionId = 'default_collection';     // Options: 'default_collection'
    // const dataStoreId = 'YOUR_DATA_STORE_ID'       // Create in Cloud Console
    // const servingConfigId = 'default_config';      // Options: 'default_config'
    // const searchQuery = 'Google';
    
    const {SearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
    // For more information, refer to:
    // https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    const apiEndpoint =
      location === 'global'
        ? 'discoveryengine.googleapis.com'
        : `${location}-discoveryengine.googleapis.com`;
    
    // Instantiates a client
    const client = new [SearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)({apiEndpoint: apiEndpoint});
    
    async function search() {
      // The full resource name of the search engine serving configuration.
      // Example: projects/{projectId}/locations/{location}/collections/{collectionId}/dataStores/{dataStoreId}/servingConfigs/{servingConfigId}
      // You must create a search engine in the Cloud Console first.
      const name = client.projectLocationCollectionDataStoreServingConfigPath(
        projectId,
        location,
        collectionId,
        dataStoreId,
        servingConfigId
      );
    
      const request = {
        pageSize: 10,
        query: searchQuery,
        servingConfig: name,
      };
    
      const IResponseParams = {
        ISearchResult: 0,
        ISearchRequest: 1,
        ISearchResponse: 2,
      };
    
      // Perform search request
      const response = await client.search(request, {
        // Warning: Should always disable autoPaginate to avoid iterate through all pages.
        //
        // By default NodeJS SDK returns an iterable where you can iterate through all
        // search results instead of only the limited number of results requested on
        // pageSize, by sending multiple sequential search requests page-by-page while
        // iterating, until it exhausts all the search results. This will be unexpected and
        // may cause high Search API usage and long wait time, especially when the matched
        // document numbers are huge.
        autoPaginate: false,
      });
      const results = response[IResponseParams.ISearchResponse].results;
    
      for (const result of results) {
        console.log(result);
      }
    }

### PHP

For more information, see the [Agent Search PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\DiscoveryEngine\V1beta\Client\SearchServiceClient;
    use Google\Cloud\DiscoveryEngine\V1beta\SearchRequest;
    use Google\Cloud\DiscoveryEngine\V1beta\SearchResponse\SearchResult;
    
    /**
     * Performs a search.
     *
     * @param string $formattedServingConfig The resource name of the Search serving config, such as
     *                                       `projects/&#42;/locations/global/collections/default_collection/engines/&#42;/servingConfigs/default_serving_config`,
     *                                       or
     *                                       `projects/&#42;/locations/global/collections/default_collection/dataStores/default_data_store/servingConfigs/default_serving_config`.
     *                                       This field is used to identify the serving configuration name, set
     *                                       of models used to make the search. Please see
     *                                       {@see SearchServiceClient::servingConfigName()} for help formatting this field.
     */
    function search_sample(string $formattedServingConfig): void
    {
        // Create a client.
        $searchServiceClient = new SearchServiceClient();
    
        // Prepare the request message.
        $request = (new SearchRequest())
            ->setServingConfig($formattedServingConfig);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $searchServiceClient->search($request);
    
            /** @var SearchResult $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedServingConfig = SearchServiceClient::servingConfigName(
            '[PROJECT]',
            '[LOCATION]',
            '[DATA_STORE]',
            '[SERVING_CONFIG]'
        );
    
        search_sample($formattedServingConfig);
    }

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"          # Values: "global", "us", "eu"
    # engine_id = "YOUR_APP_ID"
    # search_query = "YOUR_SEARCH_QUERY"
    
    
    def search_sample(
        project_id: str,
        location: str,
        engine_id: str,
        search_query: str,
    ) -> discoveryengine.services.search_service.pagers.SearchPager:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.SearchServiceClient(client_options=client_options)
    
        # The full resource name of the search app serving config
        serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"
    
        # Optional - only supported for unstructured data: Configuration options for search.
        # Refer to the `ContentSearchSpec` reference for all supported fields:
        # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
        content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
            # For information about snippets, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/snippets
            snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
                return_snippet=True
            ),
            # For information about search summaries, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
            summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                summary_result_count=5,
                include_citations=True,
                ignore_adversarial_query=True,
                ignore_non_summary_seeking_query=True,
                model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                    preamble="YOUR_CUSTOM_PROMPT"
                ),
                model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                    version="stable",
                ),
            ),
        )
    
        # Refer to the `SearchRequest` reference for all supported fields:
        # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=search_query,
            page_size=10,
            content_search_spec=content_search_spec,
            query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
                condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
            ),
            spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
                mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
            ),
            # Optional: Use fine-tuned model for this request
            # custom_fine_tuning_spec=discoveryengine.CustomFineTuningSpec(
            #     enable_search_adaptor=True
            # ),
        )
    
        page_result = client.search(request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
        return page_result
    
    

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    ##
    # Snippet for the search call in the SearchService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search.
    #
    def search
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1beta::SearchRequest.new
    
      # Call the search method.
      result = client.search request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SearchResult.
        p item
      end
    end

## Get search results for an app with website data (API key)

If you want to authenticate the search method call with an API key instead of using OAuth 2.0 through a service account or a user account, then follow this procedure, which uses the [`searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method. The `searchLite` method has the same features as the `search` method except that it can only be used to search public websites.

The `searchLite` method is particularly suitable under the following conditions:

  * You have a static website for which setting up OAuth 2.0 through a service account or a user account is not practical.

  * You have migrated to Agent Search from [Custom Search Site Restricted JSON API](https://developers.google.com/custom-search/v1/site_restricted_api) of Programmable Search Engine.

  * You don't want to use the search widget.




### Before you begin

Before you can call the [`servingConfigs.searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method, you need an API key. If you don't have an API key, then complete step 1 of [Deploy the search app (API key)](https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse#api-key-deploy).

### Procedure

### REST

To use the API to get search results for an app with public website data authenticated with an API key, use the [`engines.servingConfigs.searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method:

**Note:** You can search over an app using the [`engines.servingConfigs.searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method and you can search over a data store using the [`dataStores.servingConfigs.searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/searchLite) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl command to get search results:

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:searchLite?key=API_KEY" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "userPseudoId": "USER_PSEUDO_ID"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `API_KEY`: your API key string.

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `APP_ID`: the ID of the Agent Search app that you want to query.

     * `QUERY`: the query text to search.

     * `USER_PSEUDO_ID`: a UTF-8 encoded string, which acts as a unique pseudonymized identifier that tracks the users. It can have a maximum length of 128 characters. Google strongly recommends using this field because it improves model performance and personalization quality. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Some important considerations are as follows:

       * This identifier doesn't change when the visitor signs in or out of a website.
       * This field must not be set to the same identifier for multiple users. Otherwise, using the same user ID for multiple users can combine event histories of different users and degrade model quality.
       * This field must not include personally identifiable information (PII).
       * For a given search or browse request, this field must map to the corresponding `userPseudoId` field in the user events.



For more information, see [`userPseudoId`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search#body.request_body.FIELDS.user_pseudo_id). 

**Note:** This command uses only the required input and assumes default values for the optional fields. See [`engines.servingConfigs.searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) for a list of the additional fields that you can try. 

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"          # Values: "global", "us", "eu"
    # engine_id = "YOUR_APP_ID"
    # api_key = "YOUR_API_KEY"
    # search_query = "YOUR_SEARCH_QUERY"
    
    
    def search_lite_sample(
        project_id: str,
        location: str,
        engine_id: str,
        api_key: str,
        search_query: str,
    ) -> discoveryengine.services.search_service.pagers.SearchLitePager:
    
        client_options = ClientOptions(
            # For information on API Keys, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse#api-key-deploy
            api_key=api_key,
            #  For more information, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
            api_endpoint=(
                f"{location}-discoveryengine.googleapis.com"
                if location != "global"
                else None
            ),
        )
    
        # Create a client
        client = discoveryengine.SearchServiceClient(client_options=client_options)
    
        # The full resource name of the search app serving config
        serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"
    
        # Refer to the `SearchRequest` reference for all supported fields:
        # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=search_query,
        )
    
        page_result = client.search_lite(request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
        return page_result
    
    

## Get search results for an app with structured or unstructured data

You can preview search results from the Google Cloud console or get search results using the API.

### Console

**Note:** If you have set up third-party access control for your data source, there are additional steps to preview results in the console. Go to [Preview results for apps with third-party access control](https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control#preview).

To use the Google Cloud console to preview search results for an app with structured or unstructured data, follow these steps:

  1. Open the **Preview** page in the console.
  2. Type a search query.

If you enabled autocomplete, a list of autocomplete suggestions appears below the search bar as you type.

  3. (Optional) If you connected multiple data stores to your app but want results only from a specific data store, select the data store to get results from.

  4. Press **Enter** to submit the query.

A list of search results appears below the search bar.

For structured data, the following apply:

     * If attribute mappings are not defined in **Configurations** > **Configure fields in results** , then search results are displayed as a list of raw attribute names and values.

     * If any attribute mappings were saved in **Configurations** > **Configure fields in results** , then the search results display the same way as you see in the **Configurations** page preview.

     * If any facets were specified in **Configurations** > **Facet settings** , then they are displayed in the same way.




### REST

To use the API to get search results for an app with structured or unstructured data, use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:

**Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Get search results.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "query": "QUERY",
         "userPseudoId": "USER_PSEUDO_ID",
         "pageSize": "PAGE_SIZE",
         "offset": "OFFSET",
         "orderBy": "ORDER_BY",
         "filter": "FILTER",
         "boostSpec": "BOOST_SPEC",
         "facetSpec": "FACET_SPEC",
         "queryExpansionSpec": "QUERY_EXPANSION_SPEC",
         "spellCorrectionSpec": "SPELL_CORRECTION_SPEC",
         "contentSearchSpec": "CONTENT_SEARCH_SPEC",
         "dataStoreSpecs": [{"DATA_STORE_SPEC"}],
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `QUERY`: the query text to search.
     * `USER_PSEUDO_ID`: a UTF-8 encoded string, which acts as a unique pseudonymized identifier that tracks the users. It can have a maximum length of 128 characters. Google strongly recommends using this field because it improves model performance and personalization quality. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Some important considerations are as follows:

       * This identifier doesn't change when the visitor signs in or out of a website.
       * This field must not be set to the same identifier for multiple users. Otherwise, using the same user ID for multiple users can combine event histories of different users and degrade model quality.
       * This field must not include personally identifiable information (PII).
       * For a given search or browse request, this field must map to the corresponding `userPseudoId` field in the user events.

For more information, see [`userPseudoId`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search#body.request_body.FIELDS.user_pseudo_id). 

     * `PAGE_SIZE`: the number of results returned by the search. The maximum allowed page size depends on the data type. Page sizes above the maximum value are coerced to the maximum value.

       * Websites with basic indexing: Default `10`, Maximum `25`
       * Websites with advanced indexing: Default `25`, Maximum `50`
       * Other: Default `50`, Maximum `100`
     * `OFFSET`: optional. The starting index of the results. The default value is 0.

For example, if the offset is 2, the page size is 10, and there are 15 results to return, results 2 through 11 are returned on the first page.

     * `ORDER_BY`: optional. The order in which the results are arranged.

     * `FILTER`: optional. A text field for filtering your search using a filter expression. The default value is an empty string, which means no filter is applied.

Example: `color: ANY("red", "blue") AND score: IN(*, 100.0e)`

For more information, see [Filter search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata).

     * `BOOST_SPEC`: optional. A specification to boost or bury documents. Values:

       * `BOOST`: a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). 
       * `CONDITION`: a text filter expression to select the documents to which boost is applied. The filter must evaluate to a boolean value. For examples of filter expressions, see [Filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) and [Syntax for advanced indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing). 

To learn about boost for structured search, see [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results).

     * `FACET_SPEC`: optional. A facet specification to perform faceted search.

     * `QUERY_EXPANSION_SPEC`: optional. A specification to determine under which conditions query expansion should occur. Default is `DISABLED`.

     * `SPELL_CORRECTION_SPEC`: optional. A specification to determine under which conditions spell correction should occur. Default is `AUTO`.

     * `CONTENT_SEARCH_SPEC`: optional. For getting snippets, extractive answers, extractive segments, and search summaries. For unstructured data only. For more information, see:

       * [Use snippets and extractive content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets)
       * [Get search summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries)
     * `DATA_STORE_SPEC`: filters for a specific data store to search across. This can be used if your search app is connected to multiple data stores.

     * Viewing guided search results in the search response:

Guided search results are returned with search responses for structured and unstructured search. The guided search result contains a list of extracted attribute key-value pairs based on search result documents. This allows users to refine their search results by using some attribute keys and values as filters.

In this example response, the color green was used to refine search results by issuing a new search request with the filter field specified as `_gs.color: ANY("green")`:
           
           {
           "guidedSearchResult": {
             "refinementAttributes": [
               {
                 "attributeKey": "_gs.color",
                 "attributeValue": "green"
               },
               {
                 "attributeKey": "_gs.category",
                 "attributeValue": "shoe"
               }
             ]
           }
           }
           




### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public sealed partial class GeneratedSearchServiceClientSnippets
    {
        /// <summary>Snippet for Search</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void SearchRequestObject()
        {
            // Create client
            SearchServiceClient searchServiceClient = SearchServiceClient.Create();
            // Initialize request argument(s)
            SearchRequest request = new SearchRequest
            {
                ServingConfigAsServingConfigName = [ServingConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html).[FromProjectLocationDataStoreServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html#Google_Cloud_DiscoveryEngine_V1Beta_ServingConfigName_FromProjectLocationDataStoreServingConfig_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"),
                BranchAsBranchName = [BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName.html).[FromProjectLocationDataStoreBranch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName.html#Google_Cloud_DiscoveryEngine_V1Beta_BranchName_FromProjectLocationDataStoreBranch_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
                Query = "",
                Offset = 0,
                Filter = "",
                OrderBy = "",
                FacetSpecs =
                {
                    new SearchRequest.Types.FacetSpec(),
                },
                BoostSpec = new SearchRequest.Types.BoostSpec(),
                Params = { { "", new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)() }, },
                QueryExpansionSpec = new SearchRequest.Types.QueryExpansionSpec(),
                SpellCorrectionSpec = new SearchRequest.Types.SpellCorrectionSpec(),
                UserPseudoId = "",
                ImageQuery = new SearchRequest.Types.ImageQuery(),
                SafeSearch = false,
                UserInfo = new [UserInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UserInfo.html)(),
                UserLabels = { { "", "" }, },
                EmbeddingSpec = new SearchRequest.Types.EmbeddingSpec(),
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
                RegionCode = "",
                DisplaySpec = new SearchRequest.Types.DisplaySpec(),
                CrowdingSpecs =
                {
                    new SearchRequest.Types.CrowdingSpec(),
                },
                SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"),
                SessionSpec = new SearchRequest.Types.SessionSpec(),
                RelevanceThreshold = SearchRequest.Types.RelevanceThreshold.[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest.Types.ReconciliationMode.html#Google_Cloud_DiscoveryEngine_V1Beta_ImportDocumentsRequest_Types_ReconciliationMode_Unspecified),
                PersonalizationSpec = new SearchRequest.Types.PersonalizationSpec(),
                OneBoxPageSize = 0,
                RelevanceScoreSpec = new SearchRequest.Types.RelevanceScoreSpec(),
                RankingExpressionBackend = SearchRequest.Types.RankingExpressionBackend.[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest.Types.ReconciliationMode.html#Google_Cloud_DiscoveryEngine_V1Beta_ImportDocumentsRequest_Types_ReconciliationMode_Unspecified),
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
            string nextPageToken = singlePage.[NextPageToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse.html#Google_Cloud_DiscoveryEngine_V1Beta_ListDocumentsResponse_NextPageToken);
        }
    }

### Java

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html);
    import com.google.cloud.discoveryengine.v1.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html);
    import com.google.cloud.discoveryengine.v1.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html);
    import com.google.cloud.discoveryengine.v1.[ServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class Search {
      public static void main() throws IOException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "PROJECT_ID";
        // Location of the data store. Options: "global", "us", "eu"
        String location = "global";
        // Collection containing the data store.
        String collectionId = "default_collection";
        // Data store ID.
        String dataStoreId = "DATA_STORE_ID";
        // Serving configuration. Options: "default_search"
        String servingConfigId = "default_search";
        // Search Query for the data store.
        String searchQuery = "Google";
        search(projectId, location, collectionId, dataStoreId, servingConfigId, searchQuery);
      }
    
      /** Performs a search on a given datastore. */
      public static void search(
          String projectId,
          String location,
          String collectionId,
          String dataStoreId,
          String servingConfigId,
          String searchQuery)
          throws IOException, ExecutionException {
        // For more information, refer to:
        // https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        String endpoint = (location.equals("global")) 
            ? String.format("discoveryengine.googleapis.com:443", location) 
            : String.format("%s-discoveryengine.googleapis.com:443", location);
        [SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html) settings =
            [SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `searchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html) searchServiceClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html).create(settings)) {
          [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html) request =
              [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html).newBuilder()
                  .setServingConfig(
                      [ServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html).[formatProjectLocationCollectionDataStoreServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html#com_google_cloud_discoveryengine_v1_ServingConfigName_formatProjectLocationCollectionDataStoreServingConfigName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                          projectId, location, collectionId, dataStoreId, servingConfigId))
                  .setQuery(searchQuery)
                  .setPageSize(10)
                  .build();
          [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html) response = searchServiceClient.search(request).getPage().getResponse();
          for ([SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html).SearchResult element : response.[getResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html#com_google_cloud_discoveryengine_v1_SearchResponse_getResultsList__)()) {
            System.out.println("Response content: " + element);
          }
        }
      }
    }

### Node.js

For more information, see the [Agent Search Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_LOCATION';              // Options: 'global', 'us', 'eu'
    // const collectionId = 'default_collection';     // Options: 'default_collection'
    // const dataStoreId = 'YOUR_DATA_STORE_ID'       // Create in Cloud Console
    // const servingConfigId = 'default_config';      // Options: 'default_config'
    // const searchQuery = 'Google';
    
    const {SearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
    // For more information, refer to:
    // https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    const apiEndpoint =
      location === 'global'
        ? 'discoveryengine.googleapis.com'
        : `${location}-discoveryengine.googleapis.com`;
    
    // Instantiates a client
    const client = new [SearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)({apiEndpoint: apiEndpoint});
    
    async function search() {
      // The full resource name of the search engine serving configuration.
      // Example: projects/{projectId}/locations/{location}/collections/{collectionId}/dataStores/{dataStoreId}/servingConfigs/{servingConfigId}
      // You must create a search engine in the Cloud Console first.
      const name = client.projectLocationCollectionDataStoreServingConfigPath(
        projectId,
        location,
        collectionId,
        dataStoreId,
        servingConfigId
      );
    
      const request = {
        pageSize: 10,
        query: searchQuery,
        servingConfig: name,
      };
    
      const IResponseParams = {
        ISearchResult: 0,
        ISearchRequest: 1,
        ISearchResponse: 2,
      };
    
      // Perform search request
      const response = await client.search(request, {
        // Warning: Should always disable autoPaginate to avoid iterate through all pages.
        //
        // By default NodeJS SDK returns an iterable where you can iterate through all
        // search results instead of only the limited number of results requested on
        // pageSize, by sending multiple sequential search requests page-by-page while
        // iterating, until it exhausts all the search results. This will be unexpected and
        // may cause high Search API usage and long wait time, especially when the matched
        // document numbers are huge.
        autoPaginate: false,
      });
      const results = response[IResponseParams.ISearchResponse].results;
    
      for (const result of results) {
        console.log(result);
      }
    }

### PHP

For more information, see the [Agent Search PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\DiscoveryEngine\V1beta\Client\SearchServiceClient;
    use Google\Cloud\DiscoveryEngine\V1beta\SearchRequest;
    use Google\Cloud\DiscoveryEngine\V1beta\SearchResponse\SearchResult;
    
    /**
     * Performs a search.
     *
     * @param string $formattedServingConfig The resource name of the Search serving config, such as
     *                                       `projects/&#42;/locations/global/collections/default_collection/engines/&#42;/servingConfigs/default_serving_config`,
     *                                       or
     *                                       `projects/&#42;/locations/global/collections/default_collection/dataStores/default_data_store/servingConfigs/default_serving_config`.
     *                                       This field is used to identify the serving configuration name, set
     *                                       of models used to make the search. Please see
     *                                       {@see SearchServiceClient::servingConfigName()} for help formatting this field.
     */
    function search_sample(string $formattedServingConfig): void
    {
        // Create a client.
        $searchServiceClient = new SearchServiceClient();
    
        // Prepare the request message.
        $request = (new SearchRequest())
            ->setServingConfig($formattedServingConfig);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $searchServiceClient->search($request);
    
            /** @var SearchResult $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedServingConfig = SearchServiceClient::servingConfigName(
            '[PROJECT]',
            '[LOCATION]',
            '[DATA_STORE]',
            '[SERVING_CONFIG]'
        );
    
        search_sample($formattedServingConfig);
    }

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"          # Values: "global", "us", "eu"
    # engine_id = "YOUR_APP_ID"
    # search_query = "YOUR_SEARCH_QUERY"
    
    
    def search_sample(
        project_id: str,
        location: str,
        engine_id: str,
        search_query: str,
    ) -> discoveryengine.services.search_service.pagers.SearchPager:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.SearchServiceClient(client_options=client_options)
    
        # The full resource name of the search app serving config
        serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"
    
        # Optional - only supported for unstructured data: Configuration options for search.
        # Refer to the `ContentSearchSpec` reference for all supported fields:
        # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
        content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
            # For information about snippets, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/snippets
            snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
                return_snippet=True
            ),
            # For information about search summaries, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
            summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                summary_result_count=5,
                include_citations=True,
                ignore_adversarial_query=True,
                ignore_non_summary_seeking_query=True,
                model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                    preamble="YOUR_CUSTOM_PROMPT"
                ),
                model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                    version="stable",
                ),
            ),
        )
    
        # Refer to the `SearchRequest` reference for all supported fields:
        # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=search_query,
            page_size=10,
            content_search_spec=content_search_spec,
            query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
                condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
            ),
            spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
                mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
            ),
            # Optional: Use fine-tuned model for this request
            # custom_fine_tuning_spec=discoveryengine.CustomFineTuningSpec(
            #     enable_search_adaptor=True
            # ),
        )
    
        page_result = client.search(request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
        return page_result
    
    

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    ##
    # Snippet for the search call in the SearchService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search.
    #
    def search
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1beta::SearchRequest.new
    
      # Call the search method.
      result = client.search request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SearchResult.
        p item
      end
    end

## Get document-relevance scores with search results

Document-relevance scores are based on the similarity of the query to the document. Scores are put into 11 buckets in the range: 0, 0.1, 0.2, … to 1.0. The higher the score, the more relevant the document.

Consider document-relevance scores for these use cases:

  * Post-search filtering based on the relevance score to remove irrelevant results

  * Post-search ranking or as input to other applications

  * Debugging: relevance scores can provide insight into why some search results are returned




For each search result, a relevance score can be returned:
    
    
      "results": [
        {
          "id": "DOCUMENT_ID",
          "document": {
          ...
          },
          "modelScores": {
            "relevance_score": {
              "values": [
                DOCUMENT-RELEVANCE-SCORE
              ]
            }
          }
        },
      ...
      ]
    

Also see the example command in the procedure below.

**Before you begin:** Make sure that the search app is associated with a structured or unstructured data store. That is, document-relevance scores can't be returned for a website search app.

### REST

To request that document-relevance scores be returned with search results, use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method as follows:

**Note:** The scores might not always be returned. Make sure that your post-processing of search results doesn't rely on scores being present.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl command to get scores returned with search results.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
              "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
              "query": "QUERY",
              **"relevanceScoreSpec": {
                "returnRelevanceScore": true**
              }
         }'
         

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `QUERY`: the query text to search.

#### Example command and partial result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search" \
    -d '{
          "servingConfig": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search",
          "query": "When was Verily founded and what is its mission?",
          **"relevanceScoreSpec": {
            "returnRelevanceScore": true**
          }
    }'
    
    
    * * *
    
    
    {
      "results": [
        {
          "id": "f1b0d98bd2a078a6dfb4f809c3028565",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f1b0d98bd2a078a6dfb4f809c3028565",
            "id": "f1b0d98bd2a078a6dfb4f809c3028565",
            "derivedStructData": {
              "link": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2019_alphabet_annual_report.pdf",
              "extractive_answers": [
                {
                  "pageNumber": "70",
                  "content": "VERILY Verily is a life science and healthcare company with a mission to make the world's health data useful so that people enjoy healthier lives. In December 2018, Verily received $900 million in cash from a $1.0 billion investment round. The remaining $100 million was received in the first quarter of 2019."
                }
              ],
              "title": "2019_alphabet_annual_report"
            }
          },
          **"modelScores": {
            "relevance_score": {
              "values": [
                0.7
              ]
            }
          }**
        },
        {
          "id": "0371b29bfa18ac43896b86a7b63d00b0",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/0371b29bfa18ac43896b86a7b63d00b0",
            "id": "0371b29bfa18ac43896b86a7b63d00b0",
            "derivedStructData": {
              "link": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/20190429_alphabet_10Q.pdf",
              "title": "GOOG 10-Q Q1 2019",
              "extractive_answers": [
                {
                  "content": "Verily Verily is a life science company with a mission to make the world's health data useful so that people enjoy healthier lives. In December 2018, Verily received $900 million in cash from a $1.0 billion investment round. The remaining $100 million was received in the first quarter of 2019.",
                  "pageNumber": "21"
                }
              ]
            }
          },
         **"modelScores": {
            "relevance_score": {
              "values": [
                0.5
              ]
            }
          }**
        },
        ...
        {
          "id": "e6bbd0d82dc2a2fc7ccf1bd82ac6334f",
          "document": {
            "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/e6bbd0d82dc2a2fc7ccf1bd82ac6334f",
            "id": "e6bbd0d82dc2a2fc7ccf1bd82ac6334f",
            "derivedStructData": {
              "title": "2021_Q1_Earnings_Transcript",
              "link": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2021_Q1_Earnings_Transcript.pdf",
              "extractive_answers": [
                {
                  "pageNumber": "2",
                  "content": "Our strength in AI and ML is also helping Financial Services customers improve efficiency of payments, reduce fraud and risk, and deliver faster payment solutions."
                }
              ]
            }
          },
          **"modelScores": {
            "relevance_score": {
              "values": [
                0
              ]
            }
          }**
        }
      ],
      "totalSize": 76,
      "attributionToken": "8QHw8AoLCIW4_b0GELHd3lgSJDY3YmU1ZGMwLTAwMDAtMmM1OC04NzcyLTc0NzQ0NjNiOGMyNSIHR0VORVJJQyqcAcb77TDHy_MX8tntMI6-nRWK4uQwwvCeFYX77TDvifIwq8SKLauR3zCq-LMt0IrIMNSynRWc1rctv_7kML7l3zDZveQwkPeyMMP77TD12e0wpd_hMIfi5DCRv9owgvvtMJWSxTCOkckwu-XfMK7Eii3sifIwqJHfMKjf4TCt-LMtlL_aMJ_Wty23t4wto4CXIs2KyDDcveQwwv7kMDABShIweDU3MGFkYWI4MzQ4NmY0MGE",
      "nextPageToken": "UjMjhjYzYDN0cDN30iM3cDOtgTNjJTLwADMw0iZiRWNlJ2N2QiGBUd0gWLEG4bjhWICMIBM1IgC",
      "summary": {},
      "queryExpansionInfo": {}
    }
    




**Note:** This document-relevance score is different from and more precise than the [relevance level](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance) used to filter documents returned by a search.

## Search summarization differs by model

If you generate search summaries for your queries, you might notice that the summaries differ between the console results and the API results. If you see this, the likely reason is that the console is using a different LLM model from the API. The curl and code examples on this page use the stable LLM model.

  * To change or view the LLM model used in the **Preview** page of the UI (only supported for advanced search applications and healthcare applications).

    1. Go to your app's **Configurations** page > **UI** tab.
    2. Select a **Search Type** :

       * Select **Search with an answer** to display a generative summary above the search results.
       * Select **Search with follow-ups** to enable conversation search with generative summaries and follow-up questions.
    3. In the **Large language models for summarization** section, select a model.

  * For method calls, the stable model is the default model. To use an LLM model other than the stable model, see [Specify the summarization model](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#summary-model) and [Specify the answer model](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#answer-model).

## Next steps

  * [Add the search widget to a web page](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget).

  * Use the search API to [browse data in your generic search apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/browse-generic-search).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
