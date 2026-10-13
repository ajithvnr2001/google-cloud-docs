---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.RateGroup
title: Google Shopping Merchant Accounts V1beta Client - Class RateGroup (1.4.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:28.169584+00:00
---

# Google Shopping Merchant Accounts V1beta Client - Class RateGroup (1.4.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.RateGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Accounts V1beta Client - Class RateGroup (1.4.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.6 (latest)  1.4.1  1.3.1  1.2.2  1.1.0  1.0.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.3  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Accounts V1beta Client class RateGroup.

Shipping rate group definitions. Only the last one is allowed to have an empty `applicable_shipping_labels`, which means "everything else". The other `applicable_shipping_labels` must not overlap.

Generated from protobuf message `google.shopping.merchant.accounts.v1beta.RateGroup`

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
`↳ applicable_shipping_labels` |  `string[]`   
Required. A list of [shipping labels](https://support.google.com/merchants/answer/6324504) defining the products to which this rate group applies to. This is a disjunction: only one of the labels has to match for the rate group to apply. May only be empty for the last rate group of a service.  
`↳ single_value` |  `[Value](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Value)`   
The value of the rate group (For example flat rate $10). Can only be set if `main_table` and `subtables` are not set.  
`↳ main_table` |  `[Table](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Table)`   
A table defining the rate group, when `single_value` is not expressive enough. Can only be set if `single_value` is not set.  
`↳ subtables` |  `array<[Table](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Table)>`   
Optional. A list of subtables referred to by `main_table`. Can only be set if `main_table` is set.  
`↳ carrier_rates` |  `array<[CarrierRate](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.CarrierRate)>`   
Optional. A list of carrier rates that can be referred to by `main_table` or `single_value`.  
`↳ name` |  `string`   
Optional. Name of the rate group. If set has to be unique within shipping service.  
  
### getApplicableShippingLabels

Required. A list of [shipping labels](https://support.google.com/merchants/answer/6324504) defining the products to which this rate group applies to. This is a disjunction: only one of the labels has to match for the rate group to apply. May only be empty for the last rate group of a service.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setApplicableShippingLabels

Required. A list of [shipping labels](https://support.google.com/merchants/answer/6324504) defining the products to which this rate group applies to. This is a disjunction: only one of the labels has to match for the rate group to apply. May only be empty for the last rate group of a service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSingleValue

The value of the rate group (For example flat rate $10). Can only be set if `main_table` and `subtables` are not set.

**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Value)|null` |   
  
### hasSingleValue

### clearSingleValue

### setSingleValue

The value of the rate group (For example flat rate $10). Can only be set if `main_table` and `subtables` are not set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Value](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Value)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMainTable

A table defining the rate group, when `single_value` is not expressive enough. Can only be set if `single_value` is not set.

**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Table)|null` |   
  
### hasMainTable

### clearMainTable

### setMainTable

A table defining the rate group, when `single_value` is not expressive enough. Can only be set if `single_value` is not set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Table](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Table)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSubtables

Optional. A list of subtables referred to by `main_table`. Can only be set if `main_table` is set.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Table](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Table)>` |   
  
### setSubtables

Optional. A list of subtables referred to by `main_table`. Can only be set if `main_table` is set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Table](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Table)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCarrierRates

Optional. A list of carrier rates that can be referred to by `main_table` or `single_value`.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[CarrierRate](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.CarrierRate)>` |   
  
### setCarrierRates

Optional. A list of carrier rates that can be referred to by `main_table` or `single_value`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[CarrierRate](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.CarrierRate)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Optional. Name of the rate group.

If set has to be unique within shipping service.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasName

### clearName

### setName

Optional. Name of the rate group.

If set has to be unique within shipping service.

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
