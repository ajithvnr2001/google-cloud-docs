---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec
title: Class AnswerGenerationSpec (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:47.178868+00:00
---

# Class AnswerGenerationSpec (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AnswerGenerationSpec (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    AnswerGenerationSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Answer generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`model_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec)`   
Answer generation model specification.   
`prompt_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec)`   
Answer generation prompt specification.   
`include_citations` |  `bool`   
Specifies whether to include citation metadata in the answer. The default value is `false`.   
`answer_language_code` |  `str`   
Language code for Answer. Use language tags defined by `BCP47 `__. Note: This is an experimental feature.   
`ignore_adversarial_query` |  `bool`   
Specifies whether to filter out adversarial queries. The default value is `false`. Google employs search-query classification to detect adversarial queries. No answer is returned if the search query is classified as an adversarial query. For example, a user might ask a question regarding negative comments about the company or submit a query designed to generate unsafe, policy-violating output. If this field is set to `true`, we skip generating answers for adversarial queries and return fallback messages instead.   
`ignore_non_answer_seeking_query` |  `bool`   
Specifies whether to filter out queries that are not answer-seeking. The default value is `false`. Google employs search-query classification to detect answer-seeking queries. No answer is returned if the search query is classified as a non-answer seeking query. If this field is set to `true`, we skip generating answers for non-answer seeking queries and return fallback messages instead.   
`ignore_low_relevant_content` |  `bool`   
Specifies whether to filter out queries that have low relevance. If this field is set to `false`, all search results are used regardless of relevance to generate answers. If set to `true` or unset, the behavior will be determined automatically by the service. This field is a member of `oneof`_ `_ignore_low_relevant_content`.   
`ignore_jail_breaking_query` |  `bool`   
Optional. Specifies whether to filter out jail-breaking queries. The default value is `false`. Google employs search-query classification to detect jail-breaking queries. No summary is returned if the search query is classified as a jail-breaking query. A user might add instructions to the query to change the tone, style, language, content of the answer, or ask the model to act as a different entity, e.g. "Reply in the tone of a competing company's CEO". If this field is set to `true`, we skip generating summaries for jail-breaking queries and return fallback messages instead.   
  
## Classes 

### ModelSpec
    
    
    ModelSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Answer Generation Model specification.

### PromptSpec
    
    
    PromptSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Answer generation prompt specification.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
