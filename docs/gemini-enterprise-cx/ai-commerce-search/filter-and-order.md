---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order/
title: Filter and order results \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:19.321056+00:00
---

# Filter and order results  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Filter and order results Stay organized with collections  Save and categorize content based on your preferences. 

This page describes filtering and ordering with search.

## Semantic filtering optimizes non-default sorting

AI Commerce Search is designed to show a wide variety of results, including marginally relevant items that are popular or trending. This is effective in default searches (sorted by relevance), but in non-default searches that use the `order_by` feature, such as sort-by-price, less relevant items can appear more prominently due to lower price, for example.

To ameliorate this effect, AI Commerce Search has introduced semantic embedding-based filtering to remove these less relevant items from non-default search results, improving user experience. 

This intended behavior could, however, lead fewer search results overall. Disabling filtering can impact search-result quality. So if fewer search results is of concern, contact [support](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/support).

## Filtering tutorial

This tutorial demonstrates the filtering feature. It lets you fine-tune search requests according to your or your customer's needs. You can filter by single or multiple fields, filter by text or numeric fields, or both. You can use an expression language to construct a predicate for each field or combine different expressions using logical operators. For example, a shopper looking for shoes can use filters to narrow their search to their preferred brand and color.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_filtering_select_language&show=ide&environment_deployment=ide)

* * *

## Ordering tutorial

This tutorial shows how to order items in a search response. When an end user looks for a product on your site, they are shown results ordered by multiple fields. For example, a user is searching for a dress with the best price and discount. Price and discount are multiple fields here. The user will see the dresses ordered by price, and for the dresses with the same price, ordered by discount.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_ordering_select_language&show=ide&environment_deployment=ide)

* * *

## Example dataset

This page uses the following dataset as an example. Only the fields necessary for the example are included.

####  Example product dataset 

id | title | brands | categories | price_info.price  
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
  
## Filter

### Java
    
    
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html);
    import com.google.cloud.retail.v2.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html);
    import com.google.cloud.retail.v2.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html);
    
    public static void searchFilteredProducts(String query, int pageSize,
        String filter) throws IOException, InterruptedException {
      [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) searchRequest = [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
          .setPlacement(DEFAULT_SEARCH_PLACEMENT_NAME)
          .setBranch(DEFAULT_BRANCH_NAME)
          .setVisitorId(VISITOR_ID)
          .setQuery(query)
          .setPageSize(pageSize)
          .setFilter(filter)
          .build();
    
      try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html) searchClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html).create()) {
        [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) response = searchClient.search(searchRequest).getPage().getResponse();
        System.out.println("Search response: " + searchResponse);
      }
    }

The filter expression syntax can be summarized by the following [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#:%7E:text=In%20computer%20science%2C%20extended%20Backus,as%20a%20computer%20programming%20language):
    
    
      # A single expression or multiple expressions that are joined by "AND" or "OR".
      **filter** = **expression** , { " AND " | "OR", **expression** };
    
      # Expressions can be prefixed with "-" or "NOT" to express a negation.
      **expression** = [ "-" | "NOT " ],
        # A parenthetical expression.
        | "(", expression, ")"
        # A simple expression applying to a text field.
        # Function "ANY" returns true if the field contains any of the literals.
        ( **text_field** , ":", "ANY", "(", **literal** , { ",", **literal** }, ")"
        # A simple expression applying to a numerical field. Function "IN" returns true
        # if a field value is within the range. By default, lower_bound is inclusive and
        # upper_bound is exclusive.
        | **numerical_field** , ":", "IN", "(", **lower_bound** , ",", **upper_bound** , ")"
        # A simple expression that applies to a numerical field and compares with a double value.
        | **numerical_field** , **comparison** , double );
    
      # A lower_bound is either a double or "*", which represents negative infinity.
      # Explicitly specify inclusive bound with the character 'i' or exclusive bound
      # with the character 'e'.
      **lower_bound** = ( double, [ "e" | "i" ] ) | "*";
    
      # An upper_bound is either a double or "*", which represents infinity.
      # Explicitly specify inclusive bound with the character 'i' or exclusive bound
      # with the character 'e'.
      **upper_bound** = ( double, [ "e" | "i" ] ) | "*";
    
      # Supported comparison operators.
      **comparison** = "<=" | "<" | ">=" | ">" | "=";
    
      # A literal is any double quoted string. You must escape backslash (\) and
      # quote (") characters.
      **literal** = double quoted string;
    
      **text_field** = see the table below;
    
      **numerical_field** = see the table below;

The supported textual fields are summarized in the following table.

field | description  
---|---  
"productId" | The product ID (the last segment of Product.name).  
"brands" | The Product.brands.  
"categories" | The Product.categories.  
"genders" | The Audience.genders.  
"ageGroups" | The Audience.age_groups.  
"availability" | The Product.availability. Value is one of "IN_STOCK", "OUT_OF_STOCK", PREORDER", "BACKORDER".  
"colorFamilies" | The ColorInfo.color_families.  
"colors" | The ColorInfo.colors.  
"sizes" | The Product.sizes.  
"materials" | The Product.materials.  
"patterns" | The Product.patterns.  
"conditions" | The Product.conditions.  
"attributes.key" | The textual custom attribute in Product object. Key can be any key in the Product.attributes map, if the attribute values are textual.   
"pickupInStore" | The FulfillmentInfo.place_ids for type "pickup-in-store".  
"shipToStore" | The FulfillmentInfo.place_ids for type "ship-to-store".  
"sameDayDelivery" | The FulfillmentInfo.place_ids for type "same-day-delivery".  
"nextDayDelivery" | The FulfillmentInfo.place_ids for type "next-day-delivery".  
"customFulfillment1" | The FulfillmentInfo.place_ids for type "custom-type-1".  
"customFulfillment2" | The FulfillmentInfo.place_ids for type "custom-type-2".  
"customFulfillment3" | The FulfillmentInfo.place_ids for type "custom-type-3".  
"customFulfillment4" | The FulfillmentInfo.place_ids for type "custom-type-4".  
"customFulfillment5" | The FulfillmentInfo.place_ids for type "custom-type-5".  
"inventory(place_id,attributes.key)" | The textual custom attribute in Inventory.  
  
The supported numerical fields are summarized in the following table.

field | description  
---|---  
"price" | The PriceInfo.price.  
"discount" | The discount. Computed by (original_price - price) / original_price.  
"rating" | The Rating.average_rating.  
"ratingCount" | The Rating.rating_count.  
"attributes.key" | The numerical custom attribute in Product object. Key can be any key in the Product.attributes map, if the attribute values are numerical.   
"inventory(place_id,price)" | The inventory price.  
"inventory(place_id,original_price)" | The original inventory price.  
"inventory(place_id,attributes.key)" | The numerical custom attribute in Inventory.  
  
At most, 10 nested conjunctions or disjunctions are allowed.

For example, to search for a Google product in the following situations respectively, you could set `query` as "Google" and set `filter` as the values shown in the following table:

scenario | filter  
---|---  
not a Pixel accessory | "NOT categories: ANY(\"Pixel > featured accessories\")"  
"cheaper than 100 dollars" | "price: IN(*, 100.0e)"  
"Nest speaker not cheaper than 80 dollars" | "(categories: ANY(\"Nest > speakers and displays\")) AND (price: IN(80.0i, *))"  
**Note:** Due to the built-in pagination capability of Search, it's good to maintain local inventory fields when filtering. For more information, see [Update local inventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates).

## Order

### Java
    
    
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html);
    import com.google.cloud.retail.v2.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html);
    import com.google.cloud.retail.v2.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html);
    
    public static void searchOrderedProducts(String query, int pageSize,
        String orderBy) throws IOException, InterruptedException {
      [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) searchRequest = [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
          .setPlacement(DEFAULT_SEARCH_PLACEMENT_NAME)
          .setBranch(DEFAULT_BRANCH_NAME)
          .setVisitorId(VISITOR_ID)
          .setQuery(query)
          .setPageSize(pageSize)
          .setOrderBy(orderBy)
          .build();
    
      try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html) searchClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html).create()) {
        [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) response = searchClient.search(searchRequest).getPage().getResponse();
        System.out.println("Search response: " + searchResponse);
      }
    }

The supported orderable fields are summarized in the following table.

field | description  
---|---  
"productId" | The product ID (the last segment of Product.name).  
"title" | The Product.title.  
"brands" | The Product.brands.  
"categories" | The Product.categories.  
"genders" | The Audience.genders.  
"ageGroups" | The Audience.age_groups.  
"price" | The PriceInfo.price.  
"discount" | The discount. Computed by (original_price - price) / price.  
"rating" | The Rating.average_rating.  
"ratingCount" | The Rating.rating_count.  
"attributes.key" | The custom attribute in Product object. Key can be any key in the Product.attributes map.  
"inventory(place_id,price)" | The inventory price.  
"inventory(place_id,original_price)" | The original inventory price.  
"inventory(place_id,attributes.key)" | The numerical or textual custom attribute in Inventory.  
  
By default, the order is ascending. Descending order can be specified by "desc" suffix, such as, "rating desc".

For a numeric field with multiple values, for example, a repeated field or a field that is set for variant products, the minimum value is used for sorting by ascending order and the maximum value is used for sorting by descending order.

Ordering by multiple fields is supported through the use of comma-separated fields in order of priority. The lower priority fields are used to order items with equal values for higher priority fields. For example, "rating desc, price" orders items with the same rating by price.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
