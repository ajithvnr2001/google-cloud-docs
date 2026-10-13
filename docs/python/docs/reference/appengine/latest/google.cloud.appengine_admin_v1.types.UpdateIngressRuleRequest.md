---
url: https://docs.cloud.google.com/python/docs/reference/appengine/latest/google.cloud.appengine_admin_v1.types.UpdateIngressRuleRequest
title: Class UpdateIngressRuleRequest (1.19.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:31.211311+00:00
---

# Class UpdateIngressRuleRequest (1.19.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/appengine/latest/google.cloud.appengine_admin_v1.types.UpdateIngressRuleRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdateIngressRuleRequest (1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.0  1.17.0  1.16.0  1.15.0  1.14.2  1.13.0  1.12.1  1.11.5  1.10.0  1.9.4  1.8.1  1.7.1  1.6.0  1.5.3  1.4.1  1.3.3  1.2.1  1.1.5  1.0.2  0.2.0  0.1.0 
    
    
    UpdateIngressRuleRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for `Firewall.UpdateIngressRule`.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Name of the Firewall resource to update. Example: `apps/myapp/firewall/ingressRules/100`.   
`rule` |  `[google.cloud.appengine_admin_v1.types.FirewallRule](https://docs.cloud.google.com/python/docs/reference/appengine/latest/google.cloud.appengine_admin_v1.types.FirewallRule)`   
A FirewallRule containing the updated resource   
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Standard field mask for the set of fields to be updated.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
