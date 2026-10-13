---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.Cost
title: Class Cost (0.3.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:35.979769+00:00
---

# Class Cost (0.3.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.Cost

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Cost (0.3.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.2 (latest)  0.3.1  0.2.0  0.1.0 
    
    
    Cost(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Cost for running a model deployment on a given instance type. Currently, only USD currency code is supported.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`cost_per_million_output_tokens` |  `[google.cloud.gkerecommender_v1.types.Amount](https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.Amount)`   
Optional. The cost per million output tokens, calculated as: $/output token = GPU $/s / (1/output-to-input-cost-ratio \\* input tokens/s + output tokens/s)   
`cost_per_million_input_tokens` |  `[google.cloud.gkerecommender_v1.types.Amount](https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.Amount)`   
Optional. The cost per million input tokens. $/input token = ($/output token) / output-to-input-cost-ratio.   
`pricing_model` |  `str`   
Optional. The pricing model used to calculate the cost. Can be one of: `3-years-cud`, `1-year-cud`, `on-demand`, `spot`. If not provided, `spot` will be used.   
`output_input_cost_ratio` |  `float`   
Optional. The output-to-input cost ratio. This determines how the total GPU cost is split between input and output tokens. If not provided, `4.0` is used, assuming a 4:1 output:input cost ratio. This field is a member of `oneof`_ `_output_input_cost_ratio`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
