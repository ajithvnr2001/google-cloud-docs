---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/searchLite/
title: Method: projects.locations.collections.dataStores.servingConfigs.searchLite \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:00.083215+00:00
---

# Method: projects.locations.collections.dataStores.servingConfigs.searchLite  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/searchLite/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.servingConfigs.searchLite Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



Performs a search. Similar to the `[SearchService.Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1beta.SearchService.Search)` method, but a lite version that allows API key for authentication, where OAuth and IAM checks are not required.

Only public website search is supported by this method. If data stores and engines not associated with public website search are specified, a `FAILED_PRECONDITION` error is returned.

This method can be used for easy onboarding without having to implement an authentication backend. However, it is strongly recommended to use `[SearchService.Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1beta.SearchService.Search)` instead with required OAuth and IAM checks to provide better data security.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1beta/{servingConfig=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:searchLite`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`servingConfig` |  `string` Required. The resource name of the servingConfigs.search serving config, such as `projects/*/locations/global/collections/default_collection/engines/*/servingConfigs/default_serving_config`, or `projects/*/locations/global/collections/default_collection/dataStores/default_data_store/servingConfigs/default_serving_config`. This field is used to identify the serving configuration name, set of models used to make the search.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "branch": string,
      "query": string,
      "pageCategories": [
        string
      ],
      "imageQuery": {
        object ([ImageQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#ImageQuery))
      },
      "pageSize": integer,
      "pageToken": string,
      "offset": integer,
      "oneBoxPageSize": integer,
      "dataStoreSpecs": [
        {
          object ([DataStoreSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#DataStoreSpec))
        }
      ],
      "numResultsPerDataStore": integer,
      "filter": string,
      "canonicalFilter": string,
      "orderBy": string,
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/UserInfo))
      },
      "languageCode": string,
      "regionCode": string,
      "facetSpecs": [
        {
          object ([FacetSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#FacetSpec))
        }
      ],
      "boostSpec": {
        object ([BoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#BoostSpec))
      },
      "params": {
        string: value,
        ...
      },
      "queryExpansionSpec": {
        object ([QueryExpansionSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#QueryExpansionSpec))
      },
      "spellCorrectionSpec": {
        object ([SpellCorrectionSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SpellCorrectionSpec))
      },
      "userPseudoId": string,
      "contentSearchSpec": {
        object ([ContentSearchSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ContentSearchSpec))
      },
      "embeddingSpec": {
        object ([EmbeddingSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#EmbeddingSpec))
      },
      "rankingExpression": string,
      "rankingExpressionBackend": enum ([RankingExpressionBackend](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RankingExpressionBackend)),
      "safeSearch": boolean,
      "userLabels": {
        string: string,
        ...
      },
      "naturalLanguageQueryUnderstandingSpec": {
        object ([NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#NaturalLanguageQueryUnderstandingSpec))
      },
      "searchAsYouTypeSpec": {
        object ([SearchAsYouTypeSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchAsYouTypeSpec))
      },
      "displaySpec": {
        object ([DisplaySpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#DisplaySpec))
      },
      "crowdingSpecs": [
        {
          object ([CrowdingSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#CrowdingSpec))
        }
      ],
      "session": string,
      "sessionSpec": {
        object ([SessionSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SessionSpec))
      },
      "relevanceThreshold": enum ([RelevanceThreshold](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RelevanceThreshold)),
      "relevanceFilterSpec": {
        object ([RelevanceFilterSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RelevanceFilterSpec))
      },
      "personalizationSpec": {
        object ([PersonalizationSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/PersonalizationSpec))
      },
      "relevanceScoreSpec": {
        object ([RelevanceScoreSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RelevanceScoreSpec))
      },
      "searchAddonSpec": {
        object ([SearchAddonSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchAddonSpec))
      },
      "customRankingParams": {
        object ([CustomRankingParams](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#CustomRankingParams))
      },
      "entity": string
    }  
  
Fields  
---  
`branch` |  `string` The branch resource name, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store/branches/0`.Use `default_branch` as the branch ID or leave this field empty, to search documents under the default branch.  
`query` |  `string` Raw search query.  
`pageCategories[]` |  `string` Optional. The categories associated with a category page. Must be set for category navigation queries to achieve good search quality. The format should be the same as `[PageInfo.page_category](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.userEvents#PageInfo.FIELDS.page_category)`. This field is the equivalent of the query for browse (navigation) queries. It's used by the browse model when the query is empty.If the field is empty, it will not be used by the browse model. If the field contains more than one element, only the first element will be used.To represent full path of a category, use '>' character to separate different hierarchies. If '>' is part of the category name, replace it with other character(s). For example, `Graphics Cards > RTX>4090 > Founders Edition` where "RTX > 4090" represents one level, can be rewritten as `Graphics Cards > RTX_4090 > Founders Edition`  
`imageQuery` |  `object (`[ImageQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#ImageQuery)`)` Raw image query.  
`pageSize` |  `integer` Maximum number of `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`s to return. The maximum allowed value depends on the data type. Values above the maximum value are coerced to the maximum value.

  * Websites with basic indexing: Default `10`, Maximum `25`.
  * Websites with advanced indexing: Default `25`, Maximum `50`.
  * Other: Default `50`, Maximum `100`.

If this field is negative, an `INVALID_ARGUMENT` is returned.  
`pageToken` |  `string` A page token received from a previous `[SearchService.Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1beta.SearchService.Search)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[SearchService.Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1beta.SearchService.Search)` must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`offset` |  `integer` A 0-indexed integer that specifies the current offset (that is, starting result location, amongst the `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`s deemed by the API as relevant) in search results. This field is only considered if `[pageToken](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchRequest.FIELDS.page_token)` is unset.If this field is negative, an `INVALID_ARGUMENT` is returned.A large offset may be capped to a reasonable threshold.  
`oneBoxPageSize` |  `integer` The maximum number of results to return for OneBox. This applies to each OneBox type individually. Default number is 10.  
`dataStoreSpecs[]` |  `object (`[DataStoreSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#DataStoreSpec)`)` Specifications that define the specific `[DataStore](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores#DataStore)`s to be searched, along with configurations for those data stores. This is only considered for `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.engines#Engine)`s with multiple data stores. For engines with a single data store, the specs directly under `[SearchRequest](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchRequest)` should be used.On an engine with multiple data stores, this field is optional. If it's empty, all of the engine's data stores are searched (blended search). Unless it specifies exactly one data store, some request fields, such as `orderBy` and `queryExpansionSpec`, aren't supported and return an `INVALID_ARGUMENT` error.  
`numResultsPerDataStore` |  `integer` Optional. The maximum number of results to retrieve from each data store. If not specified, it will use the `[SearchRequest.DataStoreSpec.num_results](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#DataStoreSpec.FIELDS.num_results)` if provided, otherwise there is no limit.  
`filter` |  `string` The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive.If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.Filtering in Vertex AI servingConfigs.search is done by mapping the LHS filter key to a key property defined in the Vertex AI servingConfigs.search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)  
`canonicalFilter` |  `string` The default filter that is applied when a user performs a search without checking any filters on the search page.The filter applied to every search request when quality improvement such as query expansion is needed. In the case a query does not have a sufficient amount of results this filter will be used to determine whether or not to enable the query expansion flow. The original filter will still be used for the query expanded search. This field is strongly recommended to achieve high search quality.For more information about filter syntax, see `[SearchRequest.filter](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchRequest.FIELDS.filter)`.  
`orderBy` |  `string` The order in which documents are returned. Documents can be ordered by a field in an `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)` object. Leave it unset if ordered by relevance. `orderBy` expression is case-sensitive.For more information on ordering the website search results, see [Order web search results](https://cloud.google.com/generative-ai-app-builder/docs/order-web-search-results). For more information on ordering the healthcare search results, see [Order healthcare search results](https://cloud.google.com/generative-ai-app-builder/docs/order-hc-results). If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/UserInfo)`)` Information about the end user. Highly recommended for analytics and personalization. `[UserInfo.user_agent](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/UserInfo#FIELDS.user_agent)` is used to deduce `deviceType` for analytics.  
`languageCode` |  `string` The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see [Standard fields](https://cloud.google.com/apis/design/standard_fields). This field helps to better interpret the query. If a value isn't specified, the query language code is automatically detected, which may not be accurate.  
`regionCode` |  `string` The Unicode country/region code (CLDR) of a location, such as "US" and "419". For more information, see [Standard fields](https://cloud.google.com/apis/design/standard_fields). If set, then results will be boosted based on the regionCode provided.  
`facetSpecs[]` |  `object (`[FacetSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#FacetSpec)`)` Facet specifications for faceted search. If empty, no facets are returned.A maximum of 100 values are allowed. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`boostSpec` |  `object (`[BoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#BoostSpec)`)` Boost specification to boost certain documents. For more information on boosting, see [Boosting](https://cloud.google.com/generative-ai-app-builder/docs/boost-search-results)  
`params` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Additional search parameters.For public website search only, supported values are:

  * `user_country_code`: string. Default empty. If set to non-empty, results are restricted or boosted based on the location provided. For example, `user_country_code: "au"`

For available codes see [Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes)

  * `searchType`: double. Default empty. Enables non-webpage searching depending on the value. The only valid non-default value is 1, which enables image searching. For example, `searchType: 1`

  
`queryExpansionSpec` |  `object (`[QueryExpansionSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#QueryExpansionSpec)`)` The query expansion specification that specifies the conditions under which query expansion occurs.  
`spellCorrectionSpec` |  `object (`[SpellCorrectionSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SpellCorrectionSpec)`)` The spell correction specification that specifies the mode under which spell correction takes effect.  
`userPseudoId` |  `string` Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.This field should NOT have a fixed value such as `unknown_visitor`.This should be the same identifier as `[UserEvent.user_pseudo_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id)` and `[CompleteQueryRequest.user_pseudo_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores/completeQuery#body.QUERY_PARAMETERS.user_pseudo_id)`The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`contentSearchSpec` |  `object (`[ContentSearchSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ContentSearchSpec)`)` A specification for configuring the behavior of content search.  
`embeddingSpec` |  `object (`[EmbeddingSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#EmbeddingSpec)`)` Uses the provided embedding to do additional semantic document retrieval. The retrieval is based on the dot product of `[SearchRequest.EmbeddingSpec.EmbeddingVector.vector](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#EmbeddingVector.FIELDS.vector)` and the document embedding that is provided in `[SearchRequest.EmbeddingSpec.EmbeddingVector.field_path](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#EmbeddingVector.FIELDS.field_path)`.If `[SearchRequest.EmbeddingSpec.EmbeddingVector.field_path](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#EmbeddingVector.FIELDS.field_path)` is not provided, it will use `[ServingConfig.EmbeddingConfig.field_path](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.embedding_config)`.  
`rankingExpression` |  `string` Optional. The ranking expression controls the customized ranking on retrieval documents. This overrides `[ServingConfig.ranking_expression](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.ranking_expression)`. The syntax and supported features depend on the `rankingExpressionBackend` value. If `rankingExpressionBackend` is not provided, it defaults to `RANK_BY_EMBEDDING`.If `[rankingExpressionBackend](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchRequest.FIELDS.ranking_expression_backend)` is not provided or set to `RANK_BY_EMBEDDING`, it should be a single function or multiple functions that are joined by "+".

  * rankingExpression = function, { " + ", function };

Supported functions:

  * double * relevanceScore
  * double * dotProduct(embedding_field_path)

Function variables:

  * `relevanceScore`: pre-defined keywords, used for measure relevance between query and document.
  * `embedding_field_path`: the document embedding field used with query embedding vector.
  * `dotProduct`: embedding function between `embedding_field_path` and query embedding vector.

Example ranking expression:If document has an embedding field doc_embedding, the ranking expression could be `0.5 * relevanceScore + 0.3 * dotProduct(doc_embedding)`.If `[rankingExpressionBackend](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchRequest.FIELDS.ranking_expression_backend)` is set to `RANK_BY_FORMULA`, the following expression types (and combinations of those chained using + or * operators) are supported:

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

  
`rankingExpressionBackend` |  `enum (`[RankingExpressionBackend](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RankingExpressionBackend)`)` Optional. The backend to use for the ranking expression evaluation.  
`safeSearch` |  `boolean` Whether to turn on safe search. This is only supported for website search.  
`userLabels` |  `map (key: string, value: string)` The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.  
`naturalLanguageQueryUnderstandingSpec` |  `object (`[NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#NaturalLanguageQueryUnderstandingSpec)`)` Optional. Config for natural language query understanding capabilities, such as extracting structured field filters from the query. Refer to [this documentation](https://cloud.google.com/generative-ai-app-builder/docs/natural-language-queries) for more information. If `naturalLanguageQueryUnderstandingSpec` is not specified, no additional natural language query understanding will be done.  
`searchAsYouTypeSpec` |  `object (`[SearchAsYouTypeSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchAsYouTypeSpec)`)` servingConfigs.search as you type configuration. Only supported for the `[IndustryVertical.MEDIA](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/IndustryVertical#ENUM_VALUES.MEDIA)` vertical.  
`displaySpec` |  `object (`[DisplaySpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#DisplaySpec)`)` Optional. Config for display feature, like match highlighting on search results.  
`crowdingSpecs[]` |  `object (`[CrowdingSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#CrowdingSpec)`)` Optional. Crowding specifications for improving result diversity. If multiple CrowdingSpecs are specified, crowding will be evaluated on each unique combination of the `field` values, and maxCount will be the maximum value of `maxCount` across all CrowdingSpecs. For example, if the first CrowdingSpec has `field` = "color" and `maxCount` = 3, and the second CrowdingSpec has `field` = "size" and `maxCount` = 2, then after 3 documents that share the same color AND size have been returned, subsequent ones should be removed or demoted.  
`session` |  `string` The session resource name. Optional.Session allows users to do multi-turn /search API calls or coordination between /search API calls and /answer API calls.Example #1 (multi-turn /search API calls): Call /search API with the session ID generated in the first call. Here, the previous search query gets considered in query standing. I.e., if the first query is "How did Alphabet do in 2022?" and the current query is "How about 2023?", the current query will be interpreted as "How did Alphabet do in 2023?".Example #2 (coordination between /search API calls and /answer API calls): Call /answer API with the session ID generated in the first call. Here, the answer generation happens in the context of the search results from the first search call.  
`sessionSpec` |  `object (`[SessionSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SessionSpec)`)` Session specification.Can be used only when `session` is set.  
`relevanceThreshold` |  `enum (`[RelevanceThreshold](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RelevanceThreshold)`)` The global relevance threshold of the search results.Defaults to Google defined threshold, leveraging a balance of precision and recall to deliver both highly accurate results and comprehensive coverage of relevant information.If more granular relevance filtering is required, use the `relevanceFilterSpec` instead.This feature is not supported for healthcare search.  
`relevanceFilterSpec` |  `object (`[RelevanceFilterSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RelevanceFilterSpec)`)` Optional. The granular relevance filtering specification.If not specified, the global `relevanceThreshold` will be used for all sub-searches. If specified, this overrides the global `relevanceThreshold` to use thresholds on a per sub-search basis.This feature is currently supported only for custom and site search.  
`personalizationSpec` |  `object (`[PersonalizationSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/PersonalizationSpec)`)` The specification for personalization.Notice that if both `[ServingConfig.personalization_spec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.personalization_spec)` and `[SearchRequest.personalization_spec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchRequest.FIELDS.personalization_spec)` are set, `[SearchRequest.personalization_spec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchRequest.FIELDS.personalization_spec)` overrides `[ServingConfig.personalization_spec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.personalization_spec)`.  
`relevanceScoreSpec` |  `object (`[RelevanceScoreSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#RelevanceScoreSpec)`)` Optional. The specification for returning the relevance score.  
`searchAddonSpec` |  `object (`[SearchAddonSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#SearchAddonSpec)`)` Optional. SearchAddonSpec is used to disable add-ons for search as per new repricing model. This field is only supported for search requests.  
`customRankingParams` |  `object (`[CustomRankingParams](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#CustomRankingParams)`)` Optional. Optional configuration for the Custom Ranking feature.  
`entity` |  `string` Optional. The entity for customers that may run multiple different entities, domains, sites or regions, for example, "Google US", "Google Ads", "Waymo", "google.com", "youtube.com", etc. If this is set, it should be exactly matched with `[UserEvent.entity](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.userEvents#UserEvent.FIELDS.entity)` to get search results boosted by entity.  
  
### Response body

If successful, the response body contains an instance of `[SearchResponse](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SearchResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
