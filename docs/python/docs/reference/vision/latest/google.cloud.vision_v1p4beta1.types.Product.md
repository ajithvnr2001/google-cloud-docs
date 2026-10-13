---
url: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product
title: Class Product (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:55.423968+00:00
---

# Class Product (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Product (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    Product(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Product contains ReferenceImages.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the product. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`. This field is ignored when creating a product.   
`display_name` |  `str`   
The user-provided name for this Product. Must not be empty. Must be at most 4096 characters long.   
`description` |  `str`   
User-provided metadata to be stored with this product. Must be at most 4096 characters long.   
`product_category` |  `str`   
Immutable. The category for the product identified by the reference image. This should be either "homegoods-v2", "apparel-v2", or "toys-v2". The legacy categories "homegoods", "apparel", and "toys" are still supported, but these should not be used for new products.   
`product_labels` |  `MutableSequence[[google.cloud.vision_v1p4beta1.types.Product.KeyValue](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product.KeyValue)]`   
Key-value pairs that can be attached to a product. At query time, constraints can be specified based on the product_labels. Note that integer values can be provided as strings, e.g. "1199". Only strings with integer values can match a range-based restriction which is to be supported soon. Multiple values can be assigned to the same key. One product may have up to 500 product_labels. Notice that the total number of distinct product_labels over all products in one ProductSet cannot exceed 1M, otherwise the product search pipeline will refuse to work for that ProductSet.   
  
## Classes 

### KeyValue
    
    
    KeyValue(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A product label represented as a key-value pair.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
