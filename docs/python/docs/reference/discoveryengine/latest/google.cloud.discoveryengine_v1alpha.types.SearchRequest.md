---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest
title: Class SearchRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:26.651137+00:00
---

# Class SearchRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    SearchRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for SearchService.Search method.

## Attributes  
  
---  
**Name** | **Description**  
`serving_config` |  `str`   
Required. The resource name of the Search serving config, such as `projects/*/locations/global/collections/default_collection/engines/*/servingConfigs/default_serving_config`, or `projects/*/locations/global/collections/default_collection/dataStores/default_data_store/servingConfigs/default_serving_config`. This field is used to identify the serving configuration name, set of models used to make the search.   
`branch` |  `str`   
The branch resource name, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store/branches/0`. Use `default_branch` as the branch ID or leave this field empty, to search documents under the default branch.   
`query` |  `str`   
Raw search query.   
`image_query` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.ImageQuery](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ImageQuery)`   
Raw image query.   
`page_size` |  `int`   
Maximum number of Documents to return. The maximum allowed value depends on the data type. Values above the maximum value are coerced to the maximum value. \- Websites with basic indexing: Default `10`, Maximum `25`. \- Websites with advanced indexing: Default `25`, Maximum `50`. \- Other: Default `50`, Maximum `100`. If this field is negative, an `INVALID_ARGUMENT` is returned.   
`page_token` |  `str`   
A page token received from a previous SearchService.Search call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to SearchService.Search must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned.   
`offset` |  `int`   
A 0-indexed integer that specifies the current offset (that is, starting result location, amongst the Documents deemed by the API as relevant) in search results. This field is only considered if page_token is unset. If this field is negative, an `INVALID_ARGUMENT` is returned.   
`data_store_specs` |  `MutableSequence[[google.cloud.discoveryengine_v1alpha.types.SearchRequest.DataStoreSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.DataStoreSpec)]`   
Specs defining dataStores to filter on in a search call and configurations for those dataStores. This is only considered for engines with multiple dataStores use case. For single dataStore within an engine, they should use the specs at the top level.   
`filter` |  `str`   
The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. If this field is unrecognizable, an `INVALID_ARGUMENT` is returned. Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")' For more information about filtering including syntax and filter operators, see `Filter `__   
`canonical_filter` |  `str`   
The default filter that is applied when a user performs a search without checking any filters on the search page. The filter applied to every search request when quality improvement such as query expansion is needed. In the case a query does not have a sufficient amount of results this filter will be used to determine whether or not to enable the query expansion flow. The original filter will still be used for the query expanded search. This field is strongly recommended to achieve high search quality. For more information about filter syntax, see SearchRequest.filter.   
`order_by` |  `str`   
The order in which documents are returned. Documents can be ordered by a field in an Document object. Leave it unset if ordered by relevance. `order_by` expression is case-sensitive. For more information on ordering the website search results, see `Order web search results   
`user_info` |  `[google.cloud.discoveryengine_v1alpha.types.UserInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UserInfo)`   
Information about the end user. Highly recommended for analytics. UserInfo.user_agent is used to deduce `device_type` for analytics.   
`language_code` |  `str`   
The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see `Standard fields   
`region_code` |  `str`   
The Unicode country/region code (CLDR) of a location, such as "US" and "419". For more information, see `Standard fields   
`facet_specs` |  `MutableSequence[[google.cloud.discoveryengine_v1alpha.types.SearchRequest.FacetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.FacetSpec)]`   
Facet specifications for faceted search. If empty, no facets are returned. A maximum of 100 values are allowed. Otherwise, an `INVALID_ARGUMENT` error is returned.   
`boost_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec)`   
Boost specification to boost certain documents. For more information on boosting, see `Boosting `__   
`params` |  `MutableMapping[str, google.protobuf.struct_pb2.Value]`   
Additional search parameters. For public website search only, supported values are: \- `user_country_code`: string. Default empty. If set to non-empty, results are restricted or boosted based on the location provided. For example, `user_country_code: "au"` For available codes see `Country Codes   
`query_expansion_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.QueryExpansionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.QueryExpansionSpec)`   
The query expansion specification that specifies the conditions under which query expansion occurs.   
`spell_correction_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.SpellCorrectionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SpellCorrectionSpec)`   
The spell correction specification that specifies the mode under which spell correction takes effect.   
`user_pseudo_id` |  `str`   
A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website. This field should NOT have a fixed value such as `unknown_visitor`. This should be the same identifier as UserEvent.user_pseudo_id and CompleteQueryRequest.user_pseudo_id The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.   
`content_search_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec)`   
A specification for configuring the behavior of content search.   
`embedding_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.EmbeddingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.EmbeddingSpec)`   
Uses the provided embedding to do additional semantic document retrieval. The retrieval is based on the dot product of SearchRequest.EmbeddingSpec.EmbeddingVector.vector and the document embedding that is provided in SearchRequest.EmbeddingSpec.EmbeddingVector.field_path. If SearchRequest.EmbeddingSpec.EmbeddingVector.field_path is not provided, it will use ServingConfig.EmbeddingConfig.field_path.   
`ranking_expression` |  `str`   
The ranking expression controls the customized ranking on retrieval documents. This overrides ServingConfig.ranking_expression. The syntax and supported features depend on the `ranking_expression_backend` value. If `ranking_expression_backend` is not provided, it defaults to `RANK_BY_EMBEDDING`. If ranking_expression_backend is not provided or set to `RANK_BY_EMBEDDING`, it should be a single function or multiple functions that are joined by "+". \- ranking_expression = function, { " + ", function }; Supported functions: \- double \\* relevance_score \- double \\* dotProduct(embedding_field_path) Function variables: \- `relevance_score`: pre-defined keywords, used for measure relevance between query and document. \- `embedding_field_path`: the document embedding field used with query embedding vector. \- `dotProduct`: embedding function between `embedding_field_path` and query embedding vector. Example ranking expression: :: If document has an embedding field doc_embedding, the ranking expression could be `0.5 * relevance_score + 0.3 * dotProduct(doc_embedding)`. If ranking_expression_backend is set to `RANK_BY_FORMULA`, the following expression types (and combinations of those chained using + or \- operators) are supported: \- `double` \- `signal` \- `log(signal)` \- `exp(signal)` \- `rr(signal, double > 0)` \-- reciprocal rank transformation with second argument being a denominator constant. \- `is_nan(signal)` \-- returns 0 if signal is NaN, 1 otherwise. \- `fill_nan(signal1, signal2 | double)` \-- if signal1 is NaN, returns signal2 \| double, else returns signal1. Here are a few examples of ranking formulas that use the supported ranking expression types: \- `0.2 * semantic_similarity_score + 0.8 * log(keyword_similarity_score)` \-- mostly rank by the logarithm of `keyword_similarity_score` with slight `semantic_smilarity_score` adjustment. \- `0.2 * exp(fill_nan(semantic_similarity_score, 0)) + 0.3 * is_nan(keyword_similarity_score)` \-- rank by the exponent of `semantic_similarity_score` filling the value with 0 if it's NaN, also add constant 0.3 adjustment to the final score if `semantic_similarity_score` is NaN. \- `0.2 * rr(semantic_similarity_score, 16) + 0.8 * rr(keyword_similarity_score, 16)` \-- mostly rank by the reciprocal rank of `keyword_similarity_score` with slight adjustment of reciprocal rank of `semantic_smilarity_score`. The following signals are supported: \- `semantic_similarity_score`: semantic similarity adjustment that is calculated using the embeddings generated by a proprietary Google model. This score determines how semantically similar a search query is to a document. \- `keyword_similarity_score`: keyword match adjustment uses the Best Match 25 (BM25) ranking function. This score is calculated using a probabilistic model to estimate the probability that a document is relevant to a given query. \- `relevance_score`: semantic relevance adjustment that uses a proprietary Google model to determine the meaning and intent behind a user's query in context with the content in the documents. \- `pctr_rank`: predicted conversion rate adjustment as a rank use predicted Click-through rate (pCTR) to gauge the relevance and attractiveness of a search result from a user's perspective. A higher pCTR suggests that the result is more likely to satisfy the user's query and intent, making it a valuable signal for ranking. \- `freshness_rank`: freshness adjustment as a rank \- `document_age`: The time in hours elapsed since the document was last updated, a floating-point number (e.g., 0.25 means 15 minutes). \- `topicality_rank`: topicality adjustment as a rank. Uses proprietary Google model to determine the keyword-based overlap between the query and the document. \- `base_rank`: the default rank of the result   
`ranking_expression_backend` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.RankingExpressionBackend](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.RankingExpressionBackend)`   
The backend to use for the ranking expression evaluation.   
`safe_search` |  `bool`   
Whether to turn on safe search. This is only supported for website search.   
`user_labels` |  `MutableMapping[str, str]`   
The user labels applied to a resource must meet the following requirements: \- Each resource can have multiple labels, up to a maximum of 64\. \- Each label must be a key-value pair. \- Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters. \- Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. \- The key portion of a label must be unique. However, you can use the same key with multiple resources. \- Keys must start with a lowercase letter or international character. See `Google Cloud Document   
`natural_language_query_understanding_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec)`   
If `naturalLanguageQueryUnderstandingSpec` is not specified, no additional natural language query understanding will be done.   
`search_as_you_type_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.SearchAsYouTypeSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SearchAsYouTypeSpec)`   
Search as you type configuration. Only supported for the IndustryVertical.MEDIA vertical.   
`custom_fine_tuning_spec` |  `[google.cloud.discoveryengine_v1alpha.types.CustomFineTuningSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CustomFineTuningSpec)`   
Custom fine tuning configs. If set, it has higher priority than the configs set in ServingConfig.custom_fine_tuning_spec.   
`session` |  `str`   
The session resource name. Optional. Session allows users to do multi-turn /search API calls or coordination between /search API calls and /answer API calls. Example #1 (multi-turn /search API calls): Call /search API with the session ID generated in the first call. Here, the previous search query gets considered in query standing. I.e., if the first query is "How did Alphabet do in 2022?" and the current query is "How about 2023?", the current query will be interpreted as "How did Alphabet do in 2023?". Example #2 (coordination between /search API calls and /answer API calls): Call /answer API with the session ID generated in the first call. Here, the answer generation happens in the context of the search results from the first search call. Multi-turn Search feature is currently at private GA stage. Please use v1alpha or v1beta version instead before we launch this feature to public GA. Or ask for allowlisting through Google Support team.   
`session_spec` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.SessionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SessionSpec)`   
Session specification. Can be used only when `session` is set.   
`relevance_threshold` |  `[google.cloud.discoveryengine_v1alpha.types.SearchRequest.RelevanceThreshold](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.RelevanceThreshold)`   
The relevance threshold of the search results. Default to Google defined threshold, leveraging a balance of precision and recall to deliver both highly accurate results and comprehensive coverage of relevant information.   
  
## Classes 

### BoostSpec
    
    
    BoostSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Boost specification to boost certain documents.

### ContentSearchSpec
    
    
    ContentSearchSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A specification for configuring the behavior of content search.

### DataStoreSpec
    
    
    DataStoreSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A struct to define data stores to filter on in a search call and configurations for those data stores. Otherwise, an `INVALID_ARGUMENT` error is returned.

### EmbeddingSpec
    
    
    EmbeddingSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The specification that uses customized query embedding vector to do semantic document retrieval.

### FacetSpec
    
    
    FacetSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A facet specification to perform faceted search.

### ImageQuery
    
    
    ImageQuery(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies the image query input.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### NaturalLanguageQueryUnderstandingSpec
    
    
    NaturalLanguageQueryUnderstandingSpec(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Specification to enable natural language understanding capabilities for search requests.

### ParamsEntry
    
    
    ParamsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### QueryExpansionSpec
    
    
    QueryExpansionSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specification to determine under which conditions query expansion should occur.

### RankingExpressionBackend
    
    
    RankingExpressionBackend(value)

The backend to use for the ranking expression evaluation.

### RelevanceThreshold
    
    
    RelevanceThreshold(value)

The relevance threshold of the search results. The higher relevance threshold is, the higher relevant results are shown and the less number of results are returned.

### SearchAsYouTypeSpec
    
    
    SearchAsYouTypeSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specification for search as you type in search requests.

### SessionSpec
    
    
    SessionSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Session specification.

Multi-turn Search feature is currently at private GA stage. Please use v1alpha or v1beta version instead before we launch this feature to public GA. Or ask for allowlisting through Google Support team.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### SpellCorrectionSpec
    
    
    SpellCorrectionSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The specification for query spell correction.

### UserLabelsEntry
    
    
    UserLabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
