---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-basic/
title: Get search results \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:02.768811+00:00
---

# Get search results  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-basic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Get search results Stay organized with collections  Save and categorize content based on your preferences. 

This page describes basic querying with search, including text query searches, browse searches, pagination, optimization, and personalized results.

**Important:** Never cache personalized results from an end user generated for one `visitor_id`, as it could result in returning erroneous personalized results to a different end user. Doing so leads to poor relevance and potential data privacy leaks. To ensure accurate personalization and correct model training, every end user needs a unique search response generated specifically for their unique `visitor_id`.

## Unique user session identifiers

The required `visitor_id` string field is used to uniquely identify a user on a single device. It acts as a persistent session identifier that allows AI Commerce Search to track a specific user's behavior across their shopping journey.

AI Commerce Search uses the history associated with a specific `visitor_id` to train models and serve personalized search results. The system generates results dynamically based on the specific `visitor_id` provided in the request. For example, if a visitor frequently views green dresses, the model uses `visitor_id` to recognize them later and prioritize similar items in their search results. For this reason, the visitor ID must be formatted identically across both user event ingestion (tracking) and search or recommendations requests (serving).

## Relevance in AI Commerce Search

Relevance is different from matching. Matching is finding candidate products in the index that correspond to the user's search query. Relevance, on the other hand, is a degree of matching. It involves ranking those products in a way that best satisfies the user's intent and needs. AI Commerce Search uses techniques to improve matching and relevance for a better overall search experience for users that meets retailers' needs.

### Default search

Search defaults to relevance. However, some non-relevant products can appear at the bottom of default searches or in explicit product discovery requests. This only becomes noticeable when you set `orderBy`, because it reduces the size of search results in general. The recall size decreases because the less relevant products, which were previously being returned at the bottom of the default search, are filtered out to some degree. Read the next section to find out how to customize search.

### Non-default search

AI Commerce Search defaults to relevance in search. However, search is tuned to also surface marginally relevant items higher up in the search results to provide retailers more targeted search results to increase the conversion potential of user events.

These added search features optimize the default relevance algorithm, providing non-default features tuned to each retailer's utilization profile, including:

  * Options to sort results such as by price, top-rated, or best-selling items. Non-default search is customized to return specific search results with the correct product [variants](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels). For example, to show the cheapest or most expensive variant when sorting by price.

  * Auto-application of a tighter relevance filter for non-default user events.

  * Enabling adjustable strength boost/bury controls to fine-tune search results.


**Note:** Expected behavior is fewer products appearing in non-default search scenarios, because less relevant items are filtered out. Given the limited scope of non-default searches, occasional lower-than-expected product counts in search results don't negatively impact revenue growth.

## Text search and browse search

Search provides both text query search and browse search capabilities.

In the text query search use case, a shopper might enter a text-based query on your site. Search returns a search response containing products that fit within the parameters of controls you have set up, sorted by relevance and revenue maximization.

In the browse use case, a shopper might go to your site menu and navigate to a specific product category. Search automatically chooses the most revenue-maximizing sort order by learning from user behavior and trends. Browse results can be further refined by the controls you have set up.

Both text search and browse search requests use the [`servingConfigs.search`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/search) method.

**Note:** The wildcard (*) is not supported and its usage may lead to inconsistent results.

### Text query searches

When a user enters a text query to search on your site, search sorts potential search results based on relevance, popularity, buyability, and personalization.

Search considers a `servingConfigs.search` request as a text-based search request if it has a non-empty `query` field.

When uploading user event, send text query search events generated by search as `search` user events. If the event has a non-empty `userEvent.searchQuery` field and an empty `userEvent.pageCategories` field, search considers it a text-based search event.

#### How to process text queries and parameters

Standard queries undergo linguistic analysis, which strips standard punctuation. Filter strings are strictly case-sensitive. Understanding how to process text queries and parameters is critical for constructing API requests in AI Commerce Search properly.

  * **Query tokenization and punctuation** : Natural language text is passed into the `query` field undergoes automatic linguistic analysis and spell correction. During this process, standard punctuation (like commas, periods, `+`, or `-`) is often stripped or ignored to optimize for natural language understanding.
  * **Strict case sensitivity in parameters** : While standard text queries are generally case-insensitive, programmatic parameters are strictly case-sensitive. 
    * **Filters** : Filter expressions and their literal string values are completely case-sensitive.
    * **Sorting** : The `orderBy` expression is case-sensitive. If you sort by a field like `products.title`, the engine will sort _Apple_ before _banana_ before _artichoke._ A workaround is to upload product titles in all caps to a separate custom attribute (such as `attributes.title_upper`) and sort on that attribute to achieve case-insensitive sorting.
  * **Reserved special characters** : 
    * The `>` character is strictly reserved as the delimiter for category hierarchies (such as `Categories > Shoes`). If `>` naturally occurs in your category name, you must replace it with another character before ingestion and querying.
    * The `/` character is not supported in textual values within recommendation filter expressions.



### Browse searches

Browse uses site navigation to produce search results of equal relevance sorted by best-selling items. Search leverages AI to optimize how browse results are sorted by considering popularity, buyability, and personalization.

**Important:** For browse searches to work, the `SearchRequest.pageCategories` field cannot be empty. It must always be populated for optimal browse results.

To get the correct browse search results, consider the following:

  * The `pageCategories` and `filter` values in your search requests must exactly match the `pageCategories` and `filter` values in your uploaded user events. If the parameters in the requests don't match parameters in the events, the click-based reranking model learned from the events won't perform very well for this specific query and will negatively impact result quality.

  * AI Commerce Search categorizes a `search` user event as a browse-based event if it has an empty `userEvent.searchQuery` field and a non-empty `userEvent.pageCategories` field. This is why you need to make sure you send browse events generated by AI Commerce Search as `search` user events when uploading them.

  * A browse filter must be valid and indicate for each browse query which products belong to the product category the user is browsing in. To achieve this setup, the category ID needs to be defined in both the `filter` and the `page_category` fields. Take, for example, if you want the search results to be targeted to Home & Garden. First off, having only one `filter` value of `"in-stock"` does not refine the search enough to provide optimal browse results. To provide search results restricted to Home & Garden, you not only need to set `"Home \& Garden"` in the page category, but also in the filter with `categories: ANY("Home & Garden")`. If you neglect to define the category in the filter part, browse results could likely be too broad and include many non-Home & Garden items.




Serving requests and events with an empty query field and filled `page_categories` fields are considered browse requests and user events. The `page_categories` field specifies the browse page itself. When the `servingConfigs.search` method sends a request, search considers it a browse search request if the `query` field is empty. When that is the case, the results are based on the `filter` and `pageCategories` fields and, if available, more optimization and personalization.

You can set the category in both as in this example:

### JSON
    
    
    page_category: "Home & Garden"
    filter: "(availability: ANY("IN_STOCK")) AND (categories: ANY("Home & Garden"))"

Otherwise, because browse works with empty string queries, the products in a given category won't automatically be displayed in the results for a given page category. In other words, if the end user browses without specifying anything using a text query, the search return may not yield effectively targeted results, even if the user navigates to a category page.

## Use search requests

Use search requests to get results for both text searches and browse searches. To make a search request, use the [`servingConfigs.search`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/search) method.

All search requests require `placement`, which identifies the full resource name of the serving config that will be used. The serving config determines which settings and associated controls affect the search results.

Text query search requests require a non-empty `query` field.

Browse search requests require a non-empty `pageCategories` field.

### Python

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). For more information, see the [AI Commerce Search Python API reference documentation](https://github.com/googleapis/python-recommendations-ai). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.auth
    from google.cloud.retail import [SearchRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.SearchRequest.html), [SearchServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.search_service.SearchServiceClient.html)
    
    project_id = google.auth.default()[1]
    
    
    # get search service request:
    def get_search_request(query: str):
        default_search_placement = (
            "projects/"
            + project_id
            + "/locations/global/catalogs/default_catalog/placements/default_search"
        )
    
        search_request = SearchRequest()
        search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
        search_request.query = query
        search_request.visitor_id = "123456"  # A unique identifier to track visitors
        search_request.page_size = 10
    
        print("---search request:---")
        print(search_request)
    
        return search_request
    
    
    # call the Retail Search:
    def search():
        # TRY DIFFERENT QUERY PHRASES HERE:
        query_phrase = "Hoodie"
    
        search_request = get_search_request(query_phrase)
        search_response = SearchServiceClient().search(search_request)
    
        print("---search response---")
        if not search_response.results:
            print("The search operation returned no matching results.")
        else:
            print(search_response)
        return search_response
    
    
    search()

### Node.js

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    'use strict';
    
    async function main() {
      // Call Retail API to search for a products in a catalog using only search query.
    
      // Imports the Google Cloud client library.
      const {SearchServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)');
    
      // Instantiates a client.
      const retailClient = new [SearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      const projectId = await retailClient.getProjectId();
    
      // Placement is used to identify the Serving Config name.
      const placement = `projects/${projectId}/locations/global/catalogs/default_catalog/placements/default_search`;
    
      // Raw search query.
      const query = 'Hoodie'; //TRY DIFFERENT QUERY PHRASES
    
      // A unique identifier for tracking visitors.
      const visitorId = '12345';
    
      // Maximum number of Products to return.
      const pageSize = 10;
    
      const IResponseParams = {
        ISearchResult: 0,
        ISearchRequest: 1,
        ISearchResponse: 2,
      };
    
      const callSearch = async () => {
        console.log('Search start');
        // Construct request
        const request = {
          placement,
          query,
          visitorId,
          pageSize,
        };
        console.log('Search request: ', request);
    
        // Run request
        const response = await retailClient.search(request, {
          autoPaginate: false,
        });
        const searchResponse = response[IResponseParams.ISearchResponse];
        if (searchResponse.totalSize === 0) {
          console.log('The search operation returned no matching results.');
        } else {
          console.log('Search result: ', JSON.stringify(searchResponse, null, 4));
        }
        console.log('Search end');
      };
    
      callSearch();
    }
    
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    
    main();
    

### Java

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). For more information, see the [AI Commerce Search Java API reference documentation](https://github.com/googleapis/java-recommendations-ai/). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.[ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html);
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html);
    import com.google.cloud.retail.v2.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html);
    import com.google.cloud.retail.v2.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html);
    import java.io.IOException;
    import java.util.UUID;
    
    public class SearchSimpleQuery {
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) throws IOException {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = [ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html).getDefaultProjectId();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) defaultCatalogName =
            [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html).format("projects/%s/locations/global/catalogs/default_catalog", projectId);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) defaultSearchPlacementName = defaultCatalogName + "/placements/default_search";
    
        searchResponse(defaultSearchPlacementName);
      }
    
      public static void searchResponse([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) defaultSearchPlacementName) throws IOException {
        // TRY DIFFERENT QUERY PHRASES HERE:
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) queryPhrase = "Hoodie";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) visitorId = UUID.randomUUID().toString();
        int pageSize = 10;
    
        [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) searchRequest =
            [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
                .setPlacement(defaultSearchPlacementName)
                .setQuery(queryPhrase)
                .setVisitorId(visitorId)
                .setPageSize(pageSize)
                .build();
        System.out.println("Search request: " + searchRequest);
    
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html) client = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html).create()) {
          [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) searchResponse = client.search(searchRequest).getPage().getResponse();
          if (searchResponse.[getTotalSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html#com_google_cloud_retail_v2_SearchResponse_getTotalSize__)() == 0) {
            System.out.println("The search operation returned no matching results.");
          } else {
            System.out.println("Search response: " + searchResponse);
          }
        }
      }
    }

By default, a reasonable number of results ordered by relevance is returned.

To get product attributes returned with the search response, make sure to provide attribute values when you import your catalog data. [`Product`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products) has predefined system attributes such as brand, color, and size that you can provide values for. You can also include custom attributes that you define with [`Product.attributes`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.attributes).

### Querying tutorial

This tutorial shows you how to send a text-based search query to the AI Commerce Search service and analyze the response.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_querying_select_language&show=ide&environment_deployment=ide)

* * *

### Filter search results using autocomplete suggestions

If you have implemented enriched autocomplete suggestions on your frontend (where users can select a query combined with a specific brand or category), you must translate that selection into a filtered `SearchRequest`.

To implement this, extract the text suggestion and place it into the `query` field, and extract the selected attribute (such as a brand) and format it as an expression in the `filter` field.

#### Example search request from a filtered suggestion

If the user clicked the suggestion _shoe_ in **Nike** , structure your `SearchRequest` as follows:
    
    
    {
      "placement": "projects/YOUR_PROJECT_ID/locations/global/catalogs/default_catalog/placements/default_search",
      "query": "shoe",
      "filter": "brands: ANY(\"Nike\")",
      "visitorId": "user_session_123"
    }
    

#### Add product counts to suggestion facets

To further enhance the filtering experience, you can display the number of available products for each suggestion filter before the user even executes the search. To use suggestion facets with product counts, you must contact support to enable the feature. When enabled, include the specific textual facet key in the `facetSpecs` of your `SearchRequest` for at least 7 days to allow the system to calculate the product counts based on your search history data.

## Pagination

Use pagination to decrease lookup time and the size of responses being sent.

### Pagination tutorial

This tutorial shows how to control pagination in a text-based search request. When a shopper looks for products in a shop, they can improve their navigation through the search results. For example, they can limit the number of items in the search response by using the page size feature or jump to their preferred page by using the offset feature.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_pagination_select_language.neos.md&show=ide&environment_deployment=ide)

* * *

### Paginate

To jump from one page to another, use either `page_token` or `offset`, according to your use case.

### Python

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). For more information, see the [AI Commerce Search Python API reference documentation](https://github.com/googleapis/python-recommendations-ai). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.auth
    from google.cloud.retail import [SearchRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.SearchRequest.html), [SearchServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.search_service.SearchServiceClient.html)
    
    project_id = google.auth.default()[1]
    
    
    # get search service request:
    def get_search_request(query: str, page_size: int, offset: int, next_page_token: str):
        default_search_placement = (
            "projects/"
            + project_id
            + "/locations/global/catalogs/default_catalog/placements/default_search"
        )
    
        search_request = SearchRequest()
        search_request.placement = default_search_placement
        search_request.visitor_id = "123456"  # A unique identifier to track visitors
        search_request.query = query
        search_request.page_size = page_size
        search_request.offset = offset
        search_request.page_token = next_page_token
    
        print("---search request:---")
        print(search_request)
    
        return search_request
    
    
    # call the Retail Search:
    def search():
        # TRY DIFFERENT PAGINATION PARAMETERS HERE:
        page_size = 6
        offset = 0
        page_token = ""
    
        search_request_first_page = get_search_request(
            "Hoodie", page_size, offset, page_token
        )
        search_response_first_page = SearchServiceClient().search(search_request_first_page)
    
        print("---search response---")
        if not search_response_first_page.results:
            print("The search operation returned no matching results.")
        else:
            print(search_response_first_page)
    
        # PASTE CALL WITH NEXT PAGE TOKEN HERE:
    
        # PASTE CALL WITH OFFSET HERE:
    
        return search_response_first_page
    
    
    search()
    

### Node.js

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function main() {
      // Imports the Google Cloud client library.
      const {SearchServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)');
    
      // Instantiates a client.
      const retailClient = new [SearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      const projectId = await retailClient.getProjectId();
    
      // Placement is used to identify the Serving Config name.
      const placement = `projects/${projectId}/locations/global/catalogs/default_catalog/placements/default_search`;
    
      // Raw search query.
      const query = 'Hoodie';
    
      // A unique identifier for tracking visitors.
      const visitorId = '12345';
    
      // Maximum number of Products to return.
      const pageSize = 6; // TRY DIFFERENT PAGE SIZES, INCLUDING THOSE OVER 100
    
      // A 0-indexed integer that specifies the current offset in search results.
      const offset = 0; // TRY DIFFERENT OFFSETS TO SEE DIFFERENT PRODUCTS
    
      //A page token received from a previous search call.
      let pageToken = '';
    
      const IResponseParams = {
        ISearchResult: 0,
        ISearchRequest: 1,
        ISearchResponse: 2,
      };
    
      const callSearch = async () => {
        console.log('Search start');
        // Construct request
        const request = {
          placement,
          query,
          visitorId,
          pageSize,
          offset,
          pageToken,
        };
    
        // Run request
        const response = await retailClient.search(request, {
          autoPaginate: false,
        });
        const searchResponse = response[IResponseParams.ISearchResponse];
        if (searchResponse.totalSize === 0) {
          console.log('The search operation returned no matching results.');
        } else {
          console.log('Search result: ', JSON.stringify(searchResponse, null, 4));
          pageToken = response[IResponseParams.ISearchResponse].nextPageToken;
          console.log(
            'Next page token:',
            response[IResponseParams.ISearchResponse].nextPageToken
          );
        }
        console.log('Search end');
      };
    
      // Call search
      await callSearch();
    
      //PASTE CALL WITH NEXT PAGE TOKEN HERE:
    }
    

### Java

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). For more information, see the [AI Commerce Search Java API reference documentation](https://github.com/googleapis/java-recommendations-ai/). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.[ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html);
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html);
    import com.google.cloud.retail.v2.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html);
    import com.google.cloud.retail.v2.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html);
    import java.io.IOException;
    import java.util.UUID;
    
    public class SearchWithPagination {
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) throws IOException {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = [ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html).getDefaultProjectId();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) defaultCatalogName =
            [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html).format("projects/%s/locations/global/catalogs/default_catalog", projectId);
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) defaultSearchPlacementName = defaultCatalogName + "/placements/default_search";
    
        searchResponse(defaultSearchPlacementName);
      }
    
      public static void searchResponse([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) defaultSearchPlacementName) throws IOException {
        // TRY DIFFERENT PAGINATION PARAMETERS HERE:
        int pageSize = 6;
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) queryPhrase = "Hoodie";
        int offset = 0;
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) pageToken = "";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) visitorId = UUID.randomUUID().toString();
    
        [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) searchRequest =
            [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
                .setPlacement(defaultSearchPlacementName)
                .setVisitorId(visitorId)
                .setQuery(queryPhrase)
                .setPageSize(pageSize)
                .setOffset(offset)
                .setPageToken(pageToken)
                .build();
        System.out.println("Search request: " + searchRequest);
    
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html) client = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html).create()) {
          [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) searchResponseFirstPage = client.search(searchRequest).getPage().getResponse();
          if (searchResponseFirstPage.[getTotalSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html#com_google_cloud_retail_v2_SearchResponse_getTotalSize__)() == 0) {
            System.out.println("The search operation returned no matching results.");
          } else {
            System.out.println("Search response: " + searchResponseFirstPage);
          }
    
          // PASTE CALL WITH NEXT PAGE TOKEN HERE:
    
          // PASTE CALL WITH OFFSET HERE:
        }
      }
    }
    

#### Page token

To jump to the next page, you could use `page_token`. For example, suppose you send the following `SearchRequest`.

### JSON
    
    
    {
      placement: 'projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/placements/default_search'
      visitor_id: 'VISITOR_ID'
      query: 'shoes'
      page_size: 5
    }

From `SearchResponse`, you can get the resulting products with top 5 relevance, along with a `next_page_token`.

### JSON
    
    
    {
      results: [
        products{...}, products{...}, products{...}, products{...}, products{...}
      ]
      next_page_token: "wY4ETNkBDOlVjZ0YWLzUmM40SMhVjMtADMwATL5UGN5MGZlVDJaIQ5LaYsQUw9fC6lIwgE1EgC"
      total_size: 100
      search_token: "NtQKDAiXt4_3BRDCg_jnARABGiQ1ZWRjOTRlOC0wMDAwLTI1YTEtODJlMy1mNGY1ZTgwZDUxOGM"
    }

To get the result products with the next 5 relevance (6th to 10th), you would set `page_token` using the same `placement`, `visitor_id`, and `query` as `next_page_token` from the previous `SearchResponse`.

### Java
    
    
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html);
    import com.google.cloud.retail.v2.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html);
    import com.google.cloud.retail.v2.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html);
    
    public static void searchProducts_withNextPageToken(String query, int pageSize)
        throws IOException, InterruptedException {
      try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html) searchClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html).create()) {
        [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) firstRequest = [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
            .setPlacement(DEFAULT_SEARCH_PLACEMENT_NAME)
            .setBranch(DEFAULT_BRANCH_NAME)
            .setVisitorId(VISITOR_ID)
            .setQuery(query)
            .setPageSize(pageSize)
            .build();
    
        [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) firstResponse = searchClient.search(firstRequest).getPage()
            .getResponse();
        System.out.println("First search response: " + firstResponse);
    
        [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) secondRequest = [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
            .setPlacement(DEFAULT_SEARCH_PLACEMENT_NAME)
            .setBranch(DEFAULT_BRANCH_NAME)
            .setVisitorId(VISITOR_ID)
            .setQuery(query)
            .setPageSize(pageSize)
            .setPageToken(firstResponse.[getNextPageToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html#com_google_cloud_retail_v2_SearchResponse_getNextPageToken__)())
            .build();
    
        [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) secondResponse = searchClient.search(secondRequest).getPage()
            .getResponse();
        System.out.println("Second search response: " + secondResponse);
      }
    }

In this example, `SearchRequest` looks like this:

### JSON
    
    
    {
      placement: 'projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/placements/default_search'
      visitor_id: 'VISITOR_ID'
      query: 'shoes'
      page_size: 5
      page_token: "wY4ETNkBDOlVjZ0YWLzUmM40SMhVjMtADMwATL5UGN5MGZlVDJaIQ5LaYsQUw9fC6lIwgE1EgC"
    }

#### Offset

In some other cases, instead of navigating from page to page or getting results with top relevance, you could directly jump to a particular position with `offset`.

For example, if you want the tenth page of the results when the page size is 5, then you could set the `offset` to be 45, which is calculated by (10 - 1) * 5.

### JSON
    
    
    {
      placement: 'projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/placements/default_search'
      visitor_id: 'VISITOR_ID'
      query: 'shoes'
      page_size: 5
      offset: 45
    }

## Search performance tiers

Search offers several search performance tiers that increasingly improve your results. For example, for text query search use cases, results might be based solely on relevance. As you unlock more advanced performance tiers, search can return results that are based on relevance, popularity, revenue optimization, and personalization.

Search automatically unlocks higher performance tiers when you upload catalog and user event data that meets the minimum requirements of each tier.

For more information about using this page to view data quality and search performance tiers, see [Unlock search performance tiers](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality). The [**Data quality**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data_quality/) page on the AI Commerce Search in Gemini Enterprise for Customer Experience console provides an assessment of which requirements you have met for each tier.

## Evaluate text search and browse results

Before you update your website code to request text search or browse search results, you can preview the results to confirm that your serving config is working as you expect.

For more information about serving configs, see [About serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs).

You can preview serving config results either from the **Evaluate** page, or by going to a serving config's **Details** page in the console and clicking its **Evaluate** tab. The following steps show you how to preview from the **Evaluate** page.

To preview the results returned by your serving configuration:

###  Text search 

  1. Go to the **Evaluate** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Evaluate page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/)

  2. Click the **Search** tab.

**Note:** The **Search** tab is available only if you have search turned on. For instructions to turn it on, go to [Before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up).
  3. Select the serving config that you want to preview.

  4. Select the catalog branch that contains the catalog you want to preview.

  5. Optional: Enter a visitor ID to preview search results for that user.

  6. Optional: Enter a user ID to preview search results for that user.

  7. Optional: Enter a search time to preview search results that would appear at the specified time.

For example, if you have promoted certain products for a special sale, you can see results as they would appear on that day.

  8. Optional: Select facets to display alongside the search results and click **OK** to apply them.

The facets you select are used to generate a list of facet filters that appear under **Add facets** after you perform the initial search. These facet filters can include facets other than those you select in this step, such as dynamic facets.

  9. Enter a text-based search query to preview search results for that query.

  10. Click **Search preview** or press enter in any input field to see the results.

Search results are displayed with their available thumbnail images.

If your search triggers a redirect control, a notice appears that displays the redirect URI.

  11. Optional: Click the **Grid** icon or the **List** icon to switch how your search results are displayed in preview.

  12. Optional: If you selected facets to appear alongside your results, select one or more facet values from the facets list to filter results by those values. The results are automatically updated upon selection.

When you select multiple values of the same facet, they are applied as an OR operator would be, and values across different facets are applied as an AND operator would be. For example, after selecting the facets **color** and values "blue" and "gold", and the **material** values "cotton" and "polyester". Your search results results must have either "blue" or "gold" as an attribute, and must also have either "cotton" or "polyester" as an attribute.




###  Browse 

  1. Go to the **Evaluate** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Evaluate page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/)

  2. Click the **Browse** tab.


**Note:** The **Browse** tab is available only if you have search turned on. For instructions to turn it on, go to [Before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up).

  1. Select the serving configuration that you want to preview.

  2. Select the catalog branch that contains the catalog you want to preview.

  3. Optional: Enter a visitor ID to preview results for that user.

  4. Optional: Enter a user ID to preview results for that user.

  5. To preview how results would look with a specific filter added, enter a filter string. Use the filter expression syntax specified in the [Filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order#filter) documentation.

  6. Optional: Enter a browse time to preview results that would appear at the specified time.

For example, if you have promoted certain products for a peak sale event, you can see results as they would appear on that day.

  7. Enter the page category that you are testing browse results for.

  8. Optional: Select facets to display alongside the results and click **OK** to apply them.

The facets you select are used to generate a list of facet filters that appear under **Add facets** after you perform the initial search. These facet filters can include facets other than those you select in this step, such as dynamic facets.

  9. Click **Browse preview** or press enter in any input field to see the results.

Results are displayed with their available thumbnail images.

  10. Optional: Click the **Grid** icon or the **List** icon to switch how your results are displayed in preview.

  11. Optional: If you selected facets to appear alongside your results, select one or more facet values from the facets list to filter results by those values. The results are automatically updated upon selection.

When you select multiple values of the same facet, they are applied as an OR operator would be, and values across different facets are applied as an AND operator would be. For example, after selecting the facets **color** and **material** , you might then filter your search results by selecting the color values "blue" and "gold", and the material values "cotton" and "polyester". Your results must have either "blue" or "gold" as an attribute, and must also have either "cotton" or "polyester" as an attribute.




To see the **Details** page for the serving config you're previewing, click **View serving config** under the **Select serving config** field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
