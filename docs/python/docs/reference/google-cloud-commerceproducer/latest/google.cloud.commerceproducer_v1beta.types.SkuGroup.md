---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.SkuGroup
title: Class SkuGroup (0.1.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:02.773627+00:00
---

# Class SkuGroup (0.1.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.SkuGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SkuGroup (0.1.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.3 (latest)  0.1.2 
    
    
    SkuGroup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing SkuGroup resource

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. Name of the SkuGroup.   
`skus` |  `MutableSequence[str]`   
Output only. Partner SKUs included in the SkuGroup. Format: `projects/{project}/locations/{location}/services/{service}/skus/{sku}`  
`cloud_billing_skus` |  `MutableSequence[str]`   
Output only. Google SKUs included in the SkuGroup. Used for partner products sold by Google, such as Premium Operating System Images sold for use in Compute Engine. This is not common. SKUs of this type are not present on this API and can instead be found on the Cloud Billing API or at https://cloud.google.com/skus. Format: `services/{service}/skus/{sku}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
