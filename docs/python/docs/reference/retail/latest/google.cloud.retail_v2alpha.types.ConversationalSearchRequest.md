---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ConversationalSearchRequest
title: Class ConversationalSearchRequest (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:09.374632+00:00
---

# Class ConversationalSearchRequest (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ConversationalSearchRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ConversationalSearchRequest (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    ConversationalSearchRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for ConversationalSearchService.ConversationalSearch method.

## Attributes  
  
---  
**Name** | **Description**  
`placement` |  `str`   
Required. The resource name of the search engine placement, such as `projects/*/locations/global/catalogs/default_catalog/placements/default_search` or `projects/*/locations/global/catalogs/default_catalog/servingConfigs/default_serving_config` This field is used to identify the serving config name and the set of models that will be used to make the search.   
`branch` |  `str`   
Required. The branch resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/0`. Use "default_branch" as the branch ID or leave this field empty, to search products under the default branch.   
`query` |  `str`   
Optional. Raw search query to be searched for. If this field is empty, the request is considered a category browsing request.   
`page_categories` |  `MutableSequence[str]`   
Optional. The categories associated with a category page. Must be set for category navigation queries to achieve good search quality. The format should be the same as UserEvent.page_categories; To represent full path of category, use '>' sign to separate different hierarchies. If '>' is part of the category name, replace it with other character(s). Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: "pageCategories" : ["Sales > 2017 Black Friday Deals"].   
`conversation_id` |  `str`   
Optional. This field specifies the conversation id, which maintains the state of the conversation between client side and server side. Use the value from the previous ConversationalSearchResponse.conversation_id. For the initial request, this should be empty.   
`search_params` |  `[google.cloud.retail_v2alpha.types.ConversationalSearchRequest.SearchParams](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ConversationalSearchRequest.SearchParams)`   
Optional. Search parameters.   
`visitor_id` |  `str`   
Required. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website. This should be the same identifier as UserEvent.visitor_id. The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.   
`user_info` |  `[google.cloud.retail_v2alpha.types.UserInfo](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.UserInfo)`   
Optional. User information.   
`conversational_filtering_spec` |  `[google.cloud.retail_v2alpha.types.ConversationalSearchRequest.ConversationalFilteringSpec](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ConversationalSearchRequest.ConversationalFilteringSpec)`   
Optional. This field specifies all conversational filtering related parameters.   
`user_labels` |  `MutableMapping[str, str]`   
Optional. The user labels applied to a resource must meet the following requirements: \- Each resource can have multiple labels, up to a maximum of 64\. \- Each label must be a key-value pair. \- Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters. \- Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. \- The key portion of a label must be unique. However, you can use the same key with multiple resources. \- Keys must start with a lowercase letter or international character. See `Google Cloud Document   
`safety_settings` |  `MutableSequence[[google.cloud.retail_v2alpha.types.SafetySetting](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.SafetySetting)]`   
Optional. The safety settings to be applied to the generated content.   
  
## Classes 

### ConversationalFilteringSpec
    
    
    ConversationalFilteringSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

This field specifies all conversational filtering related parameters addition to conversational retail search.

### SearchParams
    
    
    SearchParams(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Search parameters.

### UserAnswer
    
    
    UserAnswer(mapping=None, *, ignore_unknown_fields=False, **kwargs)

This field specifies the current user answer during the conversational filtering search. This can be either user selected from suggested answers or user input plain text.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
