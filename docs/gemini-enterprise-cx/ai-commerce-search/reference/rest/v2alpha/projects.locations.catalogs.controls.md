---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls
title: REST Resource: projects.locations.catalogs.controls \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:29:56.879278+00:00
---

# REST Resource: projects.locations.catalogs.controls  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs.controls Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Control
    * JSON representation
  * Rule
    * JSON representation
  * BoostAction
    * JSON representation
  * RedirectAction
    * JSON representation
  * OnewaySynonymsAction
    * JSON representation
  * DoNotAssociateAction
    * JSON representation
  * ReplacementAction
    * JSON representation
  * IgnoreAction
    * JSON representation
  * FilterAction
    * JSON representation
  * TwowaySynonymsAction
    * JSON representation
  * ForceReturnFacetAction
    * JSON representation
  * FacetPositionAdjustment
    * JSON representation
  * RemoveFacetAction
    * JSON representation
  * PinAction
    * JSON representation
  * Condition
    * JSON representation
  * QueryTerm
    * JSON representation
  * TimeRange
    * JSON representation
  * SearchSolutionUseCase
  * Methods



## Resource: Control

Configures dynamic metadata that can be linked to a `[ServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#ServingConfig)` and affect search or recommendation results at serving time.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "rule": {
        object ([Rule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Rule))
      },
      "associatedServingConfigIds": [
        string
      ],
      "solutionTypes": [
        enum ([SolutionType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SolutionType))
      ],
      "searchSolutionUseCase": [
        enum ([SearchSolutionUseCase](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#SearchSolutionUseCase))
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. Fully qualified name `projects/*/locations/global/catalogs/*/controls/*`  
`displayName` |  `string` Required. The human readable control display name. Used in Retail UI.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is thrown.  
`rule` |  `object (`[Rule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Rule)`)` A rule control - a condition-action pair. Enacts a set action when the condition is triggered. For example: Boost "gShoe" when query full matches "Running Shoes".  
`associatedServingConfigIds[]` |  `string` Output only. List of `[serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#ServingConfig)` ids that are associated with this control in the same `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`.Note the association is managed via the `[ServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs#ServingConfig)`, this is an output only denormalized view.  
`solutionTypes[]` |  `enum (`[SolutionType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SolutionType)`)` Required. Immutable. The solution types that the control is used for. Currently we support setting only one type of solution at creation time.Only `SOLUTION_TYPE_SEARCH` value is supported at the moment. If no solution type is provided at creation time, will default to `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`searchSolutionUseCase[]` |  `enum (`[SearchSolutionUseCase](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#SearchSolutionUseCase)`)` Specifies the use case for the control. Affects what condition fields can be set. Only settable by search controls. Will default to `[SEARCH_SOLUTION_USE_CASE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#SearchSolutionUseCase.ENUM_VALUES.SEARCH_SOLUTION_USE_CASE_SEARCH)` if not specified. Currently only allow one searchSolutionUseCase per control.  
  
## Rule

A rule is a condition-action pair

  * A condition defines when a rule is to be triggered.
  * An action specifies what occurs on that trigger. Currently rules only work for `[controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Control)` with `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.

JSON representation  
---  
      
    
    {
      "condition": {
        object ([Condition](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition))
      },
    
      // Union field action can be only one of the following:
      "boostAction": {
        object ([BoostAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#BoostAction))
      },
      "redirectAction": {
        object ([RedirectAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#RedirectAction))
      },
      "onewaySynonymsAction": {
        object ([OnewaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#OnewaySynonymsAction))
      },
      "doNotAssociateAction": {
        object ([DoNotAssociateAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#DoNotAssociateAction))
      },
      "replacementAction": {
        object ([ReplacementAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#ReplacementAction))
      },
      "ignoreAction": {
        object ([IgnoreAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#IgnoreAction))
      },
      "filterAction": {
        object ([FilterAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#FilterAction))
      },
      "twowaySynonymsAction": {
        object ([TwowaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#TwowaySynonymsAction))
      },
      "forceReturnFacetAction": {
        object ([ForceReturnFacetAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#ForceReturnFacetAction))
      },
      "removeFacetAction": {
        object ([RemoveFacetAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#RemoveFacetAction))
      },
      "pinAction": {
        object ([PinAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#PinAction))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
`condition` |  `object (`[Condition](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition)`)` Required. The condition that triggers the rule. If the condition is empty, the rule will always apply.  
Union field `action`. An action must be provided. `action` can be only one of the following:  
`boostAction` |  `object (`[BoostAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#BoostAction)`)` A boost action.  
`redirectAction` |  `object (`[RedirectAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#RedirectAction)`)` Redirects a shopper to a specific page.  
`onewaySynonymsAction` |  `object (`[OnewaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#OnewaySynonymsAction)`)` Treats specific term as a synonym with a group of terms. Group of terms will not be treated as synonyms with the specific term.  
`doNotAssociateAction` |  `object (`[DoNotAssociateAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#DoNotAssociateAction)`)` Prevents term from being associated with other terms.  
`replacementAction` |  `object (`[ReplacementAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#ReplacementAction)`)` Replaces specific terms in the query.  
`ignoreAction` |  `object (`[IgnoreAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#IgnoreAction)`)` Ignores specific terms from query during search.  
`filterAction` |  `object (`[FilterAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#FilterAction)`)` Filters results.  
`twowaySynonymsAction` |  `object (`[TwowaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#TwowaySynonymsAction)`)` Treats a set of terms as synonyms of one another.  
`forceReturnFacetAction` |  `object (`[ForceReturnFacetAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#ForceReturnFacetAction)`)` Force returns an attribute as a facet in the request.  
`removeFacetAction` |  `object (`[RemoveFacetAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#RemoveFacetAction)`)` Remove an attribute as a facet in the request (if present).  
`pinAction` |  `object (`[PinAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#PinAction)`)` Pins one or more specified products to a specific position in the results.  
  
## BoostAction

A boost action to apply to results matching condition specified above.

JSON representation  
---  
      
    
    {
      "boost": number,
      "productsFilter": string
    }  
  
Fields  
---  
`boost` |  `number` Strength of the condition boost, which must be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the item a big promotion. However, it does not necessarily mean that the boosted item will be the top result at all times, nor that other items will be excluded. Results could still be shown even when none of them matches the condition. And results that are significantly more relevant to the search query can still trump your heavily favored but irrelevant items.Setting to -1.0 gives the item a big demotion. However, results that are deeply relevant might still be shown. The item will have an upstream battle to get a fairly high ranking, but it is not blocked out completely.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`productsFilter` |  `string` The filter can have a max size of 5000 characters. An expression which specifies which products to apply an action to. The syntax and supported fields are the same as a filter expression. See `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)` for detail syntax and limitations.Examples:

  * To boost products with product ID "product_1" or "product_2", and color "Red" or "Blue":  
_(id: ANY("product_1", "product_2"))  
_ _AND  
_ _(colorFamilies: ANY("Red", "Blue"))  
_

  
  
## RedirectAction

Redirects a shopper to a specific page.

  * Rule Condition: Must specify `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)`.
  * Action Input: Request Query
  * Action Result: Redirects shopper to provided uri.

JSON representation  
---  
      
    
    {
      "redirectUri": string
    }  
  
Fields  
---  
`redirectUri` |  `string` URL must have length equal or less than 2000 characters.  
  
## OnewaySynonymsAction

Maps a set of terms to a set of synonyms. Set of synonyms will be treated as synonyms of each query term only. `queryTerms` will not be treated as synonyms of each other. Example: "sneakers" will use a synonym of "shoes". "shoes" will not use a synonym of "sneakers".

JSON representation  
---  
      
    
    {
      "queryTerms": [
        string
      ],
      "synonyms": [
        string
      ],
      "onewayTerms": [
        string
      ]
    }  
  
Fields  
---  
`queryTerms[]` |  `string` Terms from the search query. Will treat synonyms as their synonyms. Not themselves synonyms of the synonyms. Can specify up to 100 terms.  
`synonyms[]` |  `string` Defines a set of synonyms. Cannot contain duplicates. Can specify up to 100 synonyms.  
`onewayTerms[]` |  `string` Will be [deprecated = true] post migration;  
  
## DoNotAssociateAction

Prevents `query_term` from being associated with specified terms during search. Example: Don't associate "gShoe" and "cheap".

JSON representation  
---  
      
    
    {
      "queryTerms": [
        string
      ],
      "doNotAssociateTerms": [
        string
      ],
      "terms": [
        string
      ]
    }  
  
Fields  
---  
`queryTerms[]` |  `string` Terms from the search query. Will not consider doNotAssociateTerms for search if in search query. Can specify up to 100 terms.  
`doNotAssociateTerms[]` |  `string` Cannot contain duplicates or the query term. Can specify up to 100 terms.  
`terms[]` |  `string` Will be [deprecated = true] post migration;  
  
## ReplacementAction

Replaces a term in the query. Multiple replacement candidates can be specified. All `queryTerms` will be replaced with the replacement term. Example: Replace "gShoe" with "google shoe".

JSON representation  
---  
      
    
    {
      "queryTerms": [
        string
      ],
      "replacementTerm": string,
      "term": string
    }  
  
Fields  
---  
`queryTerms[]` |  `string` Terms from the search query. Will be replaced by replacement term. Can specify up to 100 terms.  
`replacementTerm` |  `string` Term that will be used for replacement.  
`term` |  `string` Will be [deprecated = true] post migration;  
  
## IgnoreAction

Prevents a term in the query from being used in search. Example: Don't search for "shoddy".

JSON representation  
---  
      
    
    {
      "ignoreTerms": [
        string
      ]
    }  
  
Fields  
---  
`ignoreTerms[]` |  `string` Terms to ignore in the search query.  
  
## FilterAction

  * Rule Condition:

    * No `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` provided is a global match.
    * 1 or more `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` provided are combined with OR operator.
  * Action Input: The request query and filter that are applied to the retrieved products, in addition to any filters already provided with the SearchRequest. The AND operator is used to combine the query's existing filters with the filter rule(s). NOTE: May result in 0 results when filters conflict.

  * Action Result: Filters the returned objects to be ONLY those that passed the filter.


JSON representation  
---  
      
    
    {
      "filter": string
    }  
  
Fields  
---  
`filter` |  `string` A filter to apply on the matching condition results. Supported features:

  * `[filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#FilterAction.FIELDS.filter)` must be set.
  * Filter syntax is identical to `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`. For more information, see [Filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order#filter).
  * To filter products with product ID "product_1" or "product_2", and color "Red" or "Blue":  
_(id: ANY("product_1", "product_2"))  
_ _AND  
_ _(colorFamilies: ANY("Red", "Blue"))  
_

  
  
## TwowaySynonymsAction

Creates a set of terms that will be treated as synonyms of each other. Example: synonyms of "sneakers" and "shoes":

  * "sneakers" will use a synonym of "shoes".
  * "shoes" will use a synonym of "sneakers".

JSON representation  
---  
      
    
    {
      "synonyms": [
        string
      ]
    }  
  
Fields  
---  
`synonyms[]` |  `string` Defines a set of synonyms. Can specify up to 100 synonyms. Must specify at least 2 synonyms.  
  
## ForceReturnFacetAction

Force returns an attribute/facet in the request around a certain position or above.

  * Rule Condition: Must specify non-empty `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` (for search only) or `[Condition.page_categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.page_categories)` (for browse only), but can't specify both.

  * Action Inputs: attribute name, position

  * Action Result: Will force return a facet key around a certain position or above if the condition is satisfied.




Example: Suppose the query is "shoes", the `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` is "shoes", the `[ForceReturnFacetAction.FacetPositionAdjustment.attribute_name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#FacetPositionAdjustment.FIELDS.attribute_name)` is "size" and the `[ForceReturnFacetAction.FacetPositionAdjustment.position](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#FacetPositionAdjustment.FIELDS.position)` is 8.

Two cases: a) The facet key "size" is not already in the top 8 slots, then the facet "size" will appear at a position close to 8. b) The facet key "size" in among the top 8 positions in the request, then it will stay at its current rank.

JSON representation  
---  
      
    
    {
      "facetPositionAdjustments": [
        {
          object ([FacetPositionAdjustment](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#FacetPositionAdjustment))
        }
      ]
    }  
  
Fields  
---  
`facetPositionAdjustments[]` |  `object (`[FacetPositionAdjustment](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#FacetPositionAdjustment)`)` Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.  
  
## FacetPositionAdjustment

Each facet position adjustment consists of a single attribute name (i.e. facet key) along with a specified position.

JSON representation  
---  
      
    
    {
      "attributeName": string,
      "position": integer
    }  
  
Fields  
---  
`attributeName` |  `string` The attribute name to force return as a facet. Each attribute name should be a valid attribute name, be non-empty and contain at most 80 characters long.  
`position` |  `integer` This is the position in the request as explained above. It should be strictly positive be at most 100.  
  
## RemoveFacetAction

Removes an attribute/facet in the request if is present.

  * Rule Condition: Must specify non-empty `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` (for search only) or `[Condition.page_categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.page_categories)` (for browse only), but can't specify both.

  * Action Input: attribute name

  * Action Result: Will remove the attribute (as a facet) from the request if it is present.




Example: Suppose the query is "shoes", the `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` is "shoes" and the attribute name "size", then facet key "size" will be removed from the request (if it is present).

JSON representation  
---  
      
    
    {
      "attributeNames": [
        string
      ]
    }  
  
Fields  
---  
`attributeNames[]` |  `string` The attribute names (i.e. facet keys) to remove from the dynamic facets (if present in the request). There can't be more 3 attribute names. Each attribute name should be a valid attribute name, be non-empty and contain at most 80 characters.  
  
## PinAction

Pins one or more specified products to a specific position in the results.

  * Rule Condition: Must specify non-empty `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` (for search only) or `[Condition.page_categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.page_categories)` (for browse only), but can't specify both.

  * Action Input: mapping of `[pin_position, productId]` pairs (pin position uses 1-based indexing).

  * Action Result: Will pin products with matching ids to the position specified in the final result order.




Example: Suppose the query is `shoes`, the `[Condition.query_terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#Condition.FIELDS.query_terms)` is `shoes` and the pinMap has `{1, "pid1"}`, then product with `pid1` will be pinned to the top position in the final results.

If multiple PinActions are matched to a single request the actions will be processed from most to least recently updated.

Pins to positions larger than the max allowed page size of 120 are not allowed.

JSON representation  
---  
      
    
    {
      "pinMap": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`pinMap` |  `map (key: string ([int64](https://developers.google.com/discovery/v1/type-format) format), value: string)` Required. A map of positions to productIds.Partial matches per action are allowed, if a certain position in the map is already filled that `[position, productId]` pair will be ignored but the rest may still be applied. This case will only occur if multiple pin actions are matched to a single request, as the map guarantees that pin positions are unique within the same action.Duplicate productIds are not permitted within a single pin map.The max size of this map is 120, equivalent to the max [request page size](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#request-body).  
  
## Condition

Metadata that is used to define a condition that triggers an action. A valid condition must specify at least one of 'queryTerms' or 'productsFilter'. If multiple fields are specified, the condition is met if all the fields are satisfied e.g. if a set of query terms and productFilter are set, then only items matching the productFilter for requests with a query matching the query terms wil get boosted.

JSON representation  
---  
      
    
    {
      "queryTerms": [
        {
          object ([QueryTerm](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#QueryTerm))
        }
      ],
      "activeTimeRange": [
        {
          object ([TimeRange](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#TimeRange))
        }
      ],
      "pageCategories": [
        string
      ]
    }  
  
Fields  
---  
`queryTerms[]` |  `object (`[QueryTerm](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#QueryTerm)`)` A list (up to 10 entries) of terms to match the query on. If not specified, match all queries. If many query terms are specified, the condition is matched if any of the terms is a match (i.e. using the OR operator).  
`activeTimeRange[]` |  `object (`[TimeRange](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#TimeRange)`)` Range of time(s) specifying when Condition is active. Condition true if any time range matches.  
`pageCategories[]` |  `string` Used to support browse uses cases. A list (up to 10 entries) of categories or departments. The format should be the same as `[UserEvent.page_categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.page_categories)`;  
  
## QueryTerm

Query terms that we want to match on.

JSON representation  
---  
      
    
    {
      "value": string,
      "fullMatch": boolean
    }  
  
Fields  
---  
`value` |  `string` The value of the term to match on. Value cannot be empty. Value can have at most 3 terms if specified as a partial match. Each space separated string is considered as one term. For example, "a b c" is 3 terms and allowed, but " a b c d" is 4 terms and not allowed for a partial match.  
`fullMatch` |  `boolean` Whether this is supposed to be a full or partial match.  
  
## TimeRange

Used for time-dependent conditions. Example: Want to have rule applied for week long sale.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Start of time range. Range is inclusive.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End of time range. Range is inclusive.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SearchSolutionUseCase

The use case of Cloud Retail Search.

Enums  
---  
`SEARCH_SOLUTION_USE_CASE_UNSPECIFIED` | The value when it's unspecified. In this case, server behavior defaults to `[SEARCH_SOLUTION_USE_CASE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls#SearchSolutionUseCase.ENUM_VALUES.SEARCH_SOLUTION_USE_CASE_SEARCH)`.  
`SEARCH_SOLUTION_USE_CASE_SEARCH` | Search use case. Expects the traffic has a non-empty `[query](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query)`.  
`SEARCH_SOLUTION_USE_CASE_BROWSE` | Browse use case. Expects the traffic has an empty `[query](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query)`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/create)`

|  Creates a Control.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/delete)`

|  Deletes a Control.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/get)`

|  Gets a Control.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/list)`

|  Lists all Controls by their parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/patch)`

|  Updates a Control.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
