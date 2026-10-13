---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.LoyaltyPoints
title: Google Shopping Merchant Products V1beta Client - Class LoyaltyPoints (1.8.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:52.802626+00:00
---

# Google Shopping Merchant Products V1beta Client - Class LoyaltyPoints (1.8.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.LoyaltyPoints

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Products V1beta Client - Class LoyaltyPoints (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.5  1.6.0  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Products V1beta Client class LoyaltyPoints.

A message that represents loyalty points.

Generated from protobuf message `google.shopping.merchant.products.v1beta.LoyaltyPoints`

## Namespace

Google \ Shopping \ Merchant \ Products \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Name of loyalty points program. It is recommended to limit the name to 12 full-width characters or 24 Roman characters.  
`↳ points_value` |  `int|string`   
The retailer's loyalty points in absolute value.  
`↳ ratio` |  `float`   
The ratio of a point when converted to currency. Google assumes currency based on Merchant Center settings. If ratio is left out, it defaults to 1.0.  
  
### getName

Name of loyalty points program. It is recommended to limit the name to 12 full-width characters or 24 Roman characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Name of loyalty points program. It is recommended to limit the name to 12 full-width characters or 24 Roman characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPointsValue

The retailer's loyalty points in absolute value.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setPointsValue

The retailer's loyalty points in absolute value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRatio

The ratio of a point when converted to currency. Google assumes currency based on Merchant Center settings. If ratio is left out, it defaults to 1.0.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### setRatio

The ratio of a point when converted to currency. Google assumes currency based on Merchant Center settings. If ratio is left out, it defaults to 1.0.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
