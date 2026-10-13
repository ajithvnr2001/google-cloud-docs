---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1beta.types.CreateGuardrailRequest
title: Class CreateGuardrailRequest (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:47.988862+00:00
---

# Class CreateGuardrailRequest (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1beta.types.CreateGuardrailRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateGuardrailRequest (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    CreateGuardrailRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for AgentService.CreateGuardrail.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The resource name of the app to create a guardrail in.   
`guardrail_id` |  `str`   
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.   
`guardrail` |  `[google.cloud.ces_v1beta.types.Guardrail](https://docs.cloud.google.com/python/docs/reference/google-cloud-ces/latest/google.cloud.ces_v1beta.types.Guardrail)`   
Required. The guardrail to create.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
