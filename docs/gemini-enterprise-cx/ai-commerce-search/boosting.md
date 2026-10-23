---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/boosting/
title: Boost results \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:40.622009+00:00
---

# Boost results  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/boosting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Boost results Stay organized with collections  Save and categorize content based on your preferences. 

AI Commerce Search offers a feature that lets you specify records that should be elevated in searches. You can control the result ranking by applying a boosting rule to prioritize or de-prioritize returned search items.

Boosting lets you control the ranking of results by promoting (boosting) or demoting (burying) specific items based on criteria you define. Unlike filtering, which removes items from the result set, boosting adjusts the position of items that are already eligible to be returned.

## Boost and filter overrides

**Note:** Filtering rules always take precedence over boost rules. For more information about filtering and ordering search results, see [Filter and order results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order).

These are examples of common filter types that take precedence over boosting rules:

  1. **User-specified**. These can be things like price or brand. They appear to the end user as tiles or facets on the website.


  * **Topicality (relevance)**. These filters only exist for search queries (not browsing). They exclude less relevant products from the search results. For example, the search _refrigerator_ doesn't return microwaves or accessories, such as refrigerator handles. The filter recognizes not to boost a microwave for a refrigerator search.



## Boosting rules

Boosting rules can only be applied when there's a base relevance score, such as in relevance-ordered searches or browse results with pre-sort scores. Boosting is a multiplier function applied to search and browse results. The syntax and logic of boosting can be broken down into:

  * **Availability**. Boosting cannot override availability rules. If an item is filtered out (such as out-of-stock), boosting it won't make it appear.

  * **Operators**. You can use operations like greater-than and less-than for numerical fields in boosting conditions, which are not available in standard strict filtering.




### Boost or bury values

One product can be conditioned by multiple boost or bury rules, which are set in the [`boostSpec`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec) class of the Search API. A boost value is a floating-point number between **-1.0** and **1.0**.

  * **Positive value (0.0 to 1.0)** : Promotes the item, moving it higher in the results. A value of 1.0 gives the maximum promotion.

  * **Negative value (-1.0 to 0.0)** : Demotes (buries) the item, moving it lower in the results. A value of -1.0 gives the maximum demotion.




### Multiple boost or bury rules on a single product

Multiple boost or bury rules can affect a product, with either a sum or max of the boost values determining the final score. When several boosting rules are applied to the same product, always check if another product's score has ousted the product from the top spot. The maximum mode is set to default so that this problem is less likely to occur.

Assume one product gets boosts of 2, 3, and 0.5, and another product gets one boost of 0.5. Although the product only received a 0.5 boost score, when it's boosted repeatedly, it outranks the other product. Carefully check the boosting specification to make sure it's not overlapping—or is, as intended.

#### Conflict resolution

If multiple boosting rules apply to the same product, you can define how they interact.

  * **Max boost rule (default**): AI Commerce Search checks whichever is the maximum value and ignores the other rules.

  * **Sum of boost effect (alternative setting)** : If there's a demotion plus a promotion, AI Commerce Search adds up the values of all applicable boost and bury rules. This allows for a cumulative effect. The resulting sum is either a lowered boost or net bury effect.




## Configure boost

To configure a dataset with boost or bury rules, you define conditions based on product attributes (such as brand or price) and assign a boost value between **-1.0 (bury)** and **1.0 (boost)** to adjust the ranking score of matching items. The following products are available for configuring boost or bury controls:

  * **Search** : Topicality filter plus any other user-applied filters such as on-site facets. Read more on how to configure boost for search.

  * **Browse** : Since there is no text-query, only the user-applied filters are applied. Filters are also applied to check that the product (let's say, suits) belongs to the correct product category (not sweaters, for example). Read more on how to configure boost for recommendations.




### Example dataset

View example product dataset 

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
  
### Configuration options

In AI Commerce Search, boosting is applied as a multiplier to the base relevance score generated by the search algorithm. You can configure boosting rules directly in a search request using a boost specification or by attaching serving controls to a serving configuration. In the response, items matching these conditions receive a modified relevance score, causing them to appear higher or lower in the results list without being removed entirely. To configure a search boost or bury control:

###  Cloud console 

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. Under the **Serving controls** tab, click **Edit** _edit_ to the right of a control.

  3. In the **Edit control** fly-out, click the field under **Control name** field to modify the control name.

  4. Optional: For search, in the **Triggers** section, select what type of user behavior triggers this control. The **Browse categories** and **Search** sections are dimmed.

  5. Optional: Edit **Matching search terms**.

**Note:** If you specify a category or query term condition plus time range conditions, the control only applies when both conditions are met.
  6. Optional: Click the **Add Time Range** option to add one or more time ranges during which this control can be applied.

**Note:** If you specify time range conditions in addition to this type of condition, the control is applied only if both conditions are met.
  7. Click **Continue** to proceed to the **Actions** section.

  8. Add filters for product attributes in the **Boost/bury product** field.

Use the filter expression syntax documented in [Filter and order results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order). For example, to specify red and blue versions of "product1" and "product2": `(id: ANY("product1","product2")) AND (colorFamily: ANY("Red","Blue"))`

  9. For **Boost/bury value** , use the slider to set the strength of the boost. Positive values boost the results, and negative values bury them. Click **Continue**.

  10. In the **Serving configs** section, select which serving configs to apply the control to.

  11. Submit your control settings.




You can now find the boost or bury control rule added as a new **Control type** listed under the **Serving Controls** for your project. Find out how to create a new boost and bury control under [Create controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#boost-bury).

###  JSON 

This demonstrates an example of boosting by price.

Suppose that you want to prioritize the cheaper products (less than 95 US$) and de-prioritize the expensive ones (higher than 95 US$). You can apply a boost specification.
    
    
    {
      "condition_boost_specs": [
        {
          "condition": "price: IN(*, 95.0e)",
          "boost": 0.5
        },
        {
          "condition": "price: IN(95.0e, *)",
          "boost": -0.5
        }
      ]
    }

In this example, products under 95 US dollars receive a promotion (0.5), while those over 95 US dollars are demoted (-0.5).

In the result, `"nest_mini_2nd_gen"`, `"google_home_mini"` and `"nest_hub"` might be the first three, while `"nest_audio"`, `"nest_hub_max"` and `"google_home_max"` might be last three. However, no specific order is predetermined, in contrast to ordering by price, as discussed in [Filter and order results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order).

### Boost in search

For search, apply the ranking score of matching items dynamically by including a boost specification (`boostSpec`) with `condition_boost_specs` directly in the `SearchRequest`.

#### Conditions and triggers

Search boosting can be conditional. You can trigger a boost rule based on these conditions:

  * **Query terms** : Apply the boost only when the user searches for specific terms (such as boosting winter coats when the query contains _jacket)._

  * **Time ranges** : Apply the boost only during a specific promotional period.

  * **Global** : Apply the boost to all queries served by a specific configuration.




#### Example search request and response

In the example dataset shown previously, if you search for "Google speaker", then you would get "nest_mini_2nd_gen", "nest_audio", "nest_hub_max", "nest_hub", "google_home_max" and "google_home_mini" in no specific order.

View example search request and response 

### Java
    
    
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html);
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).[BoostSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.BoostSpec.html);
    import com.google.cloud.retail.v2.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).[BoostSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.BoostSpec.html).[ConditionBoostSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.BoostSpec.ConditionBoostSpec.html);
    import com.google.cloud.retail.v2.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html);
    import com.google.cloud.retail.v2.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html);
    
    public static void searchProductsWithBoostSpec(String query, int pageSize,
        String condition, float boostStrength) throws IOException, InterruptedException {
      [BoostSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.BoostSpec.html) boostSpec = [BoostSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.BoostSpec.html).newBuilder()
          .[addConditionBoostSpecs](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.BoostSpec.Builder.html#com_google_cloud_retail_v2_SearchRequest_BoostSpec_Builder_addConditionBoostSpecs_com_google_cloud_retail_v2_SearchRequest_BoostSpec_ConditionBoostSpec_)([ConditionBoostSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.BoostSpec.ConditionBoostSpec.html).newBuilder()
              .setCondition(condition)
              .setBoost(boostStrength)
              .build())
          .build();
    
      [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html) searchRequest = [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchRequest.html).newBuilder()
          .setPlacement(DEFAULT_SEARCH_PLACEMENT_NAME)
          .setBranch(DEFAULT_BRANCH_NAME)
          .setVisitorId(VISITOR_ID)
          .setQuery(query)
          .setPageSize(pageSize)
          .setBoostSpec(boostSpec)
          .build();
    
      try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html) searchClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchServiceClient.html).create()) {
        [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SearchResponse.html) response = searchClient.search(searchRequest).getPage().getResponse();
        System.out.println("Search response: " + searchResponse);
      }
    }

### Boost in recommendations

Boosting for recommendations is managed using serving controls. Unlike search, recommendation boosting does not support query-based conditions (as there is no user query). Instead, the control applies to all predictions generated by the serving config it is attached to. For this reason, you typically configure recommendations by attaching boost or bury serving controls to the serving config, rather than passing a boosting specification in the request.

#### Supported fields for recommendations

When defining which products to boost in recommendations, use a filter expression. While standard recommendation _filtering_ is limited to textual fields, _boosting_ supports additional numerical fields.

**Field type** | **Supported fields** | **Description**  
---|---|---  
**Textual** | `productId`, `brands`, `categories`, `genders`, `ageGroups`, `colorFamilies`, `colors`, `sizes`, `title`,`materials`, `patterns`, `conditions`, `attributes.key`, `tags` | Standard fields available for both filtering and boosting. Note that `tags` are custom tags associated with the product.   
**Numerical** | `price`, `discount`, `rating`, `ratingCount` | **Exclusive to boost/bury.** These fields allow you to boost products based on price, discounts, or user ratings.   
  
For more information, see the [Boost/bury supported fields](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs#boost-fields) section in [Filter recommendations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs).

#### Boost highly rated products

Say you want to ensure that highly-rated movies appear higher in their "Others You May Like" recommendation panel. For this use case, create a serving control to boost items with a rating count greater than 100. Configure your controls, taking into account the following:

  * **Control Type** : Boost or bury

  * **Product Selection** : Recommendation

  * **Action** :

    * **Filter Expression** : `ratingCount > 100`

    * **Boost Value** : `0.5`




This control ensures that popular, well-rated items are prioritized in the recommendation list, while still maintaining personalization relevance for the user.

## Debug and troubleshoot

Every product is eligible for unlimited boosting, but user-applied filters eliminate products from the search response. To troubleshoot why a boosted product might not appear in search and browse results, check for:

  * **Multiple boost rules (including bury demotions)** : Check boost mode configuration (sum or max) and determine the final score.
  * **Relevance** : A product must be relevant for the query and pass the relevance filters. If a search query is for Nike shoes and the product title is _Air Jordans,_ the words don't match, but their close semantic relationship results in a high relevance score. A product title such as _yellow jacket_ has a low relevance score with a Nike search query. Similarly, if the product title is a cryptic model number that has no relationship to any word whatsoever, the relevance score will be low for any query.
  * **Filters** : Filtering rules override any boost rule, and prevent boosted products from appearing in results. The filter is always applied atop the boost. If a product has user-applied filters, or if a product category filters for browsing, the boost won't work at all.



## Boosting tutorial

This tutorial shows you some examples of product boosting.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_boosting_select_language&show=ide&environment_deployment=ide)

* * *

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
