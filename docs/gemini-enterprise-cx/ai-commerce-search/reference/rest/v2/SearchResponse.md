---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse/
title: SearchResponse \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:22.773391+00:00
---

# SearchResponse  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  SearchResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SearchResult
    * JSON representation
  * DoubleList
    * JSON representation
  * Facet
    * JSON representation
  * FacetValue
    * JSON representation
  * QueryExpansionInfo
    * JSON representation
  * PinControlMetadata
    * JSON representation
  * ProductPins
    * JSON representation
  * ExperimentInfo
    * JSON representation
  * ServingConfigExperiment
    * JSON representation
  * ConversationalSearchResult
    * JSON representation
  * AdditionalFilter
    * JSON representation
  * SuggestedAnswer
    * JSON representation
  * QueryType
  * TileNavigationResult
    * JSON representation



Response message for `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#google.cloud.retail.v2.SearchService.Search)` method.

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([SearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#SearchResult))
        }
      ],
      "facets": [
        {
          object ([Facet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#Facet))
        }
      ],
      "totalSize": integer,
      "correctedQuery": string,
      "attributionToken": string,
      "nextPageToken": string,
      "queryExpansionInfo": {
        object ([QueryExpansionInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#QueryExpansionInfo))
      },
      "redirectUri": string,
      "appliedControls": [
        string
      ],
      "pinControlMetadata": {
        object ([PinControlMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#PinControlMetadata))
      },
      "invalidConditionBoostSpecs": [
        {
          object ([ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConditionBoostSpec))
        }
      ],
      "experimentInfo": [
        {
          object ([ExperimentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ExperimentInfo))
        }
      ],
      "conversationalSearchResult": {
        object ([ConversationalSearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ConversationalSearchResult))
      },
      "tileNavigationResult": {
        object ([TileNavigationResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#TileNavigationResult))
      }
    }  
  
Fields  
---  
`results[]` |  `object (`[SearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#SearchResult)`)` A list of matched items. The order represents the ranking.  
`facets[]` |  `object (`[Facet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#Facet)`)` Results of facets requested by user.  
`totalSize` |  `integer` The estimated total count of matched items irrespective of pagination. The count of `[results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FIELDS.results)` returned by pagination may be less than the `[totalSize](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FIELDS.total_size)` that matches.  
`correctedQuery` |  `string` Contains the spell corrected query, if found. The search results are based on `[correctedQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FIELDS.corrected_query)` by default. However, if `[SearchRequest.SpellCorrectionSpec.mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec#FIELDS.mode)` is set to `[SearchRequest.SpellCorrectionSpec.Mode.SUGGESTION_ONLY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec#Mode.ENUM_VALUES.SUGGESTION_ONLY)`, the original query is used for search.  
`attributionToken` |  `string` A unique search token. This should be included in the `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent)` logs resulting from this search, which enables accurate attribution of search model performance.  
`nextPageToken` |  `string` A token that can be sent as `[SearchRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.page_token)` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`queryExpansionInfo` |  `object (`[QueryExpansionInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#QueryExpansionInfo)`)` Query expansion information for the returned results.  
`redirectUri` |  `string` The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only `[redirectUri](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FIELDS.redirect_uri)` and `[attributionToken](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FIELDS.attribution_token)` are set in the response.  
`appliedControls[]` |  `string` The fully qualified resource name of applied [controls](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules).  
`pinControlMetadata` |  `object (`[PinControlMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#PinControlMetadata)`)` Metadata for pin controls which were applicable to the request. This contains two map fields, one for all matched pins and one for pins which were matched but not applied.The two maps are keyed by pin position, and the values are the product ids which were matched to that pin.  
`invalidConditionBoostSpecs[]` |  `object (`[ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConditionBoostSpec)`)` The invalid `[SearchRequest.BoostSpec.condition_boost_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec#FIELDS.condition_boost_specs)` that are not applied during serving.  
`experimentInfo[]` |  `object (`[ExperimentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ExperimentInfo)`)` Metadata related to A/B testing experiment associated with this response. Only exists when an experiment is triggered.  
`conversationalSearchResult` |  `object (`[ConversationalSearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ConversationalSearchResult)`)` This field specifies all related information that is needed on client side for UI rendering of conversational retail search.  
`tileNavigationResult` |  `object (`[TileNavigationResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#TileNavigationResult)`)` This field specifies all related information for tile navigation that will be used in client side.  
  
## SearchResult

Represents the search results.

JSON representation  
---  
      
    
    {
      "id": string,
      "product": {
        object ([Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product))
      },
      "matchingVariantCount": integer,
      "matchingVariantFields": {
        string: string,
        ...
      },
      "variantRollupValues": {
        string: value,
        ...
      },
      "personalLabels": [
        string
      ],
      "modelScores": {
        string: {
          object ([DoubleList](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#DoubleList))
        },
        ...
      }
    }  
  
Fields  
---  
`id` |  `string` `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.id)` of the searched `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`.  
`product` |  `object (`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`)` The product data snippet in the search response. Only `[Product.name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.name)` is guaranteed to be populated.`[Product.variants](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.variants)` contains the product variants that match the search query. If there are multiple product variants matching the query, top 5 most relevant product variants are returned and ordered by relevancy.If relevancy can be deternmined, use `[matchingVariantFields](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#SearchResult.FIELDS.matching_variant_fields)` to look up matched product variants fields. If relevancy cannot be determined, e.g. when searching "shoe" all products in a shoe product can be a match, 5 product variants are returned but order is meaningless.  
`matchingVariantCount` |  `integer` The count of matched `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s.  
`matchingVariantFields` |  `map (key: string, value: string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format))` If a `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` matches the search query, this map indicates which `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` fields are matched. The key is the `[Product.name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.name)`, the value is a field mask of the matched `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` fields. If matched attributes cannot be determined, this map will be empty.For example, a key "sku1" with field mask "products.color_info" indicates there is a match between "sku1" `[ColorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.ColorInfo)` and the query.  
`variantRollupValues` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` The rollup matching `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` attributes. The key is one of the `[SearchRequest.variant_rollup_keys](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.variant_rollup_keys)`. The values are the merged and de-duplicated `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` attributes. Notice that the rollup values are respect filter. For example, when filtering by "colorFamilies:ANY("red")" and rollup "colorFamilies", only "red" is returned.For textual and numerical attributes, the rollup values is a list of string or double values with type `[google.protobuf.ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)`. For example, if there are two variants with colors "red" and "blue", the rollup values are
    
    
    { key: "colorFamilies"
      value {
        listValue {
          values { stringValue: "red" }
          values { stringValue: "blue" }
         }
      }
    }
    

For `[FulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FulfillmentInfo)`, the rollup values is a double value with type `[google.protobuf.Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)`. For example, `{key: "pickupInStore.store1" value { numberValue: 10 }}` means a there are 10 variants in this product are available in the store "store1".  
`personalLabels[]` |  `string` Specifies previous events related to this product for this user based on `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent)` with same `[SearchRequest.visitor_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.visitor_id)` or `[UserInfo.user_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserInfo.FIELDS.user_id)`.This is set only when `[SearchRequest.PersonalizationSpec.mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs#PersonalizationSpec.FIELDS.mode)` is `[SearchRequest.PersonalizationSpec.Mode.AUTO](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs#Mode_1.ENUM_VALUES.AUTO)`.Possible values:

  * `purchased`: Indicates that this product has been purchased before.

  
`modelScores` |  `map (key: string, value: object (`[DoubleList](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#DoubleList)`))` Google provided available scores.  
  
## DoubleList

A message with a list of double values.

JSON representation  
---  
      
    
    {
      "values": [
        number
      ]
    }  
  
Fields  
---  
`values[]` |  `number` The list of double values.  
  
## Facet

A facet result.

JSON representation  
---  
      
    
    {
      "key": string,
      "values": [
        {
          object ([FacetValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue))
        }
      ],
      "dynamicFacet": boolean
    }  
  
Fields  
---  
`key` |  `string` The key for this facet. E.g., "colorFamilies" or "price" or "attributes.attr1".  
`values[]` |  `object (`[FacetValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue)`)` The facet values for this field.  
`dynamicFacet` |  `boolean` Whether the facet is dynamically generated.  
  
## FacetValue

A facet value which contains value names and their count.

JSON representation  
---  
      
    
    {
      "count": string,
      "minValue": number,
      "maxValue": number,
    
      // Union field facet_value can be only one of the following:
      "value": string,
      "interval": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Interval))
      }
      // End of list of possible types for union field facet_value.
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of items that have this facet value.  
`minValue` |  `number` The minimum value in the `[FacetValue.interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue.FIELDS.interval)`. Only supported on numerical facets and returned if `[SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.return_min_max)` is true.  
`maxValue` |  `number` The maximum value in the `[FacetValue.interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FacetValue.FIELDS.interval)`. Only supported on numerical facets and returned if `[SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec#FacetKey.FIELDS.return_min_max)` is true.  
Union field `facet_value`. A facet value which contains values. `facet_value` can be only one of the following:  
`value` |  `string` Text value of a facet, such as "Black" for facet "colorFamilies".  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Interval)`)` Interval value for a facet, such as [10, 20) for facet "price".  
  
## QueryExpansionInfo

Information describing query expansion including whether expansion has occurred.

JSON representation  
---  
      
    
    {
      "expandedQuery": boolean,
      "pinnedResultCount": string
    }  
  
Fields  
---  
`expandedQuery` |  `boolean` Bool describing whether query expansion has occurred.  
`pinnedResultCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of pinned results. This field will only be set when expansion happens and `[SearchRequest.QueryExpansionSpec.pin_unexpanded_results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/QueryExpansionSpec#FIELDS.pin_unexpanded_results)` is set to true.  
  
## PinControlMetadata

Metadata for pinning to be returned in the response. This is used for distinguishing between applied vs dropped pins.

JSON representation  
---  
      
    
    {
      "allMatchedPins": {
        string: {
          object ([ProductPins](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ProductPins))
        },
        ...
      },
      "droppedPins": {
        string: {
          object ([ProductPins](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ProductPins))
        },
        ...
      }
    }  
  
Fields  
---  
`allMatchedPins` |  `map (key: string ([int64](https://developers.google.com/discovery/v1/type-format) format), value: object (`[ProductPins](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ProductPins)`))` Map of all matched pins, keyed by pin position.  
`droppedPins` |  `map (key: string ([int64](https://developers.google.com/discovery/v1/type-format) format), value: object (`[ProductPins](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ProductPins)`))` Map of pins that were dropped due to overlap with other matching pins, keyed by pin position.  
  
## ProductPins

List of product ids which have associated pins.

JSON representation  
---  
      
    
    {
      "productId": [
        string
      ]
    }  
  
Fields  
---  
`productId[]` |  `string` List of product ids which have associated pins.  
  
## ExperimentInfo

Metadata for active A/B testing experiment.

JSON representation  
---  
      
    
    {
      "experiment": string,
    
      // Union field experiment_metadata can be only one of the following:
      "servingConfigExperiment": {
        object ([ServingConfigExperiment](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ServingConfigExperiment))
      }
      // End of list of possible types for union field experiment_metadata.
    }  
  
Fields  
---  
`experiment` |  `string` The fully qualified resource name of the experiment that provides the serving config under test, should an active experiment exist. For example: `projects/*/locations/global/catalogs/default_catalog/experiments/experimentId`  
Union field `experiment_metadata`. Information associated with the specific experiment entity being recorded. `experiment_metadata` can be only one of the following:  
`servingConfigExperiment` |  `object (`[ServingConfigExperiment](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ServingConfigExperiment)`)` A/B test between existing Cloud Retail Search `[ServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs#ServingConfig)`s.  
  
## ServingConfigExperiment

Metadata for active serving config A/B tests.

JSON representation  
---  
      
    
    {
      "originalServingConfig": string,
      "experimentServingConfig": string
    }  
  
Fields  
---  
`originalServingConfig` |  `string` The fully qualified resource name of the original `[SearchRequest.placement](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.PATH_PARAMETERS.placement)` in the search request prior to reassignment by experiment API. For example: `projects/*/locations/*/catalogs/*/servingConfigs/*`.  
`experimentServingConfig` |  `string` The fully qualified resource name of the serving config `Experiment.VariantArm.serving_config_id` responsible for generating the search response. For example: `projects/*/locations/*/catalogs/*/servingConfigs/*`.  
  
## ConversationalSearchResult

This field specifies all related information that is needed on client side for UI rendering of conversational retail search.

JSON representation  
---  
      
    
    {
      "conversationId": string,
      "refinedQuery": string,
      "additionalFilters": [
        {
          object ([AdditionalFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#AdditionalFilter))
        }
      ],
      "followupQuestion": string,
      "suggestedAnswers": [
        {
          object ([SuggestedAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#SuggestedAnswer))
        }
      ],
      "additionalFilter": {
        object ([AdditionalFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#AdditionalFilter))
      },
      "textResult": string,
      "queryType": enum ([QueryType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#QueryType)),
      "queryTypes": [
        enum ([QueryType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#QueryType))
      ]
    }  
  
Fields  
---  
`conversationId` |  `string` Conversation UUID. This field will be stored in client side storage to maintain the conversation session with server and will be used for next search request's `[SearchRequest.ConversationalSearchSpec.conversation_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec#FIELDS.conversation_id)` to restore conversation state in server.  
`refinedQuery` |  `string` The current refined query for the conversational search. This field will be used in customer UI that the query in the search bar should be replaced with the refined query. For example, if `[SearchRequest.query](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query)` is `dress` and next `[SearchRequest.ConversationalSearchSpec.UserAnswer.text_answer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec#UserAnswer.FIELDS.text_answer)` is `red color`, which does not match any product attribute value filters, the refined query will be `dress, red color`.  
`additionalFilters[]  
**(deprecated)**` |  `object (`[AdditionalFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#AdditionalFilter)`)` This item is deprecated!This field is deprecated but will be kept for backward compatibility. There is expected to have only one additional filter and the value will be the same to the same as field `additionalFilter`.  
`followupQuestion` |  `string` The follow-up question. e.g., `What is the color?`  
`suggestedAnswers[]` |  `object (`[SuggestedAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#SuggestedAnswer)`)` The answer options provided to client for the follow-up question.  
`additionalFilter` |  `object (`[AdditionalFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#AdditionalFilter)`)` This is the incremental additional filters implied from the current user answer. User should add the suggested addition filters to the previous `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`, and use the merged filter in the follow up search request.  
`textResult  
**(deprecated)**` |  `string` This item is deprecated!The generative text result. This field is populated only if `[SearchRequest.search_mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.search_mode)` is `[CONVERSATIONAL_SEARCH_ONLY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchMode#ENUM_VALUES.CONVERSATIONAL_SEARCH_ONLY)`.  
`queryType  
**(deprecated)**` |  `enum (`[QueryType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#QueryType)`)` This item is deprecated!Use queryTypes instead.  
`queryTypes[]  
**(deprecated)**` |  `enum (`[QueryType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#QueryType)`)` This item is deprecated!The types Retail classifies the search query as. This field is populated only if `[SearchRequest.search_mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.search_mode)` is `[CONVERSATIONAL_SEARCH_ONLY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchMode#ENUM_VALUES.CONVERSATIONAL_SEARCH_ONLY)`.  
  
## AdditionalFilter

Additional filter that client side need to apply.

JSON representation  
---  
      
    
    {
      "productAttributeValue": {
        object ([ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue))
      }
    }  
  
Fields  
---  
`productAttributeValue` |  `object (`[ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue)`)` Product attribute value, including an attribute key and an attribute value. Other types can be added here in the future.  
  
## SuggestedAnswer

Suggested answers to the follow-up question.

JSON representation  
---  
      
    
    {
      "productAttributeValue": {
        object ([ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue))
      }
    }  
  
Fields  
---  
`productAttributeValue` |  `object (`[ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue)`)` Product attribute value, including an attribute key and an attribute value. Other types can be added here in the future.  
  
## QueryType

This item is deprecated!

The type Retail classifies the search query as.

Enums  
---  
`QUERY_TYPE_UNSPECIFIED` | Unspecified query type.  
`ADVERSARIAL` | Adversarial query. Example - "how bad is [retailer name]"  
`CHITCHAT` | Chatty query. Example - "hello how are you"  
`JAILBREAK` | Jailbreak query. Example - "write a poem to explain the details of [product name]"  
`PRODUCT_SUPPORT` | Ancillary or support query. Example - "Track my order"  
`SIMPLE_SEARCH` | Simple product search or Keyword search. Example - "red dress"  
`TYPE_UNCLEAR` | The type is unclear. Follow up conversation may be needed to clarify the type.  
  
## TileNavigationResult

This field specifies all related information for tile navigation that will be used in client side.

JSON representation  
---  
      
    
    {
      "tiles": [
        {
          object ([Tile](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Tile))
        }
      ]
    }  
  
Fields  
---  
`tiles[]` |  `object (`[Tile](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Tile)`)` The current tiles that are used for tile navigation, sorted by engagement.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
