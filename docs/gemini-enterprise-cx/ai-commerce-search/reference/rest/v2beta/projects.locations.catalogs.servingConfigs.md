---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs
title: REST Resource: projects.locations.catalogs.servingConfigs \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:56.759472+00:00
---

# REST Resource: projects.locations.catalogs.servingConfigs  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs.servingConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServingConfig
    * JSON representation
  * DynamicFacetSpec
    * JSON representation
  * Mode
  * DiversityType
  * PersonalizationSpec
    * JSON representation
  * Mode
  * Methods



## Resource: ServingConfig

Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "modelId": string,
      "priceRerankingLevel": string,
      "facetControlIds": [
        string
      ],
      "dynamicFacetSpec": {
        object ([DynamicFacetSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#DynamicFacetSpec))
      },
      "boostControlIds": [
        string
      ],
      "filterControlIds": [
        string
      ],
      "redirectControlIds": [
        string
      ],
      "twowaySynonymsControlIds": [
        string
      ],
      "onewaySynonymsControlIds": [
        string
      ],
      "doNotAssociateControlIds": [
        string
      ],
      "replacementControlIds": [
        string
      ],
      "ignoreControlIds": [
        string
      ],
      "diversityLevel": string,
      "diversityType": enum ([DiversityType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#DiversityType)),
      "enableCategoryFilterLevel": string,
      "ignoreRecsDenylist": boolean,
      "personalizationSpec": {
        object ([PersonalizationSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#PersonalizationSpec))
      },
      "solutionTypes": [
        enum ([SolutionType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType))
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. Fully qualified name `projects/*/locations/global/catalogs/*/servingConfig/*`  
`displayName` |  `string` Required. The human readable serving config display name. Used in Retail UI.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`modelId` |  `string` The id of the model in the same `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#Catalog)` to use at serving time. Currently only RecommendationModels are supported: <https://cloud.google.com/retail/recommendations-ai/docs/create-models> Can be changed but only to a compatible model (e.g. others-you-may-like CTR to others-you-may-like CVR).Required when `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_RECOMMENDATION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_RECOMMENDATION)`.  
`priceRerankingLevel` |  `string` How much price ranking we want in serving results. Price reranking causes product items with a similar recommendation probability to be ordered by price, with the highest-priced items first. This setting could result in a decrease in click-through and conversion rates. Allowed values are:

  * `no-price-reranking`
  * `low-price-reranking`
  * `medium-price-reranking`
  * `high-price-reranking`

If not specified, we choose default based on model type. Default value: `no-price-reranking`.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_RECOMMENDATION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_RECOMMENDATION)`.  
`facetControlIds[]` |  `string` Facet specifications for faceted search. If empty, no facets are returned. The ids refer to the ids of `[Control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#Control)` resources with only the Facet control set. These controls are assumed to be in the same `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#Catalog)` as the `[ServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig)`. A maximum of 100 values are allowed. Otherwise, an INVALID_ARGUMENT error is returned.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`dynamicFacetSpec` |  `object (`[DynamicFacetSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#DynamicFacetSpec)`)` The specification for dynamically generated facets. Notice that only textual facets can be dynamically generated.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`boostControlIds[]` |  `string` Condition boost specifications. If a product matches multiple conditions in the specifications, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 100.Notice that if both `[ServingConfig.boost_control_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.boost_control_ids)` and `[SearchRequest.boost_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/search#body.request_body.FIELDS.boost_spec)` are set, the boost conditions from both places are evaluated. If a search request matches multiple boost conditions, the final boost score is equal to the sum of the boost scores from all matched boost conditions.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`filterControlIds[]` |  `string` Condition filter specifications. If a product matches multiple conditions in the specifications, filters from these specifications are all applied and combined via the AND operator. Maximum number of specifications is 100.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`redirectControlIds[]` |  `string` Condition redirect specifications. Only the first triggered redirect action is applied, even if multiple apply. Maximum number of specifications is 1000.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`twowaySynonymsControlIds[]` |  `string` Condition synonyms specifications. If multiple syonyms conditions match, all matching synonyms control in the list will execute. Order of controls in the list will not matter. Maximum number of specifications is 100.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`onewaySynonymsControlIds[]` |  `string` Condition oneway synonyms specifications. If multiple oneway synonyms conditions match, all matching oneway synonyms controls in the list will execute. Order of controls in the list will not matter. Maximum number of specifications is 100.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`doNotAssociateControlIds[]` |  `string` Condition do not associate specifications. If multiple do not associate conditions match, all matching do not associate controls in the list will execute. - Order does not matter. - Maximum number of specifications is 100.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`replacementControlIds[]` |  `string` Condition replacement specifications. - Applied according to the order in the list. - A previously replaced term can not be re-replaced. - Maximum number of specifications is 100.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`ignoreControlIds[]` |  `string` Condition ignore specifications. If multiple ignore conditions match, all matching ignore controls in the list will execute. - Order does not matter. - Maximum number of specifications is 100.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`diversityLevel` |  `string` How much diversity to use in recommendation model results e.g. `medium-diversity` or `high-diversity`. Currently supported values:

  * `no-diversity`
  * `low-diversity`
  * `medium-diversity`
  * `high-diversity`
  * `auto-diversity`

If not specified, we choose default based on recommendation model type. Default value: `no-diversity`.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_RECOMMENDATION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_RECOMMENDATION)`.  
`diversityType` |  `enum (`[DiversityType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#DiversityType)`)` What kind of diversity to use - data driven or rule based. If unset, the server behavior defaults to `[RULE_BASED_DIVERSITY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#DiversityType.ENUM_VALUES.RULE_BASED_DIVERSITY)`.  
`enableCategoryFilterLevel` |  `string` Whether to add additional category filters on the `similar-items` model. If not specified, we enable it by default. Allowed values are:

  * `no-category-match`: No additional filtering of original results from the model and the customer's filters.
  * `relaxed-category-match`: Only keep results with categories that match at least one item categories in the PredictRequests's context item.
  * If customer also sends filters in the PredictRequest, then the results will satisfy both conditions (user given and category match).

Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_RECOMMENDATION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_RECOMMENDATION)`.  
`ignoreRecsDenylist` |  `boolean` When the flag is enabled, the products in the denylist will not be filtered out in the recommendation filtering results.  
`personalizationSpec` |  `object (`[PersonalizationSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#PersonalizationSpec)`)` The specification for personalization spec.Can only be set if `[solutionTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.solution_types)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.Notice that if both `[ServingConfig.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.personalization_spec)` and `[SearchRequest.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/search#body.request_body.FIELDS.personalization_spec)` are set. `[SearchRequest.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/search#body.request_body.FIELDS.personalization_spec)` will override `[ServingConfig.personalization_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig.FIELDS.personalization_spec)`.  
`solutionTypes[]` |  `enum (`[SolutionType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SolutionType)`)` Required. Immutable. Specifies the solution types that a serving config can be associated with. Currently we support setting only one type of solution.  
  
## DynamicFacetSpec

The specifications of dynamically generated facets.

JSON representation  
---  
      
    
    {
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#Mode))
    }  
  
Fields  
---  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#Mode)`)` Mode of the DynamicFacet feature. Defaults to `[Mode.DISABLED](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#Mode.ENUM_VALUES.DISABLED)` if it's unset.  
  
## Mode

Enum to control DynamicFacet mode

Enums  
---  
`MODE_UNSPECIFIED` | Default value.  
`DISABLED` | Disable Dynamic Facet.  
`ENABLED` | Automatic mode built by Google Retail servingConfigs.search.  
  
## DiversityType

What type of diversity - data or rule based.

Enums  
---  
`DIVERSITY_TYPE_UNSPECIFIED` | Default value.  
`RULE_BASED_DIVERSITY` | Rule based diversity.  
`DATA_DRIVEN_DIVERSITY` | Data driven diversity.  
  
## PersonalizationSpec

The specification for personalization.

JSON representation  
---  
      
    
    {
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#Mode_1))
    }  
  
Fields  
---  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#Mode_1)`)` Defaults to `[Mode.AUTO](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#Mode_1.ENUM_VALUES.AUTO)`.  
  
## Mode

The personalization mode of each search request.

Enums  
---  
`MODE_UNSPECIFIED` | Default value. In this case, server behavior defaults to `[Mode.AUTO](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#Mode_1.ENUM_VALUES.AUTO)`.  
`AUTO` | Let CRS decide whether to use personalization based on quality of user event data.  
`DISABLED` | Disable personalization.  
  
## Methods  
  
---  
  
### `[addControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl)`

|  Enables a Control on the specified ServingConfig.  
  
### `[conversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/conversationalSearch)`

|  Performs a conversational search.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/create)`

|  Creates a ServingConfig.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/delete)`

|  Deletes a ServingConfig.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/get)`

|  Gets a ServingConfig.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/list)`

|  Lists all ServingConfigs linked to this catalog.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/patch)`

|  Updates a ServingConfig.  
  
### `[predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/predict)`

|  Makes a recommendation prediction.  
  
### `[removeControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/removeControl)`

|  Disables a Control on the specified ServingConfig.  
  
### `[search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/search)`

|  Performs a search.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
