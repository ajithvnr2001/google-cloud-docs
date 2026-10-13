---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest
title: Class AnswerQueryRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:46.458670+00:00
---

# Class AnswerQueryRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AnswerQueryRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    AnswerQueryRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for ConversationalSearchService.AnswerQuery method.

## Attributes  
  
---  
**Name** | **Description**  
`serving_config` |  `str`   
Required. The resource name of the Search serving config, such as `projects/*/locations/global/collections/default_collection/engines/*/servingConfigs/default_serving_config`, or `projects/*/locations/global/collections/default_collection/dataStores/*/servingConfigs/default_serving_config`. This field is used to identify the serving configuration name, set of models used to make the search.   
`query` |  `[google.cloud.discoveryengine_v1.types.Query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Query)`   
Required. Current user query.   
`session` |  `str`   
The session resource name. Not required. When session field is not set, the API is in sessionless mode. We support auto session mode: users can use the wildcard symbol `-` as session ID. A new ID will be automatically generated and assigned.   
`safety_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SafetySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SafetySpec)`   
Model specification.   
`related_questions_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.RelatedQuestionsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.RelatedQuestionsSpec)`   
Related questions specification.   
`grounding_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.GroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.GroundingSpec)`   
Optional. Grounding specification.   
`answer_generation_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec)`   
Answer generation specification.   
`search_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec)`   
Search specification.   
`query_understanding_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec)`   
Query understanding specification.   
`asynchronous_mode` |  `bool`   
Deprecated: This field is deprecated. Streaming Answer API will be supported. Asynchronous mode control. If enabled, the response will be returned with answer/session resource name without final answer. The API users need to do the polling to get the latest status of answer/session by calling ConversationalSearchService.GetAnswer or ConversationalSearchService.GetSession method.   
`user_pseudo_id` |  `str`   
A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website. This field should NOT have a fixed value such as `unknown_visitor`. The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.   
`user_labels` |  `MutableMapping[str, str]`   
The user labels applied to a resource must meet the following requirements: \- Each resource can have multiple labels, up to a maximum of 64\. \- Each label must be a key-value pair. \- Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters. \- Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. \- The key portion of a label must be unique. However, you can use the same key with multiple resources. \- Keys must start with a lowercase letter or international character. See `Google Cloud Document   
`end_user_spec` |  `[google.cloud.discoveryengine_v1.types.AnswerQueryRequest.EndUserSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.EndUserSpec)`   
Optional. End user specification.   
  
## Classes 

### AnswerGenerationSpec
    
    
    AnswerGenerationSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Answer generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### EndUserSpec
    
    
    EndUserSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

End user specification.

### GroundingSpec
    
    
    GroundingSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Grounding specification.

### QueryUnderstandingSpec
    
    
    QueryUnderstandingSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Query understanding specification.

### RelatedQuestionsSpec
    
    
    RelatedQuestionsSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Related questions specification.

### SafetySpec
    
    
    SafetySpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Safety specification. There are two use cases:

  1. when only safety_spec.enable is set, the BLOCK_LOW_AND_ABOVE threshold will be applied for all categories.
  2. when safety_spec.enable is set and some safety_settings are set, only specified safety_settings are applied.



### SearchSpec
    
    
    SearchSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Search specification.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

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
