---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.LoyaltyProgram
title: Google Shopping Merchant Products V1beta Client - Class LoyaltyProgram (1.8.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:58.882648+00:00
---

# Google Shopping Merchant Products V1beta Client - Class LoyaltyProgram (1.8.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.LoyaltyProgram

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Products V1beta Client - Class LoyaltyProgram (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.5  1.6.0  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Products V1beta Client class LoyaltyProgram.

A message that represents loyalty program.

Generated from protobuf message `google.shopping.merchant.products.v1beta.LoyaltyProgram`

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
`↳ program_label` |  `string`   
The label of the loyalty program. This is an internal label that uniquely identifies the relationship between a business entity and a loyalty program entity. The label must be provided so that the system can associate the assets below (for example, price and points) with a business. The corresponding program must be linked to the Merchant Center account.  
`↳ tier_label` |  `string`   
The label of the tier within the loyalty program. Must match one of the labels within the program.  
`↳ price` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
The price for members of the given tier, that is, the instant discount price. Must be smaller or equal to the regular price.  
`↳ cashback_for_future_use` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
The cashback that can be used for future purchases.  
`↳ loyalty_points` |  `int|string`   
The amount of loyalty points earned on a purchase.  
`↳ member_price_effective_date` |  `[Google\Type\Interval](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Interval.html)`   
A date range during which the item is eligible for member price. If not specified, the member price is always applicable. The date range is represented by a pair of ISO 8601 dates separated by a space, comma, or slash.  
`↳ shipping_label` |  `string`   
The label of the shipping benefit. If the field has value, this offer has loyalty shipping benefit. If the field value isn't provided, the item is not eligible for loyalty shipping for the given loyalty tier.  
  
### getProgramLabel

The label of the loyalty program. This is an internal label that uniquely identifies the relationship between a business entity and a loyalty program entity. The label must be provided so that the system can associate the assets below (for example, price and points) with a business. The corresponding program must be linked to the Merchant Center account.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasProgramLabel

### clearProgramLabel

### setProgramLabel

The label of the loyalty program. This is an internal label that uniquely identifies the relationship between a business entity and a loyalty program entity. The label must be provided so that the system can associate the assets below (for example, price and points) with a business. The corresponding program must be linked to the Merchant Center account.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTierLabel

The label of the tier within the loyalty program.

Must match one of the labels within the program.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasTierLabel

### clearTierLabel

### setTierLabel

The label of the tier within the loyalty program.

Must match one of the labels within the program.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPrice

The price for members of the given tier, that is, the instant discount price. Must be smaller or equal to the regular price.

**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)|null` |   
  
### hasPrice

### clearPrice

### setPrice

The price for members of the given tier, that is, the instant discount price. Must be smaller or equal to the regular price.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCashbackForFutureUse

The cashback that can be used for future purchases.

**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)|null` |   
  
### hasCashbackForFutureUse

### clearCashbackForFutureUse

### setCashbackForFutureUse

The cashback that can be used for future purchases.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLoyaltyPoints

The amount of loyalty points earned on a purchase.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### hasLoyaltyPoints

### clearLoyaltyPoints

### setLoyaltyPoints

The amount of loyalty points earned on a purchase.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMemberPriceEffectiveDate

A date range during which the item is eligible for member price. If not specified, the member price is always applicable. The date range is represented by a pair of ISO 8601 dates separated by a space, comma, or slash.

**Returns**  
---  
**Type** | **Description**  
`[Google\Type\Interval](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Interval.html)|null` |   
  
### hasMemberPriceEffectiveDate

### clearMemberPriceEffectiveDate

### setMemberPriceEffectiveDate

A date range during which the item is eligible for member price. If not specified, the member price is always applicable. The date range is represented by a pair of ISO 8601 dates separated by a space, comma, or slash.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Type\Interval](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Interval.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getShippingLabel

The label of the shipping benefit. If the field has value, this offer has loyalty shipping benefit. If the field value isn't provided, the item is not eligible for loyalty shipping for the given loyalty tier.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasShippingLabel

### clearShippingLabel

### setShippingLabel

The label of the shipping benefit. If the field has value, this offer has loyalty shipping benefit. If the field value isn't provided, the item is not eligible for loyalty shipping for the given loyalty tier.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
