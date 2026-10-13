---
url: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UpdateDocumentResponse
title: Class UpdateDocumentResponse (0.11.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:48.790668+00:00
---

# Class UpdateDocumentResponse (0.11.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UpdateDocumentResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdateDocumentResponse (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.11.0  0.10.0  0.9.0  0.8.0  0.7.16  0.6.0  0.5.1  0.4.1  0.3.1  0.2.1  0.1.0 
    
    
    UpdateDocumentResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Response message for DocumentService.UpdateDocument.

## Attributes  
  
---  
**Name** | **Description**  
`document` |  `[google.cloud.contentwarehouse_v1.types.Document](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.Document)`   
Updated document after executing update request.   
`rule_engine_output` |  `[google.cloud.contentwarehouse_v1.types.RuleEngineOutput](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RuleEngineOutput)`   
Output from Rule Engine recording the rule evaluator and action executor's output. Refer format in: google/cloud/contentwarehouse/v1/rule_engine.proto   
`metadata` |  `[google.cloud.contentwarehouse_v1.types.ResponseMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.ResponseMetadata)`   
Additional information for the API invocation, such as the request tracking id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
