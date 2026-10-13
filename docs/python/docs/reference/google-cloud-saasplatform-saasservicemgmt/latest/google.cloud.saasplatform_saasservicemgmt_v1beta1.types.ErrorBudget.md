---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ErrorBudget
title: Class ErrorBudget (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:38.575952+00:00
---

# Class ErrorBudget (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ErrorBudget

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ErrorBudget (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ErrorBudget(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The configuration for error budget. If the number of failed units exceeds max(allowed_count, allowed_ratio * total_units), the rollout will be paused.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`allowed_count` |  `int`   
Optional. The maximum number of failed units allowed in a location without pausing the rollout. This field is a member of `oneof`_ `_allowed_count`.   
`allowed_percentage` |  `int`   
Optional. The maximum percentage of units allowed to fail (0, 100] within a location without pausing the rollout. This field is a member of `oneof`_ `_allowed_percentage`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
