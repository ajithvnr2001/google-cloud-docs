---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.Service
title: Class Service (0.1.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:46.519649+00:00
---

# Class Service (0.1.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.Service

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Service (0.1.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.3 (latest)  0.1.2 
    
    
    Service(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing Service resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of resource.   
`title` |  `str`   
Output only. Title of the service. Not included for `SERVICE_VIEW_BASIC`.   
`document_requirement` |  `[google.cloud.commerceproducer_v1beta.types.Service.DocumentRequirement](https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.Service.DocumentRequirement)`   
Output only. Document requirement for private offers on this service. Constraints that apply to every service, such as the restriction against attaching both a standard and a custom EULA, are documented on `PrivateOfferDocument` and are not represented here.   
`product_type` |  `[google.cloud.commerceproducer_v1beta.types.Service.ProductType](https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.Service.ProductType)`   
Output only. Type of the product this service commercializes.   
  
## Classes 

### DocumentRequirement
    
    
    DocumentRequirement(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Requirements and constraints for documents attached to private offers.

### ProductType
    
    
    ProductType(value)

The type of the product this service commercializes.

Every service has a type, but only the types listed below are exposed. A service whose type is not one of the listed values reports `PRODUCT_TYPE_UNSPECIFIED`.

Values may be added over time. Clients must handle unrecognized values. When new values are added, the ProductType for an existing service may change. Clients must also be able to handle a change in ProductType.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
