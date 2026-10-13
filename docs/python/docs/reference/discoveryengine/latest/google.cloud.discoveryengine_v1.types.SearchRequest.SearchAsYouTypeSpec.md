---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec
title: Class SearchAsYouTypeSpec (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:06.966823+00:00
---

# Class SearchAsYouTypeSpec (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchAsYouTypeSpec (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    SearchAsYouTypeSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specification for search as you type in search requests.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`condition` |  `[google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec.Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec.Condition)`   
The condition under which search as you type should occur. Default to Condition.DISABLED.   
`fields` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec.Field](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec.Field)]`   
Optional. The list of fields to be used for Search As You Type scoring.   
`score_threshold` |  `float`   
Optional. Search As You Type score threshold for filtering purpose. We keep the result if `score` >= `score_threshold`. This field is a member of `oneof`_ `_score_threshold`.   
  
## Classes 

### Condition
    
    
    Condition(value)

Enum describing under which condition search as you type should occur.

### Field
    
    
    Field(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A schema field to be used for Search As You Type scoring on this request. Overrides any data-store-level Search As You Type field configuration for the duration of the request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
