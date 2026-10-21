---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search/
title: Method: projects.locations.catalogs.placements.search \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:34:36.376745+00:00
---

# Method: projects.locations.catalogs.placements.search  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.placements.search Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Performs a search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

### HTTP request

`POST https://retail.googleapis.com/v2alpha/{placement=projects/*/locations/*/catalogs/*/placements/*}:search`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`placement` |  `string` Required. The resource name of the Retail Search serving config, such as `projects/*/locations/global/catalogs/default_catalog/servingConfigs/default_serving_config` or the name of the legacy placement resource, such as `projects/*/locations/global/catalogs/default_catalog/placements/default_search`. This field is used to identify the serving config name and the set of models that are used to make the search.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "branch": string,
      "query": string,
      "visitorId": string,
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo))
      },
      "pageSize": integer,
      "pageToken": string,
      "offset": integer,
      "filter": string,
      "canonicalFilter": string,
      "orderBy": string,
      "facetSpecs": [
        {
          object ([FacetSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/FacetSpec))
        }
      ],
      "dynamicFacetSpec": {
        object ([DynamicFacetSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#DynamicFacetSpec))
      },
      "boostSpec": {
        object ([BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/BoostSpec))
      },
      "queryExpansionSpec": {
        object ([QueryExpansionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec))
      },
      "relevanceThreshold": enum ([RelevanceThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/RelevanceThreshold)),
      "variantRollupKeys": [
        string
      ],
      "experimentId": string,
      "pageCategories": [
        string
      ],
      "searchMode": enum ([SearchMode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchMode)),
      "personalizationSpec": {
        object ([PersonalizationSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#PersonalizationSpec))
      },
      "labels": {
        string: string,
        ...
      },
      "entity": string,
      "conversationalSearchSpec": {
        object ([ConversationalSearchSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/ConversationalSearchSpec))
      },
      "tileNavigationSpec": {
        object ([TileNavigationSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/TileNavigationSpec))
      },
      "languageCode": string,
      "regionCode": string,
      "placeId": string,
      "userAttributes": {
        string: {
          object ([StringList](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/StringList))
        },
        ...
      },
      "spellCorrectionSpec": {
        object ([SpellCorrectionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SpellCorrectionSpec))
      }
    }  
  
Fields  
---  
`branch` |  `string` The branch resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/0`.Use "default_branch" as the branch ID or leave this field empty, to search products under the default branch.  
`query` |  `string` Raw search query.If this field is empty, the request is considered a category browsing request and returned results are based on `[filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)` and `[pageCategories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.page_categories)`.  
`visitorId` |  `string` Required. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.This should be the same identifier as `[UserEvent.visitor_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.visitor_id)`.The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo)`)` User information.  
`pageSize` |  `integer` Maximum number of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s to return. If unspecified, defaults to a reasonable value. The maximum allowed value is 120. Values above 120 will be coerced to 120.If this field is negative, an INVALID_ARGUMENT is returned.  
`pageToken` |  `string` A page token `[SearchResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#FIELDS.next_page_token)`, received from a previous `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)` must match the call that provided the page token. Otherwise, an INVALID_ARGUMENT error is returned.  
`offset` |  `integer` A 0-indexed integer that specifies the current offset (that is, starting result location, amongst the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s deemed by the API as relevant) in search results. This field is only considered if `[pageToken](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.page_token)` is unset.If this field is negative, an INVALID_ARGUMENT is returned.  
`filter` |  `string` The filter syntax consists of an expression language for constructing a predicate from one or more fields of the products being filtered. Filter expression is case-sensitive. For more information, see [Filter](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order#filter).If this field is unrecognizable, an INVALID_ARGUMENT is returned.  
`canonicalFilter` |  `string` The default filter that is applied when a user performs a search without checking any filters on the search page.The filter applied to every search request when quality improvement such as query expansion is needed. In the case a query does not have a sufficient amount of results this filter will be used to determine whether or not to enable the query expansion flow. The original filter will still be used for the query expanded search. This field is strongly recommended to achieve high search quality.For more information about filter syntax, see `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`.  
`orderBy` |  `string` The order in which products are returned. Products can be ordered by a field in an `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` object. Leave it unset if ordered by relevance. OrderBy expression is case-sensitive. For more information, see [Order](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order#order).If this field is unrecognizable, an INVALID_ARGUMENT is returned.  
`facetSpecs[]` |  `object (`[FacetSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/FacetSpec)`)` Facet specifications for faceted search. If empty, no facets are returned.A maximum of 200 values are allowed. Otherwise, an INVALID_ARGUMENT error is returned.  
`dynamicFacetSpec  
**(deprecated)**` |  `object (`[DynamicFacetSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#DynamicFacetSpec)`)` Deprecated. Refer to <https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#dynamic> to enable dynamic facets. Do not set this field.The specification for dynamically generated facets. Notice that only textual facets can be dynamically generated.  
`boostSpec` |  `object (`[BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/BoostSpec)`)` Boost specification to boost certain products. For more information, see [Boost results](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/boosting).Notice that if both `[ServingConfig.boost_control_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.boost_control_ids)` and `[SearchRequest.boost_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.boost_spec)` are set, the boost conditions from both places are evaluated. If a search request matches multiple boost conditions, the final boost score is equal to the sum of the boost scores from all matched boost conditions.  
`queryExpansionSpec` |  `object (`[QueryExpansionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec)`)` The query expansion specification that specifies the conditions under which query expansion occurs. For more information, see [Query expansion](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/result-size#query_expansion).  
`relevanceThreshold` |  `enum (`[RelevanceThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/RelevanceThreshold)`)` The relevance threshold of the search results.Defaults to `[RelevanceThreshold.HIGH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/RelevanceThreshold#ENUM_VALUES.HIGH)`, which means only the most relevant results are shown, and the least number of results are returned. For more information, see [Adjust result size](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/result-size#relevance_thresholding).  
`variantRollupKeys[]` |  `string` The keys to fetch and rollup the matching `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s attributes, `[FulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo)` or `[LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory)`s attributes. The attributes from all the matching `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s or `[LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory)`s are merged and de-duplicated. Notice that rollup attributes will lead to extra query latency. Maximum number of keys is 30.For `[FulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo)`, a fulfillment type and a fulfillment ID must be provided in the format of "fulfillmentType.fulfillmentId". E.g., in "pickupInStore.store123", "pickupInStore" is fulfillment type and "store123" is the store ID.Supported keys are:

  * colorFamilies
  * price
  * originalPrice
  * discount
  * variantId
  * inventory(placeId,price)
  * inventory(placeId,originalPrice)
  * inventory(placeId,attributes.key), where key is any key in the `[Product.local_inventories.attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory.FIELDS.attributes)` map.
  * attributes.key, where key is any key in the `[Product.attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.attributes)` map.
  * pickupInStore.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "pickup-in-store".
  * shipToStore.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "ship-to-store".
  * sameDayDelivery.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "same-day-delivery".
  * nextDayDelivery.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "next-day-delivery".
  * customFulfillment1.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "custom-type-1".
  * customFulfillment2.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "custom-type-2".
  * customFulfillment3.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "custom-type-3".
  * customFulfillment4.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "custom-type-4".
  * customFulfillment5.id, where id is any `[FulfillmentInfo.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)` for `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` "custom-type-5".

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.  
`experimentId` |  `string` Optional. An ID for the experiment group this search belongs to.  
`pageCategories[]` |  `string` Optional. The categories associated with a category page. Must be set for category navigation queries to achieve good search quality. The format should be the same as `[UserEvent.page_categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.page_categories)`;To represent the full path of category, use '>' sign, with one space on each side, to separate different hierarchies. If '>' is part of the category name, replace it with other character(s).Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: "pageCategories" : ["Sales > 2017 Black Friday Deals"].  
`searchMode` |  `enum (`[SearchMode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchMode)`)` The search mode of the search request. If not specified, a single search request triggers both product search and faceted search.  
`personalizationSpec` |  `object (`[PersonalizationSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#PersonalizationSpec)`)` The specification for personalization.Notice that if both `[ServingConfig.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.personalization_spec)` and `[SearchRequest.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.personalization_spec)` are set. `[SearchRequest.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.personalization_spec)` will override `[ServingConfig.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.personalization_spec)`.  
`labels` |  `map (key: string, value: string)` The labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

For more information, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) in the Resource Manager documentation.  
`entity` |  `string` The entity for customers that may run multiple different entities, domains, sites or regions, for example, `Google US`, `Google Ads`, `Waymo`, `google.com`, `youtube.com`, etc. If this is set, it should be exactly matched with `[UserEvent.entity](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.entity)` to get search results boosted by entity.  
`conversationalSearchSpec` |  `object (`[ConversationalSearchSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/ConversationalSearchSpec)`)` Optional. This field specifies all conversational related parameters addition to traditional retail search.  
`tileNavigationSpec` |  `object (`[TileNavigationSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/TileNavigationSpec)`)` Optional. This field specifies tile navigation related parameters.  
`languageCode` |  `string` Optional. The BCP-47 language code, such as "en-US" or "sr-Latn" [list](https://www.unicode.org/cldr/charts/46/summary/root.html). For more information, see [Standardized codes](https://google.aip.dev/143). This field helps to better interpret the query. If a value isn't specified, the query language code is automatically detected, which may not be accurate.  
`regionCode` |  `string` Optional. The Unicode country/region code (CLDR) of a location, such as "US" and "419" [list](https://www.unicode.org/cldr/charts/46/supplemental/territory_information.html). For more information, see [Standardized codes](https://google.aip.dev/143). If set, then results will be boosted based on the regionCode provided.  
`placeId` |  `string` Optional. An id corresponding to a place, such as a store id or region id. When specified, we use the price from the local inventory with the matching product's `[LocalInventory.place_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory.FIELDS.place_id)` for revenue optimization.Note, the currency of the local inventory's price must match the currency of the product's price.  
`userAttributes` |  `map (key: string, value: object (`[StringList](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/StringList)`))` Optional. The user attributes that could be used for personalization of search results.

  * Populate at most 100 key-value pairs per query.
  * Only supports string keys and repeated string values.
  * Duplicate keys are not allowed within a single query.

Example: userAttributes: [ { key: "pets" value { values: "dog" values: "cat" } }, { key: "state" value { values: "CA" } } ]  
`spellCorrectionSpec` |  `object (`[SpellCorrectionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SpellCorrectionSpec)`)` The spell correction specification that specifies the mode under which spell correction will take effect.  
  
### Response body

If successful, the response body contains an instance of `[SearchResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `placement` resource, depending on the resource type:

  * `retail.placements.search`
  * `retail.servingConfigs.search`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
