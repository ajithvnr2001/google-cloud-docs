---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations
title: REST Resource: projects.locations.evaluations \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:31.762586+00:00
---

# REST Resource: projects.locations.evaluations  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.evaluations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Evaluation
    * JSON representation
  * EvaluationSpec
    * JSON representation
  * SearchRequest
    * JSON representation
  * ImageQuery
    * JSON representation
  * FacetSpec
    * JSON representation
  * FacetKey
    * JSON representation
  * Interval
    * JSON representation
  * QueryExpansionSpec
    * JSON representation
  * Condition
  * SpellCorrectionSpec
    * JSON representation
  * Mode
  * EmbeddingSpec
    * JSON representation
  * EmbeddingVector
    * JSON representation
  * RankingExpressionBackend
  * NaturalLanguageQueryUnderstandingSpec
    * JSON representation
  * FilterExtractionCondition
  * ExtractedFilterBehavior
  * SearchAsYouTypeSpec
    * JSON representation
  * Condition
  * Field
    * JSON representation
  * DisplaySpec
    * JSON representation
  * MatchHighlightingCondition
  * CrowdingSpec
    * JSON representation
  * Mode
  * SessionSpec
    * JSON representation
  * RelevanceThreshold
  * RelevanceFilterSpec
    * JSON representation
  * RelevanceThresholdSpec
    * JSON representation
  * RelevanceScoreSpec
    * JSON representation
  * SearchAddonSpec
    * JSON representation
  * CustomRankingParams
    * JSON representation
  * QuerySetSpec
    * JSON representation
  * QualityMetrics
    * JSON representation
  * TopkMetrics
    * JSON representation
  * State
  * Methods



## Resource: Evaluation

An evaluation is a single execution (or run) of an evaluation process. It encapsulates the state of the evaluation and the resulting data.

JSON representation  
---  
      
    
    {
      "name": string,
      "evaluationSpec": {
        object ([EvaluationSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EvaluationSpec))
      },
      "qualityMetrics": {
        object ([QualityMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#QualityMetrics))
      },
      "state": enum ([State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#State)),
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "createTime": string,
      "endTime": string,
      "errorSamples": [
        {
          object ([Status](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The full resource name of the `[Evaluation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Evaluation)`, in the format of `projects/{project}/locations/{location}/evaluations/{evaluation}`.This field must be a UTF-8 encoded string with a length limit of 1024 characters.  
`evaluationSpec` |  `object (`[EvaluationSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EvaluationSpec)`)` Required. The specification of the evaluation.  
`qualityMetrics` |  `object (`[QualityMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#QualityMetrics)`)` Output only. The metrics produced by the evaluation, averaged across all `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`s in the `[SampleQuerySet](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets#SampleQuerySet)`.Only populated when the evaluation's state is SUCCEEDED.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#State)`)` Output only. The state of the evaluation.  
`error` |  `object (`[Status](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The error that occurred during evaluation. Only populated when the evaluation's state is FAILED.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the `[Evaluation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Evaluation)` was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the `[Evaluation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Evaluation)` was completed at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`errorSamples[]` |  `object (`[Status](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. A sample of errors encountered while processing the request.  
  
## EvaluationSpec

Describes the specification of the evaluation.

JSON representation  
---  
      
    
    {
      "querySetSpec": {
        object ([QuerySetSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#QuerySetSpec))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "searchRequest": {
        object ([SearchRequest](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`querySetSpec` |  `object (`[QuerySetSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#QuerySetSpec)`)` Optional. The specification of the query set.  
The search specification. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`searchRequest` |  `object (`[SearchRequest](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest)`)` Required. The search request that is used to perform the evaluation.Only the following fields within SearchRequest are supported; if any other fields are provided, an UNSUPPORTED error will be returned:

  * `[SearchRequest.serving_config](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.serving_config)`
  * `[SearchRequest.branch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.branch)`
  * `[SearchRequest.canonical_filter](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.canonical_filter)`
  * `[SearchRequest.query_expansion_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.query_expansion_spec)`
  * `[SearchRequest.spell_correction_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.spell_correction_spec)`
  * `[SearchRequest.content_search_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.content_search_spec)`
  * `[SearchRequest.user_pseudo_id](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.user_pseudo_id)`

  
End of mutually exclusive fields.  
  
## SearchRequest

Request message for `[SearchService.Search](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1alpha.SearchService.Search)` method.

JSON representation  
---  
      
    
    {
      "servingConfig": string,
      "branch": string,
      "query": string,
      "pageCategories": [
        string
      ],
      "imageQuery": {
        object ([ImageQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#ImageQuery))
      },
      "pageSize": integer,
      "pageToken": string,
      "offset": integer,
      "oneBoxPageSize": integer,
      "dataStoreSpecs": [
        {
          object ([DataStoreSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/DataStoreSpec))
        }
      ],
      "numResultsPerDataStore": integer,
      "filter": string,
      "canonicalFilter": string,
      "orderBy": string,
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/UserInfo))
      },
      "languageCode": string,
      "regionCode": string,
      "facetSpecs": [
        {
          object ([FacetSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FacetSpec))
        }
      ],
      "boostSpec": {
        object (BoostSpec)
      },
      "params": {
        string: value,
        ...
      },
      "queryExpansionSpec": {
        object ([QueryExpansionSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#QueryExpansionSpec))
      },
      "spellCorrectionSpec": {
        object ([SpellCorrectionSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SpellCorrectionSpec))
      },
      "userPseudoId": string,
      "useLatestData": boolean,
      "contentSearchSpec": {
        object ([ContentSearchSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/ContentSearchSpec))
      },
      "embeddingSpec": {
        object ([EmbeddingSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EmbeddingSpec))
      },
      "rankingExpression": string,
      "rankingExpressionBackend": enum ([RankingExpressionBackend](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RankingExpressionBackend)),
      "safeSearch": boolean,
      "userLabels": {
        string: string,
        ...
      },
      "naturalLanguageQueryUnderstandingSpec": {
        object ([NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#NaturalLanguageQueryUnderstandingSpec))
      },
      "searchAsYouTypeSpec": {
        object ([SearchAsYouTypeSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchAsYouTypeSpec))
      },
      "customFineTuningSpec": {
        object ([CustomFineTuningSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/CustomFineTuningSpec))
      },
      "displaySpec": {
        object ([DisplaySpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#DisplaySpec))
      },
      "crowdingSpecs": [
        {
          object ([CrowdingSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#CrowdingSpec))
        }
      ],
      "session": string,
      "sessionSpec": {
        object ([SessionSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SessionSpec))
      },
      "relevanceThreshold": enum ([RelevanceThreshold](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThreshold)),
      "relevanceFilterSpec": {
        object ([RelevanceFilterSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceFilterSpec))
      },
      "personalizationSpec": {
        object ([PersonalizationSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/PersonalizationSpec))
      },
      "relevanceScoreSpec": {
        object ([RelevanceScoreSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceScoreSpec))
      },
      "searchAddonSpec": {
        object ([SearchAddonSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchAddonSpec))
      },
      "customRankingParams": {
        object ([CustomRankingParams](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#CustomRankingParams))
      },
      "entity": string
    }  
  
Fields  
---  
`servingConfig` |  `string` Required. The resource name of the Search serving config, such as `projects/*/locations/global/collections/default_collection/engines/*/servingConfigs/default_serving_config`, or `projects/*/locations/global/collections/default_collection/dataStores/default_data_store/servingConfigs/default_serving_config`. This field is used to identify the serving configuration name, set of models used to make the search.  
`branch` |  `string` The branch resource name, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store/branches/0`.Use `default_branch` as the branch ID or leave this field empty, to search documents under the default branch.  
`query` |  `string` Raw search query.  
`pageCategories[]` |  `string` Optional. The categories associated with a category page. Must be set for category navigation queries to achieve good search quality. The format should be the same as `[PageInfo.page_category](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.userEvents#PageInfo.FIELDS.page_category)`. This field is the equivalent of the query for browse (navigation) queries. It's used by the browse model when the query is empty.If the field is empty, it will not be used by the browse model. If the field contains more than one element, only the first element will be used.To represent full path of a category, use '>' character to separate different hierarchies. If '>' is part of the category name, replace it with other character(s). For example, `Graphics Cards > RTX>4090 > Founders Edition` where "RTX > 4090" represents one level, can be rewritten as `Graphics Cards > RTX_4090 > Founders Edition`  
`imageQuery` |  `object (`[ImageQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#ImageQuery)`)` Raw image query.  
`pageSize` |  `integer` Maximum number of `[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`s to return. The maximum allowed value depends on the data type. Values above the maximum value are coerced to the maximum value.

  * Websites with basic indexing: Default `10`, Maximum `25`.
  * Websites with advanced indexing: Default `25`, Maximum `50`.
  * Other: Default `50`, Maximum `100`.

If this field is negative, an `INVALID_ARGUMENT` is returned.  
`pageToken` |  `string` A page token received from a previous `[SearchService.Search](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1alpha.SearchService.Search)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[SearchService.Search](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1alpha.SearchService.Search)` must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`offset` |  `integer` A 0-indexed integer that specifies the current offset (that is, starting result location, amongst the `[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`s deemed by the API as relevant) in search results. This field is only considered if `[pageToken](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.page_token)` is unset.If this field is negative, an `INVALID_ARGUMENT` is returned.A large offset may be capped to a reasonable threshold.  
`oneBoxPageSize` |  `integer` The maximum number of results to return for OneBox. This applies to each OneBox type individually. Default number is 10.  
`dataStoreSpecs[]` |  `object (`[DataStoreSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/DataStoreSpec)`)` Specifications that define the specific `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores#DataStore)`s to be searched, along with configurations for those data stores. This is only considered for `[Engine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines#Engine)`s with multiple data stores. For engines with a single data store, the specs directly under `[SearchRequest](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest)` should be used.On an engine with multiple data stores, this field is optional. If it's empty, all of the engine's data stores are searched (blended search). Unless it specifies exactly one data store, some request fields, such as `orderBy` and `queryExpansionSpec`, aren't supported and return an `INVALID_ARGUMENT` error.  
`numResultsPerDataStore` |  `integer` Optional. The maximum number of results to retrieve from each data store. If not specified, it will use the `[SearchRequest.DataStoreSpec.num_results](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/DataStoreSpec#FIELDS.num_results)` if provided, otherwise there is no limit.  
`filter` |  `string` The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive.If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)  
`canonicalFilter` |  `string` The default filter that is applied when a user performs a search without checking any filters on the search page.The filter applied to every search request when quality improvement such as query expansion is needed. In the case a query does not have a sufficient amount of results this filter will be used to determine whether or not to enable the query expansion flow. The original filter will still be used for the query expanded search. This field is strongly recommended to achieve high search quality.For more information about filter syntax, see `[SearchRequest.filter](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.filter)`.  
`orderBy` |  `string` The order in which documents are returned. Documents can be ordered by a field in an `[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)` object. Leave it unset if ordered by relevance. `orderBy` expression is case-sensitive.For more information on ordering the website search results, see [Order web search results](https://cloud.google.com/generative-ai-app-builder/docs/order-web-search-results). For more information on ordering the healthcare search results, see [Order healthcare search results](https://cloud.google.com/generative-ai-app-builder/docs/order-hc-results). If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/UserInfo)`)` Information about the end user. Highly recommended for analytics and personalization. `[UserInfo.user_agent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/UserInfo#FIELDS.user_agent)` is used to deduce `deviceType` for analytics.  
`languageCode` |  `string` The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see [Standard fields](https://cloud.google.com/apis/design/standard_fields). This field helps to better interpret the query. If a value isn't specified, the query language code is automatically detected, which may not be accurate.  
`regionCode` |  `string` The Unicode country/region code (CLDR) of a location, such as "US" and "419". For more information, see [Standard fields](https://cloud.google.com/apis/design/standard_fields). If set, then results will be boosted based on the regionCode provided.  
`facetSpecs[]` |  `object (`[FacetSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FacetSpec)`)` Facet specifications for faceted search. If empty, no facets are returned.A maximum of 100 values are allowed. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`boostSpec` |  `object (`BoostSpec`)` Boost specification to boost certain documents. For more information on boosting, see [Boosting](https://cloud.google.com/generative-ai-app-builder/docs/boost-search-results)  
`params` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Additional search parameters.For public website search only, supported values are:

  * `user_country_code`: string. Default empty. If set to non-empty, results are restricted or boosted based on the location provided. For example, `user_country_code: "au"`

For available codes see [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes)

  * `searchType`: double. Default empty. Enables non-webpage searching depending on the value. The only valid non-default value is 1, which enables image searching. For example, `searchType: 1`

  
`queryExpansionSpec` |  `object (`[QueryExpansionSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#QueryExpansionSpec)`)` The query expansion specification that specifies the conditions under which query expansion occurs.  
`spellCorrectionSpec` |  `object (`[SpellCorrectionSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SpellCorrectionSpec)`)` The spell correction specification that specifies the mode under which spell correction takes effect.  
`userPseudoId` |  `string` Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.This field should NOT have a fixed value such as `unknown_visitor`.This should be the same identifier as `[UserEvent.user_pseudo_id](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id)` and `[CompleteQueryRequest.user_pseudo_id](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores/completeQuery#body.QUERY_PARAMETERS.user_pseudo_id)`The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`useLatestData` |  `boolean` uses the Engine, ServingConfig and Control freshly read from the database.Note: this skips config cache and introduces dependency on databases, which could significantly increase the API latency. It should only be used for testing, but not serving end users.  
`contentSearchSpec` |  `object (`[ContentSearchSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/ContentSearchSpec)`)` A specification for configuring the behavior of content search.  
`embeddingSpec` |  `object (`[EmbeddingSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EmbeddingSpec)`)` Uses the provided embedding to do additional semantic document retrieval. The retrieval is based on the dot product of `[SearchRequest.EmbeddingSpec.EmbeddingVector.vector](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EmbeddingVector.FIELDS.vector)` and the document embedding that is provided in `[SearchRequest.EmbeddingSpec.EmbeddingVector.field_path](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EmbeddingVector.FIELDS.field_path)`.If `[SearchRequest.EmbeddingSpec.EmbeddingVector.field_path](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EmbeddingVector.FIELDS.field_path)` is not provided, it will use `[ServingConfig.EmbeddingConfig.field_path](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.embedding_config)`.  
`rankingExpression` |  `string` Optional. The ranking expression controls the customized ranking on retrieval documents. This overrides `[ServingConfig.ranking_expression](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.ranking_expression)`. The syntax and supported features depend on the `rankingExpressionBackend` value. If `rankingExpressionBackend` is not provided, it defaults to `RANK_BY_EMBEDDING`.If `[rankingExpressionBackend](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.ranking_expression_backend)` is not provided or set to `RANK_BY_EMBEDDING`, it should be a single function or multiple functions that are joined by "+".

  * rankingExpression = function, { " + ", function };

Supported functions:

  * double * relevanceScore
  * double * dotProduct(embedding_field_path)

Function variables:

  * `relevanceScore`: pre-defined keywords, used for measure relevance between query and document.
  * `embedding_field_path`: the document embedding field used with query embedding vector.
  * `dotProduct`: embedding function between `embedding_field_path` and query embedding vector.

Example ranking expression:If document has an embedding field doc_embedding, the ranking expression could be `0.5 * relevanceScore + 0.3 * dotProduct(doc_embedding)`.If `[rankingExpressionBackend](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.ranking_expression_backend)` is set to `RANK_BY_FORMULA`, the following expression types (and combinations of those chained using + or * operators) are supported:

  * `double`
  * `signal`
  * `log(signal)`
  * `exp(signal)`
  * `rr(signal, double > 0)` \-- reciprocal rank transformation with second argument being a denominator constant.
  * `isNan(signal)` \-- returns 0 if signal is NaN, 1 otherwise.
  * `fillNan(signal1, signal2 | double)` \-- if signal1 is NaN, returns signal2 | double, else returns signal1.

Here are a few examples of ranking formulas that use the supported ranking expression types:

  * `0.2 * semanticSimilarityScore + 0.8 * log(keywordSimilarityScore)` \-- mostly rank by the logarithm of `keywordSimilarityScore` with slight `semantic_smilarity_score` adjustment.
  * `0.2 * exp(fillNan(semanticSimilarityScore, 0)) + 0.3 * isNan(keywordSimilarityScore)` \-- rank by the exponent of `semanticSimilarityScore` filling the value with 0 if it's NaN, also add constant 0.3 adjustment to the final score if `semanticSimilarityScore` is NaN.
  * `0.2 * rr(semanticSimilarityScore, 16) + 0.8 * rr(keywordSimilarityScore, 16)` \-- mostly rank by the reciprocal rank of `keywordSimilarityScore` with slight adjustment of reciprocal rank of `semantic_smilarity_score`.

The following signals are supported:

  * `semanticSimilarityScore`: semantic similarity adjustment that is calculated using the embeddings generated by a proprietary Google model. This score determines how semantically similar a search query is to a document.
  * `keywordSimilarityScore`: keyword match adjustment uses the Best Match 25 (BM25) ranking function. This score is calculated using a probabilistic model to estimate the probability that a document is relevant to a given query.
  * `relevanceScore`: semantic relevance adjustment that uses a proprietary Google model to determine the meaning and intent behind a user's query in context with the content in the documents.
  * `pctrRank`: predicted conversion rate adjustment as a rank use predicted Click-through rate (pCTR) to gauge the relevance and attractiveness of a search result from a user's perspective. A higher pCTR suggests that the result is more likely to satisfy the user's query and intent, making it a valuable signal for ranking.
  * `freshnessRank`: freshness adjustment as a rank
  * `documentAge`: The time in hours elapsed since the document was last updated, a floating-point number (e.g., 0.25 means 15 minutes).
  * `topicalityRank`: topicality adjustment as a rank. uses proprietary Google model to determine the keyword-based overlap between the query and the document.
  * `baseRank`: the default rank of the result
  * `mediaActorMatch`: whether the media actor matches the query
  * `mediaDirectorMatch`: whether the media director matches the query
  * `mediaGenreMatch`: whether the media genre matches the query
  * `mediaLanguageMatch`: whether the media language matches the query
  * `mediaTitleMatch`: whether the media title matches the query
  * `mediaPrefixSimilarityRank`: prefix similarity rank for media results
  * `mediaSemanticSimilarityRank`: semantic similarity rank for media results

  
`rankingExpressionBackend` |  `enum (`[RankingExpressionBackend](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RankingExpressionBackend)`)` Optional. The backend to use for the ranking expression evaluation.  
`safeSearch` |  `boolean` Whether to turn on safe search. This is only supported for website search.  
`userLabels` |  `map (key: string, value: string)` The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.  
`naturalLanguageQueryUnderstandingSpec` |  `object (`[NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#NaturalLanguageQueryUnderstandingSpec)`)` Optional. Config for natural language query understanding capabilities, such as extracting structured field filters from the query. Refer to [this documentation](https://cloud.google.com/generative-ai-app-builder/docs/natural-language-queries) for more information. If `naturalLanguageQueryUnderstandingSpec` is not specified, no additional natural language query understanding will be done.  
`searchAsYouTypeSpec` |  `object (`[SearchAsYouTypeSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchAsYouTypeSpec)`)` Search as you type configuration. Only supported for the `[IndustryVertical.MEDIA](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/IndustryVertical#ENUM_VALUES.MEDIA)` vertical.  
`customFineTuningSpec` |  `object (`[CustomFineTuningSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/CustomFineTuningSpec)`)` Custom fine tuning configs. If set, it has higher priority than the configs set in `[ServingConfig.custom_fine_tuning_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.custom_fine_tuning_spec)`.  
`displaySpec` |  `object (`[DisplaySpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#DisplaySpec)`)` Optional. Config for display feature, like match highlighting on search results.  
`crowdingSpecs[]` |  `object (`[CrowdingSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#CrowdingSpec)`)` Optional. Crowding specifications for improving result diversity. If multiple CrowdingSpecs are specified, crowding will be evaluated on each unique combination of the `field` values, and maxCount will be the maximum value of `maxCount` across all CrowdingSpecs. For example, if the first CrowdingSpec has `field` = "color" and `maxCount` = 3, and the second CrowdingSpec has `field` = "size" and `maxCount` = 2, then after 3 documents that share the same color AND size have been returned, subsequent ones should be removed or demoted.  
`session` |  `string` The session resource name. Optional.Session allows users to do multi-turn /search API calls or coordination between /search API calls and /answer API calls.Example #1 (multi-turn /search API calls): Call /search API with the session ID generated in the first call. Here, the previous search query gets considered in query standing. I.e., if the first query is "How did Alphabet do in 2022?" and the current query is "How about 2023?", the current query will be interpreted as "How did Alphabet do in 2023?".Example #2 (coordination between /search API calls and /answer API calls): Call /answer API with the session ID generated in the first call. Here, the answer generation happens in the context of the search results from the first search call.  
`sessionSpec` |  `object (`[SessionSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SessionSpec)`)` Session specification.Can be used only when `session` is set.  
`relevanceThreshold` |  `enum (`[RelevanceThreshold](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThreshold)`)` The global relevance threshold of the search results.Defaults to Google defined threshold, leveraging a balance of precision and recall to deliver both highly accurate results and comprehensive coverage of relevant information.If more granular relevance filtering is required, use the `relevanceFilterSpec` instead.This feature is not supported for healthcare search.  
`relevanceFilterSpec` |  `object (`[RelevanceFilterSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceFilterSpec)`)` Optional. The granular relevance filtering specification.If not specified, the global `relevanceThreshold` will be used for all sub-searches. If specified, this overrides the global `relevanceThreshold` to use thresholds on a per sub-search basis.This feature is currently supported only for custom and site search.  
`personalizationSpec` |  `object (`[PersonalizationSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/PersonalizationSpec)`)` The specification for personalization.Notice that if both `[ServingConfig.personalization_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.personalization_spec)` and `[SearchRequest.personalization_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.personalization_spec)` are set, `[SearchRequest.personalization_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.personalization_spec)` overrides `[ServingConfig.personalization_spec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.personalization_spec)`.  
`relevanceScoreSpec` |  `object (`[RelevanceScoreSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceScoreSpec)`)` Optional. The specification for returning the relevance score.  
`searchAddonSpec` |  `object (`[SearchAddonSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchAddonSpec)`)` Optional. SearchAddonSpec is used to disable add-ons for search as per new repricing model. This field is only supported for search requests.  
`customRankingParams` |  `object (`[CustomRankingParams](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#CustomRankingParams)`)` Optional. Optional configuration for the Custom Ranking feature.  
`entity` |  `string` Optional. The entity for customers that may run multiple different entities, domains, sites or regions, for example, "Google US", "Google Ads", "Waymo", "google.com", "youtube.com", etc. If this is set, it should be exactly matched with `[UserEvent.entity](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.userEvents#UserEvent.FIELDS.entity)` to get search results boosted by entity.  
  
## ImageQuery

Specifies the image query input.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "imageBytes": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Specifies the image bytes. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`imageBytes` |  `string` Base64 encoded image bytes. Supported image formats: JPEG, PNG, and BMP.  
End of mutually exclusive fields.  
  
## FacetSpec

A facet specification to perform faceted search.

JSON representation  
---  
      
    
    {
      "facetKey": {
        object ([FacetKey](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FacetKey))
      },
      "limit": integer,
      "excludedFilterKeys": [
        string
      ],
      "enableDynamicPosition": boolean
    }  
  
Fields  
---  
`facetKey` |  `object (`[FacetKey](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FacetKey)`)` Required. The facet key specification.  
`limit` |  `integer` Maximum facet values that are returned for this facet. If unspecified, defaults to 20. The maximum allowed value is 300. Values above 300 are coerced to 300. For aggregation in healthcare search, when the [FacetKey.key] is "healthcare_aggregation_key", the limit will be overridden to 10,000 internally, regardless of the value set here.If this field is negative, an `INVALID_ARGUMENT` is returned.  
`excludedFilterKeys[]` |  `string` List of keys to exclude when faceting.By default, `[FacetKey.key](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FacetKey.FIELDS.key)` is not excluded from the filter unless it is listed in this field.Listing a facet key in this field allows its values to appear as facet results, even when they are filtered out of search results. Using this field does not affect what search results are returned.For example, suppose there are 100 documents with the color facet "Red" and 200 documents with the color facet "Blue". A query containing the filter "color:ANY("Red")" and having "color" as `[FacetKey.key](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FacetKey.FIELDS.key)` would by default return only "Red" documents in the search results, and also return "Red" with count 100 as the only color facet. Although there are also blue documents available, "Blue" would not be shown as an available facet value.If "color" is listed in "excludedFilterKeys", then the query returns the facet values "Red" with count 100 and "Blue" with count 200, because the "color" key is now excluded from the filter. Because this field doesn't affect search results, the search results are still correctly filtered to return only "Red" documents.A maximum of 100 values are allowed. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`enableDynamicPosition` |  `boolean` Enables dynamic position for this facet. If set to true, the position of this facet among all facets in the response is determined automatically. If dynamic facets are enabled, it is ordered together. If set to false, the position of this facet in the response is the same as in the request, and it is ranked before the facets with dynamic position enable and all dynamic facets.For example, you may always want to have rating facet returned in the response, but it's not necessarily to always display the rating facet at the top. In that case, you can set enableDynamicPosition to true so that the position of rating facet in response is determined automatically.Another example, assuming you have the following facets in the request:

  * "rating", enableDynamicPosition = true
  * "price", enableDynamicPosition = false
  * "brands", enableDynamicPosition = false

And also you have a dynamic facets enabled, which generates a facet `gender`. Then the final order of the facets in the response can be ("price", "brands", "rating", "gender") or ("price", "brands", "gender", "rating") depends on how API orders "gender" and "rating" facets. However, notice that "price" and "brands" are always ranked at first and second position because their enableDynamicPosition is false.  
  
## FacetKey

Specifies how a facet is computed.

JSON representation  
---  
      
    
    {
      "key": string,
      "intervals": [
        {
          object ([Interval](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Interval))
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
      "orderBy": string
    }  
  
Fields  
---  
`key` |  `string` Required. Supported textual and numerical facet keys in `[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)` object, over which the facet values are computed. Facet key is case-sensitive.  
`intervals[]` |  `object (`[Interval](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Interval)`)` Set only if values should be bucketed into intervals. Must be set for facets with numerical values. Must not be set for facet with text values. Maximum number of intervals is 30.  
`restrictedValues[]` |  `string` Only get facet for the given restricted values. Only supported on textual fields. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "restrictedValues" to "Action > 2022", the "category" facet only contains "Action > 2022". Only supported on textual fields. Maximum is 10.  
`prefixes[]` |  `string` Only get facet values that start with the given string prefix. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "prefixes" to "Action", the "category" facet only contains "Action > 2022" and "Action > 2021". Only supported on textual fields. Maximum is 10.  
`contains[]` |  `string` Only get facet values that contain the given strings. For example, suppose "category" has three values "Action > 2022", "Action > 2021" and "Sci-Fi > 2022". If set "contains" to "2022", the "category" facet only contains "Action > 2022" and "Sci-Fi > 2022". Only supported on textual fields. Maximum is 10.  
`caseInsensitive` |  `boolean` True to make facet keys case insensitive when getting faceting values with prefixes or contains; false otherwise.  
`orderBy` |  `string` The order in which documents are returned.Allowed values are:

  * "count desc", which means order by `[SearchResponse.Facet.values.count](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SearchResponse#FacetValue.FIELDS.count)` descending.
  * "value desc", which means order by `[SearchResponse.Facet.values.value](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SearchResponse#FacetValue.FIELDS.value)` descending. Only applies to textual facets.

If not set, textual values are sorted in [natural order](https://en.wikipedia.org/wiki/Natural_sort_order); numerical intervals are sorted in the order given by `[FacetSpec.FacetKey.intervals](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FacetKey.FIELDS.intervals)`.  
  
## Interval

A floating point interval.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "minimum": number,
      "exclusiveMinimum": number
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "maximum": number,
      "exclusiveMaximum": number
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The lower bound of the interval. If neither of the min fields are set, then the lower bound is negative infinity.This field must be not larger than max. Otherwise, an `INVALID_ARGUMENT` error is returned. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`minimum` |  `number` Inclusive lower bound.  
`exclusiveMinimum` |  `number` Exclusive lower bound.  
End of mutually exclusive fields.  
The upper bound of the interval. If neither of the max fields are set, then the upper bound is positive infinity.This field must be not smaller than min. Otherwise, an `INVALID_ARGUMENT` error is returned. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`maximum` |  `number` Inclusive upper bound.  
`exclusiveMaximum` |  `number` Exclusive upper bound.  
End of mutually exclusive fields.  
  
## QueryExpansionSpec

Specification to determine under which conditions query expansion should occur.

JSON representation  
---  
      
    
    {
      "condition": enum ([Condition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition)),
      "pinUnexpandedResults": boolean
    }  
  
Fields  
---  
`condition` |  `enum (`[Condition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition)`)` The condition under which query expansion should occur. Default to `[Condition.DISABLED](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition.ENUM_VALUES.DISABLED)`.  
`pinUnexpandedResults` |  `boolean` Whether to pin unexpanded results. If this field is set to true, unexpanded products are always at the top of the search results, followed by the expanded results.  
  
## Condition

Enum describing under which condition query expansion should occur.

Enums  
---  
`CONDITION_UNSPECIFIED` | Unspecified query expansion condition. In this case, server behavior defaults to `[Condition.DISABLED](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition.ENUM_VALUES.DISABLED)`.  
`DISABLED` | Disabled query expansion. Only the exact search query is used, even if `[SearchResponse.total_size](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SearchResponse#FIELDS.total_size)` is zero.  
`AUTO` | Automatic query expansion built by the Search API.  
  
## SpellCorrectionSpec

The specification for query spell correction.

JSON representation  
---  
      
    
    {
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Mode))
    }  
  
Fields  
---  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Mode)`)` The mode under which spell correction replaces the original search query. Defaults to `[Mode.AUTO](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Mode.ENUM_VALUES.AUTO)`.  
  
## Mode

Enum describing under which mode spell correction should occur.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified spell correction mode. In this case, server behavior defaults to `[Mode.AUTO](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Mode.ENUM_VALUES.AUTO)`.  
`SUGGESTION_ONLY` | Search API tries to find a spelling suggestion. If a suggestion is found, it is put in the `[SearchResponse.corrected_query](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SearchResponse#FIELDS.corrected_query)`. The spelling suggestion won't be used as the search query.  
`AUTO` | Automatic spell correction built by the Search API. Search will be based on the corrected query if found.  
  
## EmbeddingSpec

The specification that uses customized query embedding vector to do semantic document retrieval.

JSON representation  
---  
      
    
    {
      "embeddingVectors": [
        {
          object ([EmbeddingVector](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EmbeddingVector))
        }
      ]
    }  
  
Fields  
---  
`embeddingVectors[]` |  `object (`[EmbeddingVector](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#EmbeddingVector)`)` The embedding vector used for retrieval. Limit to 1.  
  
## EmbeddingVector

Embedding vector.

JSON representation  
---  
      
    
    {
      "fieldPath": string,
      "vector": [
        number
      ]
    }  
  
Fields  
---  
`fieldPath` |  `string` Embedding field path in schema.  
`vector[]` |  `number` Query embedding vector.  
  
## RankingExpressionBackend

The backend to use for the ranking expression evaluation.

Enums  
---  
`RANKING_EXPRESSION_BACKEND_UNSPECIFIED` | Default option for unspecified/unknown values.  
`BYOE` | Deprecated: Use `RANK_BY_EMBEDDING` instead. Ranking by custom embedding model, the default way to evaluate the ranking expression. Legacy enum option, `RANK_BY_EMBEDDING` should be used instead.This item is deprecated!  
`CLEARBOX` | Deprecated: Use `RANK_BY_FORMULA` instead. Ranking by custom formula. Legacy enum option, `RANK_BY_FORMULA` should be used instead.This item is deprecated!  
`RANK_BY_EMBEDDING` | Ranking by custom embedding model, the default way to evaluate the ranking expression.  
`RANK_BY_FORMULA` | Ranking by custom formula.  
  
## NaturalLanguageQueryUnderstandingSpec

Specification to enable natural language understanding capabilities for search requests.

JSON representation  
---  
      
    
    {
      "filterExtractionCondition": enum ([FilterExtractionCondition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FilterExtractionCondition)),
      "geoSearchQueryDetectionFieldNames": [
        string
      ],
      "extractedFilterBehavior": enum ([ExtractedFilterBehavior](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#ExtractedFilterBehavior)),
      "allowedFieldNames": [
        string
      ]
    }  
  
Fields  
---  
`filterExtractionCondition` |  `enum (`[FilterExtractionCondition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FilterExtractionCondition)`)` The condition under which filter extraction should occur. Server behavior defaults to `DISABLED`.  
`geoSearchQueryDetectionFieldNames[]` |  `string` Field names used for location-based filtering, where geolocation filters are detected in natural language search queries. Only valid when the FilterExtractionCondition is set to `ENABLED`.  
`extractedFilterBehavior` |  `enum (`[ExtractedFilterBehavior](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#ExtractedFilterBehavior)`)` Optional. Controls behavior of how extracted filters are applied to the search. The default behavior depends on the request. For single datastore structured search, the default is `HARD_FILTER`. For multi-datastore search, the default behavior is `SOFT_BOOST`. location-based filters are always applied as hard filters, and the `SOFT_BOOST` setting will not affect them. This field is only used if `[SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FilterExtractionCondition)` is set to `[FilterExtractionCondition.ENABLED](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#FilterExtractionCondition.ENUM_VALUES.ENABLED)`.  
`allowedFieldNames[]` |  `string` Optional. Allowlist of fields that can be used for natural language filter extraction. By default, if this is unspecified, all indexable fields are eligible for natural language filter extraction (but are not guaranteed to be used). If any fields are specified in allowedFieldNames, only the fields that are both marked as indexable in the schema and specified in the allowlist will be eligible for natural language filter extraction. Note: for multi-datastore search, this is not yet supported, and will be ignored.  
  
## FilterExtractionCondition

Enum describing under which condition filter extraction should occur.

Enums  
---  
`CONDITION_UNSPECIFIED` | Server behavior defaults to `DISABLED`.  
`DISABLED` | Disables NL filter extraction.  
`ENABLED` | Enables NL filter extraction.  
  
## ExtractedFilterBehavior

Enum describing how extracted filters are applied to the search.

Enums  
---  
`EXTRACTED_FILTER_BEHAVIOR_UNSPECIFIED` | `EXTRACTED_FILTER_BEHAVIOR_UNSPECIFIED` will use the default behavior for extracted filters. For single datastore search, the default is to apply as hard filters. For multi-datastore search, the default is to apply as soft boosts.  
`HARD_FILTER` | Applies all extracted filters as hard filters on the results. Results that do not pass the extracted filters will not be returned in the result set.  
`SOFT_BOOST` | Applies all extracted filters as soft boosts. Results that pass the filters will be boosted up to higher ranks in the result set.  
  
## SearchAsYouTypeSpec

Specification for search as you type in search requests.

JSON representation  
---  
      
    
    {
      "condition": enum ([Condition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition_1)),
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Field))
        }
      ],
      "scoreThreshold": number
    }  
  
Fields  
---  
`condition` |  `enum (`[Condition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition_1)`)` The condition under which search as you type should occur. Default to `[Condition.DISABLED](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition_1.ENUM_VALUES.DISABLED)`.  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Field)`)` Optional. The list of fields to be used for Search As You type scoring.  
`scoreThreshold` |  `number` Optional. Search As You type score threshold for filtering purpose. We keep the result if `score` >= `scoreThreshold`.  
  
## Condition

Enum describing under which condition search as you type should occur.

Enums  
---  
`CONDITION_UNSPECIFIED` | Server behavior defaults to `[Condition.DISABLED](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Condition_1.ENUM_VALUES.DISABLED)`.  
`DISABLED` | Disables Search As You Type.  
`ENABLED` | Enables Search As You Type.  
`AUTO` | Automatic switching between search-as-you-type and standard search modes, ideal for single-API implementations (e.g., debouncing).  
  
## Field

A schema field to be used for Search As You type scoring on this request. Overrides any data-store-level Search As You type field configuration for the duration of the request.

JSON representation  
---  
      
    
    {
      "key": string,
      "weight": number
    }  
  
Fields  
---  
`key` |  `string` Required. A field key that has been indexed for Search As You type.  
`weight` |  `number` Optional. weight for scores from this field. Defaults to 1.0 if not specified.  
  
## DisplaySpec

Specifies features for display, like match highlighting.

JSON representation  
---  
      
    
    {
      "matchHighlightingCondition": enum ([MatchHighlightingCondition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#MatchHighlightingCondition))
    }  
  
Fields  
---  
`matchHighlightingCondition` |  `enum (`[MatchHighlightingCondition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#MatchHighlightingCondition)`)` The condition under which match highlighting should occur.  
  
## MatchHighlightingCondition

Enum describing under which condition match highlighting should occur.

Enums  
---  
`MATCH_HIGHLIGHTING_CONDITION_UNSPECIFIED` | Server behavior is the same as `MATCH_HIGHLIGHTING_DISABLED`.  
`MATCH_HIGHLIGHTING_DISABLED` | Disables match highlighting on all documents.  
`MATCH_HIGHLIGHTING_ENABLED` | Enables match highlighting on all documents.  
  
## CrowdingSpec

Specification for crowding. Crowding improves the diversity of search results by limiting the number of results that share the same field value. For example, crowding on the color field with a maxCount of 3 and mode DROP_CROWDED_RESULTS will return at most 3 results with the same color across all pages.

JSON representation  
---  
      
    
    {
      "field": string,
      "maxCount": integer,
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Mode_1))
    }  
  
Fields  
---  
`field` |  `string` The field to use for crowding. Documents can be crowded by a field in the `[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)` object. Crowding field is case sensitive.  
`maxCount` |  `integer` The maximum number of documents to keep per value of the field. Once there are at least maxCount previous results which contain the same value for the given field (according to the order specified in `orderBy`), later results with the same value are "crowded away". If not specified, the default value is 1.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Mode_1)`)` Mode to use for documents that are crowded away.  
  
## Mode

Enum describing the mode to use for documents that are crowded away. They can be dropped or demoted to the later pages.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified crowding mode. In this case, server behavior defaults to `[Mode.DROP_CROWDED_RESULTS](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Mode_1.ENUM_VALUES.DROP_CROWDED_RESULTS)`.  
`DROP_CROWDED_RESULTS` | Drop crowded results.  
`DEMOTE_CROWDED_RESULTS_TO_END` | Demote crowded results to the later pages.  
  
## SessionSpec

Session specification.

JSON representation  
---  
      
    
    {
      "queryId": string,
      "searchResultPersistenceCount": integer
    }  
  
Fields  
---  
`queryId` |  `string` If set, the search result gets stored to the "turn" specified by this query ID.Example: Let's say the session looks like this: session { name: ".../sessions/xxx" turns { query { text: "What is foo?" queryId: ".../questions/yyy" } answer: "Foo is ..." } turns { query { text: "How about bar then?" queryId: ".../questions/zzz" } } }The user can call /search API with a request like this:session: ".../sessions/xxx" sessionSpec { queryId: ".../questions/zzz" }Then, the API stores the search result, associated with the last turn. The stored search result can be used by a subsequent /answer API call (with the session ID and the query ID specified). Also, it is possible to call /search and /answer in parallel with the same session ID & query ID.  
`searchResultPersistenceCount` |  `integer` The number of top search results to persist. The persisted search results can be used for the subsequent /answer api call.This field is similar to the `summaryResultCount` field in `[SearchRequest.ContentSearchSpec.SummarySpec.summary_result_count](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/ContentSearchSpec#SummarySpec.FIELDS.summary_result_count)`.At most 10 results for documents mode, or 50 for chunks mode.  
  
## RelevanceThreshold

The relevance threshold of the search results. The higher relevance threshold is, the higher relevant results are shown and the less number of results are returned.

Enums  
---  
`RELEVANCE_THRESHOLD_UNSPECIFIED` | Default value. In this case, server behavior defaults to Google defined threshold.  
`LOWEST` | Lowest relevance threshold.  
`LOW` | Low relevance threshold.  
`MEDIUM` | Medium relevance threshold.  
`HIGH` | High relevance threshold.  
  
## RelevanceFilterSpec

Relevance filtering specification.

JSON representation  
---  
      
    
    {
      "keywordSearchThreshold": {
        object ([RelevanceThresholdSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThresholdSpec))
      },
      "semanticSearchThreshold": {
        object ([RelevanceThresholdSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThresholdSpec))
      }
    }  
  
Fields  
---  
`keywordSearchThreshold` |  `object (`[RelevanceThresholdSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThresholdSpec)`)` Optional. Relevance filtering threshold specification for keyword search.  
`semanticSearchThreshold` |  `object (`[RelevanceThresholdSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThresholdSpec)`)` Optional. Relevance filtering threshold specification for semantic search.  
  
## RelevanceThresholdSpec

Specification for relevance filtering on a specific sub-search.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "relevanceThreshold": enum ([RelevanceThreshold](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThreshold)),
      "semanticRelevanceThreshold": number
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Configures how the relevance threshold is determined. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`relevanceThreshold` |  `enum (`[RelevanceThreshold](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#RelevanceThreshold)`)` Pre-defined relevance threshold for the sub-search.  
`semanticRelevanceThreshold` |  `number` Custom relevance threshold for the sub-search. The value must be in [0.0, 1.0].  
End of mutually exclusive fields.  
  
## RelevanceScoreSpec

The specification for returning the document relevance score.

JSON representation  
---  
      
    
    {
      "returnRelevanceScore": boolean
    }  
  
Fields  
---  
`returnRelevanceScore` |  `boolean` Optional. Whether to return the relevance score for search results. The higher the score, the more relevant the document is to the query.  
  
## SearchAddonSpec

SearchAddonSpec is used to disable add-ons for search as per new repricing model. By default if the SearchAddonSpec is not specified, we consider that the customer wants to enable them wherever applicable.

JSON representation  
---  
      
    
    {
      "disableSemanticAddOn": boolean,
      "disableKpiPersonalizationAddOn": boolean,
      "disableGenerativeAnswerAddOn": boolean
    }  
  
Fields  
---  
`disableSemanticAddOn` |  `boolean` Optional. If true, semantic add-on is disabled. Semantic add-on includes embeddings and jetstream.  
`disableKpiPersonalizationAddOn` |  `boolean` Optional. If true, disables event re-ranking and personalization to optimize KPIs & personalize results.  
`disableGenerativeAnswerAddOn` |  `boolean` Optional. If true, generative answer add-on is disabled. Generative answer add-on includes natural language to filters and simple answers.  
  
## CustomRankingParams

Configuration parameters for the Custom Ranking feature.

JSON representation  
---  
      
    
    {
      "expressionsToPrecompute": [
        string
      ]
    }  
  
Fields  
---  
`expressionsToPrecompute[]` |  `string` Optional. A list of ranking expressions (see `rankingExpression` for the syntax documentation) to evaluate. The evaluation results will be returned in `SearchResponse.SearchResult.rank_signals.precomputed_expression_values` field.  
  
## QuerySetSpec

Describes the specification of the query set.

JSON representation  
---  
      
    
    {
      "sampleQuerySet": string
    }  
  
Fields  
---  
`sampleQuerySet` |  `string` Optional. The full resource name of the `[SampleQuerySet](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets#SampleQuerySet)` used for the evaluation, in the format of `projects/{project}/locations/{location}/sampleQuerySets/{sampleQuerySet}`.  
  
## QualityMetrics

Describes the metrics produced by the evaluation.

JSON representation  
---  
      
    
    {
      "docRecall": {
        object ([TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics))
      },
      "docPrecision": {
        object ([TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics))
      },
      "docNdcg": {
        object ([TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics))
      },
      "pageRecall": {
        object ([TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics))
      },
      "pageNdcg": {
        object ([TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics))
      }
    }  
  
Fields  
---  
`docRecall` |  `object (`[TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics)`)` Recall per document, at various top-k cutoff levels.Recall is the fraction of relevant documents retrieved out of all relevant documents.Example (top-5): * For a single `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`, If 3 out of 5 relevant documents are retrieved in the top-5, [recall@5](mailto:recall@5) = 3/5 = 0.6  
`docPrecision` |  `object (`[TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics)`)` Precision per document, at various top-k cutoff levels.Precision is the fraction of retrieved documents that are relevant.Example (top-5): * For a single `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`, If 4 out of 5 retrieved documents in the top-5 are relevant, [precision@5](mailto:precision@5) = 4/5 = 0.8  
`docNdcg` |  `object (`[TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics)`)` Normalized discounted cumulative gain (NDCG) per document, at various top-k cutoff levels.NDCG measures the ranking quality, giving higher relevance to top results.Example (top-3): Suppose `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)` with three retrieved documents (D1, D2, D3) and binary relevance judgements (1 for relevant, 0 for not relevant):Retrieved: [D3 (0), D1 (1), D2 (1)] Ideal: [D1 (1), D2 (1), D3 (0)]Calculate [NDCG@3](mailto:NDCG@3) for each `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`: * [DCG@3](mailto:DCG@3): 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13 * Ideal [DCG@3](mailto:DCG@3): 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63 * [NDCG@3](mailto:NDCG@3): 1.13/1.63 = 0.693  
`pageRecall` |  `object (`[TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics)`)` Recall per page, at various top-k cutoff levels.Recall is the fraction of relevant pages retrieved out of all relevant pages.Example (top-5): * For a single `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`, if 3 out of 5 relevant pages are retrieved in the top-5, [recall@5](mailto:recall@5) = 3/5 = 0.6  
`pageNdcg` |  `object (`[TopkMetrics](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#TopkMetrics)`)` Normalized discounted cumulative gain (NDCG) per page, at various top-k cutoff levels.NDCG measures the ranking quality, giving higher relevance to top results.Example (top-3): Suppose `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)` with three retrieved pages (P1, P2, P3) and binary relevance judgements (1 for relevant, 0 for not relevant):Retrieved: [P3 (0), P1 (1), P2 (1)] Ideal: [P1 (1), P2 (1), P3 (0)]Calculate [NDCG@3](mailto:NDCG@3) for `[SampleQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`: * [DCG@3](mailto:DCG@3): 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13 * Ideal [DCG@3](mailto:DCG@3): 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63 * [NDCG@3](mailto:NDCG@3): 1.13/1.63 = 0.693  
  
## TopkMetrics

Stores the metric values at specific top-k levels.

JSON representation  
---  
      
    
    {
      "top1": number,
      "top3": number,
      "top5": number,
      "top10": number
    }  
  
Fields  
---  
`top1` |  `number` The top-1 value.  
`top3` |  `number` The top-3 value.  
`top5` |  `number` The top-5 value.  
`top10` |  `number` The top-10 value.  
  
## State

Describes the state of an evaluation.

Enums  
---  
`STATE_UNSPECIFIED` | The evaluation is unspecified.  
`PENDING` | The service is preparing to run the evaluation.  
`RUNNING` | The evaluation is in progress.  
`SUCCEEDED` | The evaluation completed successfully.  
`FAILED` | The evaluation failed.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations/create)`

|  Creates a `[Evaluation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Evaluation)`.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations/get)`

|  Gets a `[Evaluation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Evaluation)`.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations/list)`

|  Gets a list of `[Evaluation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Evaluation)`s.  
  
### `[listResults](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations/listResults)`

|  Gets a list of results for a given a `[Evaluation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#Evaluation)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
