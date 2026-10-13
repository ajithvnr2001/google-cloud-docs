---
url: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange
title: Google Cloud Commerce Producer V1beta Client - Class PodResourceRange (0.2.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:03.864952+00:00
---

# Google Cloud Commerce Producer V1beta Client - Class PodResourceRange (0.2.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Commerce Producer V1beta Client - Class PodResourceRange (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Commerce Producer V1beta Client class PodResourceRange.

The range of pod resource values that the SKU applies to.

Generated from protobuf message `google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange`

## Namespace

Google \ Cloud \ CommerceProducer \ V1beta \ Sku \ SkuPrice \ KubernetesEnginePodUsageFee

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ start_value` |  `int|string`   
Output only. The inclusive lower bound of the range.  
`↳ end_value` |  `int|string`   
Output only. The exclusive upper bound of the range. If no end value is specified, the range is unbounded from above.  
  
### getStartValue

Output only. The inclusive lower bound of the range.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setStartValue

Output only. The inclusive lower bound of the range.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndValue

Output only. The exclusive upper bound of the range.

If no end value is specified, the range is unbounded from above.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### hasEndValue

### clearEndValue

### setEndValue

Output only. The exclusive upper bound of the range.

If no end value is specified, the range is unbounded from above.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
