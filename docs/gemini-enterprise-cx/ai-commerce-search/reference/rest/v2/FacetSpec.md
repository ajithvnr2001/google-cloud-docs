---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec/
title: FacetSpec \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:21.430376+00:00
---

# FacetSpec  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  FacetSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FacetKey
    * JSON representation



A facet specification to perform faceted search.

JSON representation  
---  
      
    
    {
      "facetKey": {
        object ([FacetKey](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey))
      },
      "limit": integer,
      "excludedFilterKeys": [
        string
      ],
      "enableDynamicPosition": boolean
    }  
  
Fields  
---  
`facetKey` |  `object (`[FacetKey](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey)`)` Required. The facet key specification.  
`limit` |  `integer` Maximum of facet values that should be returned for this facet. If unspecified, defaults to 50. The maximum allowed value is 300. Values above 300 will be coerced to 300.If this field is negative, an INVALID_ARGUMENT is returned.  
`excludedFilterKeys[]` |  `string` List of keys to exclude when faceting.By default, `[FacetKey.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.key)` is not excluded from the filter unless it is listed in this field.Listing a facet key in this field allows its values to appear as facet results, even when they are filtered out of search results. Using this field does not affect what search results are returned.For example, suppose there are 100 products with the color facet "Red" and 200 products with the color facet "Blue". A query containing the filter "colorFamilies:ANY("Red")" and having "colorFamilies" as `[FacetKey.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.key)` would by default return only "Red" products in the search results, and also return "Red" with count 100 as the only color facet. Although there are also blue products available, "Blue" would not be shown as an available facet value.If "colorFamilies" is listed in "excludedFilterKeys", then the query returns the facet values "Red" with count 100 and "Blue" with count 200, because the "colorFamilies" key is now excluded from the filter. Because this field doesn't affect search results, the search results are still correctly filtered to return only "Red" products.A maximum of 100 values are allowed. Otherwise, an INVALID_ARGUMENT error is returned.  
`enableDynamicPosition` |  `boolean` Enables dynamic position for this facet. If set to true, the position of this facet among all facets in the response is determined by Google Retail Search. It is ordered together with dynamic facets if dynamic facets is enabled. If set to false, the position of this facet in the response is the same as in the request, and it is ranked before the facets with dynamic position enable and all dynamic facets.For example, you may always want to have rating facet returned in the response, but it's not necessarily to always display the rating facet at the top. In that case, you can set enableDynamicPosition to true so that the position of rating facet in response is determined by Google Retail Search.Another example, assuming you have the following facets in the request:

  * "rating", enableDynamicPosition = true
  * "price", enableDynamicPosition = false
  * "brands", enableDynamicPosition = false

And also you have a dynamic facets enable, which generates a facet "gender". Then, the final order of the facets in the response can be ("price", "brands", "rating", "gender") or ("price", "brands", "gender", "rating") depends on how Google Retail Search orders "gender" and "rating" facets. However, notice that "price" and "brands" are always ranked at first and second position because their enableDynamicPosition values are false.  
  
## FacetKey

Specifies how a facet is computed.

JSON representation  
---  
      
    
    {
      "key": string,
      "intervals": [
        {
          object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Interval))
        }
      ],
      "restrictedValues": [
        string
      ],
      "prefixes": [
        string
      ],
      "contains": [
        string
      ],
      "caseInsensitive": boolean,
      "orderBy": string,
      "query": string,
      "returnMinMax": boolean
    }  
  
Fields  
---  
`key` |  `string` Required. Supported textual and numerical facet keys in `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` object, over which the facet values are computed. Facet key is case-sensitive.Allowed facet keys when `[FacetKey.query](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.query)` is not specified:

  * textual_field =
    * "brands"
    * "categories"
    * "genders"
    * "ageGroups"
    * "availability"
    * "colorFamilies"
    * "colors"
    * "sizes"
    * "materials"
    * "patterns"
    * "conditions"
    * "attributes.key"
    * "pickupInStore"
    * "shipToStore"
    * "sameDayDelivery"
    * "nextDayDelivery"
    * "customFulfillment1"
    * "customFulfillment2"
    * "customFulfillment3"
    * "customFulfillment4"
    * "customFulfillment5"
    * "inventory(placeId,attributes.key)"
  * numerical_field =
    * "price"
    * "discount"
    * "rating"
    * "ratingCount"
    * "attributes.key"
    * "inventory(placeId,price)"
    * "inventory(placeId,originalPrice)"
    * "inventory(placeId,attributes.key)"

  
`intervals[]` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Interval)`)` Set only if values should be bucketized into intervals. Must be set for facets with numerical values. Must not be set for facet with text values. Maximum number of intervals is 40.For all numerical facet keys that appear in the list of products from the catalog, the percentiles 0, 10, 30, 50, 70, 90, and 100 are computed from their distribution weekly. If the model assigns a high score to a numerical facet key and its intervals are not specified in the search request, these percentiles become the bounds for its intervals and are returned in the response. If the facet key intervals are specified in the request, then the specified intervals are returned instead.  
`restrictedValues[]` |  `string` Only get facet for the given restricted values. For example, when using "pickupInStore" as key and set restricted values to ["store123", "store456"], only facets for "store123" and "store456" are returned. Only supported on predefined textual fields, custom textual attributes and fulfillments. Maximum is 20.Must be set for the fulfillment facet keys:

  * pickupInStore
  * shipToStore
  * sameDayDelivery
  * nextDayDelivery
  * customFulfillment1
  * customFulfillment2
  * customFulfillment3
  * customFulfillment4
  * customFulfillment5

  
`prefixes[]` |  `string` Only get facet values that start with the given string prefix. For example, suppose "categories" has three values "Women > Shoe", "Women > Dress" and "Men > Shoe". If set "prefixes" to "Women", the "categories" facet gives only "Women > Shoe" and "Women > Dress". Only supported on textual fields. Maximum is 10.  
`contains[]` |  `string` Only get facet values that contains the given strings. For example, suppose "categories" has three values "Women > Shoe", "Women > Dress" and "Men > Shoe". If set "contains" to "Shoe", the "categories" facet gives only "Women > Shoe" and "Men > Shoe". Only supported on textual fields. Maximum is 10.  
`caseInsensitive` |  `boolean` True to make facet keys case insensitive when getting faceting values with prefixes or contains; false otherwise.  
`orderBy` |  `string` The order in which `[SearchResponse.Facet.values](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#Facet.FIELDS.values)` are returned.Allowed values are:

  * "count desc", which means order by `[SearchResponse.Facet.values.count](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue.FIELDS.count)` descending.
  * "value desc", which means order by `[SearchResponse.Facet.values.value](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue.FIELDS.value)` descending. Only applies to textual facets.

If not set, textual values are sorted in [natural order](https://en.wikipedia.org/wiki/Natural_sort_order); numerical intervals are sorted in the order given by `[FacetSpec.FacetKey.intervals](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.intervals)`; `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` are sorted in the order given by `[FacetSpec.FacetKey.restricted_values](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.restricted_values)`.  
`query` |  `string` The query that is used to compute facet for the given facet key. When provided, it overrides the default behavior of facet computation. The query syntax is the same as a filter expression. See `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)` for detail syntax and limitations. Notice that there is no limitation on `[FacetKey.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.key)` when query is specified.In the response, `[SearchResponse.Facet.values.value](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue.FIELDS.value)` is always "1" and `[SearchResponse.Facet.values.count](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue.FIELDS.count)` is the number of results that match the query.For example, you can set a customized facet for "shipToStore", where `[FacetKey.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.key)` is "customizedShipToStore", and `[FacetKey.query](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.query)` is "availability: ANY("IN_STOCK") AND shipToStore: ANY("123")". Then the facet counts the products that are both in stock and ship to store "123".  
`returnMinMax` |  `boolean` Returns the min and max value for each numerical facet intervals. Ignored for textual facets.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
