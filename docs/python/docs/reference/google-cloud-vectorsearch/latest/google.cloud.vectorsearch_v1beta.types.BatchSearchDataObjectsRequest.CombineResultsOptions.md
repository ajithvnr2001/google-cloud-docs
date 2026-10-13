---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1beta.types.BatchSearchDataObjectsRequest.CombineResultsOptions
title: Class CombineResultsOptions (0.11.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:00.576735+00:00
---

# Class CombineResultsOptions (0.11.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1beta.types.BatchSearchDataObjectsRequest.CombineResultsOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CombineResultsOptions (0.11.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.5 (latest)  0.11.4  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    CombineResultsOptions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Options for combining the results of the batch search operations.

## Attributes  
  
---  
**Name** | **Description**  
`ranker` |  `[google.cloud.vectorsearch_v1beta.types.Ranker](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1beta.types.Ranker)`   
Required. The ranker to use for combining the results.   
`output_fields` |  `[google.cloud.vectorsearch_v1beta.types.OutputFields](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1beta.types.OutputFields)`   
Optional. Mask specifying which fields to return.   
`top_k` |  `int`   
Optional. The number of results to return. If not set, a default value will be used.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
