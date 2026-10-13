---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.CustomAPIDependentRequestsConfig
title: Class CustomAPIDependentRequestsConfig (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:56.365383+00:00
---

# Class CustomAPIDependentRequestsConfig (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.CustomAPIDependentRequestsConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CustomAPIDependentRequestsConfig (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    CustomAPIDependentRequestsConfig(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Configuration for dependent requests (child chaining).

## Attributes  
  
---  
**Name** | **Description**  
`item_id_json_path` |  `str`   
Required. Enter the specific field in the response that uniquely identifies an individual record or alert.   
`item_id_variable` |  `str`   
Optional. Specify a custom variable name to hold the extracted ID, which can be linked as a placeholder in dependent requests.   
`dependent_requests` |  `MutableSequence[[google.cloud.chronicle_v1.types.CustomAPITransferNode](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.CustomAPITransferNode)]`   
Optional. Add follow-up API calls triggered for each item found in the primary request (e.g., fetching full event details for a list of basic alert IDs). Note: In MVP, the child depth fan-out limit is capped at 1.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
