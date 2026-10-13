---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.UpdateRuleRequest
title: Class UpdateRuleRequest (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:34.323054+00:00
---

# Class UpdateRuleRequest (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.UpdateRuleRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdateRuleRequest (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    UpdateRuleRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for UpdateRule method.

## Attributes  
  
---  
**Name** | **Description**  
`rule` |  `[google.cloud.chronicle_v1.types.Rule](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.Rule)`   
Required. The rule to update. The rule's `name` field is used to identify the rule to update. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to update. If not included, all fields with a non-empty value will be overwritten.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
