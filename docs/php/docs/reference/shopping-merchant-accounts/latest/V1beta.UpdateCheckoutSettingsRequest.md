---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.UpdateCheckoutSettingsRequest
title: Google Shopping Merchant Accounts V1beta Client - Class UpdateCheckoutSettingsRequest (1.4.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:09.768548+00:00
---

# Google Shopping Merchant Accounts V1beta Client - Class UpdateCheckoutSettingsRequest (1.4.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.UpdateCheckoutSettingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Accounts V1beta Client - Class UpdateCheckoutSettingsRequest (1.4.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.6 (latest)  1.4.1  1.3.1  1.2.2  1.1.0  1.0.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.3  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Accounts V1beta Client class UpdateCheckoutSettingsRequest.

Request message for the `UpdateCheckoutSettings` method.

Generated from protobuf message `google.shopping.merchant.accounts.v1beta.UpdateCheckoutSettingsRequest`

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
`↳ checkout_settings` |  `[CheckoutSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.CheckoutSettings)`   
Required. The updated version of the `CheckoutSettings`. The `name` field is used to identify the `CheckoutSettings`. Format: `accounts/{account}/programs/{program}/checkoutSettings`  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Required. List of fields being updated. The following fields are supported (in both `snake_case` and `lowerCamelCase`): - `eligible_destinations` \- `uri_settings`  
  
### getCheckoutSettings

Required. The updated version of the `CheckoutSettings`.

The `name` field is used to identify the `CheckoutSettings`. Format: `accounts/{account}/programs/{program}/checkoutSettings`

**Returns**  
---  
**Type** | **Description**  
`[CheckoutSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.CheckoutSettings)|null` |   
  
### hasCheckoutSettings

### clearCheckoutSettings

### setCheckoutSettings

Required. The updated version of the `CheckoutSettings`.

The `name` field is used to identify the `CheckoutSettings`. Format: `accounts/{account}/programs/{program}/checkoutSettings`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CheckoutSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.CheckoutSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Required. List of fields being updated.

The following fields are supported (in both `snake_case` and `lowerCamelCase`):

  * `eligible_destinations`
  * `uri_settings`



**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Required. List of fields being updated.

The following fields are supported (in both `snake_case` and `lowerCamelCase`):

  * `eligible_destinations`
  * `uri_settings`



**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`checkoutSettings` |  `[CheckoutSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.CheckoutSettings)`   
Required. The updated version of the `CheckoutSettings`. The `name` field is used to identify the `CheckoutSettings`. Format: `accounts/{account}/programs/{program}/checkoutSettings`  
`updateMask` |  `Google\Protobuf\FieldMask`   
Required. List of fields being updated. The following fields are supported (in both `snake_case` and `lowerCamelCase`):

  * `eligible_destinations`
  * `uri_settings`

  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCheckoutSettingsRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.UpdateCheckoutSettingsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
