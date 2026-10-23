---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/result-size/
title: Query expansion \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:47.603436+00:00
---

# Query expansion  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/result-size/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Query expansion Stay organized with collections  Save and categorize content based on your preferences. 

Query expansion is the incremental loosening of query constraints to include more results when none or too few are initially found. This leads to an adjustment of the result size per query.

When there are no relevant documents for a query, query expansion returns less relevant documents to ensure it doesn't return zero search results.

Unlike [dynamic faceting](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview) or [serving controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules), for example, query expansion cannot be configured directly in the Google Cloud console. Instead, you will need to configure query expansion programmatically for each search request. Read further to find out how to configure query expansion in the API. 

## Query expansion tutorial

This tutorial shows you how to enable the query-expansion feature. When a shopper uses an ambiguous or a multi-word search phrase, they can get an empty response. After turning on query expansion, the request is analyzed and the expanded list of products based on the parsed search query gets returned.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_query_expansion_select_language&show=ide&environment_deployment=ide)

* * *

## Query expansion overview

Query expansion is a powerful feature designed to improve search recall and prevent zero-result scenarios, particularly for long-tail or complex user queries.

Instead of returning no results when an exact match isn't found in the product catalog, query expansion identifies and displays related or alternative products. This enhances user experience and can increase conversion rates.

Key use cases for query expansion are:

  * **Long-tail queries** : For highly specific searches, such as _diabetic high-protein low-fat organic milk,_ the catalog might not have a perfect match. Query expansion can return products that match parts of the intent, such as products tagged with attributes or attribute values of diabetic-friendly milk, high-protein milk.
  * **Alternative products** : If your users search for a brand or product not in the catalog, such as _Starbucks coffee 100ml,_ query expansion can suggest alternative coffee brands available for purchase, preventing a dead-end search.



These next sections outline the functionality, trigger mechanism, and configuration nuances of the query-expansion feature in AI Commerce Search, with a specific focus on the critical role of the [canonical filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.canonical_filter).

### Query expansion trigger mechanism

The decision to activate query expansion or a given search query is automated and based on a quickly configurable canonical filter rule.

  * **Trigger condition** : Query expansion is triggered only if the initial search with the canonical filter query yields fewer than 3 product results.
  * **Threshold** : This threshold of 3 by default can be changed. It works well for most ecommerce use cases, ensuring that query expansion is activated only if and when the initial result set is genuinely sparse.



### Configure query expansion in the API

Query expansion is configured programmatically per request using the API as follows:

  * **API configuration** : You control query expansion by including the `queryExpansionSpec` object in your `SearchRequest`.

  * **Settings** : Within the `queryExpansionSpec`, you set the `condition` field to `AUTO` to enable the feature or `DISABLED` to turn it off, which is the default if unspecified.

  * **Pinning** : You can optionally set `pinUnexpandedResults` to `true` in the request to ensure that exact matches for the original query appear at the top of the search results, followed by the expanded results. For more information, read the [pinning](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pinning) page.




### Configure canonical filters

For query expansion to trigger effectively, you must correctly configure the `canonical_filter` in your search request.

To correctly implement query expansion, it is crucial to understand the two primary filter parameters in a search request, top-level filters and canonical filters.

  * **Top-level filter (`filter`)**: This is the main filter applied to the search results before they return to the user. It's a combination of two potential layers:

    * **Business/base filter** : Predefined rules applied to all searches, often without direct user input, such as `inStock=TRUE, category="groceries", storeId="XYZ"`.

    * **User-selected facet filters** : Filters applied dynamically by the user while interacting with the search interface, such as by selecting facet filters for _brand="Adidas", size="L"._

  * **Canonical filters (`canonical_filter`)**: This is a special-purpose filter used exclusively by the query-expansion decision module. Its sole job is to define the catalog view against which the query expansion trigger condition (less than five results) is evaluated.

**Important:** The canonical filter does not filter the final search results returned to the user. Instead, that is the job of the main filter.



### Core canonical filter functions

The canonical filter is designed to distinguish between an organically poor search result and a result set that was intentionally narrowed by the user. It can either be broad to exclude business logic to account for user-applied filters, or narrowed to trigger the query expansion when needed, depending on the user scenario.

#### Scenario 1

  * **User journey** : User searches for _t-shirt_ and gets thousands of results. There's a default `business_filter`, such that, for example, it filters only in-stock products and products that match a custom store-level attribute. User then applies facet filters for _brand="Adidas" and size="L",_ which reduces the result count to two. 
  * **If`canonical_filter` were set to include the same conditions `filter`** (such as `AVAILABILITY: IN_STOCK AND color: "Red"`: The query-expansion decision system would see only 2 results and incorrectly trigger query expansion, flooding the user with related but irrelevant products, such Nike t-shirts, breaking the user's explicit filtering.
  * **The correct setting is`canonical_filter = business filter`**. The query-expansion decision should be made based on the initial query, excluding user-selected facets. By keeping the `canonical_filter` broad, the system correctly identifies that there are plenty of matching products in the catalog, enabling it to respect the user's strict filters without forcing an expansion.



#### Scenario 2

  * **User journey** : The user searches for _adidas t-shirt with black graphic prints_ and it yields only one or two results, if any. There is a default `business_filter` such that, for example, it filters only in-stock products and products that match a custom store level attribute.
  * If `canonical_filter` is not set or not configured correctly, the search with canonical filter could find products that match the query but are out of stock or from a different store, meaning a different value of custom store level attribute. In this case, the query expansion is not triggered.
  * **The correct setting is`canonical_filter = business filter`**. With this setting, the query-expansion decision finds fewer than three products for the given long query, then triggers a query expansion and bring related products to the original query, meaning in-stock products that match the store level attribute. This expands the search results to include black graphic printed t-shirts from a different brand, other colored graphic printed t-shirt, or other t-shirt products from the queried brand. Include business constraints for this use case of `canonical_filter`. 



## Query expansion best practices

The canonical filter should almost always be set to be identical to your business or base filter. This ensures that the query-expansion module evaluates the query's potential against the same broad catalog view that your users initially see before they start applying facets.

### End-to-end search and query-expansion process flow

When a search request is made, several parallel processes occur:

  * **Request received** : The API receives the search request containing the query, the main `filter`, and the `canonical_filter`.

  * **Query-expansion decision search** : In parallel, the query-expansion decision module performs its own internal search using the query combined with the canonical filter.

  * **Result count check** : The module checks the number of products returned from its internal search.

    * **If results are five or more** : Query expansion is _not_ triggered. The standard search results proceed to the final filtering step.
    * **If results are less than five** : Query expansion _is_ triggered. The model systematically loosens the query to find related products. For example, the model might find for _Pixel 5 phone,_ Pixel 4 phones, Pixel earbuds, or even Samsung phones.


  1. **Final filtering** : The product set (the original set or the expanded set from query expansion) is passed to the final stage. In this case, the top-level filter, containing business rules and any user-selected facets, is strictly applied.


  * **Response sent** : The final filtered list of products is returned in the API response.

**Important:** Even if query expansion finds many alternative products, they are filtered out from the final response if they don't match the main filter. For example, if query expansion finds a t-shirt, but the main filter is `category="groceries"`, the t-shirt is not shown.

### Advanced use case of selective query-expansion activation

You can strategically configure the filters to enable or disable query expansion for specific parts of your catalog. 

Consider the scenario of a large catalog containing groceries, electronics, and fashion apparel. For such a scenario, you want to have the following aspects in mind.

#### Goal

Enable query expansion for hard-to-find or scarce grocery queries but show zero results for electronics or fashion items. The business need here is to only enable query expansion selectively on the groceries part.

#### Configuration

For this use case scenario, the selective query expansion can be configured as follows:

  * **`canonical_filter`** : Set it to be **broad**. It should include all categories: Groceries, electronics, and fashion, plus any base rules like stock availability, defining the canonical filter with `category="groceries" OR category="electronics" OR category="fashion") AND inStock=TRUE`)
  * **`filter`** : Set it to be **narrow** , based on the user's context. For a user in the grocery section, the filter would be `category="groceries" AND inStock=TRUE`.



#### How it works

Selective query expansion works in this scenario as follows:

  * **User searches for "iPhone 20":** The query expansion module uses the broad canonical_filter, finds existing iPhone models (< 5 results), and decides **not** to trigger query expansion. The standard search results (existing iPhones) are then passed to the main filter, which blocks them because `category="electronics"` does not match `category="groceries"`. The user correctly sees zero results.
  * **User searches for *high-protein diabetic milk:** * The query-expansion module uses the broad `canonical_filter` and finds <5 results, thus triggering query expansion by finding related milk products. These products are passed to the main filter. Since they match `category="groceries"`, these products are successfully returned to the user.



By manipulating the scope of the `canonical_filter` (the decision-making view) and the main `filter` (the final output view), you gain precise control over the search experience.

## Example dataset

This page uses the following dataset as an example. Expand it to view the fields within the sample product description dataset.

#### Example product dataset

ID | title | brands | categories | price_info.price  
---|---|---|---|---  
"nest_mini_2nd_gen" | "Nest Mini (2nd gen)" | ["Google", "Nest"] | ["Nest > speakers and displays"] | 49.00  
"nest_audio" | "Nest Audio" | ["Google", "Nest"] | ["Nest > speakers and displays"] | 99.99  
"nest_hub_max" | "Nest Hub Max" | ["Google", "Nest"] | ["Nest > speakers and displays"] | 229.00  
"nest_hub" | "Nest Hub" | ["Google", "Nest"] | ["Nest > speakers and displays"] | 88.99  
"google_home_max" | "Google Home Max" | ["Google", "Nest"] | ["Nest > speakers and displays"] | 299.00  
"google_home_mini" | "Google Home Mini" | ["Google", "Nest"] | ["Nest > speakers and displays"] | 49.00  
"google_pixel_5" | "Google Pixel 5" | ["Google", "Pixel"] | ["Pixel > phones"] | 699.00  
"google_pixel_4a_with_5g" | "Google Pixel 4a with 5G" | ["Google", "Pixel"] | ["Pixel > phones"] | 499.00  
"google_pixel_4a" | "Google Pixel 4a Phones" | ["Google", "Pixel"] | ["Pixel > phones"] | 349.00  
"google_pixel_stand" | "Google Pixel Stand" | ["Google", "Pixel"] | ["Pixel > featured accessories"] | 79.00  
"google_pixel_buds" | "Google Pixel Buds" | ["Google", "Pixel"] | ["Pixel > featured accessories"] | 179.00  
"google_pixel_5_case" | "Google Pixel 5 Case" | ["Google", "Pixel"] | ["Pixel > featured accessories"] | 40.00  
"google_pixel_4a_5g_case" | "Google Pixel 4a (5G) Case" | ["Google", "Pixel"] | ["Pixel > featured accessories"] | 40.00  
"google_pixel_4a_case" | "Google Pixel 4a Case" | ["Google", "Pixel"] | ["Pixel > featured accessories"] | 40.00  
  
## Query expansion broadens search queries for more results

Query expansion increases the recall for query terms with few results, especially long tail queries. The broadened query yields a greater search result size.

This search feature is driven by a [specification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/QueryExpansionSpec) determining query-expansion conditions. It includes a `pinUnexpandedResults` option that's off by default. When set to `true`, it displays unexpanded products at the top of search results. The top is followed by the expanded results.

### Java
    
    
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html);
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).[QueryExpansionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.QueryExpansionSpec.html);
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).[QueryExpansionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.QueryExpansionSpec.html).[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Condition.html);
    import com.google.cloud.retail.v2.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html);
    import com.google.cloud.retail.v2.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html);
    
    public static void searchProductsWithQueryExpansion(String query, int pageSize,
        [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Condition.html) condition) throws IOException, InterruptedException {
      [QueryExpansionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.QueryExpansionSpec.html) queryExpansionSpec = [QueryExpansionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.QueryExpansionSpec.html).newBuilder()
          .setCondition(condition)
          .build();
    
      [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) searchRequest = [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
          .setPlacement(DEFAULT_SEARCH_PLACEMENT_NAME)
          .setBranch(DEFAULT_BRANCH_NAME)
          .setVisitorId(VISITOR_ID)
          .setQuery(query)
          .setPageSize(pageSize)
          .[setQueryExpansionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.Builder.html#com_google_cloud_retail_v2_SearchRequest_Builder_setQueryExpansionSpec_com_google_cloud_retail_v2_SearchRequest_QueryExpansionSpec_)(queryExpansionSpec)
          .build();
    
      try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html) searchClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html).create()) {
        [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) response = searchClient.search(searchRequest).getPage().getResponse();
        System.out.println("Search response: " + searchResponse);
      }
    }

For example, if you search for _Google Pixel 5_ without query expansion, the result is restricted to `google_pixel_5` IDs. However, with query expansion, you might also get `google_pixel_4a_with_5g`, `google_pixel_4a`, and `google_pixel_5_case` IDs in the example product description dataset as well.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
