---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.LookerQuery
title: Class LookerQuery (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:00.289021+00:00
---

# Class LookerQuery (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.LookerQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LookerQuery (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    LookerQuery(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Looker Query Object `Looker API documentation <https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/run_inline_query>`__.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`model` |  `str`   
Required. The LookML model used to generate the query.   
`explore` |  `str`   
Required. The LookML explore used to generate the query.   
`fields` |  `MutableSequence[str]`   
Optional. The fields to retrieve from the explore.   
`filters` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.LookerQuery.Filter](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.LookerQuery.Filter)]`   
Optional. The filters to apply to the explore.   
`sorts` |  `MutableSequence[str]`   
Optional. The sorts to apply to the explore.   
`limit` |  `str`   
Optional. Limit in the query. This field is a member of `oneof`_ `_limit`.   
`dynamic_fields` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.DynamicField](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DynamicField)]`   
Optional. The dynamic fields used in the query.   
`query_id` |  `str`   
Optional. The primary identifier for the query resource in Looker, used for API operations. Maps to `id` (or `slug`) in the Looker API `Query` resource. This field is a member of `oneof`_ `_query_id`.   
`client_id` |  `str`   
Optional. The short alphanumeric identifier for the query, used for share links and Explore URLs (e.g., in the `qid` parameter). Maps to `client_id` in the Looker API `Query` resource. This field is a member of `oneof`_ `_client_id`.   
  
## Classes 

### Filter
    
    
    Filter(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Looker query filter.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
