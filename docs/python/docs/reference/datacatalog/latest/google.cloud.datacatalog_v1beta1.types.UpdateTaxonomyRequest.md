---
url: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1beta1.types.UpdateTaxonomyRequest
title: Class UpdateTaxonomyRequest (3.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:50.896575+00:00
---

# Class UpdateTaxonomyRequest (3.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1beta1.types.UpdateTaxonomyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdateTaxonomyRequest (3.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.32.0 (latest)  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.1  3.25.1  3.24.1  3.23.0  3.22.0  3.21.1  3.20.1  3.19.1  3.18.3  3.17.2  3.16.0  3.15.1  3.14.0  3.13.1  3.12.0  3.11.1  3.10.0  3.9.3  3.8.1  3.7.1  3.6.2  3.5.0  3.4.3  3.3.2  3.2.1  3.1.1  3.0.0  2.0.2  1.0.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    UpdateTaxonomyRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for UpdateTaxonomy.

## Attributes  
  
---  
**Name** | **Description**  
`taxonomy` |  `[google.cloud.datacatalog_v1beta1.types.Taxonomy](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1beta1.types.Taxonomy)`   
The taxonomy to update. Only description, display_name, and activated policy types can be updated.   
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask If not set, defaults to all of the fields that are allowed to update.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
