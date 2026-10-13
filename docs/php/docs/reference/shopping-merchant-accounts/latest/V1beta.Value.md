---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Value
title: Google Shopping Merchant Accounts V1beta Client - Class Value (1.4.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:29.032183+00:00
---

# Google Shopping Merchant Accounts V1beta Client - Class Value (1.4.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Value

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Accounts V1beta Client - Class Value (1.4.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.6 (latest)  1.4.1  1.3.1  1.2.2  1.1.0  1.0.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.3  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Accounts V1beta Client class Value.

The single value of a rate group or the value of a rate group table's cell.

Exactly one of `no_shipping`, `flat_rate`, `price_percentage`, `carrier_rateName`, `subtable_name` must be set.

Generated from protobuf message `google.shopping.merchant.accounts.v1beta.Value`

## Namespace

Google \ Shopping \ Merchant \ Accounts \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ no_shipping` |  `bool`   
If true, then the product can't be shipped. Must be true when set, can only be set if all other fields are not set.  
`↳ flat_rate` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
A flat rate. Can only be set if all other fields are not set.  
`↳ price_percentage` |  `string`   
A percentage of the price represented as a number in decimal notation (For example, `"5.4"`). Can only be set if all other fields are not set.  
`↳ carrier_rate` |  `string`   
The name of a carrier rate referring to a carrier rate defined in the same rate group. Can only be set if all other fields are not set.  
`↳ subtable` |  `string`   
The name of a subtable. Can only be set in table cells (For example, not for single values), and only if all other fields are not set.  
  
### getNoShipping

If true, then the product can't be shipped. Must be true when set, can only be set if all other fields are not set.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasNoShipping

### clearNoShipping

### setNoShipping

If true, then the product can't be shipped. Must be true when set, can only be set if all other fields are not set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFlatRate

A flat rate. Can only be set if all other fields are not set.

**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)|null` |   
  
### hasFlatRate

### clearFlatRate

### setFlatRate

A flat rate. Can only be set if all other fields are not set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPricePercentage

A percentage of the price represented as a number in decimal notation (For example, `"5.4"`). Can only be set if all other fields are not set.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasPricePercentage

### clearPricePercentage

### setPricePercentage

A percentage of the price represented as a number in decimal notation (For example, `"5.4"`). Can only be set if all other fields are not set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCarrierRate

The name of a carrier rate referring to a carrier rate defined in the same rate group. Can only be set if all other fields are not set.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasCarrierRate

### clearCarrierRate

### setCarrierRate

The name of a carrier rate referring to a carrier rate defined in the same rate group. Can only be set if all other fields are not set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSubtable

The name of a subtable. Can only be set in table cells (For example, not for single values), and only if all other fields are not set.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasSubtable

### clearSubtable

### setSubtable

The name of a subtable. Can only be set in table cells (For example, not for single values), and only if all other fields are not set.

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

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
