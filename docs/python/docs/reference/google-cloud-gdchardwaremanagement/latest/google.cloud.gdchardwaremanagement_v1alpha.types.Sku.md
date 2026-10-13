---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Sku
title: Class Sku (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:51.852845+00:00
---

# Class Sku (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Sku

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Sku (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    Sku(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A stock keeping unit (SKU) of GDC hardware.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of this SKU. Format: `projects/{project}/locations/{location}/skus/{sku}`  
`display_name` |  `str`   
Output only. Display name of this SKU.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this SKU was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this SKU was last updated.   
`config` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.SkuConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SkuConfig)`   
Output only. Configuration for this SKU.   
`instances` |  `MutableSequence[[google.cloud.gdchardwaremanagement_v1alpha.types.SkuInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SkuInstance)]`   
Output only. Available instances of this SKU. This field should be used for checking availability of a SKU.   
`description` |  `str`   
Output only. Description of this SKU.   
`revision_id` |  `str`   
Output only. The SKU revision ID. A new revision is created whenever `config` is updated. The format is an 8-character hexadecimal string.   
`is_active` |  `bool`   
Output only. Flag to indicate whether or not this revision is active. Only an active revision can be used in a new Order.   
`type_` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Sku.Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Sku.Type)`   
Output only. Type of this SKU.   
`vcpu_count` |  `int`   
Output only. The vCPU count associated with this SKU.   
`hardware_count_ranges` |  `MutableSequence[[google.cloud.gdchardwaremanagement_v1alpha.types.Sku.Range](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Sku.Range)]`   
Output only. The inclusive ranges of hardware counts that are allowed in a zone using this SKU.   
  
## Classes 

### Range
    
    
    Range(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Inclusive range.

### Type
    
    
    Type(value)

Valid types of a SKU.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
