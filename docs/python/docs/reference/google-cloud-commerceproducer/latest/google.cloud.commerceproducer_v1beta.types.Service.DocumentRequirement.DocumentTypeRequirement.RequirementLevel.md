---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.Service.DocumentRequirement.DocumentTypeRequirement.RequirementLevel
title: Class RequirementLevel (0.1.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:59.277536+00:00
---

# Class RequirementLevel (0.1.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.Service.DocumentRequirement.DocumentTypeRequirement.RequirementLevel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RequirementLevel (0.1.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.3 (latest)  0.1.2 
    
    
    RequirementLevel(value)

Requirement level for the document type.
    
    
        A document type omitted from `document_type_requirements`
        is also not permitted. This value is used to state the
        restriction explicitly.
    

## Enums  
  
---  
**Name** | **Description**  
`REQUIREMENT_LEVEL_UNSPECIFIED` | Unspecified requirement level. Do not use.  
`REQUIRED` | The document type is mandatory for private offers on this service. Exactly one document of this type must be attached.  
`OPTIONAL` | The document type is optional for private offers on this service. At most one document of this type may be attached.  
`NOT_ALLOWED` | The document type is not permitted for private offers on this service. No document of this type may be attached.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
