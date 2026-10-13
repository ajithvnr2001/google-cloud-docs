---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy
title: Class DataMaskingPolicy (0.10.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:35.841791+00:00
---

# Class DataMaskingPolicy (0.10.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataMaskingPolicy (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.0  0.7.0  0.6.16  0.5.3  0.4.0  0.3.2  0.2.0  0.1.1 
    
    
    DataMaskingPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The policy used to specify data masking rule.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attribute  
  
---  
**Name** | **Description**  
`predefined_expression` |  `[google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy.PredefinedExpression](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy.PredefinedExpression)`   
Optional. A predefined masking expression. This field is a member of `oneof`_ `masking_expression`.   
  
## Classes 

### PredefinedExpression
    
    
    PredefinedExpression(value)

The available masking rules. Learn more here: <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>.
    
    
        - STRING: ""
        - BYTES: b''
        - INTEGER: 0
        - FLOAT: 0.0
        - NUMERIC: 0
        - BOOLEAN: FALSE
        - TIMESTAMP: 1970-01-01 00:00:00 UTC
        - DATE: 1970-01-01
        - TIME: 00:00:00
        - DATETIME: 1970-01-01T00:00:00
        - GEOGRAPHY: POINT(0 0)
        - BIGNUMERIC: 0
        - ARRAY: []
        - STRUCT: NOT_APPLICABLE
        - JSON: NULL
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
