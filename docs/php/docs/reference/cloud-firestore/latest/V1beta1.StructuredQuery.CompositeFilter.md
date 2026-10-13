---
url: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.CompositeFilter
title: Cloud Firestore V1beta1 Client - Class CompositeFilter (2.2.0-RC1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:04.204501+00:00
---

# Cloud Firestore V1beta1 Client - Class CompositeFilter (2.2.0-RC1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.CompositeFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Firestore V1beta1 Client - Class CompositeFilter (2.2.0-RC1) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0-RC1  2.1.0  2.0.2-RC1  1.55.0  1.54.4  1.53.1  1.52.0  1.51.0  1.50.0  1.48.1  1.47.3  1.46.0  1.45.2  1.44.1  1.43.3  1.40.0  1.39.0  1.38.0  1.37.7  1.36.1  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.28.0  1.27.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Cloud Firestore V1beta1 Client class CompositeFilter.

A filter that merges multiple other filters using the given operator.

Generated from protobuf message `google.firestore.v1beta1.StructuredQuery.CompositeFilter`

## Namespace

Google \ Cloud \ Firestore \ V1beta1 \ StructuredQuery

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ op` |  `int`   
The operator for combining multiple filters.  
`↳ filters` |  `array<[Filter](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.Filter)>`   
The list of filters to combine. Must contain at least one filter.  
  
### getOp

The operator for combining multiple filters.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Operator](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.CompositeFilter.Operator).  
  
### setOp

The operator for combining multiple filters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Operator](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.CompositeFilter.Operator).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilters

The list of filters to combine.

Must contain at least one filter.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Internal\RepeatedField](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Internal/RepeatedField)` |   
  
### setFilters

The list of filters to combine.

Must contain at least one filter.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Filter](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.Filter)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
