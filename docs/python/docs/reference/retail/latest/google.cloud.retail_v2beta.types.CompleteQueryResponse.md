---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.CompleteQueryResponse
title: Class CompleteQueryResponse (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:43.752654+00:00
---

# Class CompleteQueryResponse (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.CompleteQueryResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CompleteQueryResponse (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    CompleteQueryResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Response of the autocomplete query.

## Attributes  
  
---  
**Name** | **Description**  
`completion_results` |  `MutableSequence[[google.cloud.retail_v2beta.types.CompleteQueryResponse.CompletionResult](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.CompleteQueryResponse.CompletionResult)]`   
Results of the matching suggestions. The result list is ordered and the first result is top suggestion.   
`attribution_token` |  `str`   
A unique complete token. This should be included in the UserEvent.completion_detail for search events resulting from this completion, which enables accurate attribution of complete model performance.   
`recent_search_results` |  `MutableSequence[[google.cloud.retail_v2beta.types.CompleteQueryResponse.RecentSearchResult](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.CompleteQueryResponse.RecentSearchResult)]`   
Deprecated. Matched recent searches of this user. The maximum number of recent searches is 10. This field is a restricted feature. If you want to enable it, contact Retail Search support. This feature is only available when CompleteQueryRequest.visitor_id field is set and UserEvent is imported. The recent searches satisfy the follow rules: \- They are ordered from latest to oldest. \- They are matched with CompleteQueryRequest.query case insensitively. \- They are transformed to lower case. \- They are UTF-8 safe. Recent searches are deduplicated. More recent searches will be reserved when duplication happens.   
`attribute_results` |  `MutableMapping[str, [google.cloud.retail_v2beta.types.CompleteQueryResponse.AttributeResult](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.CompleteQueryResponse.AttributeResult)]`   
A map of matched attribute suggestions. This field is only available for `cloud-retail` dataset. Current supported keys: \- `brands` \- `categories`  
  
## Classes 

### AttributeResult
    
    
    AttributeResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Resource that represents attribute results.

### AttributeResultsEntry
    
    
    AttributeResultsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### CompletionResult
    
    
    CompletionResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Resource that represents completion results.

### RecentSearchResult
    
    
    RecentSearchResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Deprecated: Recent search of this user.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
