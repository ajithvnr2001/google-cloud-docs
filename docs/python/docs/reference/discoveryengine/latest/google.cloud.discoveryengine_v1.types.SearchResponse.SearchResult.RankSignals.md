---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RankSignals
title: Class RankSignals (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:03.986417+00:00
---

# Class RankSignals (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RankSignals

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RankSignals (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    RankSignals(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A set of ranking signals.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`keyword_similarity_score` |  `float`   
Optional. Keyword matching adjustment. This field is a member of `oneof`_ `_keyword_similarity_score`.   
`relevance_score` |  `float`   
Optional. Semantic relevance adjustment. This field is a member of `oneof`_ `_relevance_score`.   
`semantic_similarity_score` |  `float`   
Optional. Semantic similarity adjustment. This field is a member of `oneof`_ `_semantic_similarity_score`.   
`pctr_rank` |  `float`   
Optional. Predicted conversion rate adjustment as a rank. This field is a member of `oneof`_ `_pctr_rank`.   
`topicality_rank` |  `float`   
Optional. Topicality adjustment as a rank. This field is a member of `oneof`_ `_topicality_rank`.   
`document_age` |  `float`   
Optional. Age of the document in hours. This field is a member of `oneof`_ `_document_age`.   
`boosting_factor` |  `float`   
Optional. Combined custom boosts for a doc. This field is a member of `oneof`_ `_boosting_factor`.   
`default_rank` |  `float`   
Optional. The default rank of the result.   
`custom_signals` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RankSignals.CustomSignal](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RankSignals.CustomSignal)]`   
Optional. A list of custom clearbox signals.   
`precomputed_expression_values` |  `MutableSequence[float]`   
Optional. A list of precomputed expression results for a given document, in the same order as requested in `SearchRequest.custom_ranking_params.expressions_to_precompute`.   
  
## Classes 

### CustomSignal
    
    
    CustomSignal(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Custom clearbox signal represented by name and value pair.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
